import requests
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display
import dill


class Score:
    team_names_sf = ["KKR","GT","MI","CSK","RR","RCB","PBKS","DC","SRH","LSG"]
    team_names_ff = ["Kolkata Knight Riders", "Gujarat Titans", "Mumbai Indians", "Chennai Super Kings","Rajasthan Royals","Royal Challengers Bangalore", "Punjab Kings","Delhi Capitals","Sunrisers Hyderabad","Lucknow Super Giants"]

    def __init__(self,url):
        self.url = url
        self.player_list,self.winner,self.man_of_the_match,self.innings_list,self.batsmen_list,self.match_score,self.did_not_bat,self.bowlers_info = self.scorecard()

    def find_team(self,text):
        def check_list(team_list):
            matches = [word for word in team_list if word in text]
            if len(matches) > 1:
                raise ValueError(f"Error: More than one match found: {matches}")
            elif len(matches) == 1:
                return matches[0]
            return None

        match = check_list(self.team_names_sf)
        if match:
            return self.team_names_ff[self.team_names_sf.index(match)]
        match = check_list(self.team_names_ff)
        if match:
            return match
        raise ValueError("Error: No match found in either list")

    def scorecard(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }

        response = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        
        innings_list = []
        batsmen_list = pd.DataFrame()
        match_score = pd.DataFrame()
        did_not_bat = pd.DataFrame()
        bowlers_info = pd.DataFrame()
        player_list = pd.DataFrame()

        winner = soup.find('p',class_="ds-text-tight-s ds-font-medium ds-truncate ds-text-typo").text.strip()
        winner = self.find_team(winner)

        match_details_table = soup.find('table',class_= "ds-w-full ds-table ds-table-sm ds-table-auto") 
        table_rows = match_details_table.find_all('tr')
        for row in table_rows:
            if "Player Of The Match" in row.text:
                man_of_the_match = row.find('td',class_="ds-text-typo").text.strip()
        
        innings_tables = soup.find_all('div', class_='ds-rounded-lg ds-mt-2')

        for innings_table in innings_tables:

            innings_number = innings_tables.index(innings_table) + 1

            team_innings_div = innings_table.find('div', class_='ds-flex ds-px-4 ds-border-b ds-border-line ds-py-3 ds-bg-ui-fill-translucent-hover')
            batting_innings = team_innings_div.text.strip().replace('\xa0',' ')
            batting_innings = self.find_team(batting_innings)
                
            innings_list.append(batting_innings)

            
            batsmen_table = innings_table.find('table', class_='ds-w-full ds-table ds-table-md ds-table-auto ci-scorecard-table')
        
            batting_info = batsmen_table.find('tbody')
            batting_info = batting_info.find_all('tr')

            for batter in batting_info:
                try:
                    batsman_stats = batter.find_all('td')
                    name = batsman_stats[0].text.strip()
                    if '†' in name:
                        name = name.replace('†','').strip()
                    if '(c)' in name:
                        name = name.replace('(c)','').strip()
                    dismissal = batsman_stats[1].text.strip()
                    runs = int(batsman_stats[2].text.strip())
                    balls = int(batsman_stats[3].text.strip())
                    fours = int(batsman_stats[5].text.strip())
                    sixes = int(batsman_stats[6].text.strip())
                    strike_rate = float(batsman_stats[7].text.strip())
                            
                    batsmen_stat = {'Innings Number': innings_number,
                        'Innings Name': batting_innings,
                        'Batsman': name,
                        'Dismissal': dismissal,
                        'Runs': runs,
                        'Balls': balls,
                        '4s': fours,
                        '6s': sixes,
                        'Strike Rate': strike_rate
                    }
                    batsmen_list = batsmen_list._append(batsmen_stat, ignore_index = True)
                    player_list = player_list._append({'Team':batting_innings, 'Player': name}, ignore_index = True)
                    d += 1
                except:
                    pass

            did_not_bat_row = batsmen_table.find('tr', class_='!ds-border-b-0')
            if did_not_bat_row:
                batsmen = did_not_bat_row.find_all('div', class_='ds-popper-wrapper ds-inline')
                for batsman in batsmen:
                    batsman_name = (batsman.get_text(strip=True)).replace(",", "")
                    if '†' in batsman_name:
                        batsman_name = batsman_name.replace('†','').strip()
                    if '(c)' in batsman_name:
                        batsman_name = batsman_name.replace('(c)','').strip()
                    did_not_bat = did_not_bat._append({'Innings Number': innings_number, 'Innings Name': batting_innings, 'Batsman':batsman_name}, ignore_index = True)
                    player_list = player_list._append({'Team':batting_innings, 'Player': batsman_name}, ignore_index = True)
                    
            bowling_table = innings_table.find('table', class_='ds-w-full ds-table ds-table-md ds-table-auto')

            if bowling_table:
                headers = []
                head_data = bowling_table.find_all('th')
                for bowler_header in head_data:
                    headers.append(bowler_header.text.strip())
                headers = list(map(lambda x: "Bowler" if x == "Bowling" else x, headers))
                headers = list(map(lambda x: "Overs" if x == "O" else x, headers))
                headers = list(map(lambda x: "Maidens" if x == "M" else x, headers))
                headers = list(map(lambda x: "Runs" if x == "R" else x, headers))
                headers = list(map(lambda x: "Wickets" if x == "W" else x, headers))
                headers = list(map(lambda x: "Economy" if x == "ECON" else x, headers))
                
                bowler_rows = bowling_table.find('tbody').find_all('tr')
                for row in bowler_rows:
                    bowler_data = {}
                    bowler_data['Innings Number'] = innings_number
                    bowler_data['Innings Name'] = batting_innings
                    bowler_row_data = row.find_all('td')

                    try:
                        for i in range(len(headers)):
                            if headers[i] in ["Maidens","Runs", "Wickets","0s"]:
                                bowler_data[headers[i]] = int(bowler_row_data[i].text.strip())
                            elif headers[i] in ["Overs","Economy"]:
                                bowler_data[headers[i]] = float(bowler_row_data[i].text.strip())
                            elif headers[i] == "Bowler":
                                bowler_data[headers[i]] = (bowler_row_data[i].text.strip())
                        bowlers_info = bowlers_info._append(bowler_data, ignore_index = True)
                    except:
                        pass
        return player_list, winner, man_of_the_match, innings_list, batsmen_list, match_score, did_not_bat, bowlers_info
    
    def printing_scorecard(self):
        print("Player List:")
        print(self.player_list)
        print()
        for innings in self.innings_list:
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")  
            print(innings + ":")
            print()
        
            print("Batsmen:")
            print(self.batsmen_list[self.batsmen_list['Innings Name'] == innings].drop(columns=['Innings Number', 'Innings Name']))
            print()

            if self.did_not_bat.empty == False:
                if self.did_not_bat[self.did_not_bat['Innings Name'] == innings].empty == False:
                    print("Did Not Bat:")
                    print(self.did_not_bat[self.did_not_bat['Innings Name'] == innings].drop(columns=['Innings Number', 'Innings Name']))
                    print()

            print("Bowlers:")
            print(self.bowlers_info[self.bowlers_info['Innings Name'] == innings].drop(columns=['Innings Number', 'Innings Name']))
            print()
        
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ") 
        print("Winner: ",self.winner)
        print()
        print("Man of the Match: ",self.man_of_the_match)

