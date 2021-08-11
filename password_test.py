import unittest
from password import User
from password import Credential

class TestPassword(unittest.TestCase):

    def setUp(self):
        self.new_user = User("Caroh","Nyambura","b243#$5")

    def test_init(self):
        self.assertEqual(self.new_user.first_name,"Caroh")
        self.assertEqual(self.new_user.last_name,"Nyambura")
        self.assertEqual(self.new_user.password,"$MyPassword!999")

    def test_save_user(self):
            """
            this method tests if the user object is saved into the userlist
            """
            self.new_user.save_user() # saves the new user
            self.assertEqual(len(User.user_list),1)
    
    def test_save_multiple_user(self):
            """
            checks if we can save multiple users
            """

            self.new_user.save_user()
            second_user = User("Victor","Kamau","#Brother2001") # new user
            second_user.save_user()
            self.assertEqual(len(User.user_list),2)

    def tearDown(second_user):
        """
        tearDown is a method that cleans up after each teat runs.
        """
        User.user_list = []

