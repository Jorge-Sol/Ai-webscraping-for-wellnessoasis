import requests
from bs4 import BeautifulSoup
import openai

# Step 1: Scrape the website
url = 'https://www.wsj.com/health?mod=nav_top_section'
headers = {'User-Agent': 'Mozilla/5.0'}  # Adding a user agent to prevent blocking
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract headlines
headlines = [headline.text for headline in soup.find_all('p', class_='e1sf124z11 css-c81msa-HeadlineTextBlock')]
print("Extracted headlines:", headlines)  # Add this line to verify extraction

# Step 2: Process the headlines using ChatGPT
openai.api_key =  'Authorization: Bearer MY_API'
for headline in headlines:
    # Step 3: Determine if the headline is about health
    prompt = f"Is the headline '{headline}' related to health?"
    print("Prompt sent to ChatGPT:", prompt)  # Add this line to verify prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        stop=None,
        temperature=0.7
    )
    print("Response from ChatGPT:", response)  # Add this line to verify response
    # Check if the response indicates the headline is related to health
    if "Yes" in response.choices[0].text:
        # Step 4: Display the filtered headlines on your website
        print("Health-related headline:", headline)
