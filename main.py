import json
import socket
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')


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

def get_last_modified_header(domain):
    response = requests.get("http://" + domain, allow_redirects=True)
    if response.status_code == 200:
        return response.headers.get("last-modified")
    else:
        return None

def get_domain_ip_adresses(domain):
    _, __, ip_addresses = socket.gethostbyname_ex(domain)
    return ip_addresses

def remove_punctuation_and_stopwords(text):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    # tokens = word_tokenize(text)
    tokens = [token for token in tokens if token.lower() not in stopwords.words("english")]
    return " ".join(tokens)

def main():
    with open(f"output/domains.csv", "w") as file:
        file.write(f"domain,is_up,ip_addresses,has_robots_file,most_common_words,text_processed\n")

    with open('domains.json') as f:
        domains = json.load(f)
        for domain in domains:
            print(domain)
            is_up = check_is_domain_up(domain)
            if not is_up:
                print(f"{domain}: {is_up}")
                continue
            ip_addresses = get_domain_ip_adresses(domain)
            response = requests.get("http://" + domain, allow_redirects=True)
            text = get_domain_text_content(domain)
            text = remove_punctuation_and_stopwords(text)
            has_robots_file = check_is_domain_up(domain + "/robots.txt")
            words_dist = FreqDist()
            for word in word_tokenize(text):
                words_dist[word.lower()] += 1
            most_common_words = words_dist.most_common(15)

            with open("output/domains.csv", "a") as file:
                file.write(f"{domain},{is_up},{str(ip_addresses)},{has_robots_file},{str(most_common_words)},{text}\n")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    with open('data.json') as f:
        domains = json.load(f)
        for domain in domains:
            print(domain)
    main()