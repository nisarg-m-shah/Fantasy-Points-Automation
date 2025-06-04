from ScrapingCricsheets import Score
import pandas as pd

full_player_list = [
    # RCB Squad
    "Philip Salt", "Virat Kohli", "Mayank Agarawal", "Rajat Patidar", "Liam Livingstone",
    "Jitesh Sharma", "Romario Shepherd", "Krunal Pandya", "Bhuvneshwar Kumar", "Yash Dayal",
    "Nuwan Thushara", "Suyash Sharma", "Josh Hazlewood", "Tim Seifert", "Rasikh Dar Salam",
    "Manoj Bhandage", "Swapnil Singh", "Blessing Muzarabani", "Tim David", "Mohit Rathee",
    "Swastik Chikara", "Abhinandan Singh",
    # PBKS Squad
    "Priyansh Arya", "Prabhsimran Singh", "Josh Inglis", "Shreyas Iyer", "Nehal Wadhera",
    "Shashank Singh", "Marcus Stoinis", "Harpreet Brar", "Kyle Jamieson", "Arshdeep Singh",
    "Vijaykumar Vyshak", "Yuzvendra Chahal", "Suryansh Shedge", "Musheer Khan", "Xavier Bartlett",
    "Praveen Dubey", "Azmatullah Omarzai", "Vishnu Vinod", "Yash Thakur", "Aaron Hardie",
    "Kuldeep Sen", "Mitchell Owen", "Harnoor Singh", "Pyla Avinash"
]

player_list = {
    "Royal Challengers Bengaluru": [
        "Philip Salt", "Virat Kohli", "Mayank Agarawal", "Rajat Patidar", "Liam Livingstone",
        "Jitesh Sharma", "Romario Shepherd", "Krunal Pandya", "Bhuvneshwar Kumar", "Yash Dayal",
        "Josh Hazlewood", "Suyash Sharma"
    ],
    "Punjab Kings": [
        "Priyansh Arya", "Prabhsimran Singh", "Josh Inglis", "Shreyas Iyer", "Nehal Wadhera",
        "Shashank Singh", "Marcus Stoinis", "Azmatullah Omarzai", "Kyle Jamieson",
        "Vijaykumar Vyshak", "Arshdeep Singh", "Yuzvendra Chahal"
    ]
}

innings_list = ["Royal Challengers Bengaluru", "Punjab Kings"]
winner = "Royal Challengers Bengaluru"
man_of_the_match = "Krunal Pandya"

catchers = [
    "Shreyas Iyer",      # Salt
    "Arshdeep Singh",    # Agarwal
    "Shreyas Iyer",      # Pandya
    "Priyansh Arya",     # Bhuvneshwar
    "Phil Salt",         # Arya (PBKS)
    "Bhuvneshwar Kumar", # Prabhsimran Singh (PBKS)
    "Liam Livingstone",  # Josh Inglis (PBKS)
    "Jitesh Sharma",     # Shreyas Iyer (PBKS)
    "Krunal Pandya",     # Nehal Wadhera (PBKS)
    "Yash Dayal",        # Marcus Stoinis (PBKS)
    "Manoj Bhandage"     # Azmatullah Omarzai (PBKS, sub)
]
stumpers = []
main_runouters = []
secondary_runouters = []
bowled = ["Vijaykumar Vyshak"]  # Jitesh Sharma
lbw = ["Kyle Jamieson", "Kyle Jamieson", "Arshdeep Singh"]  # Patidar, Livingstone, Shepherd

batsmen_list = pd.DataFrame([
    # RCB Innings
    {'Innings Number': 1, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Phil Salt', 'Dismissal': 'c Shreyas Iyer b Jamieson', 'Runs': 16, 'Balls': 9, '4s': 2, '6s': 1, 'Strike Rate': 177.77},
    {'Innings Number': 1, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Virat Kohli', 'Dismissal': 'c & b Azmatullah Omarzai', 'Runs': 43, 'Balls': 35, '4s': 3, '6s': 0, 'Strike Rate': 122.85},
    {'Innings Number': 1, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Mayank Agarwal', 'Dismissal': 'c Arshdeep Singh b Chahal', 'Runs': 24, 'Balls': 18, '4s': 2, '6s': 1, 'Strike Rate': 133.33},
    {'Innings Number': 1, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Rajat Patidar', 'Dismissal': 'lbw b Jamieson', 'Runs': 26, 'Balls': 16, '4s': 1, '6s': 2, 'Strike Rate': 162.50},
    {'Innings Number': 1, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Liam Livingstone', 'Dismissal': 'lbw b Jamieson', 'Runs': 25, 'Balls': 15, '4s': 0, '6s': 2, 'Strike Rate': 166.66},
    {'Innings Number': 1, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Jitesh Sharma', 'Dismissal': 'b Vyshak', 'Runs': 24, 'Balls': 10, '4s': 2, '6s': 2, 'Strike Rate': 240.00},
    {'Innings Number': 1, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Romario Shepherd', 'Dismissal': 'lbw b Arshdeep Singh', 'Runs': 17, 'Balls': 9, '4s': 1, '6s': 1, 'Strike Rate': 188.88},
    {'Innings Number': 1, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Krunal Pandya', 'Dismissal': 'c Iyer b Arshdeep Singh', 'Runs': 4, 'Balls': 5, '4s': 0, '6s': 0, 'Strike Rate': 80.00},
    {'Innings Number': 1, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Bhuvneshwar Kumar', 'Dismissal': 'c Arya b Arshdeep Singh', 'Runs': 1, 'Balls': 2, '4s': 0, '6s': 0, 'Strike Rate': 50.00},
    {'Innings Number': 1, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Yash Dayal', 'Dismissal': 'not out', 'Runs': 1, 'Balls': 1, '4s': 0, '6s': 0, 'Strike Rate': 100.00},
    # PBKS Innings
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Priyansh Arya', 'Dismissal': 'c Phil Salt b Hazlewood', 'Runs': 24, 'Balls': 19, '4s': 4, '6s': 0, 'Strike Rate': 126.31},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Prabhsimran Singh', 'Dismissal': 'c Bhuvneshwar Kumar b Krunal Pandya', 'Runs': 26, 'Balls': 22, '4s': 0, '6s': 2, 'Strike Rate': 118.18},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Josh Inglis', 'Dismissal': 'c Liam Livingstone b Krunal Pandya', 'Runs': 39, 'Balls': 23, '4s': 1, '6s': 4, 'Strike Rate': 169.56},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Shreyas Iyer', 'Dismissal': 'c Jitesh Sharma b Romario Shepherd', 'Runs': 1, 'Balls': 2, '4s': 0, '6s': 0, 'Strike Rate': 50.00},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Nehal Wadhera', 'Dismissal': 'c Krunal Pandya b Bhuvneshwar Kumar', 'Runs': 15, 'Balls': 18, '4s': 0, '6s': 1, 'Strike Rate': 83.33},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Shashank Singh', 'Dismissal': 'not out', 'Runs': 61, 'Balls': 30, '4s': 3, '6s': 6, 'Strike Rate': 203.33},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Marcus Stoinis', 'Dismissal': 'c Yash Dayal b Bhuvneshwar Kumar', 'Runs': 6, 'Balls': 2, '4s': 0, '6s': 1, 'Strike Rate': 300.00},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Azmatullah Omarzai', 'Dismissal': 'c sub (MS Bhandage) b Yash Dayal', 'Runs': 1, 'Balls': 2, '4s': 0, '6s': 0, 'Strike Rate': 50.00},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Kyle Jamieson', 'Dismissal': 'not out', 'Runs': 0, 'Balls': 2, '4s': 0, '6s': 0, 'Strike Rate': 0.00},
])

bowlers_info = pd.DataFrame([
    # PBKS Bowling (RCB Batting)
    {'Innings Number': 1, 'Innings Name': 'Royal Challengers Bengaluru', 'Bowler': 'Arshdeep Singh', 'Overs': '4.0', 'Maidens': 0, 'Runs': 40, 'Wickets': 3, 'Economy': 10.00, '0s': 8},
    {'Innings Number': 1, 'Innings Name': 'Royal Challengers Bengaluru', 'Bowler': 'Kyle Jamieson', 'Overs': '4.0', 'Maidens': 0, 'Runs': 48, 'Wickets': 3, 'Economy': 12.00, '0s': 9},
    {'Innings Number': 1, 'Innings Name': 'Royal Challengers Bengaluru', 'Bowler': 'Azmatullah Omarzai', 'Overs': '4.0', 'Maidens': 0, 'Runs': 35, 'Wickets': 1, 'Economy': 8.75, '0s': 3},
    {'Innings Number': 1, 'Innings Name': 'Royal Challengers Bengaluru', 'Bowler': 'Vijaykumar Vyshak', 'Overs': '4.0', 'Maidens': 0, 'Runs': 30, 'Wickets': 1, 'Economy': 7.50, '0s': 5},
    {'Innings Number': 1, 'Innings Name': 'Royal Challengers Bengaluru', 'Bowler': 'Yuzvendra Chahal', 'Overs': '4.0', 'Maidens': 0, 'Runs': 37, 'Wickets': 1, 'Economy': 9.25, '0s': 3},
    # RCB Bowling (PBKS Batting)
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Bowler': 'Bhuvneshwar Kumar', 'Overs': '4.0', 'Maidens': 0, 'Runs': 38, 'Wickets': 2, 'Economy': 9.50, '0s': 9},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Bowler': 'Yash Dayal', 'Overs': '3.0', 'Maidens': 0, 'Runs': 18, 'Wickets': 1, 'Economy': 6.00, '0s': 10},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Bowler': 'Josh Hazlewood', 'Overs': '4.0', 'Maidens': 0, 'Runs': 54, 'Wickets': 1, 'Economy': 13.50, '0s': 7},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Bowler': 'Krunal Pandya', 'Overs': '4.0', 'Maidens': 0, 'Runs': 17, 'Wickets': 2, 'Economy': 4.25, '0s': 12},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Bowler': 'Suyash Sharma', 'Overs': '2.0', 'Maidens': 0, 'Runs': 19, 'Wickets': 0, 'Economy': 9.50, '0s': 4},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Bowler': 'Romario Shepherd', 'Overs': '3.0', 'Maidens': 0, 'Runs': 30, 'Wickets': 1, 'Economy': 10.00, '0s': 5},
])

# --- Score Object Creation ---

Final_score = Score.from_data(
    json_filename="1473512.json",
    url="Final",
    full_player_list=full_player_list,
    player_list=player_list,
    innings_list=innings_list,
    winner=winner,
    man_of_the_match=man_of_the_match,
    catchers=catchers,
    stumpers=stumpers,
    main_runouters=main_runouters,
    secondary_runouters=secondary_runouters,
    bowled=bowled,
    lbw=lbw,
    batsmen_list=batsmen_list,
    bowlers_info=bowlers_info
)

#Final_score.printing_scorecard()








# --- Data Section ---

# Full squads including impact subs and players who did not bat/bowl
full_player_list = [
    # Mumbai Indians squad
    "Rohit Sharma", "Jonny Bairstow", "Tilak Varma", "Suryakumar Yadav", "Hardik Pandya",
    "Naman Dhir", "Raj Angad Bawa", "Mitchell Santner", "Trent Boult", "Jasprit Bumrah",
    "Reece Topley", "Ashwani Kumar",
    # Punjab Kings squad
    "Priyansh Arya", "Prabhsimran Singh", "Josh Inglis", "Shreyas Iyer", "Nehal Wadhera",
    "Shashank Singh", "Marcus Stoinis", "Azmatullah Omarzai", "Kyle Jamieson",
    "Vijaykumar Vyshak", "Arshdeep Singh", "Yuzvendra Chahal"
]

player_list = {
    "Mumbai Indians": [
        "Rohit Sharma", "Jonny Bairstow", "Tilak Varma", "Suryakumar Yadav", "Hardik Pandya",
        "Naman Dhir", "Raj Angad Bawa", "Mitchell Santner", "Trent Boult", "Jasprit Bumrah",
        "Reece Topley", "Ashwani Kumar"
    ],
    "Punjab Kings": [
        "Priyansh Arya", "Prabhsimran Singh", "Josh Inglis", "Shreyas Iyer", "Nehal Wadhera",
        "Shashank Singh", "Marcus Stoinis", "Azmatullah Omarzai", "Kyle Jamieson",
        "Vijaykumar Vyshak", "Arshdeep Singh", "Yuzvendra Chahal"
    ]
}

innings_list = ["Mumbai Indians", "Punjab Kings"]
winner = "Punjab Kings"
man_of_the_match = "Shreyas Iyer"

# Catchers based on dismissals
catchers = [
    "Vijaykumar Vyshak",  # Rohit Sharma
    "Josh Inglis",        # Jonny Bairstow
    "Priyansh Arya",      # Tilak Varma
    "Nehal Wadhera",      # Suryakumar Yadav
    "Josh Inglis",        # Hardik Pandya
    "Marcus Stoinis",     # Naman Dhir
    "Phil Salt",          # Priyansh Arya (Not in this match, ignore)
    "Jonny Bairstow",     # Josh Inglis (PBKS)
    "Yash Dayal",         # Marcus Stoinis (Not in this match, ignore)
    "Manoj Bhandage"      # Not in this match, ignore
]
# Remove irrelevant catchers not in this match
catchers = [
    "Vijaykumar Vyshak", "Josh Inglis", "Priyansh Arya", "Nehal Wadhera", "Josh Inglis", "Marcus Stoinis", "Jonny Bairstow","Hardik Pandya","Reece Topley", "Mitchell Santner"
]

stumpers = []  # No stumpings recorded

# Run outs
main_runouters = ["Hardik Pandya"]
secondary_runouters = []

# Bowled wickets (none in this match)
bowled = []

# LBW dismissals (none explicitly mentioned)
lbw = []

# Batsmen DataFrame
batsmen_list = pd.DataFrame([
    # Mumbai Indians innings
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Rohit Sharma', 'Dismissal': 'c Vyshak b Stoinis', 'Runs': 8, 'Balls': 7, '4s': 1, '6s': 0, 'Strike Rate': 114.28},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Jonny Bairstow', 'Dismissal': 'c Inglis b Vyshak', 'Runs': 38, 'Balls': 24, '4s': 3, '6s': 2, 'Strike Rate': 158.33},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Tilak Varma', 'Dismissal': 'c Arya b Jamieson', 'Runs': 44, 'Balls': 29, '4s': 2, '6s': 2, 'Strike Rate': 151.72},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Suryakumar Yadav', 'Dismissal': 'c Wadhera b Chahal', 'Runs': 44, 'Balls': 26, '4s': 4, '6s': 3, 'Strike Rate': 169.23},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Hardik Pandya', 'Dismissal': 'c Inglis b Azmatullah Omarzai', 'Runs': 15, 'Balls': 13, '4s': 1, '6s': 0, 'Strike Rate': 115.38},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Naman Dhir', 'Dismissal': 'c Stoinis b Azmatullah Omarzai', 'Runs': 37, 'Balls': 18, '4s': 7, '6s': 0, 'Strike Rate': 205.55},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Raj Angad Bawa', 'Dismissal': 'not out', 'Runs': 8, 'Balls': 4, '4s': 0, '6s': 0, 'Strike Rate': 200.00},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Mitchell Santner', 'Dismissal': 'not out', 'Runs': 0, 'Balls': 1, '4s': 0, '6s': 0, 'Strike Rate': 0.00},
    # Punjab Kings innings
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Priyansh Arya', 'Dismissal': 'c Pandya b Ashwani Kumar', 'Runs': 20, 'Balls': 10, '4s': 2, '6s': 1, 'Strike Rate': 200.00},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Prabhsimran Singh', 'Dismissal': 'c Topley b Boult', 'Runs': 6, 'Balls': 9, '4s': 1, '6s': 0, 'Strike Rate': 66.66},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Josh Inglis', 'Dismissal': 'c Bairstow b Pandya', 'Runs': 38, 'Balls': 21, '4s': 5, '6s': 2, 'Strike Rate': 180.95},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Shreyas Iyer', 'Dismissal': 'not out', 'Runs': 87, 'Balls': 41, '4s': 5, '6s': 8, 'Strike Rate': 212.19},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Nehal Wadhera', 'Dismissal': 'c Santner b Ashwani Kumar', 'Runs': 48, 'Balls': 29, '4s': 4, '6s': 2, 'Strike Rate': 165.51},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Shashank Singh', 'Dismissal': 'run out (Pandya)', 'Runs': 2, 'Balls': 3, '4s': 0, '6s': 0, 'Strike Rate': 66.66},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Marcus Stoinis', 'Dismissal': 'not out', 'Runs': 2, 'Balls': 2, '4s': 0, '6s': 0, 'Strike Rate': 100.00},
])