url = "https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/kolkata-knight-riders-vs-sunrisers-hyderabad-final-1426312/full-scorecard"
match1 = Score(url)
match1.printing_scorecard()
        
# class Player
# class Team
class Series:
    def __init__(self,url):
        self.url = url
        self.match_links = self.match_link_generator()
        self.match_objects = []
        for match in self.match_links:
            try:
                self.match_objects.append(Score(match))
            except:
                pass
    
    def match_link_generator(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }

        response = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        match_links = []
        match_boxes = soup.find_all('div')
        for match_box in match_boxes:
            try:
                link_part = match_box.find('a',class_="ds-no-tap-higlight")['href']
                if "indian-premier-league" in link_part or "ipl-2025" in link_part:
                    match_link = "https://www.espncricinfo.com" + link_part
                    if match_link not in match_links:
                        match_links.append(match_link)
            except:
                pass
        return match_links
    
#ipl2024 = Series("https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/match-schedule-fixtures-and-results")
#print(ipl.match_links)

ipl2025 = Series("https://www.espncricinfo.com/series/ipl-2025-1449924/match-schedule-fixtures-and-results")
print(ipl2025.match_links)
print(len(ipl2025.match_links))     

# Save list of objects to a file
with open("ipl2025matches.pkl", "wb") as file:
    dill.dump(ipl2025, file)

print("Players list saved successfully!")