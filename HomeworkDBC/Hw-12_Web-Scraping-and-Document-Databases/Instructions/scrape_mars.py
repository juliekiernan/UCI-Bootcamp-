#import dependencies
import os
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser

def scrape():
    #initiate chrome driver
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    news_title, news_p = news(browser)
    return data

    #store functions as variables in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": feat_img(browser),
        "hemispheres": hemispheres(browser),
        "weather": twitter_weather(browser),
        "last_modified": dt.datetime.now()
    }

def news(browser):
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    news_title= soup.find("div", {"class": "content_title"})
    news_p= soup.find("div", {"class": "rollover_description_inner"})
    return news_title.text
    return news_p.text

def feat_img(browser):
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    feature_image = browser.find_by_id("full_image")
    feature_image.click()
    more_info = browser.find_link_by_partial_text("more info")
    more_info.click()
    html = browser.html
    image_soup = bs(html,  'html.parser')
    image_url_rel = image_soup.select_one('figure.lede a img').get("src")
    feature_image_url = f'https://www.jpl.nasa.gov{image_url_rel}'
    return feature_image_url

def hemispheres(browser):
    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"}
    ]
    return hemisphere_image_urls

def twitter_weather(browser):
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    html = browser.html
    weather_soup = bs(html, "html.parser")
    mars_weather_tweet = mars_weather_soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})
    mars_weather = mars_weather_tweet.find("p", "tweet-text").get_text()
    return mars_weather

if __name__ == "__main__":
    print(scrape())

# exit chrome driver, get scraped data
    browser.quit()
 

