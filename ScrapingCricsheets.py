import requests
import zipfile
import os
import pandas as pd
from io import BytesIO
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium_stealth import stealth
from fake_useragent import UserAgent
from collections import defaultdict
import dill
import json
#from fuzzywuzzy import process

names = ["Mitchell Owen","Mayank Agarwal","Harsh Dubey","Atharva Taide","William O'Rourke",'Musheer Khan','Mustafizur Rahman','Kusal Mendis','Kyle Jamieson','Jonny Bairstow','Richard Gleeson','Shardul Thakur','Dhruv Jurel','Travis Head', 'Varun Chakaravarthy', 'Rahul Chahar', 'Mukesh Choudhary', 'Harshit Rana', 'Ishant Sharma', 'Jaydev Unadkat', 'Mukesh Kumar', 'Abdul Samad', 'Riyan Parag', 'Khaleel Ahmed', 'Avesh Khan', 'Faf du Plessis', 'Arjun Tendulkar', 'Mohammed Shami', 'Shivam Dube', 'Lockie Ferguson', 'Josh Hazlewood', 'Prabhsimran Singh', 'Rishabh Pant', 'Corbin Bosch', 'Mohammed Siraj', 'Prasidh Krishna', 'Marcus Stoinis', 'Harpreet Brar', 'Rahmanullah Gurbaz', 'Rashid Khan', 'Washington Sundar', 'Hardik Pandya', 'Heinrich Klaasen', 'Rinku Singh', 'Nehal Wadhera', 'Romario Shepherd', 'Manav Suthar', 'Vijaykumar Vyshak', 'Himmat Singh', 'Ayush Badoni', 'Liam Livingstone', 'Nathan Ellis', 'Moeen Ali', 'Karn Sharma', 'Yashasvi Jaiswal', 'Shimron Hetmyer', 'Axar Patel', 'Mayank Yadav', 'Abhinav Manohar', 'Ashutosh Sharma', 'Rachin Ravindra', 'Shahrukh Khan', 'Anrich Nortje', 'Mayank Markande', 'Yuzvendra Chahal', 'Tushar Deshpande', 'Noor Ahmad', 'Kagiso Rabada', 'Marco Jansen', 'Virat Kohli', 'Abhishek Sharma', 'Jitesh Sharma', 'Harnoor Singh', 'Bhuvneshwar Kumar', 'Abishek Porel', 'Angkrish Raghuvanshi', 'Kuldeep Yadav', 'David Miller', 'Anuj Rawat', 'Josh Inglis', 'Kumar Kartikeya', 'Akash Deep', 'Rahul Tewatia', 'Ramandeep Singh', 'Sherfane Rutherford', 'Glenn Maxwell', 'Sandeep Sharma', 'Suryakumar Yadav', 'Shamar Joseph', 'Pat Cummins', 'Quinton de Kock', 'Ravichandran Ashwin', 'Jasprit Bumrah', 'Sai Sudharsan', 'Shreyas Iyer', 'Swastik Chikara', 'Rajvardhan Hangargekar', 'Manoj Bhandage', 'Nitish Rana', 'Rasikh Salam Dar', 'Deepak Chahar', 'MS Dhoni', 'Aaron Hardie', 'Priyansh Arya', 'Phil Salt', 'Sameer Rizvi', 'Mitchell Santner', 'Manish Pandey', 'Suyash Sharma', 'Kamlesh Nagarkoti', 'Will Jacks', 'Azmatullah Omarzai', 'Adam Zampa', 'Spencer Johnson', 'Jamie Overton', 'Shashank Singh', 'Rovman Powell', 'Suryansh Shedge', 'Maheesh Theekshana', 'Ruturaj Gaikwad', 'Shubman Gill', 'Mohit Sharma', 'Sai Kishore', 'Raj Bawa', 'Ishan Kishan', 'Mitchell Marsh', 'Nitish Reddy', 'Karim Janat', 'Yash Dayal', 'Bevon Jacobs', 'Ryan Rickelton', 'Rajat Patidar', 'Tristan Stubbs', 'Gerald Coetzee', 'Glenn Phillips', 'Tim David', 'Ravi Bishnoi', 'Donovan Ferreira', 'Jayant Yadav', 'Trent Boult', 'Jofra Archer', 'Akash Madhwal', 'Darshan Nalkande', 'Kwena Maphaka', 'KL Rahul', 'Arshdeep Singh', 'Aiden Markram', 'Sachin Baby', 'Dushmantha Chameera', 'Naman Dhir', 'Karun Nair', 'Wanindu Hasaranga', 'Arshad Khan', 'Devdutt Padikkal', 'Robin Minz', 'Shahbaz Ahmed', 'Mohsin Khan', 'Krunal Pandya', 'Ravindra Jadeja', 'Mitchell Starc', 'Sanju Samson', 'Jos Buttler', 'Atharva Taide', 'Musheer Khan', 'Devon Conway', 'Venkatesh Iyer', 'Andre Russell', 'Sunil Narine', 'Chetan Sakariya', 'T Natarajan', 'Ajinkya Rahane', 'Shreyas Gopal', 'Tilak Varma', 'Vijay Shankar', 'Shubham Dubey', 'Anukul Roy', 'Deepak Hooda', 'Harshal Patel', 'Rahul Tripathi', 'Lungi Ngidi', 'Matheesha Pathirana', 'Vaibhav Arora', 'Nicholas Pooran', 'Jake Fraser-McGurk', 'Sam Curran', 'Rohit Sharma', 'Mujeeb ur Rahman', 'Anshul Kamboj', 'Mahipal Lomror']
roles = ["BAT","BAT","AR","AR","BOWL",'AR','BOWL','WK','BOWL','WK','BOWL','BOWL','WK','BAT', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'BAT', 'BAT', 'BOWL', 'BOWL', 'BAT', 'BOWL', 'BOWL', 'AR', 'BOWL', 'BOWL', 'WK', 'WK', 'AR', 'BOWL', 'BOWL', 'AR', 'BOWL', 'WK', 'AR', 'AR', 'AR', 'WK', 'BAT', 'BAT', 'AR', 'AR', 'BOWL', 'BAT', 'BAT', 'AR', 'BOWL', 'AR', 'BOWL', 'BAT', 'BAT', 'AR', 'BOWL', 'AR', 'AR', 'AR', 'BAT', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'AR', 'BAT', 'AR', 'WK', 'BAT', 'BOWL', 'WK', 'BAT', 'BOWL', 'BAT', 'WK', 'WK', 'BOWL', 'BOWL', 'AR', 'BAT', 'BAT', 'AR', 'BOWL', 'BAT', 'BOWL', 'BOWL', 'WK', 'AR', 'BOWL', 'BAT', 'BAT', 'BAT', 'AR', 'AR', 'BAT', 'BOWL', 'BOWL', 'WK', 'AR', 'BAT', 'WK', 'BAT', 'AR', 'BAT', 'BOWL', 'BOWL', 'AR', 'AR', 'BOWL', 'BOWL', 'AR', 'AR', 'BAT', 'AR', 'BOWL', 'BAT', 'BAT', 'BOWL', 'BOWL', 'AR', 'WK', 'AR', 'AR', 'AR', 'BOWL', 'BAT', 'WK', 'BAT', 'BAT', 'BOWL', 'AR', 'BAT', 'BOWL', 'AR', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'WK', 'BOWL', 'AR', 'BAT', 'BOWL', 'BAT', 'BAT', 'AR', 'BOWL', 'BAT', 'WK', 'AR', 'BOWL', 'AR', 'AR', 'BOWL', 'WK', 'WK', 'AR', 'AR', 'WK', 'AR', 'AR', 'AR', 'BOWL', 'BOWL', 'BAT', 'AR', 'AR', 'AR', 'BAT', 'AR', 'AR', 'BOWL', 'BAT', 'BOWL', 'BOWL', 'BOWL', 'WK', 'BAT', 'AR', 'BAT', 'BOWL', 'AR', 'AR']

