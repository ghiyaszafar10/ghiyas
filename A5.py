from random import random
import urllib.request
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://unsplash.com/s/photos/nature")
d = driver.find_element_by_css_selector("#app")
im = d.find_elements_by_tag_name("img")
c=1
for i in im:
    link = i.get_attribute("src")
    link1 = i.get_attribute("class")
    if link1 == "YVj9w":
        Path = "Nature\\" + str(random()) + ".jpg"
        urllib.request.urlretrieve(link,Path)
        if c==10:
            break
        c=c+1
driver.close()

from random import random
import urllib.request
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://unsplash.com/s/photos/beach")
d = driver.find_element_by_css_selector("#app")
im = d.find_elements_by_tag_name("img")
c=1
for i in im:
    link = i.get_attribute("src")
    link1 = i.get_attribute("class")
    if link1 == "YVj9w":
        Path = "Beach\\" + str(random()) + ".jpg"
        urllib.request.urlretrieve(link,Path)
        if c==10:
            break
        c=c+1
driver.close()

from random import random
import urllib.request
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://unsplash.com/s/photos/animals")
d = driver.find_element_by_css_selector("#app")
im = d.find_elements_by_tag_name("img")
c=1
for i in im:
    link = i.get_attribute("src")
    link1 = i.get_attribute("class")
    if link1 == "YVj9w":
        Path = "Animal\\" + str(random()) + ".jpg"
        urllib.request.urlretrieve(link,Path)
        if c==10:
            break
        c=c+1
driver.close()