# Bowlers DataFrame
bowlers_info = pd.DataFrame([
    # PBKS Bowling (MI Batting)
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Bowler': 'Arshdeep Singh', 'Overs': '4.0', 'Maidens': 0, 'Runs': 44, 'Wickets': 0, 'Economy': 11.00, '0s': 4},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Bowler': 'Kyle Jamieson', 'Overs': '4.0', 'Maidens': 0, 'Runs': 30, 'Wickets': 1, 'Economy': 7.50, '0s': 8},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Bowler': 'Marcus Stoinis', 'Overs': '1.0', 'Maidens': 0, 'Runs': 14, 'Wickets': 1, 'Economy': 14.00, '0s': 3},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Bowler': 'Azmatullah Omarzai', 'Overs': '4.0', 'Maidens': 0, 'Runs': 43, 'Wickets': 2, 'Economy': 10.75, '0s': 7},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Bowler': 'Vijaykumar Vyshak', 'Overs': '3.0', 'Maidens': 0, 'Runs': 30, 'Wickets': 1, 'Economy': 10.00, '0s': 6},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Bowler': 'Yuzvendra Chahal', 'Overs': '4.0', 'Maidens': 0, 'Runs': 39, 'Wickets': 1, 'Economy': 9.75, '0s': 7},
    # MI Bowling (PBKS Batting)
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Bowler': 'Trent Boult', 'Overs': '4.0', 'Maidens': 0, 'Runs': 38, 'Wickets': 1, 'Economy': 9.50, '0s': 9},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Bowler': 'Reece Topley', 'Overs': '3.0', 'Maidens': 0, 'Runs': 40, 'Wickets': 0, 'Economy': 13.33, '0s': 6},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Bowler': 'Jasprit Bumrah', 'Overs': '4.0', 'Maidens': 0, 'Runs': 40, 'Wickets': 0, 'Economy': 10.00, '0s': 6},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Bowler': 'Ashwani Kumar', 'Overs': '4.0', 'Maidens': 0, 'Runs': 55, 'Wickets': 2, 'Economy': 13.75, '0s': 9},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Bowler': 'Mitchell Santner', 'Overs': '2.0', 'Maidens': 0, 'Runs': 15, 'Wickets': 0, 'Economy': 7.50, '0s': 1},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Bowler': 'Hardik Pandya', 'Overs': '2.0', 'Maidens': 0, 'Runs': 19, 'Wickets': 1, 'Economy': 9.50, '0s': 4},
])

Qualifier2_score = Score.from_data(
    json_filename="1473511.json",
    url="Qualifier 2",
    full_player_list=full_player_list,
    player_list=player_list,
    innings_list=innings_list,
    winner=winner,
    man_of_the_match=man_of_the_match,
    catchers=catchers,
    stumpers=stumpers,
    main_runouters=main_runouters,
    secondary_runouters=secondary_runouters,
    bowled=bowled,
    lbw=lbw,
    batsmen_list=batsmen_list,
    bowlers_info=bowlers_info
)

#Qualifier2_score.printing_scorecard()










# --- Data Section ---

# Only the players from the actual match sheet
full_player_list = [
    # Mumbai Indians
    "Rohit Sharma", "Jonny Bairstow", "Suryakumar Yadav", "Tilak Varma", "Hardik Pandya",
    "Naman Dhir", "Mitchell Santner", "Raj Bawa", "Trent Boult", "Jasprit Bumrah",
    "Richard Gleeson", "Ashwani Kumar",
    # Gujarat Titans
    "Sai Sudharsan", "Shubman Gill", "Kusal Mendis", "Washington Sundar", "Sherfane Rutherford",
    "Rahul Tewatia", "M Shahrukh Khan", "Rashid Khan", "Sai Kishore", "Gerald Coetzee",
    "Prasidh Krishna", "Mohammed Siraj"
]

player_list = {
    "Mumbai Indians": [
        "Rohit Sharma", "Jonny Bairstow", "Suryakumar Yadav", "Tilak Varma", "Hardik Pandya",
        "Naman Dhir", "Mitchell Santner", "Raj Bawa", "Trent Boult", "Jasprit Bumrah",
        "Richard Gleeson", "Ashwani Kumar"
    ],
    "Gujarat Titans": [
        "Sai Sudharsan", "Shubman Gill", "Kusal Mendis", "Washington Sundar", "Sherfane Rutherford",
        "Rahul Tewatia", "Shahrukh Khan", "Rashid Khan", "Sai Kishore", "Gerald Coetzee",
        "Prasidh Krishna", "Mohammed Siraj"
    ]
}

innings_list = ["Mumbai Indians", "Gujarat Titans"]
winner = "Mumbai Indians"
man_of_the_match = "Rohit Sharma"

