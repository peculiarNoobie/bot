from selenium import webdriver
from login import user, password
from time import sleep


class Blackboardbot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        self.driver.get('https://mapua.blackboard.com/webapps/login/')
        sleep(2)
        
        accept1_btn = self.driver.find_element_by_xpath('/html/body/div[8]/div/div\
            /div/div/div/div/div[2]/button')
        accept1_btn.click()
        
        username = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/form/div/ul/li[1]/input')
        username.send_keys(user)
        passwords = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/form/div/ul/li[2]/input')
        passwords.send_keys(password)

        signin_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/form/div/ul/li[3]/input')
        signin_btn.click()
        sleep(2)
        logic_clk = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[13]/div/div[2]/div/div[5]/bb-base-course-card/div[1]')
        sleep(2)
        logic_clk.click()
        sleep(10)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[2]/button').click()
        Data_sci = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[13]/div/div[2]/div/div[2]/bb-base-course-card/div[1]')
        Data_sci.click()
        sleep(10)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[2]/button').click()
        
bot = Blackboardbot()
bot.login()






