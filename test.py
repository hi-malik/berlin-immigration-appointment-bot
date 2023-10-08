from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/jaidevsinghmalik/Desktop/berlin-auslanderbehorde-termin-bot/chrome-mac-x64')
driver.get("http://www.google.com")
driver.quit()
