import unittest

from app import login_auth, saveReview_auth, addFood_auth

class Tests(unittest.TestCase):
    
    def test_login_user_if_valid_data(self):
        self.assertEqual(login_auth("petar12", "8sd12g"),"Podaci su ispravni.")

    def test_login_wrong_password(self):
        self.assertEqual(login_auth("petar12", "9120sda"), "Podaci su ispravni.")

    def test_login_user_username_doesnt_exist(self):
        self.assertEqual(login_auth("abc26", "9120sda"), "Podaci su ispravni.")

    def test_save_review_if_valid_data(self):
        self.assertEqual(saveReview_auth("Odlicna hrana", 5), "Podaci su ispravni.")

    def test_save_review_if_reviewDesc_missing(self):
        self.assertEqual(saveReview_auth("", 2), "Podaci su ispravni.")
    
    def test_addFood_if_valid_data(self):
        self.assertEqual(addFood_auth("Kebab", 30), "Podaci su ispravni.")

    def test_addFood_if_price_invalid(self):
        self.assertEqual(addFood_auth("Pizza Tonno", 0), "Podaci su ispravni.")

if __name__ == '__main__':
    unittest.main()