catchers = [
    "Rashid Khan",    # Rohit Sharma, Naman Dhir
    "Coetzee",        # Jonny Bairstow
    "Washington Sundar", # Suryakumar Yadav
    "Kusal Mendis",   # Tilak Varma (†Mendis)
    "Rashid Khan",    # Naman Dhir
    "Tilak Varma",    # Sherfane Rutherford
    "Suryakumar Yadav" # M Shahrukh Khan
]

stumpers = []

main_runouters = []
secondary_runouters = []

bowled = ["Richard Gleeson", "Jasprit Bumrah"]  # Sai Sudharsan, Washington Sundar

lbw = ["Trent Boult"]  # Shubman Gill

batsmen_list = pd.DataFrame([
    # Mumbai Indians innings
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Rohit Sharma', 'Dismissal': 'c Rashid Khan b Prasidh Krishna', 'Runs': 81, 'Balls': 50, '4s': 9, '6s': 4, 'Strike Rate': 162.00},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Jonny Bairstow', 'Dismissal': 'c Coetzee b Sai Kishore', 'Runs': 47, 'Balls': 22, '4s': 4, '6s': 3, 'Strike Rate': 213.63},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Suryakumar Yadav', 'Dismissal': 'c Washington Sundar b Sai Kishore', 'Runs': 33, 'Balls': 20, '4s': 1, '6s': 3, 'Strike Rate': 165.00},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Tilak Varma', 'Dismissal': 'c †Mendis b Mohammed Siraj', 'Runs': 25, 'Balls': 11, '4s': 0, '6s': 3, 'Strike Rate': 227.27},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Hardik Pandya', 'Dismissal': 'not out', 'Runs': 22, 'Balls': 9, '4s': 0, '6s': 3, 'Strike Rate': 244.44},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Naman Dhir', 'Dismissal': 'c Rashid Khan b Prasidh Krishna', 'Runs': 9, 'Balls': 6, '4s': 0, '6s': 1, 'Strike Rate': 150.00},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Mitchell Santner', 'Dismissal': 'not out', 'Runs': 0, 'Balls': 2, '4s': 0, '6s': 0, 'Strike Rate': 0.00},
    # Gujarat Titans innings
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Batsman': 'Sai Sudharsan', 'Dismissal': 'b Gleeson', 'Runs': 80, 'Balls': 49, '4s': 10, '6s': 1, 'Strike Rate': 163.26},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Batsman': 'Shubman Gill', 'Dismissal': 'lbw b Boult', 'Runs': 1, 'Balls': 2, '4s': 0, '6s': 0, 'Strike Rate': 50.00},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Batsman': 'Kusal Mendis', 'Dismissal': 'hit wicket b Santner', 'Runs': 20, 'Balls': 10, '4s': 1, '6s': 2, 'Strike Rate': 200.00},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Batsman': 'Washington Sundar', 'Dismissal': 'b Bumrah', 'Runs': 48, 'Balls': 24, '4s': 5, '6s': 3, 'Strike Rate': 200.00},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Batsman': 'Sherfane Rutherford', 'Dismissal': 'c Tilak Varma b Boult', 'Runs': 24, 'Balls': 15, '4s': 4, '6s': 0, 'Strike Rate': 160.00},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Batsman': 'Rahul Tewatia', 'Dismissal': 'not out', 'Runs': 16, 'Balls': 11, '4s': 1, '6s': 1, 'Strike Rate': 145.45},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Batsman': 'Shahrukh Khan', 'Dismissal': 'c Suryakumar Yadav b Ashwani Kumar', 'Runs': 13, 'Balls': 7, '4s': 0, '6s': 1, 'Strike Rate': 185.71},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Batsman': 'Rashid Khan', 'Dismissal': 'not out', 'Runs': 0, 'Balls': 2, '4s': 0, '6s': 0, 'Strike Rate': 0.00},
])

bowlers_info = pd.DataFrame([
    # GT Bowling (MI Batting)
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Bowler': 'Mohammed Siraj', 'Overs': '4.0', 'Maidens': 0, 'Runs': 37, 'Wickets': 1, 'Economy': 9.25, '0s': 7},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Bowler': 'Prasidh Krishna', 'Overs': '4.0', 'Maidens': 0, 'Runs': 53, 'Wickets': 2, 'Economy': 13.25, '0s': 7},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Bowler': 'Sai Kishore', 'Overs': '4.0', 'Maidens': 0, 'Runs': 42, 'Wickets': 2, 'Economy': 10.50, '0s': 6},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Bowler': 'Rashid Khan', 'Overs': '4.0', 'Maidens': 0, 'Runs': 31, 'Wickets': 0, 'Economy': 7.75, '0s': 9},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Bowler': 'Gerald Coetzee', 'Overs': '3.0', 'Maidens': 0, 'Runs': 51, 'Wickets': 0, 'Economy': 17.00, '0s': 5},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Bowler': 'Washington Sundar', 'Overs': '1.0', 'Maidens': 0, 'Runs': 7, 'Wickets': 0, 'Economy': 7.00, '0s': 2},
    # MI Bowling (GT Batting)
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Bowler': 'Trent Boult', 'Overs': '4.0', 'Maidens': 0, 'Runs': 56, 'Wickets': 2, 'Economy': 14.00, '0s': 6},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Bowler': 'Jasprit Bumrah', 'Overs': '4.0', 'Maidens': 0, 'Runs': 27, 'Wickets': 1, 'Economy': 6.75, '0s': 11},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Bowler': 'Richard Gleeson', 'Overs': '3.3', 'Maidens': 0, 'Runs': 39, 'Wickets': 1, 'Economy': 11.14, '0s': 5},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Bowler': 'Hardik Pandya', 'Overs': '3.0', 'Maidens': 0, 'Runs': 37, 'Wickets': 0, 'Economy': 12.33, '0s': 3},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Bowler': 'Mitchell Santner', 'Overs': '1.0', 'Maidens': 0, 'Runs': 10, 'Wickets': 1, 'Economy': 10.00, '0s': 2},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Bowler': 'Naman Dhir', 'Overs': '1.0', 'Maidens': 0, 'Runs': 9, 'Wickets': 0, 'Economy': 9.00, '0s': 1},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Bowler': 'Ashwani Kumar', 'Overs': '3.3', 'Maidens': 0, 'Runs': 28, 'Wickets': 1, 'Economy': 8.00, '0s': 6},
])

# --- Score Object Creation ---
Eliminator_score = Score.from_data(
    json_filename="1473510.json",
    url="Eliminator",
    full_player_list=full_player_list,
    player_list=player_list,
    innings_list=innings_list,
    winner=winner,
    man_of_the_match=man_of_the_match,
    catchers=catchers,
    stumpers=stumpers,
    main_runouters=main_runouters,
    secondary_runouters=secondary_runouters,
    bowled=bowled,
    lbw=lbw,
    batsmen_list=batsmen_list,
    bowlers_info=bowlers_info
)

#Eliminator_score.printing_scorecard()






# --- Data Section ---

full_player_list = [
    # Punjab Kings
    "Priyansh Arya", "Prabhsimran Singh", "Josh Inglis", "Shreyas Iyer", "Nehal Wadhera",
    "Marcus Stoinis", "Shashank Singh", "Musheer Khan", "Azmatullah Omarzai", "Harpreet Brar",
    "Kyle Jamieson", "Arshdeep Singh",
    # Royal Challengers Bengaluru
    "Phil Salt", "Virat Kohli", "Mayank Agarwal", "Rajat Patidar", "Liam Livingstone",
    "Jitesh Sharma", "Romario Shepherd", "Krunal Pandya", "Bhuvneshwar Kumar",
    "Yash Dayal", "Josh Hazlewood", "Suyash Sharma"
]

player_list = {
    "Punjab Kings": [
        "Priyansh Arya", "Prabhsimran Singh", "Josh Inglis", "Shreyas Iyer", "Nehal Wadhera",
        "Marcus Stoinis", "Shashank Singh", "Musheer Khan", "Azmatullah Omarzai", "Harpreet Brar",
        "Kyle Jamieson", "Arshdeep Singh"
    ],
    "Royal Challengers Bengaluru": [
        "Phil Salt", "Virat Kohli", "Mayank Agarwal", "Rajat Patidar", "Liam Livingstone",
        "Jitesh Sharma", "Romario Shepherd", "Krunal Pandya", "Bhuvneshwar Kumar",
        "Yash Dayal", "Josh Hazlewood", "Suyash Sharma"
    ]
}

innings_list = ["Punjab Kings", "Royal Challengers Bengaluru"]
winner = "Royal Challengers Bengaluru"
man_of_the_match = "Suyash Sharma"

# Dismissals (catchers, bowled, lbw, etc.)
catchers = [
    "Krunal Pandya",      # Priyansh Arya
    "Jitesh Sharma",      # Prabhsimran Singh
    "Bhuvneshwar Kumar",  # Josh Inglis
    "Jitesh Sharma",      # Shreyas Iyer
    "Jitesh Sharma",      # Azmatullah Omarzai
    "Shreyas Iyer",       # Mayank Agarwal
    "Josh Inglis"
]
stumpers = []
main_runouters = []
secondary_runouters = []
bowled = ["Yash Dayal", "Suyash Sharma", "Suyash Sharma", "Romario Shepherd"]  # Nehal Wadhera, Josh Inglis, Marcus Stoinis, Harpreet Brar
lbw = ["Suyash Sharma"]  # Musheer Khan

