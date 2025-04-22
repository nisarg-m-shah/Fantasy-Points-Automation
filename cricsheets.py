import requests
import zipfile
import os
import shutil
from io import BytesIO
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium_stealth import stealth
from fake_useragent import UserAgent
import json
#from fuzzywuzzy import process

names = ['Shardul Thakur','Dhruv Jurel','Travis Head', 'Varun Chakaravarthy', 'Rahul Chahar', 'Mukesh Choudhary', 'Harshit Rana', 'Ishant Sharma', 'Jaydev Unadkat', 'Mukesh Kumar', 'Abdul Samad', 'Riyan Parag', 'Khaleel Ahmed', 'Avesh Khan', 'Faf du Plessis', 'Arjun Tendulkar', 'Mohammed Shami', 'Shivam Dube', 'Lockie Ferguson', 'Josh Hazlewood', 'Prabhsimran Singh', 'Rishabh Pant', 'Corbin Bosch', 'Mohammed Siraj', 'Prasidh Krishna', 'Marcus Stoinis', 'Harpreet Brar', 'Rahmanullah Gurbaz', 'Rashid Khan', 'Washington Sundar', 'Hardik Pandya', 'Heinrich Klaasen', 'Rinku Singh', 'Nehal Wadhera', 'Romario Shepherd', 'Manav Suthar', 'Vijaykumar Vyshak', 'Himmat Singh', 'Ayush Badoni', 'Liam Livingstone', 'Nathan Ellis', 'Moeen Ali', 'Karn Sharma', 'Yashasvi Jaiswal', 'Shimron Hetmyer', 'Axar Patel', 'Mayank Yadav', 'Abhinav Manohar', 'Ashutosh Sharma', 'Rachin Ravindra', 'Shahrukh Khan', 'Anrich Nortje', 'Mayank Markande', 'Yuzvendra Chahal', 'Tushar Deshpande', 'Noor Ahmad', 'Kagiso Rabada', 'Marco Jansen', 'Virat Kohli', 'Abhishek Sharma', 'Jitesh Sharma', 'Harnoor Singh', 'Bhuvneshwar Kumar', 'Abishek Porel', 'Angkrish Raghuvanshi', 'Kuldeep Yadav', 'David Miller', 'Anuj Rawat', 'Josh Inglis', 'Kumar Kartikeya', 'Akash Deep', 'Rahul Tewatia', 'Ramandeep Singh', 'Sherfane Rutherford', 'Glenn Maxwell', 'Sandeep Sharma', 'Suryakumar Yadav', 'Shamar Joseph', 'Pat Cummins', 'Quinton de Kock', 'Ravichandran Ashwin', 'Jasprit Bumrah', 'Sai Sudharsan', 'Shreyas Iyer', 'Swastik Chikara', 'Rajvardhan Hangargekar', 'Manoj Bhandage', 'Nitish Rana', 'Rasikh Salam Dar', 'Deepak Chahar', 'MS Dhoni', 'Aaron Hardie', 'Priyansh Arya', 'Phil Salt', 'Sameer Rizvi', 'Mitchell Santner', 'Manish Pandey', 'Suyash Sharma', 'Kamlesh Nagarkoti', 'Will Jacks', 'Azmatullah Omarzai', 'Adam Zampa', 'Spencer Johnson', 'Jamie Overton', 'Shashank Singh', 'Rovman Powell', 'Suryansh Shedge', 'Maheesh Theekshana', 'Ruturaj Gaikwad', 'Shubman Gill', 'Mohit Sharma', 'Sai Kishore', 'Raj Bawa', 'Ishan Kishan', 'Mitchell Marsh', 'Nitish Reddy', 'Karim Janat', 'Yash Dayal', 'Bevon Jacobs', 'Ryan Rickelton', 'Rajat Patidar', 'Tristan Stubbs', 'Gerald Coetzee', 'Glenn Phillips', 'Tim David', 'Ravi Bishnoi', 'Donovan Ferreira', 'Jayant Yadav', 'Trent Boult', 'Jofra Archer', 'Akash Madhwal', 'Darshan Nalkande', 'Kwena Maphaka', 'KL Rahul', 'Arshdeep Singh', 'Aiden Markram', 'Sachin Baby', 'Dushmantha Chameera', 'Naman Dhir', 'Karun Nair', 'Wanindu Hasaranga', 'Arshad Khan', 'Devdutt Padikkal', 'Robin Minz', 'Shahbaz Ahmed', 'Mohsin Khan', 'Krunal Pandya', 'Ravindra Jadeja', 'Mitchell Starc', 'Sanju Samson', 'Jos Buttler', 'Atharva Taide', 'Musheer Khan', 'Devon Conway', 'Venkatesh Iyer', 'Andre Russell', 'Sunil Narine', 'Chetan Sakariya', 'T Natarajan', 'Ajinkya Rahane', 'Shreyas Gopal', 'Tilak Varma', 'Vijay Shankar', 'Shubham Dubey', 'Anukul Roy', 'Deepak Hooda', 'Harshal Patel', 'Rahul Tripathi', 'Lungi Ngidi', 'Matheesha Pathirana', 'Vaibhav Arora', 'Nicholas Pooran', 'Jake Fraser-McGurk', 'Sam Curran', 'Rohit Sharma', 'Mujeeb ur Rahman', 'Anshul Kamboj', 'Mahipal Lomror']
roles = ['BOWL','WK','BAT', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'BAT', 'BAT', 'BOWL', 'BOWL', 'BAT', 'BOWL', 'BOWL', 'AR', 'BOWL', 'BOWL', 'WK', 'WK', 'AR', 'BOWL', 'BOWL', 'AR', 'BOWL', 'WK', 'AR', 'AR', 'AR', 'WK', 'BAT', 'BAT', 'AR', 'AR', 'BOWL', 'BAT', 'BAT', 'AR', 'BOWL', 'AR', 'BOWL', 'BAT', 'BAT', 'AR', 'BOWL', 'AR', 'AR', 'AR', 'BAT', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'AR', 'BAT', 'AR', 'WK', 'BAT', 'BOWL', 'WK', 'BAT', 'BOWL', 'BAT', 'WK', 'WK', 'BOWL', 'BOWL', 'AR', 'BAT', 'BAT', 'AR', 'BOWL', 'BAT', 'BOWL', 'BOWL', 'WK', 'AR', 'BOWL', 'BAT', 'BAT', 'BAT', 'AR', 'AR', 'BAT', 'BOWL', 'BOWL', 'WK', 'AR', 'BAT', 'WK', 'BAT', 'AR', 'BAT', 'BOWL', 'BOWL', 'AR', 'AR', 'BOWL', 'BOWL', 'AR', 'AR', 'BAT', 'AR', 'BOWL', 'BAT', 'BAT', 'BOWL', 'BOWL', 'AR', 'WK', 'AR', 'AR', 'AR', 'BOWL', 'BAT', 'WK', 'BAT', 'BAT', 'BOWL', 'AR', 'BAT', 'BOWL', 'AR', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'BOWL', 'WK', 'BOWL', 'AR', 'BAT', 'BOWL', 'BAT', 'BAT', 'AR', 'BOWL', 'BAT', 'WK', 'AR', 'BOWL', 'AR', 'AR', 'BOWL', 'WK', 'WK', 'AR', 'AR', 'WK', 'AR', 'AR', 'AR', 'BOWL', 'BOWL', 'BAT', 'AR', 'AR', 'AR', 'BAT', 'AR', 'AR', 'BOWL', 'BAT', 'BOWL', 'BOWL', 'BOWL', 'WK', 'BAT', 'AR', 'BAT', 'BOWL', 'AR', 'AR']

