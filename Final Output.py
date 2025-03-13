import dill
from Scraping import Series,Score
import requests
from bs4 import BeautifulSoup

# Load the object (class definition is included!)
with open("ipl2024matches.pkl", "rb") as file:
    ipl2024 = dill.load(file)

for match_url in ipl2024.keys():
    print(match_url)
#print(len(match_links))
print(len(ipl2024))

# Now, you can directly access the match list
#print(type(ipl2025))  # ✅ Should print <class '__main__.Series'>
#print(ipl2025.match_links)  # ✅ Access the stored list

#print(ipl2025.player_list)

# match = ipl2024[26]
# match.printing_scorecard()
# print((ipl2024))

# match_link = "https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/punjab-kings-vs-rajasthan-royals-27th-match-1426265/full-scorecard"
# cricbuzz_page_link = "https://www.cricbuzz.com/cricket-series/7607/indian-premier-league-2024/matches" 
# match = Score(match_link,cricbuzz_page_link)
# match.printing_scorecard()

# url = "https://www.cricbuzz.com/cricket-match-squads/91416/pbks-vs-rr-27th-match-indian-premier-league-2024"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
# }
# #catches, stumpings, runouts = 0,0,0
# response_squads = requests.get(url, headers=headers)
# soup_squads = BeautifulSoup(response_squads.content, "html.parser")
# team_matchup = soup_squads.find('h1',class_='cb-nav-hdr cb-font-18 line-ht24')
# print(team_matchup.prettify())