from enum import Flag
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def find_all_teams(url, browser):
    wait = WebDriverWait(browser, 20)
    browser.get(f'{url}standings/')
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ui-table')))
    table = browser.find_element(By.CLASS_NAME, value='ui-table')
    rows = table.find_elements(By.CLASS_NAME, value='ui-table__row  ')

    res = {}
    #count = 0
    for row in rows:
        #count += 1
        team = row.find_element(By.CLASS_NAME, value='tableCellParticipant__name').get_attribute('text')
        form = row.find_elements(By.CLASS_NAME, value='tableCellFormIcon ')
        win = 0
        #lose, draw = 0, 0
        for game in form:
            text = game.find_element(By.TAG_NAME, value='div').get_attribute('innerText')
            if text == 'W':
                win += 1
            # elif text == 'L':
            #     lose += 1
            # elif text == 'D':
            #     draw += 1
        res[team] = win
    return res

def nearbly_matches(url, browser):
    wait = WebDriverWait(browser, 20)
    browser.get(f'{url}fixtures/')
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'bet-ico ')))
    table = browser.find_element(By.ID, value='live-table')
    all_divs = table.find_elements(By.TAG_NAME, value='div')
    rows = []
    flag_round = True
    for div in all_divs:
        if div.get_attribute('title') == 'Click for match detail!':
            rows.append(div)
        # We need only one round
        if div.get_attribute('class') == 'event__round event__round--static':
            if not flag_round:
                break
            flag_round = False
    matches = []
    for row in rows:
        team_1 = row.find_element(By.CLASS_NAME, value='event__participant--home').get_attribute('innerText')
        team_2 = row.find_element(By.CLASS_NAME, value='event__participant--away').get_attribute('innerText')
        matches.append([team_1, team_2])
    return matches