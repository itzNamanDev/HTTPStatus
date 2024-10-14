import requests
import sys
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def check_subdomains(subdomain_file):
    with open(subdomain_file, 'r') as f:
        subdomains = f.read().splitlines()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    for subdomain in subdomains:
        try:
            response = requests.get(f"https://{subdomain}", timeout=10, headers=headers, verify=False)
            if response.status_code == 200:
                print(Fore.GREEN + "[200] - " + subdomain)
            elif response.status_code == 403:
                print(Fore.RED + "[403] - " + subdomain)
            elif response.status_code == 404:
                print(Fore.WHITE + "[404] - " + subdomain)
            else:
                print(Fore.WHITE + f"[{response.status_code}] - {subdomain}")
        except requests.exceptions.Timeout:
            print(Fore.WHITE + "[TIMEOUT] - " + subdomain)
        except requests.exceptions.ConnectionError:
            print(Fore.WHITE + "[CONNECTION ERROR] - " + subdomain)
        except Exception as e:
            print(Fore.WHITE + f"[ERROR] - {subdomain}: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != '-l':
        print("Usage: python3 check_http.py -l <subdomains_file>")
        sys.exit(1)
    check_subdomains(sys.argv[2])
