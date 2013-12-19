from uuid import uuid1
from sha import sha
from google.appengine.api import memcache
from google.appengine.ext import ndb

SESSION_COOKIE_NAME = getattr(config, 'SESSION_COOKIE_NAME', 'SESSION_ID')
SESSION_TIMEOUT = getattr(config, 'SESSION_TIMEOUT', 3600)
SECRET = getattr(config, 'SECRET')

class SessionModel(ndb.Model):
    session_id = ndb.StringProperty()
    data = ndb.JsonProperty()


class Session(object):

    def __init__(self, session_id=None):
        if session_id is None:
            session_id = self.create_session()
        self.id = session_id

    def create_session(self):
        return sha('%s:%s' % (uuid1(), SECRET)).hexdigest()

class SessionMiddleware(object):

    @classmethod
    def process_request(cls, request, response):
        session_id = request.session.get(SESSION_COOKIE_NAME)
        session = Session(session_id)
        response.set_cookie(SESSION_COOKIE_NAME, session.id, max_age=SESSION_TIMEOUT, secure=True)



