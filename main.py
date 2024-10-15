import time
import requests

def check_website_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Website {url} is up. Status code: {response.status_code}")
        else:
            print(f"Website {url} returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Website {url} is down. Error: {e}")

if __name__ == "__main__":
    url = "https://online-shop-4ld6.onrender.com/" 
    while True:
        check_website_status(url)
        time.sleep(40)