batsmen_list = pd.DataFrame([
    # Punjab Kings
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Priyansh Arya', 'Dismissal': 'c Pandya b Yash Dayal', 'Runs': 7, 'Balls': 5, '4s': 1, '6s': 0, 'Strike Rate': 140.00},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Prabhsimran Singh', 'Dismissal': 'c †Sharma b Kumar', 'Runs': 18, 'Balls': 10, '4s': 2, '6s': 1, 'Strike Rate': 180.00},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Josh Inglis', 'Dismissal': 'c Kumar b Hazlewood', 'Runs': 4, 'Balls': 7, '4s': 0, '6s': 0, 'Strike Rate': 57.14},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Shreyas Iyer', 'Dismissal': 'c †Sharma b Hazlewood', 'Runs': 2, 'Balls': 3, '4s': 0, '6s': 0, 'Strike Rate': 66.66},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Nehal Wadhera', 'Dismissal': 'b Yash Dayal', 'Runs': 8, 'Balls': 10, '4s': 1, '6s': 0, 'Strike Rate': 80.00},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Marcus Stoinis', 'Dismissal': 'b Suyash Sharma', 'Runs': 26, 'Balls': 17, '4s': 2, '6s': 2, 'Strike Rate': 152.94},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Shashank Singh', 'Dismissal': 'b Suyash Sharma', 'Runs': 3, 'Balls': 5, '4s': 0, '6s': 0, 'Strike Rate': 60.00},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Musheer Khan', 'Dismissal': 'lbw b Suyash Sharma', 'Runs': 0, 'Balls': 3, '4s': 0, '6s': 0, 'Strike Rate': 0.00},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Azmatullah Omarzai', 'Dismissal': 'c †Sharma b Hazlewood', 'Runs': 18, 'Balls': 12, '4s': 1, '6s': 1, 'Strike Rate': 150.00},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Harpreet Brar', 'Dismissal': 'b Shepherd', 'Runs': 4, 'Balls': 11, '4s': 0, '6s': 0, 'Strike Rate': 36.36},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Kyle Jamieson', 'Dismissal': 'not out', 'Runs': 0, 'Balls': 3, '4s': 0, '6s': 0, 'Strike Rate': 0.00},
    # RCB
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Phil Salt', 'Dismissal': 'not out', 'Runs': 56, 'Balls': 27, '4s': 6, '6s': 3, 'Strike Rate': 207.40},
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Virat Kohli', 'Dismissal': 'c †Inglis b Jamieson', 'Runs': 12, 'Balls': 12, '4s': 2, '6s': 0, 'Strike Rate': 100.00},
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Mayank Agarwal', 'Dismissal': 'c Iyer b Musheer Khan', 'Runs': 19, 'Balls': 13, '4s': 2, '6s': 1, 'Strike Rate': 146.15},
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Rajat Patidar', 'Dismissal': 'not out', 'Runs': 15, 'Balls': 8, '4s': 1, '6s': 1, 'Strike Rate': 187.50},
])

bowlers_info = pd.DataFrame([
    # PBKS Bowling (RCB Batting)
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Bowler': 'Arshdeep Singh', 'Overs': '2.0', 'Maidens': 0, 'Runs': 20, 'Wickets': 0, 'Economy': 10.00, '0s': 3},
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Bowler': 'Kyle Jamieson', 'Overs': '3.0', 'Maidens': 1, 'Runs': 27, 'Wickets': 1, 'Economy': 9.00, '0s': 9},
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Bowler': 'Azmatullah Omarzai', 'Overs': '1.0', 'Maidens': 0, 'Runs': 10, 'Wickets': 0, 'Economy': 10.00, '0s': 3},
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Bowler': 'Harpreet Brar', 'Overs': '2.0', 'Maidens': 0, 'Runs': 18, 'Wickets': 0, 'Economy': 9.00, '0s': 2},
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Bowler': 'Musheer Khan', 'Overs': '2.0', 'Maidens': 0, 'Runs': 27, 'Wickets': 1, 'Economy': 13.50, '0s': 1},
    # RCB Bowling (PBKS Batting)
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Bowler': 'Bhuvneshwar Kumar', 'Overs': '2.0', 'Maidens': 0, 'Runs': 17, 'Wickets': 1, 'Economy': 8.50, '0s': 5},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Bowler': 'Yash Dayal', 'Overs': '4.0', 'Maidens': 0, 'Runs': 26, 'Wickets': 2, 'Economy': 6.50, '0s': 11},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Bowler': 'Josh Hazlewood', 'Overs': '3.1', 'Maidens': 0, 'Runs': 21, 'Wickets': 3, 'Economy': 6.63, '0s': 10},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Bowler': 'Suyash Sharma', 'Overs': '3.0', 'Maidens': 0, 'Runs': 17, 'Wickets': 3, 'Economy': 5.66, '0s': 11},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Bowler': 'Krunal Pandya', 'Overs': '1.0', 'Maidens': 0, 'Runs': 10, 'Wickets': 0, 'Economy': 10.00, '0s': 2},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Bowler': 'Romario Shepherd', 'Overs': '1.0', 'Maidens': 0, 'Runs': 5, 'Wickets': 1, 'Economy': 5.00, '0s': 4},
])

Qualifier1_score = Score.from_data(
    json_filename="1473509.json",
    url="Qualifier 1",
    full_player_list=full_player_list,
    player_list=player_list,
    innings_list=innings_list,
    winner=winner,
    man_of_the_match=man_of_the_match,
    catchers=catchers,
    stumpers=stumpers,
    main_runouters=main_runouters,
    secondary_runouters=secondary_runouters,
    bowled=bowled,
    lbw=lbw,
    batsmen_list=batsmen_list,
    bowlers_info=bowlers_info
)

#Qualifier1_score.printing_scorecard()






# --- Data Section ---

full_player_list = [
    # Lucknow Super Giants
    "Mitchell Marsh", "Matthew Breetzke", "Rishabh Pant", "Nicholas Pooran", "Abdul Samad",
    "Ayush Badoni", "Himmat Singh", "Shahbaz Ahmed", "Digvesh Rathi", "Avesh Khan",
    "Will O’Rourke", "Akash Singh",
    # Royal Challengers Bengaluru
    "Phil Salt", "Virat Kohli", "Rajat Patidar", "Liam Livingstone", "Mayank Agarwal",
    "Jitesh Sharma", "Romario Shepherd", "Krunal Pandya", "Bhuvneshwar Kumar",
    "Yash Dayal", "Nuwan Thushara", "Suyash Sharma"
]

player_list = {
    "Lucknow Super Giants": [
        "Mitchell Marsh", "Matthew Breetzke", "Rishabh Pant", "Nicholas Pooran", "Abdul Samad",
        "Ayush Badoni", "Himmat Singh", "Shahbaz Ahmed", "Digvesh Rathi", "Avesh Khan",
        "Will O’Rourke", "Akash Singh"
    ],
    "Royal Challengers Bengaluru": [
        "Phil Salt", "Virat Kohli", "Rajat Patidar", "Liam Livingstone", "Mayank Agarwal",
        "Jitesh Sharma", "Romario Shepherd", "Krunal Pandya", "Bhuvneshwar Kumar",
        "Yash Dayal", "Nuwan Thushara", "Suyash Sharma"
    ]
}

innings_list = ["Lucknow Super Giants", "Royal Challengers Bengaluru"]
winner = "Royal Challengers Bengaluru"
man_of_the_match = "Jitesh Sharma"

# Dismissals (catchers, bowled, lbw, etc.)
catchers = [
    "Jitesh Sharma",    # Marsh
    "Yash Dayal",       # Pooran
    "Digvesh Rathi",            # Salt
    "Ayush Badoni",           # Kohli
    "Abdul Samad"       # Patidar
]
stumpers = []
main_runouters = []
secondary_runouters = []
bowled = ["Nuwan Thushara"]  # Breetzke, Pooran, Salt
lbw = ["William O'Rourke"]  # Livingstone

batsmen_list = pd.DataFrame([
    # LSG
    {'Innings Number': 1, 'Innings Name': 'Lucknow Super Giants', 'Batsman': 'Mitchell Marsh', 'Dismissal': 'c †Sharma b Kumar', 'Runs': 67, 'Balls': 37, '4s': 4, '6s': 5, 'Strike Rate': 181.08},
    {'Innings Number': 1, 'Innings Name': 'Lucknow Super Giants', 'Batsman': 'Matthew Breetzke', 'Dismissal': 'b Thushara', 'Runs': 14, 'Balls': 12, '4s': 1, '6s': 1, 'Strike Rate': 116.66},
    {'Innings Number': 1, 'Innings Name': 'Lucknow Super Giants', 'Batsman': 'Rishabh Pant', 'Dismissal': 'not out', 'Runs': 118, 'Balls': 61, '4s': 11, '6s': 8, 'Strike Rate': 193.44},
    {'Innings Number': 1, 'Innings Name': 'Lucknow Super Giants', 'Batsman': 'Nicholas Pooran', 'Dismissal': 'c Yash Dayal b Shepherd', 'Runs': 13, 'Balls': 10, '4s': 1, '6s': 0, 'Strike Rate': 130.00},
    {'Innings Number': 1, 'Innings Name': 'Lucknow Super Giants', 'Batsman': 'Abdul Samad', 'Dismissal': 'not out', 'Runs': 1, 'Balls': 1, '4s': 0, '6s': 0, 'Strike Rate': 100.00},
    # RCB
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Phil Salt', 'Dismissal': 'c Rathi b Akash Singh', 'Runs': 30, 'Balls': 19, '4s': 6, '6s': 0, 'Strike Rate': 157.89},
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Virat Kohli', 'Dismissal': 'c Badoni b Avesh Khan', 'Runs': 54, 'Balls': 30, '4s': 10, '6s': 0, 'Strike Rate': 180.00},
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Rajat Patidar', 'Dismissal': 'c Abdul Samad b O\'Rourke', 'Runs': 14, 'Balls': 7, '4s': 1, '6s': 1, 'Strike Rate': 200.00},
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Liam Livingstone', 'Dismissal': 'lbw b O\'Rourke', 'Runs': 0, 'Balls': 1, '4s': 0, '6s': 0, 'Strike Rate': 0.00},
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Mayank Agarwal', 'Dismissal': 'not out', 'Runs': 41, 'Balls': 23, '4s': 5, '6s': 0, 'Strike Rate': 178.26},
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Batsman': 'Jitesh Sharma', 'Dismissal': 'not out', 'Runs': 85, 'Balls': 33, '4s': 8, '6s': 6, 'Strike Rate': 257.57},
])

bowlers_info = pd.DataFrame([
    # RCB Bowling (LSG Batting)
    {'Innings Number': 1, 'Innings Name': 'Lucknow Super Giants', 'Bowler': 'Nuwan Thushara', 'Overs': '4.0', 'Maidens': 0, 'Runs': 26, 'Wickets': 1, 'Economy': 6.50, '0s': 10},
    {'Innings Number': 1, 'Innings Name': 'Lucknow Super Giants', 'Bowler': 'Krunal Pandya', 'Overs': '2.0', 'Maidens': 0, 'Runs': 14, 'Wickets': 0, 'Economy': 7.00, '0s': 5},
    {'Innings Number': 1, 'Innings Name': 'Lucknow Super Giants', 'Bowler': 'Yash Dayal', 'Overs': '3.0', 'Maidens': 0, 'Runs': 44, 'Wickets': 0, 'Economy': 14.66, '0s': 3},
    {'Innings Number': 1, 'Innings Name': 'Lucknow Super Giants', 'Bowler': 'Bhuvneshwar Kumar', 'Overs': '4.0', 'Maidens': 0, 'Runs': 46, 'Wickets': 1, 'Economy': 11.50, '0s': 8},
    {'Innings Number': 1, 'Innings Name': 'Lucknow Super Giants', 'Bowler': 'Suyash Sharma', 'Overs': '3.0', 'Maidens': 0, 'Runs': 39, 'Wickets': 0, 'Economy': 13.00, '0s': 4},
    {'Innings Number': 1, 'Innings Name': 'Lucknow Super Giants', 'Bowler': 'Romario Shepherd', 'Overs': '4.0', 'Maidens': 0, 'Runs': 51, 'Wickets': 1, 'Economy': 12.75, '0s': 6},
    # LSG Bowling (RCB Batting)
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Bowler': 'Akash Singh', 'Overs': '4.0', 'Maidens': 0, 'Runs': 40, 'Wickets': 1, 'Economy': 10.00, '0s': 6},
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Bowler': 'Will O\'Rourke', 'Overs': '4.0', 'Maidens': 0, 'Runs': 74, 'Wickets': 2, 'Economy': 18.50, '0s': 3},
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Bowler': 'Digvesh Rathi', 'Overs': '4.0', 'Maidens': 0, 'Runs': 36, 'Wickets': 0, 'Economy': 9.00, '0s': 5},
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Bowler': 'Shahbaz Ahmed', 'Overs': '3.0', 'Maidens': 0, 'Runs': 39, 'Wickets': 0, 'Economy': 13.00, '0s': 3},
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Bowler': 'Avesh Khan', 'Overs': '3.0', 'Maidens': 0, 'Runs': 32, 'Wickets': 1, 'Economy': 10.66, '0s': 5},
    {'Innings Number': 2, 'Innings Name': 'Royal Challengers Bengaluru', 'Bowler': 'Ayush Badoni', 'Overs': '0.4', 'Maidens': 0, 'Runs': 9, 'Wickets': 0, 'Economy': 13.50, '0s': 1},
])

