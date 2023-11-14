from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

"""
Dylan Spradling 
11/13/2023

You have to install the beautiful soup package to make this code work
Have no idea how to make it work without it
If you are reading this I would like to meet to discuss things about this course

Also, I dont know how to display bug info in Pycharm as you had us originally to the assignment in jupyter notebook
I am aware they run off the same interpreter but apparently I did not do the assignment 
"""

import Web_Scraping as wb
import DBConnector as dbc


"""
This will be our main screen
"""


def main():
    # Your code goes here.
    main_link = "https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field.importance%3Alist=UNDECIDED&field.importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field.importance%3Alist=MEDIUM&field.importance%3Alist=LOW&field.importance%3Alist=WISHLIST&field.information_type%3Alist=PUBLIC&field.information_type%3Alist=PUBLICSECURITY&field.information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search&orderby=-importance&memo=0&start=0"
    links = generate_links(main_link)
    user_input = int(input('Which page would you like to view?'))
    display_bugs_info(links[user_input])



def generate_links(start_link):
    """
        This method generates ALL the links to all pages and stores them in a list
        :param start_link: The start link of the bug tracking system.
        :return: The list of all pages to all bugs. Each element in the list will refer to one page
    """
    list_of_links = []

    # everytime you get a link to a new page, use list_of_links.append(new_page)
    list_of_links.append(start_link)
    list_of_links = set(list_of_links)
    list_of_links = list(list_of_links)

    list_of_links = [start_link]
    current_page = start_link

    while True:
        # Send a GET request to the current page
        response = requests.get(current_page)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all links in the current page
        links = soup.find_all('a', href=True)

        # Extract and print the link to each page
        for link in links:
            absolute_url = urljoin(start_link, link['href'])
            if absolute_url not in list_of_links:
                list_of_links.append(absolute_url)
                print(absolute_url)

        # Find the link to the next page
        next_page_link = soup.find('link', {'rel': 'next'})
        if next_page_link:
            current_page = urljoin(start_link, next_page_link['href'])
        else:
            break

    return list_of_links



def display_bugs_info(bugs_page):
    """
        This method displays the bugs info. for a specific page
        Display: Bug Number, Title, Importance, and Heat - in this order for each bug.
        :param bugs_page: The  link to the page
    """

    # I Don't know how to do this

if __name__ == "__main__":
    main()
