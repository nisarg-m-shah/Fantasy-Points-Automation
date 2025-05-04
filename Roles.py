from fuzzywuzzy import process
from Scraping import find_full_name
from selenium import webdriver
# import undetected_chromedriver as uc
from selenium_stealth import stealth
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import requests
import time
import undetected_chromedriver as uc
import random

# ua = UserAgent()
# random_user_agent = ua.random
# valid_user_agent = ua.chrome

# options = uc.ChromeOptions()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument(f'user-agent={random_user_agent}')
# driver = uc.Chrome(options=options)

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
}

begin = time.time()

# options = webdriver.ChromeOptions()
# options.add_argument(f"user-agent={valid_user_agent}")
# options.add_argument("--headless")
# driver = webdriver.Chrome(options=options)

# options = uc.ChromeOptions()
# options.add_argument(f"user-agent={valid_user_agent}")
# options.add_argument("--headless")
# driver = uc.Chrome(options=options)

# stealth(driver,
#     languages=["en-US", "en"],
#     vendor="Google Inc.",
#     platform="Win32",
#     webgl_vendor="Intel Inc.",
#     renderer="Intel Iris OpenGL Engine",
#     fix_hairline=True,
# )

# Open the webpage
# url = "https://www.espncricinfo.com/auction/ipl-2025-auction-1460972/all-players"
# driver.get(url)
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# # Wait for initial elements to load
# time.sleep(1)

# last_height = driver.execute_script("return document.body.scrollHeight")  # Get initial height

# while True:
#     # Scroll to the bottom
#     print("Scrolling")
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
#     # Wait for new content to load
#     time.sleep(1)
    
#     # Get new scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
    
#     # If no new content is loaded, break
#     if new_height == last_height:
#         print("No more new content. Stopping scroll.")
#         break

#     last_height = new_height  # Update the last height

# print("Reached the bottom of the page.")
# #print(driver.page_source)

# soup = BeautifulSoup(driver.page_source, "html.parser")
# with open("player_list.txt", "w", encoding="utf-8") as file:
#     file.write(soup.prettify())
# print("Saved to player_list.txt")

player_list = []
position_list = []
team_list = []

# Read the file
with open("player_list.txt", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse it with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")
#tables = soup.find_all('table')
#print(tables)
#print(soup.prettify())
table = soup.find('table').find('tbody')#,class_='ds-w-full ds-table ds-table-sm ds-table-auto ds-overflow-scroll ds-scrollbar-hide').find('tbody')

players = table.find_all('tr')
for player in players:
    player_link_part = player.find('td').find('a',class_='ds-inline-flex ds-items-start ds-leading-none')
    player_link = "https://www.espncricinfo.com" + player_link_part['href']
    name = player_link_part['title']
    print(name)

    print(player_link)
#try:
    rand_num = random.randint(2,5)
    print("Sleeping for",rand_num,"seconds")
    for i in range(1,rand_num+1):
        print(i)
        time.sleep(i)
    session = requests.Session()
    response = session.get(player_link, headers=headers)
    if "Access Denied" in response.text:
        print("Access Denied — try using proxies or rotating headers.")
        break
    else:
        soup = BeautifulSoup(response.text, "html.parser")
    # driver.get(player_link)
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    # time.sleep(1)
    #soup_player = BeautifulSoup(driver.page_source, "html.parser")
    #print(soup_player.prettify())
    # headers = {"User-Agent": valid_user_agent}
    # proxies = {"http": "http://user:pass@proxy_ip:port", "https": "https://user:pass@proxy_ip:port"}
    # response = requests.get(player_link, headers=headers, proxies=proxies)
    soup_player = BeautifulSoup(response.text, "html.parser")
    try:
        player_info = soup_player.find('div',class_='ds-grid lg:ds-grid-cols-3 ds-grid-cols-2 ds-gap-4 ds-mb-8')
        player_parts = player_info.find_all('div')
    except:
        print(soup_player.prettify())
    # with open("page_pretty.txt", "w", encoding="utf-8") as file:
    #     file.write(soup_player.prettify())
    # print("Saved to page_pretty.txt")
    for part in player_parts:
        try:
            header = part.find('p').text.strip()
            info = part.find('span').text.strip()
        except:
            continue
        if "Full Name" in header:
            print(info)
        elif "Playing Role" in header:
            position = info
            print(position)
    player_list.append(name)
    position_list.append(position)
    team_list.append("")
    # except:
    #     print("Failed to process:",player_link)
    #     break


    # name = player_name['title'].strip()
    # parts = player.find_all('td',class_="ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-text-right")
    # team = parts[0]
    # print(team)
    # team = team.text.strip()
    # position = parts[1]
    # print(position)
    # position = position.text.strip()
    # player_list.append(name)
    # position_list.append(position)
    # team_list.append(team)

#Close the browser
#driver.quit()
end = time.time()
print(end-begin)
print(player_list)
print(position_list)

players = ['Ayush Mhatre','Dasun Shanaka','Shardul Thakur','Travis Head','Varun Chakaravarthy','Rahul Chahar','Mukesh Choudhary','Harshit Rana','Ishant Sharma','Jaydev Unadkat','Mukesh Kumar','Abdul Samad','Riyan Parag','Khaleel Ahmed','Avesh Khan','Faf du Plessis','Arjun Tendulkar','Mohammed Shami','Shivam Dube','Lockie Ferguson','Josh Hazlewood','Prabhsimran Singh','Rishabh Pant','Corbin Bosch','Mohammed Siraj','Prasidh Krishna','Marcus Stoinis','Harpreet Brar','Rahmanullah Gurbaz','Rashid Khan','Washington Sundar','Hardik Pandya','Heinrich Klaasen','Rinku Singh','Nehal Wadhera','Romario Shepherd','Manav Suthar','Vijaykumar Vyshak','Himmat Singh','Ayush Badoni','Liam Livingstone','Nathan Ellis','Moeen Ali','Karn Sharma','Yashasvi Jaiswal','Shimron Hetmyer','Axar Patel','Mayank Yadav','Abhinav Manohar','Ashutosh Sharma','Rachin Ravindra','Shahrukh Khan','Anrich Nortje','Mayank Markande','Yuzvendra Chahal','Tushar Deshpande','Noor Ahmad','Kagiso Rabada','Marco Jansen',
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
        final_player_list.append((player,position,team))
    else:
        best_match = find_full_name(player_list,player)
        #best_match, score = process.extractOne(player, player_list)
        #best_match3, score, _ = process.extractOne(parts[0], player_list)
        if best_match is not None and best_match in player_list:
            print(player,"- Best Match -",best_match)
            player_number = player_list.index(best_match)
            position = position_list[player_number]
            team = team_list[player_number]
            final_player_list.append((player,position,team))
        else:
            print("Not found",player)

names = []
roles = []
teams = []
for player in final_player_list:
    name, role, team = player
    if "Batter" in role:
        role = "BAT"
    elif "Bowler" in role:
        role = "BOWL"
    elif "rounder" in role:
        role = "AR"
    elif "keeper" in role:
        role = "WK"
    names.append(name)
    roles.append(role)
    teams.append(team)

print(names)
print(roles)
print(teams)
