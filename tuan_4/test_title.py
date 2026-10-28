#!/usr/bin/env python
# coding: utf-8

# In[4]:



from selenium import webdriver

def test_page_title():
    driver = webdriver.Chrome()

    driver.get("https://the-internet.herokuapp.com/")

    assert driver.title == "The Internet"

    driver.quit()


# In[ ]:




