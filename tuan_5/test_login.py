#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_success():
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        message = driver.find_element(By.ID, "flash").text

        assert "You logged into a secure area!" in message
    finally:
        driver.quit()


def test_wrong_password():
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("WrongPassword")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        message = driver.find_element(By.ID, "flash").text

        assert "Your password is invalid!" in message
    finally:
        driver.quit()


def test_wrong_username():
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        driver.find_element(By.ID, "username").send_keys("wronguser")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        message = driver.find_element(By.ID, "flash").text

        assert "Your username is invalid!" in message
    finally:
        driver.quit()


# In[ ]:




