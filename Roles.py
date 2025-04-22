from fuzzywuzzy import process
from selenium import webdriver
# import undetected_chromedriver as uc
from selenium_stealth import stealth
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time

begin = time.time()

ua = UserAgent()
#random_user_agent = ua.random
valid_user_agent = ua.chrome


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

# Open the webpage
url = "https://www.espncricinfo.com/auction/ipl-2025-auction-1460972/all-players"
driver.get(url)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Wait for initial elements to load
time.sleep(1)

last_height = driver.execute_script("return document.body.scrollHeight")  # Get initial height

while True:
    # Scroll to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Wait for new content to load
    time.sleep(1)
    
    # Get new scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    
    # If no new content is loaded, break
    if new_height == last_height:
        print("No more new content. Stopping scroll.")
        break

    last_height = new_height  # Update the last height

print("Reached the bottom of the page.")
#print(driver.page_source)

player_list = []
position_list = []
team_list = []

soup = BeautifulSoup(driver.page_source, "html.parser")
with open("page_pretty.txt", "w", encoding="utf-8") as file:
    file.write(soup.prettify())
print("Saved to page_pretty.txt")
#tables = soup.find_all('table')
#print(tables)
#print(soup.prettify())
table = soup.find('table').find('tbody')#,class_='ds-w-full ds-table ds-table-sm ds-table-auto ds-overflow-scroll ds-scrollbar-hide').find('tbody')

players = table.find_all('tr')
for player in players:
    player_name = player.find('td').find('a',class_='ds-inline-flex ds-items-start ds-leading-none')
    name = player_name['title'].strip()
    parts = player.find_all('td',class_="ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-text-right")
    team = parts[0]
    print(team)
    team = team.text.strip()
    position = parts[1]
    print(position)
    position = position.text.strip()
    player_list.append(name)
    position_list.append(position)
    team_list.append(team)

#Close the browser
driver.quit()
end = time.time()
print(end-begin)

players = ['Shardul Thakur','Travis Head','Varun Chakaravarthy','Rahul Chahar','Mukesh Choudhary','Harshit Rana','Ishant Sharma','Jaydev Unadkat','Mukesh Kumar','Abdul Samad','Riyan Parag','Khaleel Ahmed','Avesh Khan','Faf du Plessis','Arjun Tendulkar','Mohammed Shami','Shivam Dube','Lockie Ferguson','Josh Hazlewood','Prabhsimran Singh','Rishabh Pant','Corbin Bosch','Mohammed Siraj','Prasidh Krishna','Marcus Stoinis','Harpreet Brar','Rahmanullah Gurbaz','Rashid Khan','Washington Sundar','Hardik Pandya','Heinrich Klaasen','Rinku Singh','Nehal Wadhera','Romario Shepherd','Manav Suthar','Vijaykumar Vyshak','Himmat Singh','Ayush Badoni','Liam Livingstone','Nathan Ellis','Moeen Ali','Karn Sharma','Yashasvi Jaiswal','Shimron Hetmyer','Axar Patel','Mayank Yadav','Abhinav Manohar','Ashutosh Sharma','Rachin Ravindra','Shahrukh Khan','Anrich Nortje','Mayank Markande','Yuzvendra Chahal','Tushar Deshpande','Noor Ahmad','Kagiso Rabada','Marco Jansen',
'Virat Kohli','Abhishek Sharma','Jitesh Sharma','Harnoor Singh','Bhuvneshwar Kumar','Abishek Porel','Angkrish Raghuvanshi','Kuldeep Yadav','David Miller','Anuj Rawat','Josh Inglis','Kumar Kartikeya','Akash Deep','Rahul Tewatia','Ramandeep Singh','Sherfane Rutherford','Glenn Maxwell','Sandeep Sharma','Suryakumar Yadav','Shamar Joseph','Pat Cummins','Quinton de Kock','Ravichandran Ashwin',
'Jasprit Bumrah','Sai Sudharsan','Shreyas Iyer','Swastik Chikara','Rajvardhan Hangargekar','Manoj Bhandage','Nitish Rana','Rasikh Salam Dar','Deepak Chahar','MS Dhoni','Aaron Hardie','Priyansh Arya','Phil Salt','Sameer Rizvi','Mitchell Santner','Manish Pandey','Suyash Sharma','Kamlesh Nagarkoti','Will Jacks','Azmatullah Omarzai','Adam Zampa','Spencer Johnson','Jamie Overton','Shashank Singh','Rovman Powell','Suryansh Shedge','Maheesh Theekshana',
'Ruturaj Gaikwad','Shubman Gill','Mohit Sharma','Sai Kishore','Raj Bawa','Ishan Kishan','Mitchell Marsh','Nitish Kumar Reddy','Karim Janat','Yash Dayal','Bevon Jacobs','Ryan Rickelton','Rajat Patidar','Tristan Stubbs','Gerald Coetzee','Glenn Phillips','Tim David','Ravi Bishnoi','Donovan Ferreira','Jayant Yadav','Trent Boult','Jofra Archer','Akash Madhwal','Darshan Nalkande','Kwena Maphaka',
'KL Rahul','Arshdeep Singh','Aiden Markram','Sachin Baby','Dushmantha Chameera','Naman Dhir','Karun Nair','Wanindu Hasaranga','Arshad Khan','Devdutt Padikkal','Robin Minz','Shahbaz Ahmed','Mohsin Khan','Krunal Pandya','Ravindra Jadeja','Mitchell Starc','Sanju Samson','Jos Buttler','Atharva Taide','Musheer Khan','Devon Conway','Venkatesh Iyer',
'Andre Russell','Sunil Narine','Chetan Sakariya','T Natarajan','Ajinkya Rahane','Shreyas Gopal','Tilak Varma','Vijay Shankar','Shubham Dubey','Anukul Roy','Deepak Hooda','Harshal Patel','Rahul Tripathi','Lungi Ngidi','Matheesha Pathirana','Vaibhav Arora','Nicholas Pooran','Jake Fraser-McGurk','Sam Curran','Rohit Sharma','Mujeeb Ur Rahman','Anshul Kamboj','Mahipal Lomror'
]
final_player_list = []
for player in players:
    if 'Mujeeb' in player:
        final_player_list.append(('Mujeeb ur Rahman','BOWL','MI'))
        continue
    if 'Corbin Bosch' in player:
        final_player_list.append(('Corbin Bosch','AR','MI'))
        continue
    if 'Chetan Sak' in player:
        final_player_list.append(('Chetan Sakariya','BOWL','KKR'))
        continue
    if player in player_list:
        player_number = player_list.index(player)
        position = position_list[player_number]
        team = team_list[player_number]
    else:
        best_match, score = process.extractOne(player, player_list)
        #best_match3, score, _ = process.extractOne(parts[0], player_list)
        if score>70:
            print(player,"Best Match",best_match)
            player = best_match
            player_number = player_list.index(best_match)
            position = position_list[player_number]
            team = team_list[player_number]
        else:
            print("Not found",player)
            position = ""
    final_player_list.append((player,position,team))

names = []
roles = []
teams = []
for player in final_player_list:
    name, role, team = player
    names.append(name)
    roles.append(role)
    teams.append(team)

print(names)
print(roles)
print(teams)
