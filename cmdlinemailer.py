#! python3
# cmdlinemailer.py - takes 2 arguments, an e-mail and a message
# and then uses selenium to go into an email and send an e-mail
# Lines 39, 48 and 66 require you to put in your own email and password or change to input()


import sys, re, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Please type in an e-mail address, and the message you'd like to send")
#Take email and string of text from command line

email_regex = re.compile(r'^.*@.*')
print(sys.argv[1] + sys.argv[2])
email_mo = email_regex.findall(sys.argv[1])
print(email_mo)

while email_mo == []:
    print(r'The e-mail you entered is invalid. Please try again.')
    email_mo = email_regex.findall(input('please enter a new e-mail address:   \n'))

email_message = str(' '.join(sys.argv[2:]))
print('Sending e-mail to: \n->' + email_mo[0].ljust(3,' '))
print('E-mail message is: \n->' + email_message.ljust(3,' '))

#TODO: Open firefox and navigate to gmail

browser = webdriver.Firefox()
browser.get('https://gmail.com')

#TODO: login using credentials

login_elem = browser.find_element_by_css_selector('#identifierId')
login_elem.click()
login_elem.send_keys('EMAIL')
login_elem.send_keys(Keys.ENTER)
time.sleep(3)

pass_elem = browser.find_element_by_css_selector('#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
##wrong_password = browser.find_elements_by_css_selector('.OyEIQ')
pass_elem.click()
##print('please type in your password:')
##pass_elem.send_keys(str(input()))
pass_elem.send_keys('PASSWORD')
pass_elem.send_keys(Keys.ENTER)
time.sleep(5) #login time, waiting for the page to load before checking success/fail

# Checking to see if the password was correct
wrong_password = browser.find_elements_by_css_selector('.OyEIQ')
print(wrong_password)
while wrong_password != []:
    print('the password was wrong')
    print('Please re-enter your password')
    pass_elem.send_keys(str(input()))
    pass_elem.send_keys(Keys.ENTER)
    time.sleep(5)
    wrong_password = browser.find_elements_by_css_selector('.OyEIQ')
print('successfully logged in')

try:
    compose_element = WebDriverWait(browser,20).until(
        EC.title_contains('EMAIL'))
    print(r"Yay, You're in!")
except:
    print('not loading yet')

compose_element = browser.find_element_by_css_selector('.T-I-KE')
compose_element.click()

time.sleep(10)


#Navigate to compose, enter in email and text to field and send
compose_element = browser.find_element_by_name("to")
compose_element.send_keys(str(email_mo[0]))

compose_element = browser.find_element_by_name("subjectbox")
compose_element.send_keys(str('testing web scraping'))

compose_element = browser.find_element_by_css_selector("div[aria-label='Message Body']")
compose_element.send_keys(str(email_message))

compose_element = browser.find_element_by_css_selector("div[aria-label=\'Send ‪(Ctrl-Enter)‬\']")
compose_element.click()

print('e-mail sent!')

browser.quit()





