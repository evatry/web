from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        #self.browser.implicity_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME,'h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element(By.ID,'id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
                )

        inputbox.send_keys('Buy peacock feathers')
        time.sleep(5)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(10)
        table = self.browser.find_element(By.ID,'id_list_table')
        rows = table.find_elements(By.ID,'tr')
        self.assertTrue(
                any(row.text == '1: Buy peacock frathers' for row in rows),
                "New to-do item did not appear in table"
                )
        self.fail('Finish the test!')

if __name__ =='__main__':
    unittest.main(warnings='ignore')




#browser = webdriver.Firefox()
#browser.get('http://localhost:8000')
#assert 'To-do' in browser.title
#bowser.quit()

