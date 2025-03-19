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

def op_caps(url):
    #url = "https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/stats" #ipl-2025-1449924
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36"
    }

    # Send an HTTP request
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")  # Parse the HTML
    stats = soup.find_all('div',class_="ds-p-0")
    batsmen = stats[1]
    orange_cap = batsmen.find('span',class_="ds-text-title-xs ds-font-bold").text.strip()
    bowlers = stats[2]
    purple_cap = bowlers.find('span',class_="ds-text-title-xs ds-font-bold").text.strip()
    return orange_cap,purple_cap


if __name__ == '__main__':
    begin = time.time()
    team_names_sf = ["KKR","GT","MI","CSK","RR","RCB","PBKS","DC","SRH","LSG"]
    team_names_ff = ["Kolkata Knight Riders", "Gujarat Titans", "Mumbai Indians", "Chennai Super Kings","Rajasthan Royals","Royal Challengers Bengaluru", "Punjab Kings","Delhi Capitals","Sunrisers Hyderabad","Lucknow Super Giants"]
    cricbuzz_page_link = "https://www.cricbuzz.com/cricket-series/7607/indian-premier-league-2024/matches" #Change thi later
    ipl24_url = "https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/match-schedule-fixtures-and-results" #Change this later
    #cricbuzz_page_link = "https://www.cricbuzz.com/cricket-series/9237/indian-premier-league-2025/matches"
    #ipl24_url = "https://www.espncricinfo.com/series/ipl-2025-1449924/match-schedule-fixtures-and-results"
    ipl2024 = Series(ipl24_url,cricbuzz_page_link) #Change this later
    match_objects = ipl2024.match_objects

    teams = {'Gujju Gang':['Varun Chakaravarthy','Travis Head','Rahul Chahar','Mukesh Choudhary','Harshit Rana','Ishant Sharma','Jaydev Unadkat','Mukesh Kumar','Abdul Samad','Riyan Parag','Khaleel Ahmed','Avesh Khan','Faf du Plessis','Arjun Tendulkar','Mohammed Shami','Shivam Dube','Lockie Ferguson','Josh Hazlewood','Prabhsimran Singh','Rishabh Pant','Corbin Bosch','Mohammed Siraj','Prasidh Krishna','Marcus Stoinis','Harpreet Brar','Rahmanullah Gurbaz','Rashid Khan','Washington Sundar'],
             'Hilarious Hooligans':['Hardik Pandya','Heinrich Klaasen','Rinku Singh','Nehal Wadhera','Romario Shepherd','Manav Suthar','Vijaykumar Vyshak','Himmat Singh','Ayush Badoni','Liam Livingstone','Nathan Ellis','Moeen Ali','Karn Sharma','Yashasvi Jaiswal','Shimron Hetmyer','Axar Patel','Mayank Yadav','Abhinav Manohar','Ashutosh Sharma','Rachin Ravindra','Shahrukh Khan','Anrich Nortje','Mayank Markande','Yuzvendra Chahal','Tushar Deshpande','Noor Ahmad','Kagiso Rabada','Marco Jansen'],
             'Tormented Titans':['Virat Kohli','Abhishek Sharma','Jitesh Sharma','Harnoor Singh','Bhuvneshwar Kumar','Abishek Porel','Angkrish Raghuvanshi','Kuldeep Yadav','David Miller','Anuj Rawat','Josh Inglis','Kumar Kartikeya','Akash Deep','Rahul Tewatia','Ramandeep Singh','Sherfane Rutherford','Glenn Maxwell','Sandeep Sharma','Suryakumar Yadav','Shamar Joseph','Pat Cummins','Quinton de Kock','Ravichandran Ashwin'],
             'La Furia Roja':['Jasprit Bumrah','Sai Sudharsan','Shreyas Iyer','Swastik Chikara','Rajvardhan Hangargekar','Manoj Bhandage','Nitish Rana','Rasikh Dar Salam','Deepak Chahar','MS Dhoni','Aaron Hardie','Priyansh Arya','Phil Salt','Sameer Rizvi','Mitchell Santner','Manish Pandey','Suyash Sharma','Kamlesh Nagarkoti','Will Jacks','Azmatullah Omarzai','Adam Zampa','Spencer Johnson','Jamie Overton','Shashank Singh','Rovman Powell','Suryansh Shedge','Maheesh Theekshana'],
             'Supa Jinx Strikas':['Ruturaj Gaikwad','Shubman Gill','Mohit Sharma','Sai Kishore','Raj Bawa','Ishan Kishan','Mitchell Marsh','Nitish Kumar Reddy','Karim Janat','Yash Dayal','Bevon Jacobs','Ryan Rickelton','Rajat Patidar','Tristan Stubbs','Gerald Coetzee','Glenn Phillips','Tim David','Ravi Bishnoi','Donovan Ferreira','Jayant Yadav','Trent Boult','Jofra Archer','Akash Madhwal','Darshan Nalkande','Kwena Maphaka'],
             'Raging Raptors':['KL Rahul','Arshdeep Singh','Aiden Markram','Sachin Baby','Dushmantha Chameera','Naman Dhir','Karun Nair','Wanindu Hasaranga','Arshad Khan','Devdutt Padikkal','Robin Minz','Shahbaz Ahmed','Mohsin Khan','Krunal Pandya','Ravindra Jadeja','Mitchell Starc','Sanju Samson','Jos Buttler','Atharva Taide','Musheer Khan','Devon Conway','Venkatesh Iyer'],
             'The Travelling Bankers':['Sunil Narine','Andre Russell','Chetan Sakariya','T Natarajan','Ajinkya Rahane','Shreyas Gopal','Tilak Varma','Vijay Shankar','Shubham Dubey','Anukul Roy','Deepak Hooda','Harshal Patel','Rahul Tripathi','Lungi Ngidi','Matheesha Pathirana','Vaibhav Arora','Nicholas Pooran','Jake Fraser-McGurk','Sam Curran','Rohit Sharma','Mujeeb Ur Rahman','Anshul Kamboj','Mahipal Lomror']
             }
    boosters = {'Gujju Gang':{"https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/royal-challengers-bengaluru-vs-kolkata-knight-riders-10th-match-1422128/full-scorecard":"Triple Power"},
             'Hilarious Hooligans':{"https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/royal-challengers-bengaluru-vs-kolkata-knight-riders-10th-match-1422128/full-scorecard":"Double Power"},
             'Tormented Titans':{"https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/royal-challengers-bengaluru-vs-kolkata-knight-riders-10th-match-1422128/full-scorecard":"Batting Powerplay"},
             'La Furia Roja':{"https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/royal-challengers-bengaluru-vs-kolkata-knight-riders-10th-match-1422128/full-scorecard":"Bowling Powerplay"},
             'Supa Jinx Strikas':{"https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/royal-challengers-bengaluru-vs-kolkata-knight-riders-10th-match-1422128/full-scorecard":"Double Power","https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/kolkata-knight-riders-vs-sunrisers-hyderabad-3rd-match-1422121/full-scorecard":"Triple Captain"},
             'Raging Raptors':{},
             'The Travelling Bankers':{}
             } #for example Change this later
    
    orange_cap,purple_cap = op_caps("https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/stats") #ipl-2025-1449924 #Change this later

    #url = "https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/kolkata-knight-riders-vs-sunrisers-hyderabad-3rd-match-1422121/full-scorecard"             
    cricbuzz_page_link = "https://www.cricbuzz.com/cricket-series/7607/indian-premier-league-2024/matches"   
    match_urls = list(match_objects.keys())
    spreadsheet = {}
    spreadsheet['Team Final Points'] = {}
    for match_number in range(1,74):
        try:
            match_url = match_urls[match_number-1]
        except:
            break
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
        match = Match(teams,match_object,boosters)
        team_breakdown = match.match_points_breakdown
        # if "KKR vs RCB" in match_name:
        #     print(team_breakdown)
        General_points_list = match.general_player_points_list

        spreadsheet[(match_name+" - Points Breakdown")] = General_points_list
        spreadsheet[(match_name+" - CFC Points")] = team_breakdown
        final_points = spreadsheet['Team Final Points']
        for team in list(team_breakdown.index):
            final_points.setdefault(team, {}).setdefault("Total Points", 0)
            final_points.setdefault(team, {}).setdefault("Orange Cap", 0)
            final_points.setdefault(team, {}).setdefault("Purple Cap", 0)
            final_points[team][match_name] = team_breakdown.loc[team,'Total Points']
            final_points[team]['Total Points'] += final_points[team][match_name]
        print(match_name,"added")

    final_points = spreadsheet['Team Final Points']
    for team in list(final_points.keys()):
        orange_cap_points = 0
        purple_cap_points = 0
        if orange_cap in teams[team]:
            orange_cap_points = 500
        if purple_cap in teams[team]:
            purple_cap_points = 500
        final_points[team]['Total Points'] += orange_cap_points + purple_cap_points
        final_points[team]['Orange Cap'] = orange_cap_points
        final_points[team]['Purple Cap'] = purple_cap_points
    print("Purple Cap, Orange Cap, Total Points added")
    spreadsheet['Team Final Points'] = dict(sorted(final_points.items(), key=lambda x: x[1]['Total Points'], reverse=True))
        

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



        

