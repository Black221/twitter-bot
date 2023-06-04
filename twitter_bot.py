import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


def document_initialised(driver):
    return driver.find_element(By.CLASS_NAME, 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0')


quitte = False
succes = 0

nombre_aleatoire = random.randint(3, 5)
(str(nombre_aleatoire) + "s")

options = Options()
options.page_load_strategy = 'eager'
options.set_preference("webdriver.load.strategy", "unstable")

profile = webdriver.FirefoxProfile()

driver = webdriver.Firefox(firefox_profile=profile, options=options)
driver.get('https://twitter.com/joloffpapi/status/1665029495307350016')
driver.implicitly_wait(nombre_aleatoire)
WebDriverWait(driver, timeout=10).until(document_initialised)


for _ in range(10000):
    try:
       
        if quitte:
            nombre_aleatoire = random.randint(3, 5)
            (str(nombre_aleatoire) + "s")
            driver = webdriver.Firefox(firefox_profile=profile, options=options)
            driver.get('https://twitter.com/joloffpapi/status/1665029495307350016')
            driver.implicitly_wait(nombre_aleatoire)
            WebDriverWait(driver, timeout=10).until(document_initialised)
            quitte = False

      
        start = time.time()
        retweet_button = driver.find_element(By.CLASS_NAME, 'css-18t94o4.css-1dbjc4n.r-1777fci.r-1jayy0c.r-bnwqim')
        retweet_button.click()
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]//span[text()="Retweet"]')))
        retweet_confirm_button = driver.find_element(By.XPATH, '//div[@role="dialog"]//span[text()="Retweet"]')
        retweet_confirm_button.click()
        end = time.time()
        duree = start - end

        succes = succes + 1
        print(str(succes) + " retweet - Confirmation : Succès")

       
        wait_time = random.randint(0, int(duree) + 1)
        time.sleep(wait_time)

    except NoSuchElementException as e:
        quitte = True
        print("Élément non trouvé : ", str(e))
        print(" retweet - Confirmation : Échec")
        driver.quit()

    except Exception as e:
        print("Erreur inattendue : ", str(e))
        print(" retweet - Confirmation : Échec")
