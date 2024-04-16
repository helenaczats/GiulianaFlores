#Framework de Teste de Unidade

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

class Teste_usuario():
    
  url = "https://www.giulianaflores.com.br"
  
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(10)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_criar_usuario(self):
      
    self.driver.get("https://www.giulianaflores.com.br/")
    self.driver.set_window_size(1440, 900)
    
    #Home
    self.driver.find_element(By.ID, "perfil-hidden").click() #Menu
    self.driver.find_element(By.ID, "UrlLogin").click() #Login
    
    #Transição de Telas
    self.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click() #criar cadastro
    
    #Cadastro
    self.driver.find_element(By.ID, "ContentSite_txtName").click() #cadastro nome
    self.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Antonio Nogueira") 
    
    self.driver.find_element(By.ID, "ContentSite_txtCpf").click() #cadastro CPF
    self.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys("810.634.782-60")
    
    self.driver.find_element(By.ID, "ContentSite_txtEmail").click() #cadastro email
    self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("antonio.nogueira@viaterrestre.com")
    
    self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").click() #cadastra senha
    self.driver.execute_script("window.scrollTo(0,55)") #rola tela para baixo
    self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("QAZwsx25") 
    
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").click() #cadastra CPF
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("02870-160")
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_btnAddressFind").click() #ok para CEP
    
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").click() #cadastra número da casa
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("162")
    
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").click() #cadastra celular
    self.driver.execute_script("window.scrollTo(0,838)") #rola a tela
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("11981559169")
    
    #Finaliza cadastro
    self.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()
  
   
