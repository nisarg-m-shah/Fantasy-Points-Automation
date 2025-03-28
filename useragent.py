from fake_useragent import UserAgent
from selenium import webdriver

ua = UserAgent()
valid_user_agents = []

# Test multiple user agents
for i in range(10):  # Test 10 different user agents
    user_agent = ua.random
    print(f"Testing User Agent {i+1}: {user_agent}")

    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--headless")  # Run without opening a window

    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://www.cricbuzz.com")  # Test with your website

        # Check if the page loaded successfully
        if "Cricbuzz" in driver.title:
            print(f"✅ Working User Agent: {user_agent}")
            valid_user_agents.append(user_agent)

    except Exception as e:
        print(f"❌ Failed: {e}")

    finally:
        driver.quit()

# Save working user agents to a file
with open("valid_user_agents.txt", "w") as f:
    for agent in valid_user_agents:
        f.write(agent + "\n")

print("\nSaved valid user agents to valid_user_agents.txt!")
