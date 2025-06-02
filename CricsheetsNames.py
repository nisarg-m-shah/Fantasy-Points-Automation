from fuzzywuzzy import process
import json

names = ['Shardul Thakur','Dhruv Jurel','Travis Head', 'Varun Chakaravarthy', 'Rahul Chahar', 'Mukesh Choudhary', 'Harshit Rana', 'Ishant Sharma', 'Jaydev Unadkat', 'Mukesh Kumar', 'Abdul Samad', 'Riyan Parag', 'Khaleel Ahmed', 'Avesh Khan', 'Faf du Plessis', 'Arjun Tendulkar', 'Mohammed Shami', 'Shivam Dube', 'Lockie Ferguson', 'Josh Hazlewood', 'Prabhsimran Singh', 'Rishabh Pant', 'Corbin Bosch', 'Mohammed Siraj', 'Prasidh Krishna', 'Marcus Stoinis', 'Harpreet Brar', 'Rahmanullah Gurbaz', 'Rashid Khan', 'Washington Sundar', 'Hardik Pandya', 'Heinrich Klaasen', 'Rinku Singh', 'Nehal Wadhera', 'Romario Shepherd', 'Manav Suthar', 'Vijaykumar Vyshak', 'Himmat Singh', 'Ayush Badoni', 'Liam Livingstone', 'Nathan Ellis', 'Moeen Ali', 'Karn Sharma', 'Yashasvi Jaiswal', 'Shimron Hetmyer', 'Axar Patel', 'Mayank Yadav', 'Abhinav Manohar', 'Ashutosh Sharma', 'Rachin Ravindra', 'Shahrukh Khan', 'Anrich Nortje', 'Mayank Markande', 'Yuzvendra Chahal', 'Tushar Deshpande', 'Noor Ahmad', 'Kagiso Rabada', 'Marco Jansen', 'Virat Kohli', 'Abhishek Sharma', 'Jitesh Sharma', 'Harnoor Singh', 'Bhuvneshwar Kumar', 'Abishek Porel', 'Angkrish Raghuvanshi', 'Kuldeep Yadav', 'David Miller', 'Anuj Rawat', 'Josh Inglis', 'Kumar Kartikeya', 'Akash Deep', 'Rahul Tewatia', 'Ramandeep Singh', 'Sherfane Rutherford', 'Glenn Maxwell', 'Sandeep Sharma', 'Suryakumar Yadav', 'Shamar Joseph', 'Pat Cummins', 'Quinton de Kock', 'Ravichandran Ashwin', 'Jasprit Bumrah', 'Sai Sudharsan', 'Shreyas Iyer', 'Swastik Chikara', 'Rajvardhan Hangargekar', 'Manoj Bhandage', 'Nitish Rana', 'Rasikh Salam Dar', 'Deepak Chahar', 'MS Dhoni', 'Aaron Hardie', 'Priyansh Arya', 'Phil Salt', 'Sameer Rizvi', 'Mitchell Santner', 'Manish Pandey', 'Suyash Sharma', 'Kamlesh Nagarkoti', 'Will Jacks', 'Azmatullah Omarzai', 'Adam Zampa', 'Spencer Johnson', 'Jamie Overton', 'Shashank Singh', 'Rovman Powell', 'Suryansh Shedge', 'Maheesh Theekshana', 'Ruturaj Gaikwad', 'Shubman Gill', 'Mohit Sharma', 'Sai Kishore', 'Raj Bawa', 'Ishan Kishan', 'Mitchell Marsh', 'Nitish Reddy', 'Karim Janat', 'Yash Dayal', 'Bevon Jacobs', 'Ryan Rickelton', 'Rajat Patidar', 'Tristan Stubbs', 'Gerald Coetzee', 'Glenn Phillips', 'Tim David', 'Ravi Bishnoi', 'Donovan Ferreira', 'Jayant Yadav', 'Trent Boult', 'Jofra Archer', 'Akash Madhwal', 'Darshan Nalkande', 'Kwena Maphaka', 'KL Rahul', 'Arshdeep Singh', 'Aiden Markram', 'Sachin Baby', 'Dushmantha Chameera', 'Naman Dhir', 'Karun Nair', 'Wanindu Hasaranga', 'Arshad Khan', 'Devdutt Padikkal', 'Robin Minz', 'Shahbaz Ahmed', 'Mohsin Khan', 'Krunal Pandya', 'Ravindra Jadeja', 'Mitchell Starc', 'Sanju Samson', 'Jos Buttler', 'Atharva Taide', 'Musheer Khan', 'Devon Conway', 'Venkatesh Iyer', 'Andre Russell', 'Sunil Narine', 'Chetan Sakariya', 'T Natarajan', 'Ajinkya Rahane', 'Shreyas Gopal', 'Tilak Varma', 'Vijay Shankar', 'Shubham Dubey', 'Anukul Roy', 'Deepak Hooda', 'Harshal Patel', 'Rahul Tripathi', 'Lungi Ngidi', 'Matheesha Pathirana', 'Vaibhav Arora', 'Nicholas Pooran', 'Jake Fraser-McGurk', 'Sam Curran', 'Rohit Sharma', 'Mujeeb ur Rahman', 'Anshul Kamboj', 'Mahipal Lomror']

