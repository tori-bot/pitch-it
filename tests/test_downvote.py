import unittest
from app.models import Downvote

class UserModelTest(unittest.TestCase):
    
    def setUp(self):
        self.new_downvote=Downvote(upvote=2)

    def tearDown(self):
        print('teardown')

    def test_init(self):
        self.assertEqual(self.new_downvote.downvote,2)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_downvote,Downvote))