import os
import json
import requests
from bs4 import BeautifulSoup

def extract_and_analyze_matches(url):
    team_name = extract_team_name(url)
    # Make a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all <tr> elements with the specified attribute
        matches = soup.find_all('tr', attrs={"data-highlight-row": True})
        
        # Analyze each match
        for match_number, match in enumerate(matches, start=1):
            # Extract the HTML data for the match
            html_data = str(match)
            
            # Analyze the match using the HTML analysis function
            analyze_html_match(html_data, team_name, match_number)
            
            print(f"Match {match_number} analyzed successfully.")
        
        print("All matches analyzed successfully.")
    else:
        # Print an error message if the request was not successful
        print(f"Failed to fetch URL: {url}")

def extract_team_name(url):
    # Split the URL by '/' and get the third element
    parts = url.split('/')
    team_name = parts[4]
    return team_name

def get_next_match_number(team_name, match_prefix):
    directory = os.path.join(os.getcwd(), team_name)
    if not os.path.exists(directory):
        os.makedirs(directory)  # Create the directory if it doesn't exist
    match_files = [file for file in os.listdir(directory) if file.startswith(match_prefix)]
    return len(match_files) + 1

def analyze_html_match(html_data, team_name, match_number):
    soup = BeautifulSoup(html_data, 'html.parser')

    # Extract date
    match_date = soup.find_all('td', class_= 'mhgame-result')[0].text

    # Extract patch_version
    a_tag = soup.find_all('td')[2].find('a')
    patch_version = a_tag.get('title')

    # Extract patch_version
    a_tag = soup.find_all('td', class_= 'mhgame-result')[1].find('a')
    tournament = a_tag.get('title')

    # Extract WIN/LOSE
    win_lose = soup.find_all('td', class_= 'mhgame-result')[3].text

    # Extract match_side
    match_side = soup.find_all('td')[4].text

    # Extract enemy_team
    a_tag = soup.find_all('td')[5].find('a')
    enemy_team = a_tag.get('data-to-id')

    # Extract players_name
    td_element = soup.find_all('td')[10]
    if td_element:
        # Find all <a> tags within the <td> element
        a_tags = td_element.find_all('a')

        # Extract the text content of each <a> tag
        player_names = [a_tag.text for a_tag in a_tags]
    else:
        print("No <td> element found.")
        player_names = []

    # Extract bans for ally team
    ally_bans_td = soup.find_all('td', class_='mhgame-bans')[0]
    ally_bans_champion_spans = ally_bans_td.find_all('span', class_='sprite champion-sprite')
    ally_bans_champion_names = [span['title'] for span in ally_bans_champion_spans]

    # Extract picks for ally team
    ally_picks_td = soup.find_all('td')[8] 
    ally_picks_champion_spans = ally_picks_td.find_all('span', class_='sprite champion-sprite')
    ally_picks_champion_names = [span['title'] for span in ally_picks_champion_spans]

    # Extract bans for enemy team
    enemy_bans_td = soup.find_all('td', class_='mhgame-bans')[1]
    enemy_bans_champion_spans = enemy_bans_td.find_all('span', class_='sprite champion-sprite')
    enemy_bans_champion_names = [span['title'] for span in enemy_bans_champion_spans]

    # Extract picks for enemy team
    enemy_picks_td = soup.find_all('td')[9]
    enemy_picks_champion_spans = enemy_picks_td.find_all('span', class_='sprite champion-sprite')
    enemy_picks_champion_names = [span['title'] for span in enemy_picks_champion_spans]

    # Construct dictionary with extracted data
    match_prefix = f"{match_date.replace('-', '_')}_{tournament.replace(' ', '_')}_{team_name}vs{enemy_team}"
    match_number = get_next_match_number(team_name, match_prefix)

    data = {
        "Team": team_name,
        "Match_number": match_number,
        "Match_date": match_date,
        "Patch_version": patch_version,
        "Tournament" : tournament,
        "Result": win_lose,
        "Side": match_side,
        "Enemy_team": enemy_team,
        "Ally_team_bans": ally_bans_champion_names,
        "Ally_team_picks": ally_picks_champion_names,
        "Enemy_team_bans": enemy_bans_champion_names,
        "Enemy_team_picks": enemy_picks_champion_names,
        "Players": player_names
    }

    # Convert dictionary to JSON string
    json_data = json.dumps(data, indent=4)

    file_name = f"{match_prefix}_match{match_number}.json"
    file_path = os.path.join(team_name, file_name)
    if not os.path.exists(file_path):
        with open(file_path, 'w') as json_file:
            json_file.write(json_data)
    else:
        print(f"File {file_name} already exists. Skipping analysis for match {match_number}.")

    return json_data
