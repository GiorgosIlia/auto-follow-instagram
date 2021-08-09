# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:46:11 2020

@author: jegen
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox(executable_path= "/path/to/gecko/driver.exe")
driver.get('https://www.instagram.com')
sleep(2)

driver.find_element_by_xpath('//button[text()="Accept"]').click()
sleep(1)

driver.find_element_by_xpath(("//input[@name=\"username\"]"))\
.send_keys(("username"))
driver.find_element_by_xpath(("//input[@name=\"password\"]"))\
.send_keys(("password"))

driver.find_element_by_xpath('//button[@type="submit"]').click()
sleep(5)

driver.find_element_by_xpath('//button[text()="Not Now"]').click()
sleep(5)

driver.find_element_by_xpath('//button[text()="Not Now"]').click()
sleep(5)
for i in range (3):
    for j in range(5):
            driver.find_element_by_xpath('//div[@class="_7UhW9  PIoXz        qyrsm           uL8Hv         " and text()="Follow"]').click()
            sleep(1)
    driver.refresh()
    sleep(2)