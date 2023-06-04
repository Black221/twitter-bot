import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def document_initialised(driver):
    return driver.find_element(By.ID, 'choice-1685059209622')
quitte = False
succes = 0

nombre_aleatoire = random.randint(3, 5)
(str(nombre_aleatoire) + "s")
options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)
driver.get('https://twitter.com/joloffpapi/status/1665029495307350016')
driver.implicitly_wait(nombre_aleatoire)
WebDriverWait(driver, timeout=10).until(document_initialised)

# Boucle pour répéter l'opération 10 fois
for _ in range(10000):
    try:
        # Initialisation du pilote Chrome WebDriver
        if(quitte):
            nombre_aleatoire = random.randint(3, 5)
            (str(nombre_aleatoire) + "s")
            driver = webdriver.Chrome()
            driver.get('https://twitter.com/joloffpapi/status/1665029495307350016')
            driver.implicitly_wait(nombre_aleatoire)
            WebDriverWait(driver, timeout=10).until(document_initialised)
            quitte = False

        # Sélection de la reine et soumission du vote
        start = time.time()
        tweet = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block public-DraftStyleDefault-ltr')
        tweet.text = "@elonmusk"
        submit_button = driver.find_element(By.CLASS_NAME, 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0')
        submit_button.click()
        end = time.time()
        duree = start - end

        succes = succes + 1
        print(str(succes) + " vote - Confirmation : Succès")

        # Temps d'attente aléatoire entre 0 secondes et 10 s
        wait_time = random.randint(0, int(duree)+1)
        time.sleep(wait_time)



    except NoSuchElementException as e:
        quitte = True
        print("Élément non trouvé : ", str(e))
        print(" vote - Confirmation : Échec")
        driver.quit()


    except Exception as e:
        print("Erreur inattendue : ", str(e))
        print(" vote - Confirmation : Échec")