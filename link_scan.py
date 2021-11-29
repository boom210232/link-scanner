from selenium import webdriver
from urllib.request import urlopen
from urllib import error
from selenium.webdriver.common.by import By
import sys


def get_links(url):
    """Find all links on page at the given url.

    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    if "http" not in url:
        print("Invalid link type! Please use valid http website.")
        exit(0)
    result = []
    compare = []
    browser = webdriver.Chrome('/Users/boom/Desktop/link-scanner/chromedriver')
    # Change to your own path in bracket.
    browser.get(url)
    context = browser.find_elements(By.CSS_SELECTOR, 'a[href^="http"]')
    for i in context:
        # print(i)
        url_name = str(i.get_attribute('href'))
        compare.append(url_name)
        if url_name.__contains__('?') or url_name.__contains__('#'):
            question_split = url_name.split('?')
            hashtag_split = question_split[0].split('#')
            if hashtag_split[0] not in result:
                result.append(hashtag_split[0])
        else:
            if url_name not in result:
                result.append(url_name)
    # print(compare)
    return result


def is_valid_url(url: str):
    try:
        opener = urlopen(url)
        opener.close()

    except (error.URLError, ValueError):
        return False
    except error.HTTPError as e:
        if e.code != 403:  # 403 forbidden = have but can't access
            return False
        if e.code == 200 or e.code == 302:
            return True
    return True


def invalid_urls(urllist: list) -> list:
    """Validate the urls in urllist and return a new list containing
    the invalid or unreachable urls.
    """
    invalid_links = []
    for all_url in urllist:
        if not is_valid_url(all_url):
            invalid_links.append(all_url)
    # print(invalid_links)
    return invalid_links


if __name__ == "__main__":
    # print(is_valid_url("https://www.thaizeed.net/"))
    # print(is_valid_url("https://www.maimeeyoujing.co.th/"))
    # print(invalid_urls(["https://www.thaizeed.net/","https://www.maimeeyoujing.co.th/"]))
    # print(get_links('https://cpske.github.io/ISP'))
    # print(get_links('http://anicheck-isp.herokuapp.com/'))
    # print(invalid_urls(
    #     ["https://www.thaizeed.net/", "https://www.maimeeyoujing.co.th/", "https://refactoring.guru/refactoring"]))

    if len(sys.argv) != 2:
        print("Usage:  python3 link_scan.py [url]\n")
        print("Test all hyperlinks on the given url.")
        exit(0)

    all_link = get_links(sys.argv[1])
    for links in all_link:
        if is_valid_url(links):
            print(links)
    print("\nBad Links:\n")
    for left in invalid_urls(all_link):
        print(left)
