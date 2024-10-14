import requests
import sys

# Function to check the status code of each subdomain
def check_subdomains(file_path):
    try:
        with open(file_path, 'r') as file:
            subdomains = file.readlines()
            
        for subdomain in subdomains:
            subdomain = subdomain.strip()  # Removing newline characters
            if subdomain:  # If the line is not empty
                try:
                    response = requests.get(f"http://{subdomain}")
                    print(f"[{response.status_code}] - {subdomain}")
                except requests.exceptions.RequestException as e:
                    print(f"[ERROR] - {subdomain} ({e})")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python http.py -l <subdomains.txt>")
    elif sys.argv[1] == "-l":
        check_subdomains(sys.argv[2])
