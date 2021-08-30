from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def aguardarclique(driver, tempo, elemento):
    try:
        element = WebDriverWait(driver, tempo).until(
            EC.presence_of_element_located((By.XPATH, elemento))
        )
        element.click()
    except:
        print("1")

def AguardeElemento(driver, tempo, elemento):
    try:
        element = WebDriverWait(driver, tempo).until(
            EC.presence_of_element_located((By.XPATH, elemento))
        )
    except:
        print("1")


def ExtrairTexto(driver, elemento):
    try:
        variavel = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, elemento))).text
        return variavel
    except:
        print("1")

