import requests
import sys
from colorama import Fore, Style, init
import urllib3
from requests.exceptions import Timeout, RequestException

# Initialize colorama for colorized output
init(autoreset=True)

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Function to check the status code of each subdomain
def check_subdomains(file_path):
    try:
        with open(file_path, 'r') as file:
            subdomains = file.readlines()
            
        for subdomain in subdomains:
            subdomain = subdomain.strip()  # Removing newline characters
            if subdomain:  # If the line is not empty
                try:
                    response = requests.get(f"http://{subdomain}", timeout=10, verify=False)
                    status_code = response.status_code

                    if status_code == 200:
                        print(f"{Fore.GREEN}[{status_code}] - {subdomain}")
                    elif status_code == 403:
                        print(f"{Fore.RED}[{status_code}] - {subdomain}")
                    elif status_code == 404:
                        print(f"{Fore.WHITE}[{status_code}] - {subdomain}")
                    else:
                        print(f"{Fore.WHITE}[{status_code}] - {subdomain}")
                
                except Timeout:
                    print(f"{Fore.WHITE}[TIMEOUT] - {subdomain}")
                except RequestException as e:
                    print(f"{Fore.WHITE}[CONNECTION ERROR] - {subdomain}")
    
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python check_http.py -l <subdomains.txt>")
    elif sys.argv[1] == "-l":
        check_subdomains(sys.argv[2])