class Score:
    def __init__(self,json_filename):
        self.json_filename = json_filename
        self.data = self.scorecard()
        #self.full_player_list,self.player_list,self.winner,self.man_of_the_match,self.catchers,self.stumpers,self.main_runouters,self.secondary_runouters,self.bowled,self.lbw,self.innings_list,self.batsmen_list,self.bowlers_info = self.scorecard()
    def scorecard(self):
        # Define the file path
        file_path = "filtered_ipl_json/"+self.json_filename
        # Open and read the JSON file
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)  # Convert JSON to Python dictionary      
        return data  # Output the dictionary

def name_matching(player):
    if player == "Nithish Kumar Reddy":
        print("Nitish Reddy")
        return "Nitish Reddy"
    if player == "VR Iyer":
        print("Venkatesh Iyer")
        return "Venkatesh Iyer"
    if player == "RK Singh":
        print("Rinku Singh")
        return "Rinku Singh"
    if player == "JM Sharma":
        print("Jitesh Sharma")
        return "Jitesh Sharma"
    if player == "TH David":
        print("Tim David")
        return "Tim David"
    if player == "KH Pandya":
        print("Krunal Pandya")
        return "Krunal Pandya"
    if player == "N Rana":
        print("Nitish Rana")
        return "Nitish Rana"
    if player == "YBK Jaiswal":
        print("Yashasvi Jaiswal")
        return "Yashasvi Jaiswal"
    if player == "RG Sharma":
        print("Rohit Sharma")
        return "Rohit Sharma"
    if player == "SA Yadav":
        print("Suryakumar Yadav")
        return "Suryakumar Yadav"
    if player == "DL Chahar":
        print("Deepak Chahar")
        return "Deepak Chahar"
    if player == "TA Boult":
        print("Trent Boult")
        return "Trent Boult"
    if player == "MM Sharma":
        print("Mohit Sharma")
        return "Mohit Sharma"
    if player == "PWH de Silva":
        print("Wanindu Hasaranga")
        return "Wanindu Hasaranga"
    if player == "Akash Singh":
        return None
    if player == "KK Nair":
        return "Karun Nair"
    if player == "D Brevis":
        return "Dewald Brevis"
    if player == "Urvil Patel":
        return player
    if player == "A Mhatre":
        return "Ayush Mhatre"
    if player == "PHKD Mendis":
        return "Kusal Mendis"
    # if player == "Fazalhaq Farooqi":
    #     return player
    if player == "B Kumar":
        return "Bhuvneshwar Kumar"
    if player == "WP O'Rourke":
        return "Will O'Rourke"
    if player == "Lhuan-dre Pretorius":
        return "Lhuan-dre Pretorius"
    if player == "Mustafizur Rahman":
        return "Mustafizur Rahman"
    if player == "M Khan":
        return "Musheer Khan"
    best_match, score = process.extractOne(player, names)
    if score > 74:
        print(f"Matched",player,"to",best_match,"Score:",score)
        names.pop(names.index(best_match))
        return best_match
    else:
        print("No close match found for",player,"Score",score,best_match)
        return None
    
def final_names_list():
    file_number = 1473438
    cricsheets_names = []
    espn_names = []
    not_found = []

    while True:
        file_name = str(file_number) + ".json"
        try:
            match_score = Score(file_name)
        except:
            break

        data = match_score.data
        info = data['info']
        players = info['players']

        for team in players:
            for player in players[team]:
                if player not in cricsheets_names:
                    final_name = name_matching(player)
                    if final_name != None:
                        cricsheets_names.append(player)
                        espn_names.append(final_name)
                    else:
                        if player not in not_found:
                            not_found.append(player)
        file_number += 1
    return cricsheets_names,espn_names,not_found


cricsheets_names,espn_names,not_found = final_names_list()
print("-"*100)
for i in range(len(cricsheets_names)):
    print(cricsheets_names[i],espn_names[i])
print(cricsheets_names)
print(espn_names)
print(not_found)