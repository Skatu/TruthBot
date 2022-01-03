from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback

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

def click_btn_to_generate_img(driver, xpath):
    print("getting generator button...")   
    WebDriverWait(driver,10).until(
      EC.element_to_be_clickable((By.XPATH,xpath))
    )
    btn=driver.find_element_by_xpath(xpath)
    print("button found")
    btn.click()
    print("button clicked")  

def get_img(driver, xpath):
    print("getting image..")
    WebDriverWait(driver, 10).until(
      lambda driver: driver.find_element_by_xpath(xpath).get_attribute('src') != ''
    )
    img=driver.find_element_by_xpath(xpath)
    print("img:", img)
    link=img.get_attribute('src')
    print("link:",link)
    return link

def getinspirationalimage():  
  url='https://inspirobot.me/'
  btn_xpath='//*[@id="top"]/div[1]/div[2]/div/div[2]'
  img_xpath='/html/body/div[2]/div[1]/div[1]/div[1]/img'
  driver=get_driver()
  try:
    open_website(driver,url)
    click_btn_to_generate_img(driver,btn_xpath)
    return get_img(driver, img_xpath)
  except:
    print("erro ao obter imagem")
    print(traceback.format_exc())
    return "Deu merda. Não há inspiração para ninguém .l."
  finally:
    driver.quit()