from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://lms.umt.edu.pk/login/index.php")
driver.find_element_by_id("username").send_keys("f2019065218@umt.edu.pk")
driver.find_element_by_id("password").send_keys("06e7c41C@")
driver.find_element_by_css_selector("#loginbtn").click()