cricsheet_names = ["MJ Owen","KT Maphaka","MA Agarwal","Harsh Dubey","Atharva Taide","W O'Rourke",'Aniket Verma', 'Simarjeet Singh', 'Fazalhaq Farooqi', 'V Puthur', 'PVSN Raju', 'M Siddharth', 'DS Rathi', 'Prince Yadav', 'V Nigam', 'PWA Mulder', 'Zeeshan Ansari', 'Ashwani Kumar', 'Yudhvir Singh', 'Yash Thakur', 'K Khejroliya', 'E Malinga', 'SK Rasheed', 'XC Bartlett', 'V Suryavanshi', 'JG Bethell', 'KS Rathore', 'Akash Singh', 'M Tiwari','M Khan','Mustafizur Rahman','Kusal Mendis','Kyle Jamieson','VG Arora', 'Q de Kock', 'SP Narine', 'AM Rahane', 'VR Iyer', 'A Raghuvanshi', 'RK Singh', 'AD Russell', 'Ramandeep Singh', 'Harshit Rana', 'SH Johnson', 'CV Varun', 'Suyash Sharma', 'PD Salt', 'V Kohli', 'D Padikkal', 'RM Patidar', 'LS Livingstone', 'JM Sharma', 'TH David', 'KH Pandya', 'Rasikh Salam', 'JR Hazlewood', 'Yash Dayal', 'A Zampa', 'Abhishek Sharma', 'TM Head', 'Ishan Kishan', 'Nithish Kumar Reddy', 'H Klaasen', 'A Manohar', 'PJ Cummins', 'HV Patel', 'Mohammed Shami', 'YBK Jaiswal', 'SV Samson', 'R Parag', 'N Rana', 'Dhruv Jurel', 'SO Hetmyer', 'SB Dubey', 'JC Archer', 'M Theekshana', 'TU Deshpande', 'Sandeep Sharma', 'RG Sharma', 'RD Rickelton', 'WG Jacks', 'SA Yadav', 'Tilak Varma', 'R Minz', 'Naman Dhir', 'MJ Santner', 'DL Chahar', 'TA Boult', 'KK Ahmed', 'R Ravindra', 'RA Tripathi', 'RD Gaikwad', 'S Dube', 'DJ Hooda', 'SM Curran', 'RA Jadeja', 'MS Dhoni', 'R Ashwin', 'Noor Ahmad', 'NT Ellis', 'AK Markram', 'MR Marsh', 'N Pooran', 'RR Pant', 'DA Miller', 'A Badoni', 'SN Thakur', 'Shahbaz Ahmed', 'Ravi Bishnoi', 'Mukesh Kumar', 'J Fraser-McGurk', 'F du Plessis', 'Abishek Porel', 'Sameer Rizvi', 'AR Patel', 'T Stubbs', 'Ashutosh Sharma', 'MA Starc', 'Kuldeep Yadav', 'MM Sharma', 'Priyansh Arya', 'P Simran Singh', 'SS Iyer', 'Azmatullah Omarzai', 'GJ Maxwell', 'MP Stoinis', 'Shashank Singh', 'Suryansh Shedge', 'M Jansen', 'Arshdeep Singh', 'YS Chahal', 'Vijaykumar Vyshak', 'B Sai Sudharsan', 'Shubman Gill', 'JC Buttler', 'SE Rutherford', 'R Tewatia', 'M Shahrukh Khan', 'Arshad Khan', 'R Sai Kishore', 'Rashid Khan', 'K Rabada', 'Mohammed Siraj', 'M Prasidh Krishna', 'PWH de Silva', 'MM Ali', 'Abdul Samad', 'Avesh Khan', 'B Kumar', 'M Pathirana', 'I Sharma', 'HH Pandya', 'Mujeeb Ur Rahman', 'KL Rahul', 'K Kartikeya', 'V Shankar', 'J Overton', 'MK Pandey', 'N Wadhera', 'LH Ferguson', 'PHKD Mendis', 'Akash Deep', 'RA Bawa', 'DP Conway', 'Mukesh Choudhary', 'JD Unadkat', 'Washington Sundar', 'JJ Bumrah', 'A Kamboj', 'Himmat Singh', 'KV Sharma', 'KK Nair', 'JP Inglis', 'A Nortje', 'RD Chahar', 'MS Bhandage', 'Harpreet Brar', 'D Ferreira', 'R Shepherd', 'A Mhatre', 'Rahmanullah Gurbaz', 'PVD Chameera', 'D Brevis', 'C Sakariya', 'R Powell', 'C Bosch', 'MP Yadav', 'Karim Janat', 'AS Roy', 'Akash Madhwal', 'G Coetzee', 'L Ngidi', 'T Natarajan', 'Sachin Baby', 'Urvil Patel']
espn_names = ["Mitchell Owen","Kwena Maphaka","Mayank Agarwwal","Harsh Dubey","Atharva Taide","William O'Rourke",'Aniket Verma', 'Simarjeet Singh', 'Fazalhaq Farooqi', 'Vignesh Puthur', 'Satyanarayana Raju', 'Manimaran Siddharth', 'Digvesh Rathi', 'Prince Yadav', 'Vipraj Nigam', 'Wiaan Mulder', 'Zeeshan Ansari', 'Ashwani Kumar', 'Yudhvir Singh Charak', 'Yash Thakur', 'Kulwant Khejroliya', 'Eeshan Malinga', 'Shaikh Rasheed', 'Xavier Bartlett', 'Vaibhav Suryavanshi', 'Jacob Bethell', 'Kunal Singh Rathore', 'Akash Singh', 'Madhav Tiwari','Musheer Khan','Mustafizur Rahman','Kusal Mendis','Kyle Jamieson','Vaibhav Arora', 'Quinton de Kock', 'Sunil Narine', 'Ajinkya Rahane', 'Venkatesh Iyer', 'Angkrish Raghuvanshi', 'Rinku Singh', 'Andre Russell', 'Ramandeep Singh', 'Harshit Rana', 'Spencer Johnson', 'Varun Chakaravarthy', 'Suyash Sharma', 'Phil Salt', 'Virat Kohli', 'Devdutt Padikkal', 'Rajat Patidar', 'Liam Livingstone', 'Jitesh Sharma', 'Tim David', 'Krunal Pandya', 'Rasikh Salam Dar', 'Josh Hazlewood', 'Yash Dayal', 'Adam Zampa', 'Abhishek Sharma', 'Travis Head', 'Ishan Kishan', 'Nitish Reddy', 'Heinrich Klaasen', 'Abhinav Manohar', 'Pat Cummins', 'Harshal Patel', 'Mohammed Shami', 'Yashasvi Jaiswal', 'Sanju Samson', 'Riyan Parag', 'Nitish Rana', 'Dhruv Jurel', 'Shimron Hetmyer', 'Shubham Dubey', 'Jofra Archer', 'Maheesh Theekshana', 'Tushar Deshpande', 'Sandeep Sharma', 'Rohit Sharma', 'Ryan Rickelton', 'Will Jacks', 'Suryakumar Yadav', 'Tilak Varma', 'Robin Minz', 'Naman Dhir', 'Mitchell Santner', 'Deepak Chahar', 'Trent Boult', 'Khaleel Ahmed', 'Rachin Ravindra', 'Rahul Tripathi', 'Ruturaj Gaikwad', 'Shivam Dube', 'Deepak Hooda', 'Sam Curran', 'Ravindra Jadeja', 'MS Dhoni', 'Ravichandran Ashwin', 'Noor Ahmad', 'Nathan Ellis', 'Aiden Markram', 'Mitchell Marsh', 'Nicholas Pooran', 'Rishabh Pant', 'David Miller', 'Ayush Badoni', 'Shardul Thakur', 'Shahbaz Ahmed', 'Ravi Bishnoi', 'Mukesh Kumar', 'Jake Fraser-McGurk', 'Faf du Plessis', 'Abishek Porel', 'Sameer Rizvi', 'Axar Patel', 'Tristan Stubbs', 'Ashutosh Sharma', 'Mitchell Starc', 'Kuldeep Yadav', 'Mohit Sharma', 'Priyansh Arya', 'Prabhsimran Singh', 'Shreyas Iyer', 'Azmatullah Omarzai', 'Glenn Maxwell', 'Marcus Stoinis', 'Shashank Singh', 'Suryansh Shedge', 'Marco Jansen', 'Arshdeep Singh', 'Yuzvendra Chahal', 'Vijaykumar Vyshak', 'Sai Sudharsan', 'Shubman Gill', 'Jos Buttler', 'Sherfane Rutherford', 'Rahul Tewatia', 'Shahrukh Khan', 'Arshad Khan', 'Sai Kishore', 'Rashid Khan', 'Kagiso Rabada', 'Mohammed Siraj', 'Prasidh Krishna', 'Wanindu Hasaranga', 'Moeen Ali', 'Abdul Samad', 'Avesh Khan', 'Bhuvneshwar Kumar', 'Matheesha Pathirana', 'Ishant Sharma', 'Hardik Pandya', 'Mujeeb ur Rahman', 'KL Rahul', 'Kumar Kartikeya', 'Vijay Shankar', 'Jamie Overton', 'Manish Pandey', 'Nehal Wadhera', 'Lockie Ferguson', 'Kusal Mendis', 'Akash Deep', 'Raj Bawa', 'Devon Conway', 'Mukesh Choudhary', 'Jaydev Unadkat', 'Washington Sundar', 'Jasprit Bumrah', 'Anshul Kamboj', 'Himmat Singh', 'Karn Sharma', 'Karun Nair', 'Josh Inglis', 'Anrich Nortje', 'Rahul Chahar', 'Manoj Bhandage', 'Harpreet Brar', 'Donovan Ferreira', 'Romario Shepherd', 'Ayush Mhatre', 'Rahmanullah Gurbaz', 'Dushmantha Chameera', 'Dewald Brevis', 'Chetan Sakariya', 'Rovman Powell', 'Corbin Bosch', 'Mayank Yadav', 'Karim Janat', 'Anukul Roy', 'Akash Madhwal', 'Gerald Coetzee', 'Lungi Ngidi', 'T Natarajan', 'Sachin Baby', 'Urvil Patel']

