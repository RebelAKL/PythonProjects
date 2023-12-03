import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    else:
        print("Failed to retrieve the webpage.")
        return None


def extract_information(soup):
    # this can be edited as per requirement
    lists = soup.find_all("ul")
    list_contents = [li.get_text() for ul in lists for li in ul.find_all("li")]
    return "\n".join(list_contents)


def main():
    print("Simple Web Scraper")

    webpage_url = input("Enter the URL of the webpage to scrape: ")

    soup = scrape_website(webpage_url)

    if soup:
        information = extract_information(soup)
        print("Extracted Information:")
        print(information)


if __name__ == "__main__":
    main()
