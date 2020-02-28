



from selenium import webdriver
import selenium
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
        sleep(5)
        perm='y'
        while perm=='y':
            answer=[]
            answer=input('|Wiley | Check all the subjects\nWhat would you like to do with the bot: ')
            
            if answer == 'Check all the subjects': 
                
                Data_sci = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[13]/div/div[2]/div/div[2]/bb-base-course-card/div[1]')
                Data_sci.click()
                sleep(10)
                self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[2]/button').click()
                
                logic_clk = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[13]/div/div[2]/div/div[5]/bb-base-course-card/div[1]')
                sleep(2)
                logic_clk.click()
                sleep(10)
                self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[2]/button').click()

                DE_clk = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]\
                    /div/div/div[13]/div/div[2]/div/div[3]/bb-base-course-card')
                sleep(2)
                DE_clk.click()
                sleep(10)
                self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[2]/button').click()

                fil_clk = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]\
                    /div[1]/div/div/div[13]/div/div[2]/div/div[6]/bb-base-course-card')
                sleep(2)
                fil_clk.click()
                sleep(10)
                self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[2]/button').click()

                
                sofdev_clk = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]\
                    /div[1]/div/div/div[13]/div/div[2]/div/div[7]/bb-base-course-card')
                sleep(2)
                sofdev_clk.click()
                sleep(10)
                self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[2]/button').click()

                
                sofdevl_clk = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]\
                    /div[1]/div/div/div[13]/div/div[2]/div/div[8]/bb-base-course-card')
                sleep(2)
                sofdevl_clk.click()
                sleep(10)
                self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[2]/button').click()
                     
            elif answer == 'Wiley':
                print('Loading...')
                self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/header/section').click()
                sleep(2)
                self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[4]/li').click()
                sleep(2)
                self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[13]/div/div[2]/div/div[3]/bb-base-course-card').click()
                sleep(2)
                self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div/div/iframe'))
                sleep(2)
                self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div/div/div[2]/ul/li[28]/div[1]/h3/a').click()
                sleep(2)
                self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[2]/ul/li[9]/div[1]/h3/a').click()
          
            else:
                print('invalid output')
            
            
            
            perm = input('Would you like to check out blackboard more? ')
            if perm == "y": 
                if answer == 'Check all the subjects':
                    continue
                elif answer == 'Wiley':
                    print('Loading...')
                    self.driver.switch_to.default_content()
                    self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[2]/button').click()
                    self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/header/section').click()
                    self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]').click()
                else:
                    continue
            elif perm == 'n':
                print('\n\n\n\t\t\tG\tO\tO\tD\t\t\tB\tY\tE    !\n\n\n')
                break
            else:
                
                while perm != 'y':
                    perm = []
                    print('Invalid Input!')
                    perm = input('Would you like to check out blackboard more? ')
                    if perm == 'n':
                        print('\n\n\n\t\t\tG\tO\tO\tD\t\t\tB\tY\tE    !')
                        break
                    
                try:
                    if answer == 'Check all the subjects':
                        continue
                    elif answer == 'Wiley':
                        print('Loading...')
                        self.driver.switch_to.default_content()
                        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[2]/button').click()                            
                        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/header/section').click()
                        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]').click()
                    else:
                        continue
                except:
                    continue


bot = Blackboardbot()
bot.login()


