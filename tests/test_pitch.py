import unittest
from app.models import Pitch

class UserModelTest(unittest.TestCase):
    
    def setUp(self):
        self.new_pitch=Pitch(title='girls')

