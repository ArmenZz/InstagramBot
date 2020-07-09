from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import configparser
import functools
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class InstagramBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--mute-audio")
        self.bot      = webdriver.Chrome(chrome_options=chrome_options)

    def login(self):
        bot = self.bot
        bot.get('https://instagram.com/accounts/login')
        time.sleep(1)
        bot.find_element_by_name('username').send_keys(self.username)
        bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)
        time.sleep(3)


    def likeLink(self,link):

        bot= self.bot
        bot.get(link)
        try:
            wait = WebDriverWait(bot, 20).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button')))
            wait.click()                                                                                                              
        except Exception:
            print("wtf went wrong bruh")
        
        time.sleep(1)

    
    def followUser(self,user):
        bot=self.bot
        bot.get('https://www.instagram.com/' + user)
        try:
            wait1 = WebDriverWait(bot, 10).until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')))
            wait1.click()                                                                    
        except Exception:
            print("Follow Button Variation 1 Not Found")
            try:
                wait2 = WebDriverWait(bot, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[2]/button')))
                wait2.click()                                                                    
            except Exception:
                print("Follow Button Variation 2 Not Found")
                try:
                    wait3 = WebDriverWait(bot, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[1]/button')))
                    wait3.click()                                                                       
                except Exception:
                    print('Follow Button Variation 3 Not Found')
                   
        time.sleep(1)


    def viewLink(self,link):

        bot= self.bot
        bot.get(link)
        try:
            wait = WebDriverWait(bot, 20).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[1]/div/div/div[3]')))
            wait.click()                                                                                                              
        except Exception:
            print("rah wtf")
        time.sleep(10)




    def exitBot(self):

        bot= self.bot
        bot.close()


config_file_path = './config.ini'
path = config_file_path.split('.')
assert(path[len(path)-1] == 'ini')
config = configparser.ConfigParser()
config.read(config_file_path)

insta = InstagramBot(config['ACCOUNTS']['account1'],'yourpassword')
insta.login()
#insta.followUser(config['IG_SETTINGS']['USER'])
#insta.viewLink(config['IG_SETTINGS']['VIEWLINK'])
#insta.likeLink(config['IG_SETTINGS']['LIKELINK'])
insta.exitBot()
