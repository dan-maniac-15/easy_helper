#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def click_button(webbrowser, xpath):
    elem_button = WebDriverWait(webbrowser, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    actions = ActionChains(webbrowser)
    actions.move_to_element(elem_button)
    actions.click(elem_button)
    actions.perform() 
    return webbrowser

def move_button(webbrowser, xpath):
    elem_button = WebDriverWait(webbrowser, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    actions = ActionChains(webbrowser)
    actions.move_to_element(elem_button)
    actions.perform() 
    return webbrowser

def input_texts(webbrowser, xpath, texts):
    elem_input = WebDriverWait(webbrowser, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    elem_input.clear()
    elem_input.send_keys(texts)
    return webbrowser

def get_webbrowser(status):
    """open google chrome"""
    #selenium
    selenium_directory = "/usr/bin/chromedriver"
    #headless mode
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument("--window-size=1920x1080")
    if(status == "server"):
        options.add_argument('--headless')
        chrome_service = fs.Service(executable_path=selenium_directory) 
        webbrowser = webdriver.Chrome(service=chrome_service, options=options)
    else:
        webbrowser = webdriver.Chrome(options=options)
    
    return webbrowser