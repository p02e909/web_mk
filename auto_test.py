from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from time import sleep

ids = []
url = 'https://facebook.com'
with open('pass.txt', 'rt') as f:
    pwd = f.read()
#---------------------------------------------------

browser = webdriver.Firefox()
browser.get(url)
#---------------------------------------------------


def learn():
    username = browser.find_element_by_id('email')
    username.send_keys('p02e909@gmail.com')

    password = browser.find_element_by_id('pass')
    password.send_keys('asdf')

    sleep(2)
    submit = browser.find_element_by_id('u_0_2')
    submit.click()
#---------------------------------------------------

    password_when_fail = browser.find_element_by_id('pass')
    password_when_fail.send_keys(pwd)

    submit = browser.find_element_by_id('loginbutton')
    submit.click()
#---------------------------------------------------


def test_UI(ids):
    for elem in ids:
        clicker = browser.find_element_by_id(elem)
        sleep(3)
        print("{}: done".format(elem))


def main():
    test_UI(ids)
    print("ALL: done")
    #browser.quit()


if __name__ == "__main__":
    main()
