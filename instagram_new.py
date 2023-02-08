#!/usr/bin/env python3

from re import I
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os

from time import sleep

def __get_webbrowser():
    """open google chrome"""
    #headless mode
    options = Options()
    #uncomment this at headless mode
    #options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    #options.add_argument("--window-size=1920x1080")
    options.add_argument("--window-size=760x760")
    webbrowser = webdriver.Chrome(options=options)
    
    return webbrowser


def __login_sequence(webbrowser, username, password):
    """get element of username and password"""
    elem_username = WebDriverWait(webbrowser, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
    elem_password = webbrowser.find_element(By.NAME, "password")
    
    #input username and password
    elem_username.send_keys(username)
    elem_password.send_keys(password)
    
    #click login button
    elem_button = WebDriverWait(webbrowser, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')))
    actions = ActionChains(webbrowser)
    actions.move_to_element(elem_button)
    actions.click(elem_button)
    actions.perform()

    return webbrowser

def __logout_sequence(webbrowser):
    #click hambuger menu
    elem_button = WebDriverWait(webbrowser, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div/div/a')))
    actions = ActionChains(webbrowser)
    actions.move_to_element(elem_button)
    actions.click(elem_button)
    actions.perform()

    sleep(5)

    #click logout button
    elem_button = WebDriverWait(webbrowser, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[1]/div/div[1]/div[7]')))
    actions = ActionChains(webbrowser)
    actions.move_to_element(elem_button)
    actions.click(elem_button)
    actions.perform()

    return webbrowser


def __login_setting(webbrowser):
    """login setting check"""
    #elem_button = WebDriverWait(webbrowser, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')))
    elem_button = WebDriverWait(webbrowser, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')))
    actions = ActionChains(webbrowser)
    actions.move_to_element(elem_button)
    actions.click(elem_button)
    actions.perform()

    return webbrowser

def __notice_setting(webbrowser):
    """notice setting check"""
    #move to next tab
    #webbrowser.switch_to.window(webbrowser.window_handles[1])
    elem_button = WebDriverWait(webbrowser, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
    actions = ActionChains(webbrowser)
    actions.move_to_element(elem_button)
    actions.click(elem_button)
    actions.perform()

    return webbrowser

def __alert_setting(webbrowser):
    """alert setting check"""
    elem_button = WebDriverWait(webbrowser, 3).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
    actions = ActionChains(webbrowser)
    actions.move_to_element(elem_button)
    actions.click(elem_button)
    actions.perform()

    return webbrowser

def __click_good(webbrowser):
    """click good"""
    for i in range(1, 20):
        try:
            #button_path = '' + str(i) + ''
            #button_path = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/section/div/div[3]/div[1]/div/article[' + str(i) + ']/div/div[3]/div/div/section[1]/span[1]/button'
            #elem_first_target = WebDriverWait(webbrowser, 3).until(EC.visibility_of_element_located((By.XPATH, button_path)))
            elem_first_target = WebDriverWait(webbrowser, 3).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "_aamw")))[i]
            actions           = ActionChains(webbrowser)
            actions.move_to_element(elem_first_target)
            actions.click(elem_first_target)
            actions.perform()
        except Exception as e:
            print(e)

def __ret_login_info(file):
    #call the file
    with open(file) as file_data:    
        username = ""
        password = ""
        for line in file_data:
            key   = line.split('=')[0].strip()
            value = line.split('=')[1].strip()
            if key == "username":
                username = value.strip("\"")
            if key == "password":
                password = value.strip("\"")
        return username, password

def __post(webbrowser):
    file_path = os.getcwd() + "/file/"
    file_list = os.listdir(file_path)

    print(file_list[0])

    elem_button = WebDriverWait(webbrowser, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button/div/svg')))
    actions = ActionChains(webbrowser)
    actions.move_to_element(elem_button)
    actions.click(elem_button)
    actions.perform()

    return webbrowser


def main():
    #Instagram URL
    url      = "https://www.instagram.com"

    ############################
    #Login info
    #Create a setting file and put the directory of the file
    #Format
    #username =
    #password =
    #Execute at the directory this python code and the setting file are placed
    ############################

    path = os.getcwd() + "/"
    file = "instagram_setting.txt"

    username, password = __ret_login_info(path + file)

    #open google chrome
    webbrowser = __get_webbrowser()

    #open instagram
    webbrowser.get(url)
    
    sleep(2) #Wait until the page opens
    
    #get element of username and password
    webbrowser = __login_sequence(webbrowser, username, password)
    print('login sequence is done')
    sleep(10)

    #login setting check
    webbrowser = __login_setting(webbrowser)
    print('login settting is done')
    sleep(5)

    #notice setting check
    webbrowser = __notice_setting(webbrowser)
    print('notice settting is done')
    sleep(5)

    #alert setting check
    #webbrowser = alert_setting(webbrowser)
    #sleep(5)

    #click good
    __click_good(webbrowser)   
    sleep(5)    

    #logout
    __logout_sequence(webbrowser)
    sleep(5)    

    webbrowser.close()

if __name__ == "__main__":
    main()
