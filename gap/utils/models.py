import logging
from google.appengine.ext import deferred
from google.appengine.ext import ndb
from google.appengine.runtime import DeadlineExceededError


class ExtModelMixin(object):

    page_size = 100

    @classmethod
    def paged_query(cls, query=None, page_size=None, **kwargs):
        if query is None:
            query = cls.query(**kwargs)
        if page_size is None:
            page_size = cls.page_size

        has_more = True
        cursor = None
        while has_more:
            page, cursor, has_more = query.fetch_page(page_size, start_cursor=cursor)
            yield page

    def query(self, *args, **kwargs):
        query = super(ExtModelMixin, self).query(*args, **kwargs)
        query.pages = self.pages(query)
        return query


class BatchUpdater(object):

    page_size = 100
    model = None
    pickle_exclude = ()

    def __init__(self):
        self._cursor = None
        self._running = False
        self._to_put = []
        self._objects_updated = 0

    def _run(self):
        old_cursor = self._cursor  # save old cursor in case of troubles
        objects, self._cursor, more = self.get_query().fetch_page(self.page_size, start_cursor=self._cursor)
        logging.debug('_run %d objects' % len(objects))
        self._running = True

        try:
            for obj in objects:
                if self.needs_update(obj):
                    self._objects_updated += 1
                    self.update_obj(obj)
                    self._to_put.append(obj)
        except DeadlineExceededError:
            # page is too large, let's try with a litle shorter steps
            self._flush()
            if old_cursor:
                self._cursor = old_cursor
                self.page_size /= 2
                self._defer()
        else:
            self._flush()
            if self._eof() or not more:
                self.finish()
            else:
                self._defer()

    def _eof(self):
        '''returns true if we have passed over last resordset'''
        return self._cursor is None

    def _defer(self):
        logging.debug("%r deffering after %d objects processed." % (self.__class__.__name__, self._objects_updated))
        for prop in self.pickle_exclude:
            if hasattr(self, prop):
                logging.info('Deleting %s' % prop)
                delattr(self, prop)
            else:
                logging.info('Skipping deleting %s - does not exist.' % prop)

        if not self._eof():
            deferred.defer(self._run)

    def _flush(self):
        for itm in self._to_put:
            itm.put()
        self._to_put = []

    def start(self):
        logging.info('%r is starting.' % self.__class__.__name__)
        self._run()

    def get_query(self):
        '''extend this method to get custom query'''
        return self.model.query()

    def needs_update(self, obj):
        return True

    def update_obj(self, obj):
        raise NotImplementedError()

    def finish(self):
        logging.info("%r finished (%d objects processed)." % (self.__class__.__name__, self._objects_updated))


class ModelWalk(BatchUpdater):

    def __call__(self, query, callback, page_size=100):
        if isinstance(query, ndb.Model):
            query = query.query()
        self.page_size = page_size
        self.query = query
        self.callback = callback

    def get_query(self):
        return self.query

    def needs_update(self, obj):
        return True

    def update_obj(self, obj):
        return self.callback(obj)
