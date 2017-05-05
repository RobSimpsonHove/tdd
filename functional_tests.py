from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8082')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)  #5
        self.fail('Finish the test!')  #6

        # She is invited to enter a to-do item straight away

if __name__ == '__main__':  #7
    unittest.main()  #8
