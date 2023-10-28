"""
Dylan Spradling
10/27/2023
In Class Activity 8
"""
import Web_Scraping

def main():


    page_tree = Web_Scraping.get_web_tree("https://www.wvu.edu/")

    print("/html/body/header/div/div/text()")
    print("/html/body/header/div/text()")
    print("/html/body/header/div/div/text()")
    print("/html/body/nav/text()")
    print("/html/body/header/div/div/a[4]/text()")