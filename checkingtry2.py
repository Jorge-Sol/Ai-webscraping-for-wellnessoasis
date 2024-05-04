import requests
from bs4 import BeautifulSoup
import openai

# Step 1: Scrape the website
url = 'https://www.wsj.com/health?mod=nav_top_section'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract headlines
headlines = [headline.text for headline in soup.find_all('h3', class_='WSJTheme--headline--7VCzo7Ay')]
# Additional processing may be needed based on the website's structure

# Step 2: Process the headlines using ChatGPT
openai.organization = 'org-3iExrA2f4S5W5h2XvmVcKz8j'
openai.project = 'proj_wZtFEHxXrZ6W0GIMA9KjSw3p'

for headline in headlines:
    # Step 3: Determine if the headline is about health
    prompt = f"Is the headline '{headline}' related to health?"
    print("Prompt:", prompt)  # Print the prompt sent to ChatGPT
    try:
        response = openai.Completion.create(
            engine="davinci-002",
            prompt=prompt,
            max_tokens=50,
            stop=None,
            temperature=0.7,
            headers={"Authorization": "Bearer MY_APY"}
        )
        print("Response:", response.choices[0].text)  # Print the response received from ChatGPT
        # Check if the response indicates the headline is related to health
        if "Yes" in response.choices[0].text:
            # Step 4: Display the filtered headlines on your website
            print("Health-related headline:", headline)
    except Exception as e:
        print("An error occurred:", e)
