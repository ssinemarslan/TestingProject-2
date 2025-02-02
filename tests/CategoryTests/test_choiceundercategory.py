#Test Senaryosu  Adı: Seçilen Kategoriye göre Kursların Listelenmesi
#Test Case2: Alt kategori seçilerek kursların listelenmesi kontrolü 
# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from constants import categoryConstants as cco
from time import sleep


class TestChoiceundercategory():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.get(cco.PORTAL_URL)
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_choiceundercategory(self):
    #self.driver.get("https://www.btkakademi.gov.tr/portal")
    #self.driver.set_window_size(1382, 744)
    sleep(3)
    system_button=self.driver.find_element(By.ID,cco.SYSTEM_WORLD_BUTTON_ID)
    system_button.click()
    sleep(4)
    direction_button=self.driver.find_element(By.XPATH,cco.DIRECTION_BUTTON_XPATH)
    direction_button.click()
    cybersecurity_button=self.driver.find_element(By.XPATH,cco.CYBER_SECURITY_XPATH)
    cybersecurity_button.click()
    total_education=self.driver.find_element(By.XPATH,cco.REVEALED2_EDUCATION_XPATH)
    assert total_education.text ==cco.EVIDENCE2_EDUCATION_TEXT
    

