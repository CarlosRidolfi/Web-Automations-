from selenium import webdriver

browser =  webdriver.Chrome()

url = 'http://www.google.com'
search_path = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
enter_path = 'btnK'
dEd = '//*[@id="rso"]/div[3]/div/div/div[1]/a'

browser.get(url)

browser_search = browser.find_element_by_xpath(search_path)

browser_search.send_keys('Dungeons and Dragons')

browser_search.submit()

search_link = browser.find_element_by_xpath(dEd)

search_link.click()