lsgvrcb_score = Score.from_data(
    json_filename="1473508.json",
    url="LSG vs RCB",
    full_player_list=full_player_list,
    player_list=player_list,
    innings_list=innings_list,
    winner="Royal Challengers Bengaluru",
    man_of_the_match=man_of_the_match,
    catchers=catchers,
    stumpers=stumpers,
    main_runouters=main_runouters,
    secondary_runouters=secondary_runouters,
    bowled=bowled,
    lbw=lbw,
    batsmen_list=batsmen_list,
    bowlers_info=bowlers_info
)

#lsgvrcb_score.printing_scorecard()





# --- Data Section ---

full_player_list = [
    # Mumbai Indians
    "Ryan Rickelton", "Rohit Sharma", "Suryakumar Yadav", "Tilak Varma", "Will Jacks",
    "Hardik Pandya", "Naman Dhir", "Mitchell Santner", "Deepak Chahar", "Trent Boult",
    "Jasprit Bumrah", "Ashwani Kumar",
    # Punjab Kings
    "Priyansh Arya", "Prabhsimran Singh", "Josh Inglis", "Shreyas Iyer", "Nehal Wadhera",
    "Shashank Singh", "Marcus Stoinis", "Marco Jansen", "Harpreet Brar", "Kyle Jamieson",
    "Arshdeep Singh", "Vijaykumar Vyshak"
]

player_list = {
    "Mumbai Indians": [
        "Ryan Rickelton", "Rohit Sharma", "Suryakumar Yadav", "Tilak Varma", "Will Jacks",
        "Hardik Pandya", "Naman Dhir", "Mitchell Santner", "Deepak Chahar", "Trent Boult",
        "Jasprit Bumrah", "Ashwani Kumar"
    ],
    "Punjab Kings": [
        "Priyansh Arya", "Prabhsimran Singh", "Josh Inglis", "Shreyas Iyer", "Nehal Wadhera",
        "Shashank Singh", "Marcus Stoinis", "Marco Jansen", "Harpreet Brar", "Kyle Jamieson",
        "Arshdeep Singh", "Vijaykumar Vyshak"
    ]
}

innings_list = ["Mumbai Indians", "Punjab Kings"]
winner = "Punjab Kings"
man_of_the_match = "Josh Inglis"

catchers = [
    "Shreyas Iyer",       # Rickelton
    "Nehal Wadhera",      # Rohit Sharma
    "Josh Inglis",        # Hardik Pandya
    "Arshdeep Singh",     # Tilak Varma
    "Marco Jansen",             # Will Jacks
    "Priyansh Arya",               # Naman Dhir
    "Suryakumar Yadav",   # Arya (PBKS)
    "Ashwani Kumar"       # Prabhsimran Singh (PBKS)
]

stumpers = []
main_runouters = []
secondary_runouters = []
bowled = []  # Vyshak (Tilak Varma), Santner (Arya, Inglis), Bumrah (Prabhsimran)
lbw = ["Arshdeep Singh", "Mitchell Santner"]       # Suryakumar Yadav, Inglis

batsmen_list = pd.DataFrame([
    # Mumbai Indians
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Ryan Rickelton', 'Dismissal': 'c Iyer b Jansen', 'Runs': 27, 'Balls': 20, '4s': 5, '6s': 0, 'Strike Rate': 135.00},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Rohit Sharma', 'Dismissal': 'c Wadhera b Harpreet Brar', 'Runs': 24, 'Balls': 21, '4s': 2, '6s': 1, 'Strike Rate': 114.28},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Suryakumar Yadav', 'Dismissal': 'lbw b Arshdeep Singh', 'Runs': 57, 'Balls': 39, '4s': 6, '6s': 2, 'Strike Rate': 146.15},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Tilak Varma', 'Dismissal': 'c Arshdeep Singh b Vyshak', 'Runs': 1, 'Balls': 4, '4s': 0, '6s': 0, 'Strike Rate': 25.00},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Will Jacks', 'Dismissal': 'c Jansen b Vyshak', 'Runs': 17, 'Balls': 8, '4s': 2, '6s': 1, 'Strike Rate': 212.50},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Hardik Pandya', 'Dismissal': 'c †Inglis b Jansen', 'Runs': 26, 'Balls': 15, '4s': 2, '6s': 2, 'Strike Rate': 173.33},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Naman Dhir', 'Dismissal': 'c Arya b Arshdeep Singh', 'Runs': 20, 'Balls': 12, '4s': 0, '6s': 2, 'Strike Rate': 166.66},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Batsman': 'Mitchell Santner', 'Dismissal': 'not out', 'Runs': 1, 'Balls': 1, '4s': 0, '6s': 0, 'Strike Rate': 100.00},
    # Punjab Kings
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Priyansh Arya', 'Dismissal': 'c Yadav b Santner', 'Runs': 62, 'Balls': 35, '4s': 9, '6s': 2, 'Strike Rate': 177.14},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Prabhsimran Singh', 'Dismissal': 'c Ashwani Kumar b Bumrah', 'Runs': 13, 'Balls': 16, '4s': 1, '6s': 1, 'Strike Rate': 81.25},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Josh Inglis', 'Dismissal': 'lbw b Santner', 'Runs': 73, 'Balls': 42, '4s': 9, '6s': 3, 'Strike Rate': 173.80},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Shreyas Iyer', 'Dismissal': 'not out', 'Runs': 26, 'Balls': 16, '4s': 1, '6s': 2, 'Strike Rate': 162.50},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Batsman': 'Nehal Wadhera', 'Dismissal': 'not out', 'Runs': 2, 'Balls': 2, '4s': 0, '6s': 0, 'Strike Rate': 100.00},
])

bowlers_info = pd.DataFrame([
    # PBKS Bowling (MI Batting)
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Bowler': 'Arshdeep Singh', 'Overs': '4.0', 'Maidens': 0, 'Runs': 28, 'Wickets': 2, 'Economy': 7.00, '0s': 11},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Bowler': 'Kyle Jamieson', 'Overs': '4.0', 'Maidens': 0, 'Runs': 42, 'Wickets': 0, 'Economy': 10.50, '0s': 8},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Bowler': 'Marco Jansen', 'Overs': '4.0', 'Maidens': 0, 'Runs': 34, 'Wickets': 2, 'Economy': 8.50, '0s': 12},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Bowler': 'Harpreet Brar', 'Overs': '4.0', 'Maidens': 0, 'Runs': 36, 'Wickets': 1, 'Economy': 9.00, '0s': 5},
    {'Innings Number': 1, 'Innings Name': 'Mumbai Indians', 'Bowler': 'Vijaykumar Vyshak', 'Overs': '4.0', 'Maidens': 0, 'Runs': 44, 'Wickets': 2, 'Economy': 11.00, '0s': 10},
    # MI Bowling (PBKS Batting)
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Bowler': 'Trent Boult', 'Overs': '3.3', 'Maidens': 0, 'Runs': 36, 'Wickets': 0, 'Economy': 10.28, '0s': 7},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Bowler': 'Deepak Chahar', 'Overs': '3.0', 'Maidens': 1, 'Runs': 28, 'Wickets': 0, 'Economy': 9.33, '0s': 10},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Bowler': 'Jasprit Bumrah', 'Overs': '4.0', 'Maidens': 0, 'Runs': 23, 'Wickets': 1, 'Economy': 5.75, '0s': 15},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Bowler': 'Mitchell Santner', 'Overs': '4.0', 'Maidens': 0, 'Runs': 41, 'Wickets': 2, 'Economy': 10.25, '0s': 7},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Bowler': 'Hardik Pandya', 'Overs': '2.0', 'Maidens': 0, 'Runs': 29, 'Wickets': 0, 'Economy': 14.50, '0s': 1},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Bowler': 'Ashwani Kumar', 'Overs': '1.0', 'Maidens': 0, 'Runs': 16, 'Wickets': 0, 'Economy': 16.00, '0s': 0},
    {'Innings Number': 2, 'Innings Name': 'Punjab Kings', 'Bowler': 'Will Jacks', 'Overs': '1.0', 'Maidens': 0, 'Runs': 11, 'Wickets': 0, 'Economy': 11.00, '0s': 2},
])

mivpbks_score = Score.from_data(
    json_filename="1473507.json",
    url="MI vs PBKS",
    full_player_list=full_player_list,
    player_list=player_list,
    innings_list=innings_list,
    winner="Punjab Kings",
    man_of_the_match=man_of_the_match,
    catchers=catchers,
    stumpers=stumpers,
    main_runouters=main_runouters,
    secondary_runouters=secondary_runouters,
    bowled=bowled,
    lbw=lbw,
    batsmen_list=batsmen_list,
    bowlers_info=bowlers_info
)

mivpbks_score.printing_scorecard()




# --- Data Section ---

full_player_list = [
    # Sunrisers Hyderabad
    "Abhishek Sharma", "Travis Head", "Heinrich Klaasen", "Ishan Kishan", "Aniket Verma",
    "Nitish Kumar Reddy", "Abhinav Manohar", "Pat Cummins", "Harshal Patel", "Jaydev Unadkat",
    "Eshan Malinga", "Harsh Dubey",
    # Kolkata Knight Riders
    "Quinton de Kock", "Sunil Narine", "Ajinkya Rahane", "Angkrish Raghuvanshi", "Rinku Singh",
    "Andre Russell", "Manish Pandey", "Ramandeep Singh", "Harshit Rana", "Vaibhav Arora",
    "Anrich Nortje", "Varun Chakravarthy"
]

