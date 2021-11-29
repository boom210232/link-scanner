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
    result = []
    compare = []
    browser = webdriver.Chrome('/Users/boom/Desktop/link-scanner/chromedriver')
    # Change to your own path in bracket.
    browser.get(url)
    context = browser.find_elements(By.CSS_SELECTOR, 'a[href^="http"]')
    for i in context:
        # print(i)
        v_url = str(i.get_attribute('href'))
        compare.append(v_url)
        if v_url.__contains__('?') or v_url.__contains__('#'):
            question_split = v_url.split('?')
            hashtag_split = question_split[0].split('#')
            if hashtag_split[0] not in result:
                result.append(hashtag_split[0])
        else:
            if v_url not in result:
                result.append(v_url)
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
    pass
