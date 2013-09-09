from common.test_base.test_base import TestBase


class TestSimple(TestBase):

    def setUp(self):
        print ("Setup called before each test method")

    def tearDown(self):
        print ("Teardown called after each test method")

    @classmethod
    def setUpClass(cls):
        print ("Set up of a class, called before any methods in the class")

    @classmethod
    def tearDownClass(cls):
        print ("Tear down of a class, called after all methods in the class")

    def test_simple_equals_20(self):
        """Equality test"""
        assert 5 * 4 == 20

    def test_simple_equals_10(self):
        """Equality test"""
        assert 5 * 2 == 10
