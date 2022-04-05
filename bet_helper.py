from selenium import webdriver
from selenium.webdriver.common.by import By
from func import find_all_teams, nearbly_matches
from prettytable import PrettyTable

dict_leagues = {
    'Premier League' : 'https://www.flashscore.com/football/england/premier-league/',
    'Ligue 1' : 'https://www.flashscore.com/football/france/ligue-1/',
    'Bundesliga' : 'https://www.flashscore.com/football/germany/bundesliga/',
    'Serie A' : 'https://www.flashscore.com/football/italy/serie-a/',
    'LaLiga' : 'https://www.flashscore.com/football/spain/laliga/',
}

leagues = ['Premier League', 'Ligue 1', 'Bundesliga', 'Serie A', 'LaLiga']

options = webdriver.FirefoxOptions() # init variable with options
options.set_preference('dom.webdriver.enabled', False) # Hide selenium serfing
options.set_preference('dom.webnotifications.enabled', False) # Disable notifications
options.set_preference('dom.volume_scale', '0.0') # Disable sounds
options.headless = True # Disable browser interface

browser = webdriver.Firefox(options=options)

for league in leagues:
    print('***********************************************************')
    print(league)
    print('***********************************************************')
    teams = find_all_teams(dict_leagues[league], browser)
    matches = nearbly_matches(dict_leagues[league], browser)
    table = PrettyTable()
    table.field_names = ['№', 'Home team', '-', 'Away team', 'Predicted winner']
    count = 0
    for match in matches:
        count += 1
        if teams[match[0]] == 5 and teams[match[1]] < 3:
            table.add_row([count, match[0], '-', match[1], match[0]])
        elif teams[match[0]] == 4 and teams[match[1]] < 2:
            table.add_row([count, match[0], '-', match[1], match[0]])
        else:
            table.add_row([count, match[0], '-', match[1], 'not predictable'])
    print(table)


browser.quit()