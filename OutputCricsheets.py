import dill
from ScrapingCricsheets import Series
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
from PointsCricsheets import Match
from collections import OrderedDict
import json
import numpy as np
# from selenium import webdriver
# # import undetected_chromedriver as uc
# from selenium_stealth import stealth
# from fake_useragent import UserAgent
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from ScoreEntry import Final_score,gtvscsk_score,lsgvrcb_score,mivpbks_score,pbksvsdc_score,srhvskkr_score,Eliminator_score,Qualifier1_score,Qualifier2_score

def convert_values(obj):
    """ Recursively convert DataFrame and NumPy objects to serializable formats """
    if isinstance(obj, pd.DataFrame):
        return obj.to_dict(orient="records")  # Convert DataFrame to list of dicts
    elif isinstance(obj, np.ndarray):
        return obj.tolist()  # Convert NumPy arrays to lists
    elif isinstance(obj, dict):
        return {k: convert_values(v) for k, v in obj.items()}  # Recursively process dicts
    elif isinstance(obj, list):
        return [convert_values(v) for v in obj]  # Process lists
    return obj

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)  # Convert int64 to int
        elif isinstance(obj, np.floating):
            return float(obj)  # Convert float64 to float
        return super().default(obj)


def excel_to_dict(file_path):
    # Read all sheets into a dictionary of DataFrames
    excel_data = pd.read_excel(file_path, sheet_name=None, index_col=0)  

    parsed_dict = {}

    for sheet_name, df in excel_data.items():
        # Convert DataFrame back to its original structure
        if df.index.dtype == 'O':  # If index is non-integer, it's likely a dictionary
            parsed_dict[sheet_name] = df.to_dict(orient='index')  
        else:  # Otherwise, assume it was originally a list
            parsed_dict[sheet_name] = df.to_dict(orient='records')

    return parsed_dict

def op_caps(url):
    ua = UserAgent()
    #random_user_agent = ua.random
    valid_user_agent = ua.chrome
    # Set up Selenium with stealth mode
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={valid_user_agent}")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )
    
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Get page source and parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")

    try:
        stats = soup.find_all('div',class_="ds-p-0")
        batsmen = stats[3]
        orange_cap = batsmen.find('span',class_="ds-text-title-xs ds-font-bold").text.strip()
        bowlers = stats[4]
        purple_cap = bowlers.find('span',class_="ds-text-title-xs ds-font-bold").text.strip()    
    except:
        orange_cap,purple_cap = "",""
    return orange_cap,purple_cap


def match_name_generator(url):
    match_name = match_url.split('/')[-2]
    parts = match_name.split('-')
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
    return match_name


