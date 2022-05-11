import unittest
from app.models import Upvote

class UserModelTest(unittest.TestCase):
    
    def setUp(self):
        self.new_upvote=Upvote(upvote=2)

    def tearDown(self):
        print('teardown')

    def test_init(self):
        self.assertEqual(self.new_upvote.upvote,2)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_upvote,Upvote))