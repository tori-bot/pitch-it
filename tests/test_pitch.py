import unittest
from app.models import Pitch

class UserModelTest(unittest.TestCase):
    
    def setUp(self):
        self.new_pitch=Pitch(title='girls')

    def tearDown(self):
        print('teardown')

    def test_init(self):
        self.assertEqual(self.new_pitch.title,'girls')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))