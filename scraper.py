import requests
from bs4 import BeautifulSoup

class Scraper:
    @staticmethod
    def fetch_latest_version():
        url = "https://www.techpowerup.com"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes
            
            soup = BeautifulSoup(response.text, 'html.parser')
            drivers = soup.find_all(class_="s--drivers__driver s--drivers__driver--nvidia")
            
            if drivers:
                # Assuming the first match is the latest driver
                latest_driver = drivers[0].text.strip()
                return latest_driver
            else:
                return "No driver information found"
        
        except requests.RequestException as e:
            return f"Error fetching data: {str(e)}"
