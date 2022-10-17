form selenium import webdriver
import umittest

class NewivistorTest(unittest.TestCase):

    def setup(self):
        self.browser = webdriver.Firfox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warning = 'ignore')