cricsheet_names = ['VG Arora', 'Q de Kock', 'SP Narine', 'AM Rahane', 'VR Iyer', 'A Raghuvanshi', 'RK Singh', 'AD Russell', 'Ramandeep Singh', 'Harshit Rana', 'SH Johnson', 'CV Varun', 'Suyash Sharma', 'PD Salt', 'V Kohli', 'D Padikkal', 'RM Patidar', 'LS Livingstone', 'JM Sharma', 'TH David', 'KH Pandya', 'Rasikh Salam', 'JR Hazlewood', 'Yash Dayal', 'A Zampa', 'Abhishek Sharma', 'TM Head', 'Ishan Kishan', 'Nithish Kumar Reddy', 'H Klaasen', 'A Manohar', 'PJ Cummins', 'HV Patel', 'Mohammed Shami', 'YBK Jaiswal', 'SV Samson', 'R Parag', 'N Rana', 'Dhruv Jurel', 'SO Hetmyer', 'SB Dubey', 'JC Archer', 'M Theekshana', 'TU Deshpande', 'Sandeep Sharma', 'RG Sharma', 'RD Rickelton', 'WG Jacks', 'SA Yadav', 'Tilak Varma', 'R Minz', 'Naman Dhir', 'MJ Santner', 'DL Chahar', 'TA Boult', 'KK Ahmed', 'R Ravindra', 'RA Tripathi', 'RD Gaikwad', 'S Dube', 'DJ Hooda', 'SM Curran', 'RA Jadeja', 'MS Dhoni', 'R Ashwin', 'Noor Ahmad', 'NT Ellis', 'AK Markram', 'MR Marsh', 'N Pooran', 'RR Pant', 'DA Miller', 'A Badoni', 'SN Thakur', 'Shahbaz Ahmed', 'Ravi Bishnoi', 'Mukesh Kumar', 'J Fraser-McGurk', 'F du Plessis', 'Abishek Porel', 'Sameer Rizvi', 'AR Patel', 'T Stubbs', 'Ashutosh Sharma', 'MA Starc', 'Kuldeep Yadav', 'MM Sharma', 'Priyansh Arya', 'P Simran Singh', 'SS Iyer', 'Azmatullah Omarzai', 'GJ Maxwell', 'MP Stoinis', 'Shashank Singh', 'Suryansh Shedge', 'M Jansen', 'Arshdeep Singh', 'YS Chahal', 'Vijaykumar Vyshak', 'B Sai Sudharsan', 'Shubman Gill', 'JC Buttler', 'SE Rutherford', 'R Tewatia', 'M Shahrukh Khan', 'Arshad Khan', 'R Sai Kishore', 'Rashid Khan', 'K Rabada', 'Mohammed Siraj', 'M Prasidh Krishna', 'PWH de Silva', 'MM Ali', 'Abdul Samad', 'Avesh Khan']
espn_names = ['Vaibhav Arora', 'Quinton de Kock', 'Sunil Narine', 'Ajinkya Rahane', 'Venkatesh Iyer', 'Angkrish Raghuvanshi', 'Rinku Singh', 'Andre Russell', 'Ramandeep Singh', 'Harshit Rana', 'Spencer Johnson', 'Varun Chakaravarthy', 'Suyash Sharma', 'Phil Salt', 'Virat Kohli', 'Devdutt Padikkal', 'Rajat Patidar', 'Liam Livingstone', 'Jitesh Sharma', 'Tim David', 'Krunal Pandya', 'Rasikh Salam Dar', 'Josh Hazlewood', 'Yash Dayal', 'Adam Zampa', 'Abhishek Sharma', 'Travis Head', 'Ishan Kishan', 'Nitish Reddy', 'Heinrich Klaasen', 'Abhinav Manohar', 'Pat Cummins', 'Harshal Patel', 'Mohammed Shami', 'Yashasvi Jaiswal', 'Sanju Samson', 'Riyan Parag', 'Nitish Rana', 'Dhruv Jurel', 'Shimron Hetmyer', 'Shubham Dubey', 'Jofra Archer', 'Maheesh Theekshana', 'Tushar Deshpande', 'Sandeep Sharma', 'Rohit Sharma', 'Ryan Rickelton', 'Will Jacks', 'Suryakumar Yadav', 'Tilak Varma', 'Robin Minz', 'Naman Dhir', 'Mitchell Santner', 'Deepak Chahar', 'Trent Boult', 'Khaleel Ahmed', 'Rachin Ravindra', 'Rahul Tripathi', 'Ruturaj Gaikwad', 'Shivam Dube', 'Deepak Hooda', 'Sam Curran', 'Ravindra Jadeja', 'MS Dhoni', 'Ravichandran Ashwin', 'Noor Ahmad', 'Nathan Ellis', 'Aiden Markram', 'Mitchell Marsh', 'Nicholas Pooran', 'Rishabh Pant', 'David Miller', 'Ayush Badoni', 'Shardul Thakur', 'Shahbaz Ahmed', 'Ravi Bishnoi', 'Mukesh Kumar', 'Jake Fraser-McGurk', 'Faf du Plessis', 'Abishek Porel', 'Sameer Rizvi', 'Axar Patel', 'Tristan Stubbs', 'Ashutosh Sharma', 'Mitchell Starc', 'Kuldeep Yadav', 'Mohit Sharma', 'Priyansh Arya', 'Prabhsimran Singh', 'Shreyas Iyer', 'Azmatullah Omarzai', 'Glenn Maxwell', 'Marcus Stoinis', 'Shashank Singh', 'Suryansh Shedge', 'Marco Jansen', 'Arshdeep Singh', 'Yuzvendra Chahal', 'Vijaykumar Vyshak', 'Sai Sudharsan', 'Shubman Gill', 'Jos Buttler', 'Sherfane Rutherford', 'Rahul Tewatia', 'Shahrukh Khan', 'Arshad Khan', 'Sai Kishore', 'Rashid Khan', 'Kagiso Rabada', 'Mohammed Siraj', 'Prasidh Krishna', 'Wanindu Hasaranga', 'Moeen Ali', 'Abdul Samad', 'Avesh Khan']

