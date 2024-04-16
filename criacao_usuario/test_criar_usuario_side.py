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

class TestCriarusuarioGiulianaFlores():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
    self.driver.implicitly_wait(5)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_criarusuarioGiulianaFlores(self):
    self.driver.get("https://www.giulianaflores.com.br/")
    self.driver.set_window_size(1440, 900)
    self.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
    self.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()
    self.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()
    self.driver.find_element(By.ID, "ContentSite_txtName").click()
    self.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Analu Vieira")
    self.driver.find_element(By.ID, "ContentSite_txtCpf").click()
    self.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys("201.773.858-12")
    self.driver.find_element(By.ID, "ContentSite_txtEmail").click()
    self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("analu.vieira@viaterrestre.com")
    self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").click()
    self.driver.execute_script("window.scrollTo(0,55)")
    self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("QAZwsx25")
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").click()
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("02870-160")
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").click()
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("162")
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").click()
    self.driver.execute_script("window.scrollTo(0,838)")
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("11981559169")
    self.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()
  
   