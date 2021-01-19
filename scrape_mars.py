from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars = {}

    url_news = "https://mars.nasa.gov/news/"
    browser.visit(url_news)
    time.sleep(1)
    html_news = browser.html
    soup_news = bs(html_news, 'html.parser')
    results_news = soup_news.find_all('div', class_='content_title')
    print(results_news[1].text)
    paragraphs_news = soup_news.find_all('div', class_="article_teaser_body")
    print(paragraphs_news[0].text)

    mars = {"news_title": results_news[1].text,
            "news_description": paragraphs_news[0].text}


    url_image = 'https://www.jpl.nasa.gov/images/?search=&category=Mars'
    browser.visit(url_image)
    time.sleep(1)
    html_image = browser.html
    soup_image = bs(html_image, 'html.parser')
    results_image = browser.find_by_css('div[class=SearchResultCard]')
    results_image[0].click()
    mars_image = browser.find_by_id('96342')['src']
    mars_image

    mars["featured_image"] = mars_image

    url_facts = "https://space-facts.com/mars/"
    browser.visit(url_facts)
    time.sleep(1)
    html_facts = browser.html
    soup_facts = bs(html_facts, 'html.parser')
    mars_tables = pd.read_html(url_facts)
    mars_facts_df = mars_tables[0]
    mars_facts_df = mars_facts_df.rename(columns={"0": "", "1": "Mars"})
    mars_facts_html_table = mars_facts_df.to_html()
    mars_facts_html_table
    facts_table = mars_facts_html_table.replace('\n', '')

    mars["facts_table"] = facts_table


    url_hemi = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_hemi)
    time.sleep(1)
    html_hemi = browser.html
    soup_hemi = bs(html_hemi, 'html.parser')
    hemi_image_url = []
    for x in range(4):
       results_hemi = browser.find_by_tag('h3')[x]
       results_name = browser.find_by_tag('h3')[x].text
       results_hemi.click()
       hemi_image = browser.find_by_text('Sample')['href']
       hemi_image_url.append({"name":results_name, "url": hemi_image})
       browser.back()

    mars["hemisphere_images"] = hemi_image_url

    return mars
