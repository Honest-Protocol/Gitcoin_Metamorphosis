## Analysis of suspicious domains

This is a project to build a dataset around ScamSniffer's [list of domains](https://github.com/scamsniffer/scam-database/blob/main/blacklist/domains.json) (or any website in general) in order to shed more light into scam operations.

This dataset could eventually help to:
- Categorize the scams: NFTs, ICO, Exchange, Donation campaign, airdrop, seed phrase theft...
- Find links between scam operations: using the same IP addresses
- Automatically extract further information about the scam: wallet addresses, email addresses, social media accounts...
- Assist in reporting the scam: geo-locate and identify the jurisdiction it falls under, identify third-parties to report to (hosting providers, domain names registrar...)

## Data collected

The data that seems relevant to me, in a rough order of importance:
- [x] Most common words in the website
- [x] Text contents of the website
- [x] IP addresses of the domain
- [] JavaSript tags and external scripts
- [] Subdomains and paths of the website

## How to run locally

This explains how to setup the repository and run the data extraction yourself.
The outputs will all be saved in the `output` directory.
You will find in it the `domains.csv` file that includes the following information:
- Is the website up?
- IP addresses associated with the website
- Does the website have a `robots.txt` file? (Could be used later to identify paths, or identify suspicious behaviour for blocking SEO indexing)
- Processed text contents of the website: text with punctuation and English [stopwords](https://en.wikipedia.org/wiki/Stop_word) removed

The HTML itself of the websites will also be dumped into the `output/htmls` directory. It can be used for manual inspection, archiving the suspicious website, or avoiding an HTTP request in the code.


```bash
# Download list of suspicious domains
wget https://raw.githubusercontent.com/scamsniffer/scam-database/main/blacklist/domains.json

## Install Python dependencies
pip install -r requirements.txt
## Run the script
python main.py
```

## Further improvements

- [ ] Save into a JSON instead of a CSV (more suitable for array of IPs, most common words...)
- [ ] [Lemmatise](https://en.wikipedia.org/wiki/Lemmatisation) text contents
- [ ] Scrape websites that require JavaScript to be enabled
- [ ] Download JS files referenced in website and scan them for further information (API calls, wallet addresses...)
- [ ] Check if the reputation of the IP addresses 
- [ ] Retrieve history of the domain from the [WayBack Archive](https://archive.org/web/)
- [ ] List technologies the website is built with using [Wappalyzer](https://github.com/wappalyzer/wappalyzer)