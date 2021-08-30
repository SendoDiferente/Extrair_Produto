import time
from selenium import webdriver

from Extracao_site.AguardarElemento import *


def extracted_site(site_name):
    driver = webdriver.Chrome("chromedriver/chromedriver.exe")
    driver.get(site_name)
    driver.maximize_window()
    aguardarclique(driver, 10, "//*[@id='home-firstscreen']/div/div/div[2]/div/div/div[2]/dl[5]/dt/span/a")
    aguardarclique(driver, 10, "/html/body/div[3]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/ul/li[2]")
    x = 1

    for x in range(100):
        try:
            print(x)
            time.sleep(2)
            nome_produto = ExtrairTexto(driver,
                                        f"/html/body/div[3]/div/div/div[2]/div[2]/div/div[2]/div[{x}]/div/div[1]/a/span")
            total_de_vendidos1 = ExtrairTexto(driver,
                                              f"/html/body/div[3]/div/div/div[2]/div[2]/div/div[2]/div[{x}]/div/div[3]/a/span").split(
                " ")

            if total_de_vendidos1 is None:
                total_de_vendidos1 = ExtrairTexto(driver,
                                                  f"/html/body/div[3]/div/div/div[2]/div[2]/div/div[2]/div[{x}]/div/div[4]/a/span").split(
                    " ")
            total_de_vendidos = total_de_vendidos1[0]

            avaliacao_produto = ExtrairTexto(driver,
                                             f"/html/body/div[3]/div/div/div[2]/div[2]/div/div[2]/div[{x}]/div/div[3]/div/a/span")
            if avaliacao_produto is None:
                avaliacao_produto = ExtrairTexto(driver,
                                                 f"/html/body/div[3]/div/div/div[2]/div[2]/div/div[2]/div[{x}]/div/div[4]/div/a/span").split()

            preco1 = ExtrairTexto(driver,
                                  f"/html/body/div[3]/div/div/div[2]/div[2]/div/div[2]/div[{x}]/div/div[2]/div").split()
            if preco1 is None:
                preco1 = ExtrairTexto(driver,
                                      f"/html/body/div[3]/div/div/div[2]/div[2]/div/div[2]/div[{x}]/div/div[3]/div").split()
            preco = preco1[1]
        except:
            print(x)
