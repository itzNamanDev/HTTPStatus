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
                    # Adding timeout and disabling SSL verification
                    response = requests.get(f"http://{subdomain}", timeout=5, verify=False)
                    print(f"[{response.status_code}] - {subdomain}")
                except requests.exceptions.SSLError as ssl_err:
                    print(f"[SSL ERROR] - {subdomain} ({ssl_err})")
                except requests.exceptions.Timeout as timeout_err:
                    print(f"[TIMEOUT] - {subdomain} ({timeout_err})")
                except requests.exceptions.RequestException as e:
                    print(f"[ERROR] - {subdomain} ({e})")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python check_http.py -l <subdomains.txt>")
    elif sys.argv[1] == "-l":
        check_subdomains(sys.argv[2])
