#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.dice.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("a.loginDD > span").click()
        driver.find_element_by_id("Email_1").clear()
        driver.find_element_by_id("Email_1").send_keys("thelma1944@gmail.com")
        driver.find_element_by_id("Password_1").clear()
        driver.find_element_by_id("Password_1").send_keys("meowpurr1")
        driver.find_element_by_id("LoginBtn_1").click()
        self.assertEqual("Dice.com - Job Search for Technology Professionals", driver.title)
        driver.find_element_by_link_text("Logout").click()
        self.assertEqual("Dice - JobTools Login", driver.title)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
   
        except Exception:
            pass
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