player_list = {
    "Sunrisers Hyderabad": [
        "Abhishek Sharma", "Travis Head", "Heinrich Klaasen", "Ishan Kishan", "Aniket Verma",
        "Nitish Kumar Reddy", "Abhinav Manohar", "Pat Cummins", "Harshal Patel", "Jaydev Unadkat",
        "Eshan Malinga", "Harsh Dubey"
    ],
    "Kolkata Knight Riders": [
        "Quinton de Kock", "Sunil Narine", "Ajinkya Rahane", "Angkrish Raghuvanshi", "Rinku Singh",
        "Andre Russell", "Manish Pandey", "Ramandeep Singh", "Harshit Rana", "Vaibhav Arora",
        "Anrich Nortje", "Varun Chakravarthy"
    ]
}

innings_list = ["Sunrisers Hyderabad", "Kolkata Knight Riders"]
winner = "Sunrisers Hyderabad"
man_of_the_match = "Heinrich Klaasen"

# Dismissals (catchers, bowled, lbw, etc.)
catchers = [
    "Rinku Singh",                # Abhishek Sharma (c Singh b Narine)
    "Andre Russell",              # Travis Head (c Russell b Narine)
    "Anrich Nortje",               # Ishan Kishan (c Nortje b Arora)
    "Abhinav Manohar",      # Quinton de Kock (c Manohar b Malinga)
    "Abhishek Sharma",      # Rahane (c Abhishek Sharma b Unadkat)
    "Nitish Kumar Reddy",   # Raghuvanshi (c Nitish Kumar Reddy b Malinga)
    "Nitish Kumar Reddy",   # Rinku Singh (c Nitish Kumar Reddy b Dubey)
    "Abhinav Manohar",      # Manish Pandey (c Manohar b Unadkat)
    "Eeshan Malinga",              # Harshit Rana (c & b Malinga)
]
stumpers = []
main_runouters = ["Jaydev Unadkat"]   # Vaibhav Arora run out (Unadkat)
secondary_runouters = []
bowled = ["Jaydev Unadkat", "Harsh Dubey"]  # Narine, Raghuvanshi, Ramandeep
lbw = ["Harsh Dubey"]  # Russell

batsmen_list = pd.DataFrame([
    # Sunrisers Hyderabad
    {'Innings Number': 1, 'Innings Name': 'Sunrisers Hyderabad', 'Batsman': 'Abhishek Sharma', 'Dismissal': 'c Singh b Narine', 'Runs': 32, 'Balls': 16, '4s': 4, '6s': 2, 'Strike Rate': 200.00},
    {'Innings Number': 1, 'Innings Name': 'Sunrisers Hyderabad', 'Batsman': 'Travis Head', 'Dismissal': 'c Russell b Narine', 'Runs': 76, 'Balls': 40, '4s': 6, '6s': 6, 'Strike Rate': 190.00},
    {'Innings Number': 1, 'Innings Name': 'Sunrisers Hyderabad', 'Batsman': 'Heinrich Klaasen', 'Dismissal': 'not out', 'Runs': 105, 'Balls': 39, '4s': 7, '6s': 9, 'Strike Rate': 269.23},
    {'Innings Number': 1, 'Innings Name': 'Sunrisers Hyderabad', 'Batsman': 'Ishan Kishan', 'Dismissal': 'c Nortje b Arora', 'Runs': 29, 'Balls': 20, '4s': 4, '6s': 1, 'Strike Rate': 145.00},
    {'Innings Number': 1, 'Innings Name': 'Sunrisers Hyderabad', 'Batsman': 'Aniket Verma', 'Dismissal': 'not out', 'Runs': 12, 'Balls': 6, '4s': 1, '6s': 1, 'Strike Rate': 200.00},
    # Kolkata Knight Riders
    {'Innings Number': 2, 'Innings Name': 'Kolkata Knight Riders', 'Batsman': 'Quinton de Kock', 'Dismissal': 'c Manohar b Malinga', 'Runs': 9, 'Balls': 13, '4s': 0, '6s': 0, 'Strike Rate': 69.23},
    {'Innings Number': 2, 'Innings Name': 'Kolkata Knight Riders', 'Batsman': 'Sunil Narine', 'Dismissal': 'b Unadkat', 'Runs': 31, 'Balls': 16, '4s': 3, '6s': 3, 'Strike Rate': 193.75},
    {'Innings Number': 2, 'Innings Name': 'Kolkata Knight Riders', 'Batsman': 'Ajinkya Rahane', 'Dismissal': 'c Abhishek Sharma b Unadkat', 'Runs': 15, 'Balls': 8, '4s': 3, '6s': 0, 'Strike Rate': 187.50},
    {'Innings Number': 2, 'Innings Name': 'Kolkata Knight Riders', 'Batsman': 'Angkrish Raghuvanshi', 'Dismissal': 'c Nitish Kumar Reddy b Malinga', 'Runs': 14, 'Balls': 18, '4s': 1, '6s': 0, 'Strike Rate': 77.77},
    {'Innings Number': 2, 'Innings Name': 'Kolkata Knight Riders', 'Batsman': 'Rinku Singh', 'Dismissal': 'c Nitish Kumar Reddy b Dubey', 'Runs': 9, 'Balls': 6, '4s': 0, '6s': 1, 'Strike Rate': 150.00},
    {'Innings Number': 2, 'Innings Name': 'Kolkata Knight Riders', 'Batsman': 'Andre Russell', 'Dismissal': 'lbw b Dubey', 'Runs': 0, 'Balls': 1, '4s': 0, '6s': 0, 'Strike Rate': 0.00},
    {'Innings Number': 2, 'Innings Name': 'Kolkata Knight Riders', 'Batsman': 'Manish Pandey', 'Dismissal': 'c Manohar b Unadkat', 'Runs': 37, 'Balls': 23, '4s': 2, '6s': 3, 'Strike Rate': 160.86},
    {'Innings Number': 2, 'Innings Name': 'Kolkata Knight Riders', 'Batsman': 'Ramandeep Singh', 'Dismissal': 'b Dubey', 'Runs': 13, 'Balls': 5, '4s': 0, '6s': 2, 'Strike Rate': 260.00},
    {'Innings Number': 2, 'Innings Name': 'Kolkata Knight Riders', 'Batsman': 'Harshit Rana', 'Dismissal': 'c & b Malinga', 'Runs': 34, 'Balls': 21, '4s': 2, '6s': 3, 'Strike Rate': 161.90},
    {'Innings Number': 2, 'Innings Name': 'Kolkata Knight Riders', 'Batsman': 'Vaibhav Arora', 'Dismissal': 'run out (Unadkat)', 'Runs': 0, 'Balls': 1, '4s': 0, '6s': 0, 'Strike Rate': 0.00},
    {'Innings Number': 2, 'Innings Name': 'Kolkata Knight Riders', 'Batsman': 'Anrich Nortje', 'Dismissal': 'not out', 'Runs': 0, 'Balls': 0, '4s': 0, '6s': 0, 'Strike Rate': 0.00},
])

bowlers_info = pd.DataFrame([
    # KKR Bowling (SRH Batting)
    {'Innings Number': 1, 'Innings Name': 'Sunrisers Hyderabad', 'Bowler': 'Vaibhav Arora', 'Overs': '4.0', 'Maidens': 0, 'Runs': 39, 'Wickets': 1, 'Economy': 9.75, '0s': 10},
    {'Innings Number': 1, 'Innings Name': 'Sunrisers Hyderabad', 'Bowler': 'Anrich Nortje', 'Overs': '4.0', 'Maidens': 0, 'Runs': 60, 'Wickets': 0, 'Economy': 15.00, '0s': 7},
    {'Innings Number': 1, 'Innings Name': 'Sunrisers Hyderabad', 'Bowler': 'Harshit Rana', 'Overs': '3.0', 'Maidens': 0, 'Runs': 40, 'Wickets': 0, 'Economy': 13.33, '0s': 5},
    {'Innings Number': 1, 'Innings Name': 'Sunrisers Hyderabad', 'Bowler': 'Sunil Narine', 'Overs': '4.0', 'Maidens': 0, 'Runs': 42, 'Wickets': 2, 'Economy': 10.50, '0s': 8},
    {'Innings Number': 1, 'Innings Name': 'Sunrisers Hyderabad', 'Bowler': 'Varun Chakravarthy', 'Overs': '3.0', 'Maidens': 0, 'Runs': 54, 'Wickets': 0, 'Economy': 18.00, '0s': 2},
    {'Innings Number': 1, 'Innings Name': 'Sunrisers Hyderabad', 'Bowler': 'Andre Russell', 'Overs': '2.0', 'Maidens': 0, 'Runs': 34, 'Wickets': 0, 'Economy': 17.00, '0s': 2},
    # SRH Bowling (KKR Batting)
    {'Innings Number': 2, 'Innings Name': 'Kolkata Knight Riders', 'Bowler': 'Pat Cummins', 'Overs': '2.0', 'Maidens': 0, 'Runs': 25, 'Wickets': 0, 'Economy': 12.50, '0s': 6},
    {'Innings Number': 2, 'Innings Name': 'Kolkata Knight Riders', 'Bowler': 'Jaydev Unadkat', 'Overs': '4.0', 'Maidens': 0, 'Runs': 24, 'Wickets': 3, 'Economy': 6.00, '0s': 12},
    {'Innings Number': 2, 'Innings Name': 'Kolkata Knight Riders', 'Bowler': 'Harshal Patel', 'Overs': '2.0', 'Maidens': 0, 'Runs': 21, 'Wickets': 0, 'Economy': 10.50, '0s': 5},
    {'Innings Number': 2, 'Innings Name': 'Kolkata Knight Riders', 'Bowler': 'Eshan Malinga', 'Overs': '3.4', 'Maidens': 0, 'Runs': 31, 'Wickets': 3, 'Economy': 8.45, '0s': 10},
    {'Innings Number': 2, 'Innings Name': 'Kolkata Knight Riders', 'Bowler': 'Harsh Dubey', 'Overs': '4.0', 'Maidens': 0, 'Runs': 34, 'Wickets': 3, 'Economy': 8.50, '0s': 10},
    {'Innings Number': 2, 'Innings Name': 'Kolkata Knight Riders', 'Bowler': 'Nitish Kumar Reddy', 'Overs': '1.0', 'Maidens': 0, 'Runs': 6, 'Wickets': 0, 'Economy': 6.00, '0s': 1},
    {'Innings Number': 2, 'Innings Name': 'Kolkata Knight Riders', 'Bowler': 'Abhishek Sharma', 'Overs': '2.0', 'Maidens': 0, 'Runs': 25, 'Wickets': 0, 'Economy': 12.50, '0s': 4},
])

