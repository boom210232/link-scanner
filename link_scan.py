from selenium import webdriver
from urllib.request import urlopen
from urllib import error
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
import sys


def get_links(url):
    """Find all links on page at the given url.

    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    pass



def is_valid_url(url: str):
    try:
        opener = urlopen(url)
        opener.close()

    except (error.URLError, ValueError):
        return False
    except error.HTTPError as e:
        if e.code != 403:  # 403 forbidden = have but can't access
            return False
    return True


def invalid_urls(urllist):
    """Validate the urls in urllist and return a new list containing
    the invalid or unreachable urls.
    """
    invalid_links = []
    for all_url in urllist:
        if not is_valid_url(all_url):
            invalid_links.append(all_url)
    print(invalid_links)
    return invalid_links


if __name__ == "__main__":
    # print(is_valid_url("https://www.thaizeed.net/"))
    # print(is_valid_url("https://www.maimeeyoujing.co.th/"))
    # invalid_urls(["https://www.thaizeed.net/","https://www.maimeeyoujing.co.th/"])


