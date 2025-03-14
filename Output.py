import dill
from Scraping import Series,Score,find_full_name
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display
from rapidfuzz import process
from Points import Player,Team,Match
import re
import xlsxwriter

if __name__ == '__main__':
    begin = time.time()
    team_names_sf = ["KKR","GT","MI","CSK","RR","RCB","PBKS","DC","SRH","LSG"]
    team_names_ff = ["Kolkata Knight Riders", "Gujarat Titans", "Mumbai Indians", "Chennai Super Kings","Rajasthan Royals","Royal Challengers Bengaluru", "Punjab Kings","Delhi Capitals","Sunrisers Hyderabad","Lucknow Super Giants"]
    cricbuzz_page_link = "https://www.cricbuzz.com/cricket-series/7607/indian-premier-league-2024/matches"   
    ipl24_url = "https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/match-schedule-fixtures-and-results"
    ipl2024 = Series(ipl24_url,cricbuzz_page_link)
    match_objects = ipl2024.match_objects

    teams = {'Participant1':['Shivam Dube','Mahendra Singh Dhoni','Sai Kishore','Noor Ahmad','Sandeep Sharma'],
             'Participant2':['K Sharma','Kohli','Narine','V Iyer']
             }

    #url = "https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/royal-challengers-bengaluru-vs-kolkata-knight-riders-10th-match-1422128/full-scorecard"             
    cricbuzz_page_link = "https://www.cricbuzz.com/cricket-series/7607/indian-premier-league-2024/matches"   
    match_urls = list(match_objects.keys())
    spreadsheet = {}
    spreadsheet['Team Final Points'] = {}
    for match_number in range(1,72):
        match_url = match_urls[match_number-1]
        match_object = match_objects[match_url]
        #match_object.printing_scorecard()
        match_name = match_url.split('/')[-2]
        parts = match_name.split('-')
        #print(parts)
        #print(match_name)
        #print(match_name)
        if 'eliminator' in parts:
            match_name = 'Eliminator'
        elif 'final' in parts:
            match_name = 'Final'
        elif 'qualifier' in parts:
            if '1' in parts:
                match_name = "Qualifier 1"
            else:
                match_name = "Qualifier 2"
        else:
            match_name = " ".join(parts[:-3])
        match_name = match_name.title()
        match_name = match_name.replace('Vs','vs')
        for ipl_team in team_names_ff:
            if ipl_team in match_name:
                match_name = match_name.replace(ipl_team,team_names_sf[team_names_ff.index(ipl_team)])
        match = Match(teams,match_object)
        team_breakdown = match.match_points_breakdown
        General_points_list = match.general_player_points_list

        spreadsheet[(match_name+" - Points Breakdown")] = General_points_list
        spreadsheet[(match_name+" - CFC Points")] = team_breakdown
        final_points = spreadsheet['Team Final Points']
        for team in list(team_breakdown.index):
            final_points.setdefault(team, {}).setdefault("Total Points", 0)
            final_points[team][match_name] = team_breakdown.loc[team,'Total Points']
            final_points[team]['Total Points'] += final_points[team][match_name]
            spreadsheet['Team Final Points'] = dict(sorted(final_points.items(), key=lambda x: x[1]['Total Points'], reverse=True))
        print(match_name,"added")

    file_path = "CFC Fantasy League.xlsx"
    # Write to Excel
    with pd.ExcelWriter(file_path, engine="xlsxwriter") as writer:
        for sheet_name, data in spreadsheet.items():
            if isinstance(data, dict):  # If it's a dictionary, convert it to a DataFrame
                df = pd.DataFrame.from_dict(data, orient='index')
            elif isinstance(data, list):  # If it's a list, convert to DataFrame
                df = pd.DataFrame(data)
            else:
                df = data  # If it's already a DataFrame

            df.to_excel(writer, sheet_name=sheet_name)  # Keep index for readability

        print(f"Excel file saved successfully as {file_path} in the current folder.")

    end = time.time()
    total_time_taken = end-begin
    minutes = str(int(total_time_taken/60))
    seconds = str(round(total_time_taken % 60,3))
    total_time_taken = minutes+"m "+seconds+"s"
    print(f"Time taken to process data: {total_time_taken}")        



        

