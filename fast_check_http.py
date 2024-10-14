import requests
import sys
import warnings
from colorama import init, Fore, Style
import threading

# Suppress InsecureRequestWarning
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

# Initialize colorama
init(autoreset=True)

def check_subdomain(subdomain):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
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
        print(Fore.BLUE + "[TIMEOUT] - " + subdomain)
    except requests.exceptions.ConnectionError:
        print(Fore.WHITE + "[CONNECTION ERROR] - " + subdomain)
    except Exception as e:
        print(Fore.WHITE + f"[ERROR] - {subdomain}: {str(e)}")

def check_subdomains(subdomain_file):
    with open(subdomain_file, 'r') as f:
        subdomains = f.read().splitlines()

    threads = []
    for subdomain in subdomains:
        thread = threading.Thread(target=check_subdomain, args=(subdomain,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != '-l':
        print("Usage: python3 fast_check_http.py -l <subdomains_file>")
        sys.exit(1)
    check_subdomains(sys.argv[2])
