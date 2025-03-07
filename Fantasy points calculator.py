import requests
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display

class Score:
    team_names_sf = ["KKR","GT","MI","CSK","RR","RCB","PBKS","DC","SRH","LSG"]
    team_names_ff = ["Kolkata Knight Riders", "Gujarat Titans", "Mumbai Indians", "Chennai Super Kings","Rajasthan Royals","Royal Challengers Bangalore", "Punjab Kings","Delhi Capitals","Sunrisers Hyderabad","Lucknow Super Giants"]

    def __init__(self,url):
        self.url = url
        self.winner,self.man_of_the_match,self.innings_list,self.batsmen_list,self.match_score,self.did_not_bat,self.bowlers_info = self.scorecard()

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
        
        # Initialize lists to store data for the match
        innings_list = []
        batsmen_list = pd.DataFrame()
        match_score = pd.DataFrame()
        did_not_bat = pd.DataFrame()
        bowlers_info = pd.DataFrame()

        winner = soup.find('p',class_="ds-text-tight-s ds-font-medium ds-truncate ds-text-typo").text.strip()
        winner = self.find_team(winner)

        match_details_table = soup.find('table',class_= "ds-w-full ds-table ds-table-sm ds-table-auto") 
        table_rows = match_details_table.find_all('tr')
        for row in table_rows:
            if "Player Of The Match" in row.text:
                man_of_the_match = row.find('td',class_="ds-text-typo").text.strip()
        
        # Find all divs with class "ds-rounded-lg ds-mt-2" (which contain innings tables)
        innings_tables = soup.find_all('div', class_='ds-rounded-lg ds-mt-2')

        # Loop through each innings table div
        for innings_table in innings_tables:

            innings_number = innings_tables.index(innings_table) + 1

            # Find the div that contains the team name and innings number
            team_innings_div = innings_table.find('div', class_='ds-flex ds-px-4 ds-border-b ds-border-line ds-py-3 ds-bg-ui-fill-translucent-hover')
            batting_innings = team_innings_div.text.strip().replace('\xa0',' ')
            batting_innings = self.find_team(batting_innings)
                
            innings_list.append(batting_innings)

            
            batsmen_table = innings_table.find('table', class_='ds-w-full ds-table ds-table-md ds-table-auto ci-scorecard-table')
        
            # Batsmen details extraction
            batting_info = batsmen_table.find('tbody')
            batting_info = batting_info.find_all('tr')

            for batter in batting_info:
                try:
                    batsman_stats = batter.find_all('td')
                    name = batsman_stats[0].text.strip()
                    dismissal = batsman_stats[1].text.strip()
                    runs = int(batsman_stats[2].text.strip())
                    balls = int(batsman_stats[3].text.strip())
                    fours = int(batsman_stats[5].text.strip())
                    sixes = int(batsman_stats[6].text.strip())
                    strike_rate = float(batsman_stats[7].text.strip())
                            
                    # Append the details to the list
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
                    d += 1
                except:
                    pass

            # Extract "Did Not Bat" information
            did_not_bat_row = batsmen_table.find('tr', class_='!ds-border-b-0')
            if did_not_bat_row:
                batsmen = did_not_bat_row.find_all('div', class_='ds-popper-wrapper ds-inline')
                for batsman in batsmen:
                    batsman_name = (batsman.get_text(strip=True)).replace(",", "")
                    did_not_bat = did_not_bat._append({'Innings Number': innings_number, 'Innings Name': batting_innings, 'Batsman':batsman_name}, ignore_index = True)

                    
            #Extracting Bowling Info
            bowling_table = innings_table.find('table', class_='ds-w-full ds-table ds-table-md ds-table-auto')

            # Check if the bowling table is present
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
                headers = list(map(lambda x: "Wides" if x == "WD" else x, headers))
                headers = list(map(lambda x: "No Balls" if x == "NB" else x, headers))
                
                bowler_rows = bowling_table.find('tbody').find_all('tr')
                #try:
                for row in bowler_rows:
                    bowler_data = {}
                    bowler_data['Innings Number'] = innings_number
                    bowler_data['Innings Name'] = batting_innings
                    bowler_row_data = row.find_all('td')

                    try:
                        for i in range(len(headers)):
                            if headers[i] in ["Maidens","Runs", "Wickets","0s","4s","6s","Wides","No Balls"]:
                                bowler_data[headers[i]] = int(bowler_row_data[i].text.strip())
                            elif headers[i] == ["Overs","Economy"]:
                                bowler_data[headers[i]] = float(bowler_row_data[i].text.strip())
                            else:
                                bowler_data[headers[i]] = (bowler_row_data[i].text.strip())

                        # Append the bowler's data to the list
                        bowlers_info = bowlers_info._append(bowler_data, ignore_index = True)
                    except:
                        pass
        return winner, man_of_the_match, innings_list, batsmen_list, match_score, did_not_bat, bowlers_info
    
    def printing_scorecard(self):
        for innings in self.innings_list:
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")  
            print(innings + ":")
            print()
        
            print("Batsmen:")
            print(self.batsmen_list[self.batsmen_list['Innings Name'] == innings].drop(columns=['Innings Number', 'Innings Name']))
            print()

            # Print "Did Not Bat" information)
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
        