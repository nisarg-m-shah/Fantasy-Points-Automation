import requests
from bs4 import BeautifulSoup
import re
import time
import pandas as pd
import os

def extract_team_players(players_list, impact_sub_class):
    team = []
    for i in range(16):
        if i > 10:
            impact_sub = players_list[i].find('span', class_= impact_sub_class)
            if impact_sub is None:
                continue
            else:
                player = clean_player_name(players_list[i].text)
                team.append(player)
                break
        player = clean_player_name(players_list[i].text)
        team.append(player)
    return team

def clean_player_name(text):
    return text.split('      ')[1].split('  ')[0].split(' (C)')[0].split(' (WK)')[0].strip()

def match_squads_generator(ipl_url, match_number):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    response = requests.get(ipl_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    matches = soup.find_all('div', class_='cb-col-75 cb-col')
    match = matches[match_number - 1]
    match_link = "https://www.cricbuzz.com" + match.find('a')['href']
    
    if 'live-cricket-scores' in match_link:
        match_link = match_link.replace('live-cricket-scores', 'cricket-match-squads')
    elif 'cricket-scores' in match_link:
        match_link = match_link.replace('cricket-scores', 'cricket-match-squads')

    response_squads = requests.get(match_link, headers=headers)
    soup_squads = BeautifulSoup(response_squads.content, "html.parser")

    players_team1 = soup_squads.find_all('a', class_='cb-col cb-col-100 pad10 cb-player-card-left')
    players_team2 = soup_squads.find_all('a', class_='cb-col cb-col-100 pad10 cb-player-card-right')

    team1 = extract_team_players(players_team1, "cb-plus-match-change-icon cb-bg-min cb-match-change-left")
    team2 = extract_team_players(players_team2, "cb-plus-match-change-icon cb-bg-min cb-match-change-right")

    return team1, team2

ipl24 = "https://www.cricbuzz.com/cricket-series/7607/indian-premier-league-2024/matches"
ipl25 = "https://www.cricbuzz.com/cricket-series/9237/indian-premier-league-2025/matches"
team1,team2 = match_squads_generator(ipl24,7)
print(team1)
print(team2)