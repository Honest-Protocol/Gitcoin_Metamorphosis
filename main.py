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

def get_domain_text_content(domain):
    response = requests.get("http://" + domain, allow_redirects=True)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return " ".join(soup.text.split())
    else:
        return ""

def get_domain_ip_adresses(domain):
    _, __, ip_addresses = socket.gethostbyname_ex(domain)
    return ip_addresses

def main():
    with open('domains.json') as f:
        domains = json.load(f)
        for domain in domains:
            print(domain)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    with open('data.json') as f:
        domains = json.load(f)
        for domain in domains:
            print(domain)
    main()