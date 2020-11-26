from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import winsound
import os

# completer avec vos identifiants
mail=""
mdp=""

#initialisation
driver = webdriver.Chrome()
driver.get("https://www.leonard-de-vinci.net/")

#login page 1
id_box = driver.find_element_by_id('login')
id_box.send_keys(mail)
suivant_box=driver.find_element_by_id("btn_next")
suivant_box.click()
#login page 2
driver.implicitly_wait(3)
mdp_box=driver.find_element_by_id("passwordInput")
mdp_box.send_keys(mdp)
connexion_box=driver.find_element_by_id("submitButton")
connexion_box.click()
#tableau de présence
driver.implicitly_wait(3)
driver.get("https://www.leonard-de-vinci.net/student/presences/")
driver.implicitly_wait(3)

#attente cours disponible
while True:
    os.system('cls')
    try:
		#ligne classe en cours
        ligne=driver.find_element_by_class_name("warning")
        ligne.find_element_by_class_name("btn").click()
        break
    except:
        print("Aucun cours en cour pour le moment")
        time.sleep(1)
        driver.refresh()

#ouvre le zoom
driver.find_element_by_xpath(r"/html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/table/tbody/tr/td[4]/a").click()
driver.switch_to.window(driver.window_handles[0])

#test appel ouvert
while True:
    os.system('cls')
    try:
		#son quand l'appel est ouvert
        driver.find_element_by_id("set-presence")
        winsound.Beep(700,500)
        break
    except:
        print(driver.find_element_by_class_name("alert-success").text)
        break
        try :
            pass
        except:
            print("L'appel n'est pas encore ouvert")
            time.sleep(1)
            driver.refresh()