class Score:
    def __init__(self,json_filename):
        self.json_filename = json_filename
        #self.full_player_list,self.player_list,self.winner,self.man_of_the_match,self.catchers,self.stumpers,self.main_runouters,self.secondary_runouters,self.bowled,self.lbw,self.innings_list,self.batsmen_list,self.bowlers_info = self.scorecard()
    def scorecard(self):
        # Define the file path
        file_path = "filtered_ipl_json/"+self.json_filename
        # Open and read the JSON file
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)  # Convert JSON to Python dictionary      
        #print(data)  # Output the dictionary
        info = data['info']
        man_of_the_match = info['player_of_match']
        #registry = info['registry']
        teams = info['teams']
        player_list = info['players']
        full_player_list = []
        innings_list = list(player_list.keys())
        winner = info['outcome']['winner']
        for team in player_list.keys():
            for player in player_list[team]:
                full_player_list.append(player)
        innings = data['innings']
        first_innings = innings[0]
        second_innings = innings[1]
        team_first_innings = first_innings['team']
        overs_first_innings = first_innings['overs'][0]
        {'over': 0, 'deliveries': [{'batter': 'B Sai Sudharsan', 'bowler': 'Arshdeep Singh', 'non_striker': 'Shubman Gill', 'runs': {'batter': 4, 'extras': 0, 'total': 4}}, {'batter': 'B Sai Sudharsan', 'bowler': 'Arshdeep Singh', 'non_striker': 'Shubman Gill', 'runs': {'batter': 0, 'extras': 0, 'total': 0}}, {'batter': 'B Sai Sudharsan', 'bowler': 'Arshdeep Singh', 'non_striker': 'Shubman Gill', 'runs': {'batter': 0, 'extras': 0, 'total': 0}}, {'batter': 'B Sai Sudharsan', 'bowler': 'Arshdeep Singh', 'non_striker': 'Shubman Gill', 'runs': {'batter': 0, 'extras': 0, 'total': 0}}, {'batter': 'B Sai Sudharsan', 'bowler': 'Arshdeep Singh', 'non_striker': 'Shubman Gill', 'runs': {'batter': 0, 'extras': 0, 'total': 0}}, {'batter': 'B Sai Sudharsan', 'bowler': 'Arshdeep Singh', 'non_striker': 'Shubman Gill', 'runs': {'batter': 1, 'extras': 0, 'total': 1}}]}
        team_second_innings = second_innings['team']
        overs_second_innings = second_innings['overs'][0]
        bowled = []
        catchers = []
        lbw = []
        main_runouters = []
        secondary_runouters = []
        stumpers = []
        for over in overs_first_innings:
            for ball in over['deliveries']:
                if 'wickets' in ball.keys():
                    if ball['wickets'][0]['kind'] == 'bowled':
                        bowler = ball['bowler']
                        if bowler in cricsheet_names:
                            bowler = espn_names[cricsheet_names.index(bowler)]
                            bowled.append(bowler)
                    if ball['wickets'][0]['kind'] == 'lbw':
                        bowler = ball['bowler']
                        if bowler in cricsheet_names:
                            bowler = espn_names[cricsheet_names.index(bowler)]
                            bowled.append(bowler)
                    if ball['wickets'][0]['kind'] == 'run out':
                        fielders = ball['wickets'][0]['fielders']
                        if len(fielders) == 1:
                            fielder_main = fielders[0]['name']
                            if fielder_main in cricsheet_names:
                                fielder_main = espn_names[cricsheet_names.index(fielder_main)]
                                main_runouters.append(fielder_main)
                        elif len(fielders) == 2:
                            fielder_main = fielders[1]['name']
                            if fielder_main in cricsheet_names:
                                fielder_main = espn_names[cricsheet_names.index(fielder_main)]
                                main_runouters.append(fielder_main)
                            fielder_secondary = fielders[0]['name']
                            if fielder_secondary in cricsheet_names:
                                fielder_secondary = espn_names[cricsheet_names.index(fielder_secondary)]
                                main_runouters.append(fielder_secondary)
                    if ball['wickets'][0]['kind'] == 'caught':
                        #print(ball['wickets'][0]['fielders'][0]['name'])
                        catcher = ball['wickets'][0]['fielders'][0]['name']
                        if catcher in cricsheet_names:
                            catcher = espn_names[cricsheet_names.index(catcher)]
                            catchers.append(catcher)
                    if ball['wickets'][0]['kind'] == 'stumped':
                        stumper = ball['wickets'][0]['fielders'][0]['name']
                        if stumper in cricsheet_names:
                            stumper = espn_names[cricsheet_names.index(stumper)]
                            stumpers.append(stumper)
        for over in overs_second_innings:
            for ball in over['deliveries']:
                if 'wickets' in ball.keys():
                    if ball['wickets'][0]['kind'] == 'bowled':
                        bowler = ball['bowler']
                        if bowler in cricsheet_names:
                            bowler = espn_names[cricsheet_names.index(bowler)]
                            bowled.append(bowler)
                    if ball['wickets'][0]['kind'] == 'lbw':
                        bowler = ball['bowler']
                        if bowler in cricsheet_names:
                            bowler = espn_names[cricsheet_names.index(bowler)]
                            bowled.append(bowler)
                    if ball['wickets'][0]['kind'] == 'run out':
                        fielders = ball['wickets'][0]['fielders']
                        if len(fielders) == 1:
                            fielder_main = fielders[0]['name']
                            if fielder_main in cricsheet_names:
                                fielder_main = espn_names[cricsheet_names.index(fielder_main)]
                                main_runouters.append(fielder_main)
                        elif len(fielders) == 2:
                            fielder_main = fielders[1]['name']
                            if fielder_main in cricsheet_names:
                                fielder_main = espn_names[cricsheet_names.index(fielder_main)]
                                main_runouters.append(fielder_main)
                            fielder_secondary = fielders[0]['name']
                            if fielder_secondary in cricsheet_names:
                                fielder_secondary = espn_names[cricsheet_names.index(fielder_secondary)]
                                main_runouters.append(fielder_secondary)
                    if ball['wickets'][0]['kind'] == 'caught':
                        #print(ball['wickets'][0]['fielders'][0]['name'])
                        catcher = ball['wickets'][0]['fielders'][0]['name']
                        if catcher in cricsheet_names:
                            catcher = espn_names[cricsheet_names.index(catcher)]
                            catchers.append(catcher)
                    if ball['wickets'][0]['kind'] == 'stumped':
                        stumper = ball['wickets'][0]['fielders'][0]['name']
                        if stumper in cricsheet_names:
                            stumper = espn_names[cricsheet_names.index(stumper)]
                            stumpers.append(stumper)
        print("Bowled")
        for player in bowled:
            print(player)
        print()
        print("LBW")
        for player in lbw:
            print(player)
        print()
        print("Main Run Outs")
        for player in main_runouters:
            print(player)
        print()
        print("Secondary Run Outs")
        for player in secondary_runouters:
            print(player)
        print()
        print("Caught")
        for player in catchers:
            print(player)
        print()
        print("Stumped")
        for player in stumpers:
            print(player)

    

match_score = Score("1473439.json")
match_score.scorecard()

class Series:
    def __init__(self):
        pass
    def scraping(self):
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

            # Open the ZIP file as a byte stream
            with zipfile.ZipFile(BytesIO(zip_response.content), "r") as zip_ref:
                # Extract only relevant JSON files (1473438 and onwards)
                for file_name in zip_ref.namelist():
                    if file_name.endswith(".json"):
                        try:
                            file_number = int(file_name.split(".")[0])
                            if file_number >= 1473438:
                                zip_ref.extract(file_name, extract_path)
                                print(f"Extracted: {file_name}")
                        except ValueError:
                            pass  # Ignore non-numeric files like README.txt

            print(f"Updated files in '{extract_path}'")
        else:
            print("JSON ZIP file link not found.")

series_object = Series()
