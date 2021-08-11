import unittest
from password import User
from password import Credential

class TestPassword(unittest.TestCase):

    def setUp(self):
        self.new_user = User("carol","nyambu","b243#$5")

    def test_init(self):
        self.assertEqual(self.new_user.first_name,"carol")
        self.assertEqual(self.new_user.last_name,"nyambu")
        self.assertEqual(self.new_user.password,"b243#$5")




