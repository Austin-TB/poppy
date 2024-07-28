import requests
import os
from bs4 import BeautifulSoup

class Scraper:
    @staticmethod
    def fetch_latest_version():
        url = os.getenv('WEBSITE_URL')
        classname = os.getenv('CLASS_NAME')
        
        if not url or classname:
            return "URL/CLASS_NAME not found in environment variables"

        try:
            response = requests.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            drivers = soup.find_all(class_=classname)
            
            if drivers:
                latest_driver = drivers[0].text.strip()
                return latest_driver
            else:
                return "No driver information found"
        
        except requests.RequestException as e:
            return f"Error fetching data: {str(e)}"
