
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

class TestLoginNegativo():
    
  url = "https://www.giulianaflores.com.br"
  
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(10)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_loginNegativo(self):
      
    self.driver.get("https://www.giulianaflores.com.br/")
    self.driver.set_window_size(1440, 807)
    
    #Login
  
    self.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click() #menu Home
    self.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click() #botão login
    
    self.driver.find_element(By.ID, "ContentSite_txtEmail").click() #digitar email (usuário correto)
    self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("vinicius.manuel.dasilva@icloud.com")
    
    self.driver.find_element(By.ID, "ContentSite_txtPassword").click() #digitar senha incorreta (1)
    self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("ujh")
    
    self.driver.find_element(By.ID, "ContentSite_ibtContinue").click() #botão continuar (1)
    
    self.driver.find_element(By.ID, "ContentSite_txtPassword").click() #por erro do site digitar novamente senha incorreta(1)
    self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("ujh")
    
    self.driver.find_element(By.ID, "adopt-accept-all-button").click() #botão aceitar cookies
    
    time.sleep(10) #tempo para resolver manualmente o captcha
    
    self.driver.find_element(By.ID, "ContentSite_ibtContinue").click() #botão continuar (2)
    
    
  