srhvskkr_score = Score.from_data(
    json_filename="1473506.json",
    url="SRH vs KKR",
    full_player_list=full_player_list,
    player_list=player_list,
    innings_list=innings_list,
    winner=winner,
    man_of_the_match=man_of_the_match,
    catchers=catchers,
    stumpers=stumpers,
    main_runouters=main_runouters,
    secondary_runouters=secondary_runouters,
    bowled=bowled,
    lbw=lbw,
    batsmen_list=batsmen_list,
    bowlers_info=bowlers_info
)

#srhvskkr_score.printing_scorecard()




# --- Data Section ---

full_player_list = [
    # Chennai Super Kings
    "Ayush Mhatre", "Devon Conway", "Urvil Patel", "Shivam Dube", "Dewald Brevis",
    "Ravindra Jadeja", "MS Dhoni", "Deepak Hooda", "Noor Ahmad", "Anshul Kamboj",
    "Khaleel Ahmed", "Matheesha Pathirana",
    # Gujarat Titans
    "Sai Sudharsan", "Shubman Gill", "Jos Buttler", "Sherfane Rutherford", "Shahrukh Khan",
    "Rahul Tewatia", "Rashid Khan", "Gerald Coetzee", "Arshad Khan", "Sai Kishore",
    "Mohammed Siraj", "Prasidh Krishna"
]

player_list = {
    "Chennai Super Kings": [
        "Ayush Mhatre", "Devon Conway", "Urvil Patel", "Shivam Dube", "Dewald Brevis",
        "Ravindra Jadeja", "MS Dhoni", "Deepak Hooda", "Noor Ahmad", "Anshul Kamboj",
        "Khaleel Ahmed", "Matheesha Pathirana"
    ],
    "Gujarat Titans": [
        "Sai Sudharsan", "Shubman Gill", "Jos Buttler", "Sherfane Rutherford", "M Shahrukh Khan",
        "Rahul Tewatia", "Rashid Khan", "Gerald Coetzee", "Arshad Khan", "Sai Kishore",
        "Mohammed Siraj", "Prasidh Krishna"
    ]
}

innings_list = ["Chennai Super Kings", "Gujarat Titans"]
winner = "Chennai Super Kings"
man_of_the_match = "Dewald Brevis"

catchers = [
    "Mohammed Siraj",    # Ayush Mhatre
    "Shubman Gill",      # Urvil Patel
    "Gerald Coetzee",           # Shivam Dube
    "Jos Buttler",       # Dewald Brevis
    "Shivam Dube",              # Sai Sudharsan
    "Urvil Patel",             # Shubman Gill
    "Anshul Kamboj",            # Jos Buttler
    "Ayush Mhatre",            # Sherfane Rutherford
    "Matheesha Pathirana",         # M Shahrukh Khan
    "Shivam Dube",              # Rahul Tewatia
    "Urvil Patel",             # Rashid Khan
    "MS Dhoni"              # Sai Kishore
]

stumpers = []
main_runouters = []
secondary_runouters = []
bowled = [
    "Rashid Khan","Noor Ahmad", "Pathirana"
]  # Devon Conway, Urvil Patel, Shivam Dube, Sai Sudharsan, Rahul Tewatia, Gerald Coetzee, Sai Kishore
lbw = []

batsmen_list = pd.DataFrame([
    # CSK
    {'Innings Number': 1, 'Innings Name': 'Chennai Super Kings', 'Batsman': 'Ayush Mhatre', 'Dismissal': 'c Mohammed Siraj b Prasidh Krishna', 'Runs': 34, 'Balls': 17, '4s': 3, '6s': 3, 'Strike Rate': 200.00},
    {'Innings Number': 1, 'Innings Name': 'Chennai Super Kings', 'Batsman': 'Devon Conway', 'Dismissal': 'b Rashid Khan', 'Runs': 52, 'Balls': 35, '4s': 6, '6s': 2, 'Strike Rate': 148.57},
    {'Innings Number': 1, 'Innings Name': 'Chennai Super Kings', 'Batsman': 'Urvil Patel', 'Dismissal': 'c Shubman Gill b Sai Kishore', 'Runs': 37, 'Balls': 19, '4s': 4, '6s': 2, 'Strike Rate': 194.73},
    {'Innings Number': 1, 'Innings Name': 'Chennai Super Kings', 'Batsman': 'Shivam Dube', 'Dismissal': 'c Coetzee b M Shahrukh Khan', 'Runs': 17, 'Balls': 8, '4s': 0, '6s': 2, 'Strike Rate': 212.50},
    {'Innings Number': 1, 'Innings Name': 'Chennai Super Kings', 'Batsman': 'Dewald Brevis', 'Dismissal': 'c †Buttler b Prasidh Krishna', 'Runs': 57, 'Balls': 23, '4s': 4, '6s': 5, 'Strike Rate': 247.82},
    {'Innings Number': 1, 'Innings Name': 'Chennai Super Kings', 'Batsman': 'Ravindra Jadeja', 'Dismissal': 'not out', 'Runs': 21, 'Balls': 18, '4s': 1, '6s': 1, 'Strike Rate': 116.66},
    # GT
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Batsman': 'Sai Sudharsan', 'Dismissal': 'c Dube b Jadeja', 'Runs': 41, 'Balls': 28, '4s': 6, '6s': 0, 'Strike Rate': 146.42},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Batsman': 'Shubman Gill', 'Dismissal': 'c Patel b Kamboj', 'Runs': 13, 'Balls': 9, '4s': 1, '6s': 1, 'Strike Rate': 144.44},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Batsman': 'Jos Buttler', 'Dismissal': 'c Kamboj b Ahmed', 'Runs': 5, 'Balls': 7, '4s': 0, '6s': 0, 'Strike Rate': 71.42},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Batsman': 'Sherfane Rutherford', 'Dismissal': 'c Mhatre b Kamboj', 'Runs': 0, 'Balls': 4, '4s': 0, '6s': 0, 'Strike Rate': 0.00},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Batsman': 'Shahrukh Khan', 'Dismissal': 'c Pathirana b Jadeja', 'Runs': 19, 'Balls': 15, '4s': 0, '6s': 2, 'Strike Rate': 126.66},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Batsman': 'Rahul Tewatia', 'Dismissal': 'c Dube b Noor Ahmad', 'Runs': 14, 'Balls': 10, '4s': 1, '6s': 0, 'Strike Rate': 140.00},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Batsman': 'Rashid Khan', 'Dismissal': 'c Patel b Noor Ahmad', 'Runs': 12, 'Balls': 8, '4s': 1, '6s': 1, 'Strike Rate': 150.00},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Batsman': 'Gerald Coetzee', 'Dismissal': 'b Pathirana', 'Runs': 5, 'Balls': 5, '4s': 1, '6s': 0, 'Strike Rate': 100.00},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Batsman': 'Arshad Khan', 'Dismissal': 'b Noor Ahmad', 'Runs': 20, 'Balls': 14, '4s': 0, '6s': 3, 'Strike Rate': 142.85},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Batsman': 'Sai Kishore', 'Dismissal': 'c †Dhoni b Kamboj', 'Runs': 3, 'Balls': 7, '4s': 0, '6s': 0, 'Strike Rate': 42.85},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Batsman': 'Mohammed Siraj', 'Dismissal': 'not out', 'Runs': 3, 'Balls': 4, '4s': 0, '6s': 0, 'Strike Rate': 75.00},
])

bowlers_info = pd.DataFrame([
    # GT Bowling (CSK Batting)
    {'Innings Number': 1, 'Innings Name': 'Chennai Super Kings', 'Bowler': 'Mohammed Siraj', 'Overs': '4.0', 'Maidens': 0, 'Runs': 47, 'Wickets': 0, 'Economy': 11.75, '0s': 9},
    {'Innings Number': 1, 'Innings Name': 'Chennai Super Kings', 'Bowler': 'Arshad Khan', 'Overs': '2.0', 'Maidens': 0, 'Runs': 42, 'Wickets': 0, 'Economy': 21.00, '0s': 1},
    {'Innings Number': 1, 'Innings Name': 'Chennai Super Kings', 'Bowler': 'Prasidh Krishna', 'Overs': '4.0', 'Maidens': 0, 'Runs': 22, 'Wickets': 2, 'Economy': 5.50, '0s': 15},
    {'Innings Number': 1, 'Innings Name': 'Chennai Super Kings', 'Bowler': 'Gerald Coetzee', 'Overs': '3.0', 'Maidens': 0, 'Runs': 34, 'Wickets': 0, 'Economy': 11.33, '0s': 5},
    {'Innings Number': 1, 'Innings Name': 'Chennai Super Kings', 'Bowler': 'Sai Kishore', 'Overs': '2.0', 'Maidens': 0, 'Runs': 23, 'Wickets': 1, 'Economy': 11.50, '0s': 3},
    {'Innings Number': 1, 'Innings Name': 'Chennai Super Kings', 'Bowler': 'Rashid Khan', 'Overs': '4.0', 'Maidens': 0, 'Runs': 42, 'Wickets': 1, 'Economy': 10.50, '0s': 5},
    {'Innings Number': 1, 'Innings Name': 'Chennai Super Kings', 'Bowler': 'M Shahrukh Khan', 'Overs': '1.0', 'Maidens': 0, 'Runs': 13, 'Wickets': 1, 'Economy': 13.00, '0s': 1},
    # CSK Bowling (GT Batting)
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Bowler': 'Ravindra Jadeja', 'Overs': '3.0', 'Maidens': 0, 'Runs': 17, 'Wickets': 2, 'Economy': 5.66, '0s': 5},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Bowler': 'Khaleel Ahmed', 'Overs': '3.0', 'Maidens': 0, 'Runs': 17, 'Wickets': 1, 'Economy': 5.66, '0s': 12},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Bowler': 'Anshul Kamboj', 'Overs': '2.3', 'Maidens': 0, 'Runs': 13, 'Wickets': 3, 'Economy': 5.20, '0s': 9},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Bowler': 'Shivam Dube', 'Overs': '2.0', 'Maidens': 0, 'Runs': 33, 'Wickets': 0, 'Economy': 16.50, '0s': 1},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Bowler': 'Noor Ahmad', 'Overs': '4.0', 'Maidens': 0, 'Runs': 21, 'Wickets': 3, 'Economy': 5.25, '0s': 12},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Bowler': 'Matheesha Pathirana', 'Overs': '3.0', 'Maidens': 0, 'Runs': 29, 'Wickets': 1, 'Economy': 9.66, '0s': 9},
    {'Innings Number': 2, 'Innings Name': 'Gujarat Titans', 'Bowler': 'Deepak Hooda', 'Overs': '1.0', 'Maidens': 0, 'Runs': 15, 'Wickets': 0, 'Economy': 15.00, '0s': 1},
])