team_names_sf = ["KKR","GT","MI","CSK","RR","RCB","PBKS","DC","SRH","LSG"]
team_names_ff = ["Kolkata Knight Riders", "Gujarat Titans", "Mumbai Indians", "Chennai Super Kings","Rajasthan Royals","Royal Challengers Bengaluru", "Punjab Kings","Delhi Capitals","Sunrisers Hyderabad","Lucknow Super Giants"]

def espn_name(player):
    return espn_names[cricsheet_names.index(player)]

def dismissal_generator(ball_dict):
    bowler = espn_name(ball_dict['bowler'])
    wicket = ball_dict['wickets'][0]
    player_out = wicket['player_out']
    player_out = espn_name(player_out)
    dismissal_type = wicket['kind']
    if dismissal_type == "caught":
        catcher = wicket['fielders'][0]['name']
        if catcher in cricsheet_names:
            catcher = espn_name(catcher)
        dismissal = "c "+catcher+" b "+bowler
    if dismissal_type == "bowled":
        dismissal = "b "+bowler
    if dismissal_type == "caught and bowled":
        dismissal = "c & b "+bowler
    if dismissal_type == "lbw":
        dismissal = "lbw b "+bowler
    if dismissal_type == "stumped":
        keeper = wicket['fielders'][0]['name']
        if keeper in cricsheet_names:
            keeper = espn_name(keeper)
        dismissal = "st "+ keeper + " b " + bowler
    if dismissal_type == "run out":
        dismissal = "run out ("
        for fielder in wicket['fielders']:
            fielder_name = fielder['name']
            if fielder['name'] in cricsheet_names:
                fielder_name = espn_name(fielder_name)
            dismissal += fielder_name + "/"
        dismissal = dismissal[:-1]
        dismissal += ")"
    if dismissal_type == "retired hurt":
        dismissal = "retired hurt"
    if dismissal_type == "retired out":
        dismissal = "retired out"
    if dismissal_type == "hit wicket":
        dismissal = "hit wicket b " + bowler
    return dismissal,player_out
    

