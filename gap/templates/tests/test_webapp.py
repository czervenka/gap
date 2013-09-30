from gap.utils.tests import WebAppTestBase


class TestApp(WebAppTestBase):

    def test_welcome(self):
        resp = self.get('/')
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(resp.content_type, 'text/html')
        self.assertTrue('<b>Example project</b>' in resp,)
