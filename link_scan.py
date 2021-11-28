from selenium import webdriver

browser = webdriver.Chrome('/Users/boom/Desktop/link-scanner/chromedriver')
browser.get('https://google.com')


def get_links(url):
    """Find all links on page at the given url.

    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    browser = webdriver.Chrome('/Users/boom/Desktop/link-scanner/chromedriver')  # Change to your own path in bracket.
    browser.get(url)
    finder = browser.find_elements("//a[@href]")


def is_valid_url(url: str):
    pass


def invalid_urls(urllist: List):
    pass


if __name__ == "__main__":
    pass
