import os
import pandas as pd
from bs4 import BeautifulSoup

def parse_html_to_messages(html_file):
    """
    Parse a single HTML file and extract messages.
    Args:
        html_file (str): Path to the HTML file.
    Returns:
        list of dict: A list of dictionaries containing parsed messages.
    """
    data = []
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    # Find all messages in the HTML
    messages = soup.find_all('div', class_='message')  # Adjust class name if needed
    
    for message in messages:
        # Extract fields (modify as per actual HTML structure)
        sender = message.find('div', class_='from_name').text if message.find('div', class_='from_name') else None
        timestamp = message.find('div', class_='date').get('title') if message.find('div', class_='date') else None
        text = message.find('div', class_='text').text if message.find('div', class_='text') else None
        
        data.append({'Sender': sender, 'Timestamp': timestamp, 'Message': text})
    return data

def extract_messages_from_html_files(html_files, output_csv):
    """
    Extract messages from multiple HTML files and save them to a CSV file.
    Args:
        html_files (list of str): List of paths to the HTML files.
        output_csv (str): Path to the output CSV file.
    """
    all_data = []
    for html_file in html_files:
        all_data.extend(parse_html_to_messages(html_file))
    
    # Save to CSV
    df = pd.DataFrame(all_data)
    df.to_csv(output_csv, index=False, encoding='utf-8')
    print(f"Messages successfully saved to {output_csv}")

def load_csv_to_dataframe(csv_file):
    """
    Load the saved CSV file into a pandas DataFrame.
    Args:
        csv_file (str): Path to the CSV file.
    Returns:
        pd.DataFrame: A pandas DataFrame containing the CSV data.
    """
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"CSV file not found: {csv_file}")
    return pd.read_csv(csv_file)
