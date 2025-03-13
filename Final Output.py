import dill
#from Scraping import Series,Score

# Load the object (class definition is included!)
with open("ipl2024matches.pkl", "rb") as file:
    ipl2024 = dill.load(file)

# Now, you can directly access the match list
#print(type(ipl2025))  # ✅ Should print <class '__main__.Series'>
#print(ipl2025.match_links)  # ✅ Access the stored list

#print(ipl2025.player_list)

match = ipl2024.match_objects[25]
match.printing_scorecard()