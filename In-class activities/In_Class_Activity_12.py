import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


"""
Dylan Spradling
11/10/2023
In class activity for CYBER493

This assignment was completed with help from ChatGPT as I am not understanding the concepts of Wbe scrapping at this time


"""
def get_all_page_links(base_url):
    # Initialize variables
    page_links = [base_url]
    current_page = base_url

    while True:
        # Send a GET request to the current page
        response = requests.get(current_page)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all links in the current page
        links = soup.find_all('a', href=True)

        # Extract and print the link to each page
        for link in links:
            absolute_url = urljoin(base_url, link['href'])
            if absolute_url not in page_links:
                page_links.append(absolute_url)
                print(absolute_url)

        # Find the link to the next page
        next_page_link = soup.find('link', {'rel': 'next'})
        if next_page_link:
            current_page = urljoin(base_url, next_page_link['href'])
        else:
            break

    return page_links

# Example usage
base_url = "https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field.importance%3Alist=UNDECIDED&field.importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field.importance%3Alist=MEDIUM&field.importance%3Alist=LOW&field.importance%3Alist=WISHLIST&field.information_type%3Alist=PUBLIC&field.information_type%3Alist=PUBLICSECURITY&field.information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search&orderby=-importance&memo=75&start=0"
get_all_page_links(base_url)