class Score:
    def __init__(self,json_filename):
        self.json_filename = json_filename
        self.url,self.full_player_list,self.player_list,self.winner,self.man_of_the_match,self.catchers,self.stumpers,self.main_runouters,self.secondary_runouters,self.bowled,self.lbw,self.innings_list,self.batsmen_list,self.bowlers_info = self.scorecard()
    
    def scorecard(self):
        # Define the file path
        file_path = "filtered_ipl_json/"+self.json_filename
        file_number = int(self.json_filename.split('.')[0])
        # Open and read the JSON file
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)  # Convert JSON to Python dictionary      
        #print(data)  # Output the dictionary
        info = data['info']
        teams = list(info['players'].keys())

        # url = team_names_sf[team_names_ff.index(teams[0])] + " vs " + team_names_sf[team_names_ff.index(teams[1])]
        # if self.json_filename == "1473509.json":
        #     url = "Qualifier 1"
        # elif self.json_filename == "1473510.json":
        #     url = "Eliminator"
        # elif self.json_filename == "1473511.json":
        #     url = "Qualifier 2"
        # elif self.json_filename == "1473512.json":
        #     url = "Final"
        matches = [
    "KKR vs RCB",
    "SRH vs RR",
    "MI vs CSK",
    "DC vs LSG",
    "PBKS vs GT",
    "RR vs KKR",
    "SRH vs LSG",
    "CSK vs RCB",
    "GT vs MI",
    "SRH vs DC",
    "RR vs CSK",
    "KKR vs MI",
    "LSG vs PBKS",
    "RCB vs GT",
    "KKR vs SRH",
    "LSG vs MI",
    "DC vs CSK",
    "RR vs PBKS",
    "SRH vs GT",
    "RCB vs MI",
    "LSG vs KKR",
    "PBKS vs CSK",
    "GT vs RR",
    "RCB vs DC",
    "CSK vs KKR",
    "GT vs LSG",
    "PBKS vs SRH",
    "RR vs RCB",
    "DC vs MI",
    "LSG vs CSK",
    "PBKS vs KKR",
    "DC vs RR",
    "MI vs SRH",
    "RCB vs PBKS",
    "GT vs DC",
    "LSG vs RR",
    "PBKS vs RCB",
    "CSK vs MI",
    "GT vs KKR",
    "LSG vs DC",
    "SRH vs MI",
    "RCB vs RR",
    "CSK vs SRH",
    "KKR vs PBKS",
    "MI vs LSG",
    "DC vs RCB",
    "RR vs GT",
    "KKR vs DC",
    "CSK vs PBKS",
    "MI vs RR",
    "GT vs SRH",
    "RCB vs CSK",
    "KKR vs RR",
    "PBKS vs LSG",
    "DC vs SRH",
    "MI vs GT",
    "KKR vs CSK",
    "RCB vs KKR",
    "PBKS vs RR",
    "DC vs GT",
    "LSG vs SRH",
    "CSK vs RR",
    "MI vs DC",
    "LSG vs GT",
    "SRH vs RCB",
    "PBKS vs DC",
    "CSK vs GT",
    "SRH vs KKR",
    "MI vs PBKS",
    "LSG vs RCB",
    "Qualifier 1",
    "Eliminator",
    "Qualifier 2",
    "Final"
]
        url = matches[file_number - 1473438]

        if 'player_of_match' in info.keys():
            man_of_the_match = info['player_of_match'][0]
            man_of_the_match = espn_name(man_of_the_match)
        else:
            man_of_the_match = "Nobody"
        # print("Man of the Match:",man_of_the_match)
        #registry = info['registry']
        teams = info['teams']
        # print("Teams:",teams)
        player_list = info['players']
        full_player_list = []
        innings_list = list(player_list.keys())
        if 'winner' in info['outcome'].keys():
            winner = info['outcome']['winner']
        else:
            winner = "No Result"
        # print("Winner:",winner)
        player_list_copy = {innings_list[0]:[],innings_list[1]:[]}
        for team in innings_list:
            for player in player_list[team]:
                if player in cricsheet_names:
                    player = espn_name(player)
                    full_player_list.append(player)
                    player_list_copy[team].append(player)
                else:
                    print(player,"not in auction")
        player_list = player_list_copy
        # print("Full Player list:",full_player_list)
        # print("Player List",player_list)
        innings = data['innings']
        first_innings = innings[0]
        team_first_innings = first_innings['team']
        overs_first_innings = first_innings['overs']
        if len(innings)==2:
            second_innings = innings[1]
            team_second_innings = second_innings['team']
            overs_second_innings = second_innings['overs']
            innings_name_list = [team_first_innings,team_second_innings]
            overs_lists = [overs_first_innings,overs_second_innings]
        else:
            innings_name_list = [team_first_innings]
            overs_lists = [overs_first_innings]

        bowled = []
        catchers = []
        lbw = []
        main_runouters = []
        secondary_runouters = []
        stumpers = []
        batsmen_list = pd.DataFrame()
        batsmen_stats = defaultdict(lambda: {'Innings Number': None,'Innings Name': None,'Dismissal': 'not out', 'Runs': 0, 'Balls': 0,'4s':0,'6s':0})
        bowlers_info = pd.DataFrame()
        bowlers_stats = defaultdict(lambda: {'Innings Number': None,'Innings Name': None,'Overs': 0, 'Maidens': 0, 'Runs': 0,'Wickets':0,'0s':0})
        
        #print(overs_first_innings)
        for innings_number in range(1,len(overs_lists)+1):
            innings = overs_lists[innings_number-1]
            innings_name = innings_name_list[innings_number-1]
            for over in innings:
                maiden_counter = 0
                bowler_of_over = over['deliveries'][0]['bowler']
            #print(over)
                for ball in over['deliveries']:
                    batter = ball['batter']
                    if batter in cricsheet_names:
                        batter = espn_name(batter)
                        batsmen_stats[batter]['Innings Number'] = innings_number
                        batsmen_stats[batter]['Innings Name'] = innings_name
                        if "wickets" in ball.keys():
                            dismissal,batter_dismissed = dismissal_generator(ball)
                            batsmen_stats[batter_dismissed]['Dismissal'] = dismissal
                        runs = ball['runs']['batter']
                        batsmen_stats[batter]['Runs'] += runs
                        batsmen_stats[batter]['Balls'] += 1
                        if 'extras' in ball.keys():
                            extra_type = list(ball['extras'].keys())[0]
                            if extra_type in ['wides']:
                                batsmen_stats[batter]['Balls'] -= 1
                        if runs == 4:
                            batsmen_stats[batter]['4s'] += 1
                        if runs == 6:
                            batsmen_stats[batter]['6s'] += 1      
                        #print(batter,innings_number,innings,runs)


                    bowler = ball['bowler']
                    if bowler in cricsheet_names:
                        bowler = espn_name(bowler)
                        bowlers_stats[bowler]['Innings Number'] = innings_number
                        bowlers_stats[bowler]['Innings Name'] = innings_name
                        bowlers_stats[bowler]['Overs'] += 1
                        runs = ball['runs']['total']
                        if 'extras' in ball.keys():
                            extra_type = list(ball['extras'].keys())[0]
                            if extra_type in ['legbyes','byes']:
                                runs = 0
                        bowlers_stats[bowler]['Runs'] += runs
                        if runs == 0:
                            bowlers_stats[bowler]['0s'] += 1
                            if bowler_of_over == bowler:
                                maiden_counter += 1
                        if "wickets" in ball.keys():
                            wicket_type = ball['wickets'][0]['kind']
                            if wicket_type in ['bowled','caught','lbw','stumped','hit wicket','caught and bowled']:
                                bowlers_stats[bowler]['Wickets'] += 1


                            if ball['wickets'][0]['kind'] == 'bowled':
                                bowled.append(bowler)
                            if ball['wickets'][0]['kind'] == 'lbw':
                                lbw.append(bowler)
                            if ball['wickets'][0]['kind'] == 'run out':
                                fielders = ball['wickets'][0]['fielders']
                                if len(fielders) == 1:
                                    fielder_main = fielders[0]['name']
                                    if fielder_main in cricsheet_names:
                                        fielder_main = espn_name(fielder_main)
                                        main_runouters.append(fielder_main)
                                elif len(fielders) == 2:
                                    fielder_main = fielders[1]['name']
                                    if fielder_main in cricsheet_names:
                                        fielder_main = espn_name(fielder_main)
                                        main_runouters.append(fielder_main)
                                    fielder_secondary = fielders[0]['name']
                                    if fielder_secondary in cricsheet_names:
                                        fielder_secondary = espn_name(fielder_secondary)
                                        main_runouters.append(fielder_secondary)
                                elif len(fielders) == 3:
                                    fielder_main = fielders[2]['name']
                                    if fielder_main in cricsheet_names:
                                        fielder_main = espn_name(fielder_main)
                                        main_runouters.append(fielder_main)
                                    fielder_secondary = fielders[1]['name']
                                    if fielder_secondary in cricsheet_names:
                                        fielder_secondary = espn_name(fielder_secondary)
                                        main_runouters.append(fielder_secondary)
                            if ball['wickets'][0]['kind'] == 'caught':
                                #print(ball['wickets'][0]['fielders'][0]['name'])
                                catcher = ball['wickets'][0]['fielders'][0]['name']
                                if catcher in cricsheet_names:
                                    catcher = espn_name(catcher)
                                    catchers.append(catcher)
                            if ball['wickets'][0]['kind'] == 'stumped':
                                stumper = ball['wickets'][0]['fielders'][0]['name']
                                if stumper in cricsheet_names:
                                    stumper = espn_name(stumper)
                                    stumpers.append(stumper)
                            if ball['wickets'][0]['kind'] == 'caught and bowled':
                                catchers.append(bowler)

                if maiden_counter == 6:
                    bowlers_stats[bowler]['Maidens'] += 1

        # print("Bowled:")
        # for player in bowled:
        #     print(player)
        # print()
        # print("LBW:")
        # for player in lbw:
        #     print(player)
        # print()
        # print("Main Run Outs:")
        # for player in main_runouters:
        #     print(player)
        # print()
        # print("Secondary Run Outs:")
        # for player in secondary_runouters:
        #     print(player)
        # print()
        # print("Caught:")
        # for player in catchers:
        #     print(player)
        # print()
        # print("Stumped:")
        # for player in stumpers:
        #     print(player)

        for batter in batsmen_stats.keys():
            batsman_stats = batsmen_stats[batter]
            innings_number = batsman_stats['Innings Number']
            innings =  batsman_stats['Innings Name']
            dismissal = batsman_stats['Dismissal']
            runs = batsman_stats['Runs']
            balls = batsman_stats['Balls']
            fours = batsman_stats['4s']
            sixes = batsman_stats['6s']
            if balls != 0:
                strike_rate = round(runs*100/balls,2)
            else:
                strike_rate = 0
            stat = {'Innings Number': innings_number,
                'Innings Name': innings,
                'Batsman': batter,
                'Dismissal': dismissal,
                'Runs': runs,
                'Balls': balls,
                '4s': fours,
                '6s': sixes,
                'Strike Rate': strike_rate
            }
            batsmen_list = batsmen_list._append(stat, ignore_index = True)

        for bowler in bowlers_stats.keys():
            bowler_stats = bowlers_stats[bowler]
            innings_number = bowler_stats['Innings Number']
            innings =  bowler_stats['Innings Name']
            overs = bowler_stats['Overs']
            maidens = bowler_stats['Maidens']
            runs = bowler_stats['Runs']
            wickets = bowler_stats['Wickets']
            dots = bowler_stats['0s']

            economy = round(runs*6/overs,2)
            overs = str(overs//6)+"."+str(overs%6)
            stat = {'Innings Number': innings_number,
                'Innings Name': innings,
                'Bowler': bowler,
                'Overs': overs,
                'Maidens': maidens,
                'Runs': runs,
                'Wickets': wickets,
                'Economy': economy,
                '0s': dots
            }
            bowlers_info = bowlers_info._append(stat, ignore_index = True)

        return url,full_player_list,player_list,winner,man_of_the_match,catchers,stumpers,main_runouters,secondary_runouters,bowled,lbw,innings_list,batsmen_list,bowlers_info

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

            print("Bowlers:")
            print(self.bowlers_info[self.bowlers_info['Innings Name'] == innings].drop(columns=['Innings Number', 'Innings Name']))
            print()

        print("Catchers:")
        print(self.catchers)
        print()

        print("Stumpings:")
        print(self.stumpers)
        print()

        print("Main Run Outs:")
        print(self.main_runouters)
        print()

        print("Secondary Run Outs:")
        print(self.secondary_runouters)
        print()
        
        print("Bowled:")
        print(self.bowled)
        print()
        
        print("LBW:")
        print(self.lbw)
        print()
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ") 
        print("Winner: ",self.winner)
        print()
        print("Man of the Match: ",self.man_of_the_match)

class Series:
    def __init__(self,database_name):
        #generated_json_list = self.match_json_generator()
        folder_path = "filtered_ipl_json"
        generated_json_list = [f for f in os.listdir(folder_path) if f.endswith('.json')]

        self.database_name = database_name
        self.match_objects = {}
        try:
            with open(self.database_name, "rb") as file:
                ipl = dill.load(file)
        except:
            ipl = {}

        match_objects = ipl

        match_names_list = list(match_objects.keys())
        print(match_names_list)
        if len(generated_json_list)>len(ipl):
            if len(generated_json_list) != 0:
                for match in generated_json_list:
                    print("Scraping:",match)
                    match_object = Score(match)
                    match_name = match_object.url
                    if match_name not in match_names_list:
                        #match_object.printing_scorecard()
                        match_objects[match_name] = match_object
                        print("Added:",match_name)
                if len(match_objects) == len(generated_json_list):
                    self.match_jsons = generated_json_list
                    self.match_objects = match_objects
                    with open(self.database_name, "wb") as file:
                        dill.dump(match_objects, file)
                    print("LOADING SUCCESSFUL")
                else:
                    print(list(match_objects.keys()),len(list(match_objects.keys())))
                    print(generated_json_list,len(generated_json_list))
        else:
            print("DATA UP TO DATE")
            self.match_objects = match_objects

    def match_json_generator(self):
        # Generate a random user-agent
        ua = UserAgent()
        random_user_agent = ua.random

        # Set up Chrome options
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-agent={random_user_agent}")
        options.add_argument("--headless")  # Optional: Run in headless mode
        options.add_argument("--disable-blink-features=AutomationControlled")

        driver = webdriver.Chrome(options=options)

        # Apply stealth mode
        stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )

        # URL of the page
        page_url = "https://cricsheet.org/matches/"

        driver.get(page_url)

        # Headers to mimic a real browser request
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }

        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Find the <dt> containing "Indian Premier League"
        ipl_dt = soup.find("dt", string="Indian Premier League")

        if ipl_dt:
            # Find the next <dd> after this <dt>
            ipl_dd = ipl_dt.find_next_sibling("dd")
            
            if ipl_dd:
                print("Found <dd>:", ipl_dd)
            else:
                print("<dd> not found after <dt>.")
        else:
            print("<dt> with 'Indian Premier League' not found.")

        # Find the <a> tag containing the JSON ZIP file link
        json_zip_tag = ipl_dd.find("a", href=True, string="JSON")  # Match exact text "JSON"

        if json_zip_tag:
            # Convert relative URL to absolute URL
            json_zip_url = requests.compat.urljoin(page_url, json_zip_tag["href"])
            print("Downloading ZIP file from:", json_zip_url)
            
            # Download the ZIP file
            zip_response = requests.get(json_zip_url, headers=headers)
            
            # Extract directory
            extract_path = "filtered_ipl_json"
            os.makedirs(extract_path, exist_ok=True)

            # Find the last JSON file (largest number)
            existing_files = [f for f in os.listdir(extract_path) if f.endswith(".json")]
            json_numbers = [int(f.split(".")[0]) for f in existing_files if f.split(".")[0].isdigit()]
            
            if json_numbers:
                last_json_number = max(json_numbers)
                last_json_file = f"{last_json_number}.json"
                os.remove(os.path.join(extract_path, last_json_file))  # Delete last JSON file
                print(f"Deleted outdated file: {last_json_file}")
            
            match_list = []
            # Open the ZIP file as a byte stream
            with zipfile.ZipFile(BytesIO(zip_response.content), "r") as zip_ref:
                # Extract only relevant JSON files (1473438 and onwards)
                for file_name in zip_ref.namelist():
                    if file_name.endswith(".json"):
                        try:
                            file_number = int(file_name.split(".")[0])
                            if file_number >= 1473438 and file_name != "1473495.json":
                                zip_ref.extract(file_name, extract_path)
                                print(f"Extracted: {file_name}")
                                match_list.append(file_name)
                        except ValueError:
                            pass  # Ignore non-numeric files like README.txt

            print(f"Updated files in '{extract_path}'")
            return match_list
        else:
            print("JSON ZIP file link not found.")
            return None



if __name__ == "__main__":
    match_score = Score("1473468.json")
    match_score.printing_scorecard()
    database = "ipl2025matches_cricsheets.pkl"
    ipl2025 = Series(database)