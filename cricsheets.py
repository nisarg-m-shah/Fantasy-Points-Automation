import requests
import zipfile
import os
import shutil
from io import BytesIO
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium_stealth import stealth
from fake_useragent import UserAgent

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
