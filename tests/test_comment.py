import unittest
from app.models import Comment

class UserModelTest(unittest.TestCase):
    
    def setUp(self):
        self.new_comment=Comment(content='girls are the coolest')

    def tearDown(self):
        print('teardown')

    def test_init(self):
        self.assertEqual(self.new_comment.content,'girls are the coolest')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))