if __name__ == '__main__':
    begin = time.time()
    team_names_sf = ["KKR","GT","MI","CSK","RR","RCB","PBKS","DC","SRH","LSG"]
    team_names_ff = ["Kolkata Knight Riders", "Gujarat Titans", "Mumbai Indians", "Chennai Super Kings","Rajasthan Royals","Royal Challengers Bengaluru", "Punjab Kings","Delhi Capitals","Sunrisers Hyderabad","Lucknow Super Giants"]
    
    # cricbuzz_page_link = "https://www.cricbuzz.com/cricket-series/7607/indian-premier-league-2024/matches" #Change this later
    # ipl_url = "https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/match-schedule-fixtures-and-results" #Change this later
    # database = "ipl2024matches.pkl" #Change this later
    # file_path = "CFC Fantasy League.xlsx"
    # json_filename = "CFC Fantasy League.json"
    # orange_cap,purple_cap = op_caps("https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/stats") #ipl-2025-1449924 #Change this later

    cricbuzz_page_link = "https://www.cricbuzz.com/cricket-series/9237/indian-premier-league-2025/matches"
    ipl_url = "https://www.espncricinfo.com/series/ipl-2025-1449924/match-schedule-fixtures-and-results"
    database = "ipl2025matches_cricsheets.pkl"
    file_path = "CFC Fantasy League 2025 Cricsheets.xlsx"
    json_filename = "CFC Fantasy League 2025 Cricsheets.json"
    #orange_cap,purple_cap = op_caps("https://www.espncricinfo.com/series/ipl-2025-1449924/stats")
    orange_cap = "Sai Sudharsan"
    purple_cap = "Prasidh Krishna"
    emerging_player = "Sai Sudharsan"
    mvp = "Suryakumar Yadav"

    ipl = Series(database)

    try:
        spreadsheet = excel_to_dict(file_path)
        lalelula = spreadsheet['Player Final Points']
    except:
        spreadsheet = {}
        spreadsheet['Team Final Points'] = {}
        spreadsheet['Player Final Points'] = {}

        columns = ["Total Points"]
        team_list = [
    "Gujju Gang", "Hilarious Hooligans", "Tormented Titans", 
    "La Furia Roja", "Supa Jinx Strikas", "Raging Raptors", "The Travelling Bankers"
]

        data = {
            "Team Final Points": {
                team: {column: 0 for column in columns} for team in team_list
            },
            "Player Final Points": {}  # Keep this empty for now
        }

        # Write the JSON to the file
        with open(json_filename, "w") as file:
            json.dump(data, file, indent=4, cls=NumpyEncoder)
        print("JSON file created successfully!")

        df = pd.DataFrame(index=team_list, columns=columns)

        # Write to an Excel file
        with pd.ExcelWriter(file_path, engine="xlsxwriter") as writer:  
            df.to_excel(writer, sheet_name="Team Final Points")  

        print(f"Excel file '{file_path}' created successfully!")

    match_objects = ipl.match_objects

    #Adding unresolved matches
    match_objects["PBKS vs DC"] = pbksvsdc_score
    match_objects["GT vs CSK"] = gtvscsk_score
    match_objects["SRH vs KKR"] = srhvskkr_score
    match_objects["MI vs PBKS"] = mivpbks_score
    match_objects["LSG vs RCB"] = lsgvrcb_score
    match_objects["Qualifier 1"] = Qualifier1_score
    match_objects["Eliminator"] = Eliminator_score
    match_objects["Qualifier 2"] = Qualifier2_score
    match_objects["Final"] = Final_score

    teams = {'Gujju Gang':['Varun Chakaravarthy','Travis Head','Prasidh Krishna','Kyle Jamieson','Harshit Rana','Rahul Chahar','Mukesh Choudhary','Ishant Sharma','Jaydev Unadkat','Mukesh Kumar','Abdul Samad','Riyan Parag','Khaleel Ahmed','Avesh Khan','Faf du Plessis','Arjun Tendulkar','Mohammed Shami','Shivam Dube','Lockie Ferguson','Josh Hazlewood','Prabhsimran Singh','Rishabh Pant','Corbin Bosch','Mohammed Siraj','Marcus Stoinis','Harpreet Brar','Rahmanullah Gurbaz','Rashid Khan','Washington Sundar'],
             'Hilarious Hooligans':['Yashasvi Jaiswal','Axar Patel','Hardik Pandya',"William O'Rourke",'Heinrich Klaasen','Rinku Singh','Nehal Wadhera','Romario Shepherd','Manav Suthar','Vijaykumar Vyshak','Himmat Singh','Ayush Badoni','Liam Livingstone','Nathan Ellis','Moeen Ali','Karn Sharma','Shimron Hetmyer','Mayank Yadav','Abhinav Manohar','Ashutosh Sharma','Rachin Ravindra','Shahrukh Khan','Anrich Nortje','Mayank Markande','Yuzvendra Chahal','Tushar Deshpande','Noor Ahmad','Kagiso Rabada','Marco Jansen'],
             'Tormented Titans':['Virat Kohli','Suryakumar Yadav','Kuldeep Yadav','Mitchell Owen','Abhishek Sharma','Jitesh Sharma','Harnoor Singh','Bhuvneshwar Kumar','Abishek Porel','Angkrish Raghuvanshi','Dhruv Jurel','David Miller','Anuj Rawat','Josh Inglis','Kumar Kartikeya','Akash Deep','Rahul Tewatia','Ramandeep Singh','Sherfane Rutherford','Glenn Maxwell','Sandeep Sharma','Shamar Joseph','Pat Cummins','Quinton de Kock','Ravichandran Ashwin'],
             'La Furia Roja':['Shreyas Iyer','Sai Sudharsan','Phil Salt','Jonny Bairstow','Harsh Dubey','Lhuan dre Pretorius','Jasprit Bumrah','Swastik Chikara','Rajvardhan Hangargekar','Manoj Bhandage','Nitish Rana','Rasikh Dar Salam','Deepak Chahar','MS Dhoni','Aaron Hardie','Priyansh Arya','Sameer Rizvi','Mitchell Santner','Manish Pandey','Suyash Sharma','Kamlesh Nagarkoti','Will Jacks','Azmatullah Omarzai','Adam Zampa','Spencer Johnson','Jamie Overton','Shashank Singh','Rovman Powell','Suryansh Shedge','Maheesh Theekshana'],
             'Supa Jinx Strikas':['Shubman Gill',['Ayush Mhatre','Ruturaj Gaikwad'],'Sai Kishore','Richard Gleeson','Nitish Reddy','Mohit Sharma','Raj Bawa','Ishan Kishan','Mitchell Marsh','Karim Janat','Yash Dayal','Bevon Jacobs','Ryan Rickelton','Rajat Patidar','Tristan Stubbs','Gerald Coetzee','Glenn Phillips','Tim David','Ravi Bishnoi','Donovan Ferreira','Jayant Yadav','Trent Boult','Jofra Archer','Akash Madhwal','Darshan Nalkande','Kwena Maphaka'],
             'Raging Raptors':['KL Rahul','Venkatesh Iyer',['Mitchell Starc','Mustafizur Rahman'],'Kusal Mendis','Arshdeep Singh','Mayank Agarwal','Shardul Thakur','Ravindra Jadeja','Aiden Markram','Sachin Baby','Dushmantha Chameera','Naman Dhir','Karun Nair','Wanindu Hasaranga','Arshad Khan','Devdutt Padikkal','Robin Minz','Shahbaz Ahmed','Mohsin Khan','Krunal Pandya','Sanju Samson','Jos Buttler','Atharva Taide','Musheer Khan','Devon Conway'],
             'The Travelling Bankers':['Sunil Narine','Andre Russell','Nicholas Pooran','Harshal Patel','Umran Malik','Chetan Sakariya','T Natarajan','Ajinkya Rahane','Shreyas Gopal','Tilak Varma','Vijay Shankar','Shubham Dubey','Anukul Roy','Deepak Hooda','Rahul Tripathi','Lungi Ngidi','Matheesha Pathirana','Vaibhav Arora','Jake Fraser-McGurk','Sam Curran','Rohit Sharma','Mujeeb Ur Rahman','Anshul Kamboj','Mahipal Lomror']
             }
    # boosters = {'Gujju Gang':{"https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/royal-challengers-bengaluru-vs-kolkata-knight-riders-10th-match-1422128/full-scorecard":"Triple Power"},
    #          'Hilarious Hooligans':{"https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/royal-challengers-bengaluru-vs-kolkata-knight-riders-10th-match-1422128/full-scorecard":"Double Power"},
    #          'Tormented Titans':{"https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/royal-challengers-bengaluru-vs-kolkata-knight-riders-10th-match-1422128/full-scorecard":"Batting Powerplay"},
    #          'La Furia Roja':{"https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/royal-challengers-bengaluru-vs-kolkata-knight-riders-10th-match-1422128/full-scorecard":"Bowling Powerplay"},
    #          'Supa Jinx Strikas':{"https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/royal-challengers-bengaluru-vs-kolkata-knight-riders-10th-match-1422128/full-scorecard":"Double Power","https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/kolkata-knight-riders-vs-sunrisers-hyderabad-3rd-match-1422121/full-scorecard":"Triple Captain"},
    #          'Raging Raptors':{},
    #          'The Travelling Bankers':{}
    #          } #for example Change this later
    boosters = {'Gujju Gang':{"KKR vs GT":"Double Power","SRH vs MI":"Batting Powerplay","KKR vs RR":"Triple Captain","Eliminator":"Bowling Powerplay"},
             'Hilarious Hooligans':{"CSK vs PBKS":"Bowling Powerplay","RR vs MI":"Double Power","KKR vs RR":"Triple Captain","SRH vs DC":"Batting Powerplay"},
             'Tormented Titans':{"SRH vs DC":"Bowling Powerplay","SRH vs RCB":"Double Power"},
             'La Furia Roja':{"KKR vs PBKS":"Batting Powerplay","PBKS vs DC":"Triple Captain"},
             'Supa Jinx Strikas':{'MI vs SRH':'Batting Powerplay',"RR vs MI":"Bowling Powerplay","GT vs SRH":"Triple Captain","GT vs CSK":"Double Power"},
             'Raging Raptors':{'DC vs RR':'Batting Powerplay',"LSG vs DC":"Double Power","MI vs DC":"Triple Captain","PBKS vs DC":"Bowling Powerplay"},
             'The Travelling Bankers':{"KKR vs LSG":"Batting Powerplay","KKR vs PBKS":"Bowling Powerplay","SRH vs KKR":"Triple Captain","KKR vs CSK":"Double Power"}
             }
    #url = "https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/kolkata-knight-riders-vs-sunrisers-hyderabad-3rd-match-1422121/full-scorecard"             
    match_urls = list(match_objects.keys())
    number_of_matches = len(match_objects)
    for match_number in range(number_of_matches,0,-1):
        
        match_url = match_urls[match_number-1] 
        match_object = match_objects[match_url] 
        match_name = match_url
        match = Match(teams,match_object,boosters)
        team_breakdown = match.match_points_breakdown
        General_points_list = match.general_player_points_list
        points_key = match_name+" - CFC Points"
        # To safely check if data has changed:
        if points_key in spreadsheet.keys():
            existing_data = spreadsheet[points_key]
            # Check if key columns are the same length
            if len(list(existing_data.keys())) == len(list(team_breakdown.index)):
                
                # Check if the sum of player points is the same
                count = 0
                for player in (list(team_breakdown.index)):
                    if existing_data[player]['Total Points'] != team_breakdown['Total Points'][player]: 
                        count += 1
                        break
                if count==0:
                    print(f"Match {match_name} already processed and unchanged, skipping...")
                    break

        spreadsheet[(match_name+" - Points Breakdown")] = General_points_list
        spreadsheet[(match_name+" - CFC Points")] = team_breakdown

        for team in list(team_breakdown.index):
            spreadsheet['Team Final Points'].setdefault(team, {}).setdefault("Total Points", 0)
            spreadsheet['Team Final Points'].setdefault(team, {}).setdefault("Orange Cap", 0)
            spreadsheet['Team Final Points'].setdefault(team, {}).setdefault("Purple Cap", 0)
            spreadsheet['Team Final Points'].setdefault(team, {}).setdefault("Emerging Player", 0)
            spreadsheet['Team Final Points'].setdefault(team, {}).setdefault("MVP", 0)
            spreadsheet['Team Final Points'][team][match_name] = team_breakdown.loc[team,'Total Points']
            #final_points[team]['Total Points'] += final_points[team][match_name]
        print(match_name,"added")
    try:
        if number_of_matches>=9:
            print(orange_cap)
            print(purple_cap)
            print(emerging_player)
            print(mvp)
            for team in list(spreadsheet['Team Final Points'].keys()):
                orange_cap_points = 0
                purple_cap_points = 0
                mvp_points = 0
                emerging_player_points = 0
                if orange_cap in teams[team]:
                    orange_cap_points = 500
                if purple_cap in teams[team]:
                    purple_cap_points = 500
                if mvp in teams[team]:
                    mvp_points = 750
                if emerging_player in teams[team]:
                    emerging_player_points = 300
                #final_points[team]['Total Points'] += orange_cap_points + purple_cap_points
                spreadsheet['Team Final Points'][team]['Orange Cap'] = orange_cap_points
                spreadsheet['Team Final Points'][team]['Purple Cap'] = purple_cap_points
                spreadsheet['Team Final Points'][team]['Emerging Player'] = emerging_player_points
                spreadsheet['Team Final Points'][team]['MVP'] = mvp_points
            print("Purple Cap, Orange Cap, Emerging Player, MVP Total Points added")

        player_list_points = []
        match_list_points = []
        for key in spreadsheet.keys():
            if " - Points Breakdown" in key:
                match_breakdown = spreadsheet[key]
                match_name = key.split(' - Points Breakdown')[0]
                if isinstance(match_breakdown, pd.DataFrame):
                    # If it's a DataFrame, iterate through the index
                    for player in match_breakdown.index:
                        spreadsheet['Player Final Points'].setdefault(player,{}).setdefault("Total Points",0)
                        spreadsheet['Player Final Points'].setdefault(player,{}).setdefault("Orange Cap",0)
                        spreadsheet['Player Final Points'].setdefault(player,{}).setdefault("Purple Cap",0)
                        spreadsheet['Player Final Points'].setdefault(player,{}).setdefault("Emerging Player",0)
                        spreadsheet['Player Final Points'].setdefault(player,{}).setdefault("MVP",0)
                        spreadsheet['Player Final Points'].setdefault(player,{}).setdefault(match_name,0)
                        player_points = match_breakdown.loc[player, 'Player Points']
                        #spreadsheet['Player Final Points'][player]['Total Points'] += player_points
                        spreadsheet['Player Final Points'][player][match_name] = player_points
                else:
                    # If it's a dictionary, use the keys and access dictionary values
                    for player in match_breakdown:
                        spreadsheet['Player Final Points'].setdefault(player,{}).setdefault("Total Points",0)
                        spreadsheet['Player Final Points'].setdefault(player,{}).setdefault("Orange Cap",0)
                        spreadsheet['Player Final Points'].setdefault(player,{}).setdefault("Purple Cap",0)
                        spreadsheet['Player Final Points'].setdefault(player,{}).setdefault("Emerging Player",0)
                        spreadsheet['Player Final Points'].setdefault(player,{}).setdefault("MVP",0)
                        spreadsheet['Player Final Points'].setdefault(player,{}).setdefault(match_name,0)
                        player_points = match_breakdown[player]['Player Points']
                        #spreadsheet['Player Final Points'][player]['Total Points'] += player_points
                        spreadsheet['Player Final Points'][player][match_name] = player_points
                for player in list(spreadsheet['Player Final Points'].keys()):
                    if player not in player_list_points:
                        player_list_points.append(player)
                    if match_name not in match_list_points:
                        match_list_points.append(match_name)
                    try:
                        hululu = spreadsheet['Player Final Points'][player][match_name]
                    except:
                        spreadsheet['Player Final Points'][player][match_name] = 0

        for participant in spreadsheet['Team Final Points'].keys(): 
            spreadsheet['Team Final Points'][participant]['Total Points'] = 0
            for match_name in spreadsheet['Team Final Points'][participant].keys():
                if match_name != 'Total Points':
                    spreadsheet['Team Final Points'][participant]['Total Points'] += spreadsheet['Team Final Points'][participant][match_name]
        spreadsheet['Team Final Points'] = dict(sorted(spreadsheet['Team Final Points'].items(), key=lambda x: x[1]['Total Points'], reverse=True))
        print("Final Team Points Added")

        for player in spreadsheet['Player Final Points'].keys():  
            if number_of_matches>=9:
                if player not in player_list_points:
                    player_list_points.append(player)      
                if player == orange_cap:
                    spreadsheet['Player Final Points'][player]['Orange Cap'] = 500
                else:
                    spreadsheet['Player Final Points'][player]['Orange Cap'] = 0
                if player == purple_cap:
                    spreadsheet['Player Final Points'][player]['Purple Cap'] = 500
                else:
                    spreadsheet['Player Final Points'][player]['Purple Cap'] = 0
                if player == emerging_player:
                    spreadsheet['Player Final Points'][player]['Emerging Player'] = 300
                else:
                    spreadsheet['Player Final Points'][player]['Emerging Player'] = 0
                if player == mvp:
                    spreadsheet['Player Final Points'][player]['MVP'] = 750
                else:
                    spreadsheet['Player Final Points'][player]['MVP'] = 0
        for player in player_list_points:
            for match in match_list_points:
                try:
                    hululu2 = spreadsheet['Player Final Points'][player][match]
                except:
                    spreadsheet['Player Final Points'][player][match] = 0

        for player in spreadsheet['Player Final Points'].keys(): 
            spreadsheet['Player Final Points'][player]['Total Points'] = 0
            for match_name in spreadsheet['Player Final Points'][player].keys():
                if match_name != 'Total Points':
                    spreadsheet['Player Final Points'][player]['Total Points'] += spreadsheet['Player Final Points'][player][match_name]
        spreadsheet['Player Final Points'] = dict(sorted(spreadsheet['Player Final Points'].items(), key=lambda x: x[1]['Total Points'], reverse=True))

        # Extract the first player's column order before sorting
        first_player = next(iter(spreadsheet['Player Final Points'].values()))  # Get the first player's stats
        column_order = list(first_player.keys())  # Maintain the original column order

        # Sort players by 'Total Points'
        sorted_players = OrderedDict(
            sorted(spreadsheet['Player Final Points'].items(), key=lambda x: x[1]['Total Points'], reverse=True)
        )

        # Reorder each player's stats to match the original column order
        for player in sorted_players:
            sorted_players[player] = OrderedDict((key, sorted_players[player][key]) for key in column_order)

        # Assign back to the spreadsheet
        spreadsheet['Player Final Points'] = sorted_players

        print("Player Points Added")

        spreadsheet_serializable = convert_values(spreadsheet)
        #json_filename = "CFC Fantasy League.json"
        with open(json_filename, "w") as json_file:
            json.dump(spreadsheet_serializable, json_file, indent=4, cls=NumpyEncoder)
        print("JSON file created successfully!")

        # Write to Excel
        with pd.ExcelWriter(file_path, engine="xlsxwriter") as writer:
            for sheet_name, data in spreadsheet.items():
                if isinstance(data, dict):  # If it's a dictionary, convert it to a DataFrame
                    df = pd.DataFrame.from_dict(data, orient='index')
                elif isinstance(data, list):  # If it's a list, convert to DataFrame
                    df = pd.DataFrame(data)
                else:
                    df = data  # If it's already a DataFrame
                if df.empty:
                    df = pd.DataFrame(columns=["Placeholder"])  
                df.to_excel(writer, sheet_name=sheet_name)  # Keep index for readability
                
            print(f"Excel file saved successfully as {file_path} in the current folder.")
    except:
        print("No New Data was Added")

    end = time.time()
    total_time_taken = end-begin
    minutes = str(int(total_time_taken/60))
    seconds = str(round(total_time_taken % 60,3))
    total_time_taken = minutes+"m "+seconds+"s"
    print(f"Time taken to process data: {total_time_taken}")        