gtvscsk_score = Score.from_data(
    json_filename="1473505.json",
    url="GT vs CSK",
    full_player_list=full_player_list,
    player_list=player_list,
    innings_list=innings_list,
    winner=winner,
    man_of_the_match=man_of_the_match,
    catchers=catchers,
    stumpers=stumpers,
    main_runouters=main_runouters,
    secondary_runouters=secondary_runouters,
    bowled=bowled,
    lbw=lbw,
    batsmen_list=batsmen_list,
    bowlers_info=bowlers_info
)

#gtvscsk_score.printing_scorecard()

# --- Data Section ---

full_player_list = [
    # Punjab Kings
    "Priyansh Arya", "Prabhsimran Singh", "Josh Inglis", "Shreyas Iyer", "Nehal Wadhera",
    "Shashank Singh", "Marcus Stoinis", "Azmatullah Omarzai", "Marco Jansen", "Harpreet Brar",
    "Arshdeep Singh",
    # Delhi Capitals
    "KL Rahul", "Faf du Plessis", "Karun Nair", "Sediqullah Atal", "Sameer Rizvi",
    "Tristan Stubbs", "Ashutosh Sharma", "Vipraj Nigam", "Kuldeep Yadav", "Mohit Sharma",
    "Mustafizur Rahman", "Mukesh Kumar", "Praveen Dubey"
]

player_list = {
    "Punjab Kings": [
        "Priyansh Arya", "Prabhsimran Singh", "Josh Inglis", "Shreyas Iyer", "Nehal Wadhera",
        "Shashank Singh", "Marcus Stoinis", "Azmatullah Omarzai", "Marco Jansen", "Harpreet Brar",
        "Arshdeep Singh"
    ],
    "Delhi Capitals": [
        "KL Rahul", "Faf du Plessis", "Karun Nair", "Sediqullah Atal", "Sameer Rizvi",
        "Tristan Stubbs", "Ashutosh Sharma", "Vipraj Nigam", "Kuldeep Yadav", "Mohit Sharma",
        "Mustafizur Rahman", "Mukesh Kumar", "Praveen Dubey"
    ]
}

innings_list = ["Punjab Kings", "Delhi Capitals"]
winner = "Delhi Capitals"
man_of_the_match = "Sameer Rizvi"

catchers = [
    "Tristan Stubbs",              # Priyansh Arya (†Stubbs b Mustafizur)
    "Mohit Sharma",           # Shreyas Iyer (c MM Sharma b Kuldeep)
    "Faf du Plessis",          # Nehal Wadhera (c du Plessis b Mukesh)
    "Tristan Stubbs",              # Shashank Singh (c †Stubbs b Mustafizur)
    "Sameer Rizvi",        # Azmatullah Omarzai (c Sameer Rizvi b Kuldeep)
    "Tristan Stubbs",              # Marco Jansen (c †Stubbs b Mustafizur)
    "Shashank Singh",      # KL Rahul (c Shashank Singh b Jansen)
    "Priyansh Arya",                # Faf du Plessis (c Arya b Harpreet)
    "Arshdeep Singh",      # Sediqullah Atal (c Arshdeep Singh b Dubey)
]

stumpers = ["Tristan Stubbs"]  # Josh Inglis (st †Stubbs b Nigam)
main_runouters = []
secondary_runouters = []
bowled = ["Vipraj Nigam", "Harpreet Brar"]  # Prabhsimran, KL Rahul, Karun Nair, Azmatullah, Sediqullah
lbw = []

batsmen_list = pd.DataFrame([
    # Punjab Kings
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Priyansh Arya', 'Dismissal': 'c †Stubbs b Mustafizur Rahman', 'Runs': 6, 'Balls': 9, '4s': 1, '6s': 0, 'Strike Rate': 66.66},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Prabhsimran Singh', 'Dismissal': 'b Nigam', 'Runs': 28, 'Balls': 18, '4s': 4, '6s': 1, 'Strike Rate': 155.55},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Josh Inglis', 'Dismissal': 'st †Stubbs b Nigam', 'Runs': 32, 'Balls': 12, '4s': 3, '6s': 2, 'Strike Rate': 266.66},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Shreyas Iyer', 'Dismissal': 'c MM Sharma b Kuldeep Yadav', 'Runs': 53, 'Balls': 34, '4s': 5, '6s': 2, 'Strike Rate': 155.88},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Nehal Wadhera', 'Dismissal': 'c du Plessis b Mukesh Kumar', 'Runs': 16, 'Balls': 16, '4s': 1, '6s': 0, 'Strike Rate': 100.00},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Shashank Singh', 'Dismissal': 'c †Stubbs b Mustafizur Rahman', 'Runs': 11, 'Balls': 10, '4s': 0, '6s': 0, 'Strike Rate': 110.00},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Marcus Stoinis', 'Dismissal': 'not out', 'Runs': 44, 'Balls': 16, '4s': 3, '6s': 4, 'Strike Rate': 275.00},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Azmatullah Omarzai', 'Dismissal': 'c Sameer Rizvi b Kuldeep Yadav', 'Runs': 1, 'Balls': 3, '4s': 0, '6s': 0, 'Strike Rate': 33.33},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Marco Jansen', 'Dismissal': 'c †Stubbs b Mustafizur Rahman', 'Runs': 0, 'Balls': 2, '4s': 0, '6s': 0, 'Strike Rate': 0.00},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Batsman': 'Harpreet Brar', 'Dismissal': 'not out', 'Runs': 7, 'Balls': 2, '4s': 0, '6s': 1, 'Strike Rate': 350.00},
    # Delhi Capitals
    {'Innings Number': 2, 'Innings Name': 'Delhi Capitals', 'Batsman': 'KL Rahul', 'Dismissal': 'c Shashank Singh b Jansen', 'Runs': 35, 'Balls': 21, '4s': 6, '6s': 1, 'Strike Rate': 166.66},
    {'Innings Number': 2, 'Innings Name': 'Delhi Capitals', 'Batsman': 'Faf du Plessis', 'Dismissal': 'c Arya b Harpreet Brar', 'Runs': 23, 'Balls': 15, '4s': 2, '6s': 1, 'Strike Rate': 153.33},
    {'Innings Number': 2, 'Innings Name': 'Delhi Capitals', 'Batsman': 'Karun Nair', 'Dismissal': 'b Harpreet Brar', 'Runs': 44, 'Balls': 27, '4s': 5, '6s': 2, 'Strike Rate': 162.96},
    {'Innings Number': 2, 'Innings Name': 'Delhi Capitals', 'Batsman': 'Sediqullah Atal', 'Dismissal': 'c Arshdeep Singh b Dubey', 'Runs': 22, 'Balls': 16, '4s': 0, '6s': 2, 'Strike Rate': 137.50},
    {'Innings Number': 2, 'Innings Name': 'Delhi Capitals', 'Batsman': 'Sameer Rizvi', 'Dismissal': 'not out', 'Runs': 58, 'Balls': 25, '4s': 3, '6s': 5, 'Strike Rate': 232.00},
    {'Innings Number': 2, 'Innings Name': 'Delhi Capitals', 'Batsman': 'Tristan Stubbs', 'Dismissal': 'not out', 'Runs': 18, 'Balls': 14, '4s': 2, '6s': 0, 'Strike Rate': 128.57},
])

bowlers_info = pd.DataFrame([
    # DC Bowling (PBKS Batting)
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Bowler': 'Mukesh Kumar', 'Overs': '4.0', 'Maidens': 0, 'Runs': 49, 'Wickets': 1, 'Economy': 12.25, '0s': 9},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Bowler': 'Mustafizur Rahman', 'Overs': '4.0', 'Maidens': 0, 'Runs': 33, 'Wickets': 3, 'Economy': 8.25, '0s': 8},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Bowler': 'Mohit Sharma', 'Overs': '4.0', 'Maidens': 0, 'Runs': 47, 'Wickets': 0, 'Economy': 11.75, '0s': 5},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Bowler': 'Vipraj Nigam', 'Overs': '4.0', 'Maidens': 0, 'Runs': 38, 'Wickets': 2, 'Economy': 9.50, '0s': 5},
    {'Innings Number': 1, 'Innings Name': 'Punjab Kings', 'Bowler': 'Kuldeep Yadav', 'Overs': '4.0', 'Maidens': 0, 'Runs': 39, 'Wickets': 2, 'Economy': 9.75, '0s': 7},
    # PBKS Bowling (DC Batting)
    {'Innings Number': 2, 'Innings Name': 'Delhi Capitals', 'Bowler': 'Arshdeep Singh', 'Overs': '4.0', 'Maidens': 0, 'Runs': 35, 'Wickets': 0, 'Economy': 8.75, '0s': 6},
    {'Innings Number': 2, 'Innings Name': 'Delhi Capitals', 'Bowler': 'Azmatullah Omarzai', 'Overs': '4.0', 'Maidens': 0, 'Runs': 46, 'Wickets': 0, 'Economy': 11.50, '0s': 6},
    {'Innings Number': 2, 'Innings Name': 'Delhi Capitals', 'Bowler': 'Harpreet Brar', 'Overs': '4.0', 'Maidens': 0, 'Runs': 41, 'Wickets': 2, 'Economy': 10.25, '0s': 5},
    {'Innings Number': 2, 'Innings Name': 'Delhi Capitals', 'Bowler': 'Marco Jansen', 'Overs': '4.0', 'Maidens': 0, 'Runs': 41, 'Wickets': 1, 'Economy': 10.25, '0s': 8},
    {'Innings Number': 2, 'Innings Name': 'Delhi Capitals', 'Bowler': 'Praveen Dubey', 'Overs': '2.0', 'Maidens': 0, 'Runs': 20, 'Wickets': 1, 'Economy': 10.00, '0s': 4},
    {'Innings Number': 2, 'Innings Name': 'Delhi Capitals', 'Bowler': 'Marcus Stoinis', 'Overs': '1.3', 'Maidens': 0, 'Runs': 21, 'Wickets': 0, 'Economy': 14.00, '0s': 1},
])

pbksvsdc_score = Score.from_data(
    json_filename="1473504.json",
    url="PBKS vs DC",
    full_player_list=full_player_list,
    player_list=player_list,
    innings_list=innings_list,
    winner=winner,
    man_of_the_match=man_of_the_match,
    catchers=catchers,
    stumpers=stumpers,
    main_runouters=main_runouters,
    secondary_runouters=secondary_runouters,
    bowled=bowled,
    lbw=lbw,
    batsmen_list=batsmen_list,
    bowlers_info=bowlers_info
)

pbksvsdc_score.printing_scorecard()