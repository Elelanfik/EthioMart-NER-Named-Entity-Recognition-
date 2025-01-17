from bs4 import BeautifulSoup
import pandas as pd

def extract_messages_from_html(html_file, output_csv):
    """
    Extracts messages from an HTML file and saves them to a CSV file.

    Args:
        html_file (str): Path to the HTML file.
        output_csv (str): Path to save the output CSV file.
    """
    # Load the HTML file
    with open(html_file, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Initialize data storage
    messages_data = []

    # Extract all message blocks
    messages = soup.find_all("div", class_="message default clearfix")
    for message in messages:
        # Extract details
        date = message.find_previous("div", class_="body details").get_text(strip=True) if message.find_previous("div", class_="body details") else "Unknown"
        time = message.find("div", class_="pull_right date details").get_text(strip=True) if message.find("div", class_="pull_right date details") else "Unknown"
        sender = message.find("div", class_="from_name").get_text(strip=True) if message.find("div", class_="from_name") else "Unknown"
        text = message.find("div", class_="text").get_text(strip=True) if message.find("div", class_="text") else "No text"

        # Parse text for specific fields
        lines = text.split("●")
        product_name = lines[1].strip() if len(lines) > 1 else "Unknown"

        # Safely handle price extraction with a check for ':-' in the line
        price = next((line.split(":-")[1].strip() for line in lines if "ዋጋ" in line and ":-" in line), "Unknown")

        # Safely handle other fields with the same check for ':-'
        size = next((line.split(":-")[1].strip() for line in lines if "size" in line and ":-" in line), "Unknown")
        made_in = next((line.split(":-")[1].strip() for line in lines if "made in" in line and ":-" in line), "Unknown")
        phone = next((line.split(":-")[1].strip() for line in lines if "ስልክ" in line and ":-" in line), "Unknown")
        color = next((line.split(":-")[1].strip() for line in lines if "Colour" in line and ":-" in line), "Unknown")
        contact_link = next((line.split(":-")[1].strip() for line in lines if "ለማናገር" in line and ":-" in line), "Unknown")
        address = next((line.split(":-")[1].strip() for line in lines if "አድራሻ" in line and ":-" in line), "Unknown")

        # Append the extracted data to the list
        messages_data.append({
            "Date": date,
            "Time": time,
            "Sender": sender,
            "Product Name": product_name,
            "Price": price,
            "Size": size,
            "Made In": made_in,
            "Phone Number": phone,
            "Color": color,
            "Contact Link": contact_link,
            "Address": address,
        })

    # Convert the extracted data into a DataFrame
    df = pd.DataFrame(messages_data)

    # Save as a CSV file
    df.to_csv(output_csv, index=False, encoding="utf-8")
    print(f"Messages extracted and saved to {output_csv}")

def load_and_preview_csv(csv_file, num_rows=5):
    """
    Loads a CSV file into a Pandas DataFrame and prints the first few rows.

    Args:
        csv_file (str): Path to the CSV file.
        num_rows (int): Number of rows to preview. Default is 5.

    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    # Load the CSV file
    df = pd.read_csv(csv_file)
    # Print the first few rows
    print(df.head(num_rows))
    return df
