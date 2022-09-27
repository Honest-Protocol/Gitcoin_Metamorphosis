import json
import socket
import requests
from bs4 import BeautifulSoup


def check_is_domain_up(domain):
    try:
        response = requests.head("http://" + domain, allow_redirects=True)
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        print(f"Exception for domain: {domain}")
        return False

def main():
    print()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    with open('data.json') as f:
        domains = json.load(f)
        for domain in domains:
            print(domain)
    main()