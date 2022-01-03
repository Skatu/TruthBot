from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_driver():
  chromeOptions = Options()
  chromeOptions.add_argument('headless')
  chromeOptions.add_argument('--no-sandbox')
  chromeOptions.add_argument('--disable-dev-shm-usage')
  return webdriver.Chrome(options=chromeOptions)

def open_website(driver, url):
    print("opening website...")
    driver.get(url)
    print("site opened")


def get_nouns(driver):
  URL='https://www.textfixer.com/tools/random-nouns.php'
  XPATH='//*[@id="wordList"]'
  ID1='wordspan0'
  ID2='wordspan2'
  open_website(driver,URL)
  WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,XPATH))
  )
  w1=driver.find_element_by_id(ID1).text
  w2=driver.find_element_by_id(ID2).text
  return [w1,w2]


def get_verb(driver):
  URL='https://www.textfixer.com/tools/random-verbs.php'
  XPATH='//*[@id="wordspan0"]'
  open_website(driver,URL)
  WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,XPATH))
  )
  return driver.find_element_by_xpath(XPATH).text


def get_phrase():
  driver=get_driver()
  nouns=get_nouns(driver)
  verb=get_verb(driver)
  if verb.endswith('h'):
    verb+='e'
  verb+='s'
  driver.quit()
  return 'The '+nouns[0]+' '+verb+' the '+nouns[1]+'.'