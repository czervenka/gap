from gap.utils.tests import WebAppTestBase


class TestApp(WebAppTestBase):

    def test_welcome(self):
        resp = self.app.get('/')
        self.assertEquals(resp.content_type, 'text/html', msg='Welcome page is not serving.')
        self.assertTrue(
            '<b>Example project</b>' in resp,
            msg='Project name not in page.'
        )
