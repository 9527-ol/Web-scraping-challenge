from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd



def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_url(url):
    
    browser = init_browser()
    browser.visit(url)
    time.sleep(3)
    html = browser.html

    soup = bs(html, 'html.parser')
   
    browser.quit()
    return soup




def scrape():

    mars_data = {}

    news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    news_soup = scrape_url(url_news)
    latest_title = news_soup.find('div', class_='content_title').find('a').text
    latest_text = news_soup.find('div', class_='rollover_description_inner').text

    mars_data['latest_title'] = latest_title
    mars_data['latest_text'] = latest_text



    img_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA23852_hires.jpg'
    img_soup = scrape_url(img_url)
    image_url = img_soup.find('div',class_='img').find('img')['src']
    featured_image_url = f'https://www.jpl.nasa.gov{img_url}'

    mars_data['featured_image_url'] = featured_image_url


    weather_url = 'https://twitter.com/marswxreport?lang=en'
    weather_soup = scrape_url(weather_url)
    mars_weather = soup.find('div', class_='js-tweet-text-container').text

    mars_data['mars_weather'] = mars_weather

    table_url = 'https://space-facts.com/mars/'
    table_soup = scrape_url(table_url)
    table_soup = scrape_url(url_table)
    mars_table = str(table_soup.find('tbody'))
    
    mars_data['mars_facts'] = mars_table


    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    hemisphere_soup = scrape_url(hemisphere_url)
    items = hemisphere_soup.find_all('div', class_='item')

    hemisphere_image_urls = []
    main_url = 'https://astrogeology.usgs.gov'

    for item in items:
        
        title = item.find('h3').text
        
        sm_img_url = item.find('a', class_='itemLink product-item')['href']

        browser.visit(main_url + sm_img_url)
        
        img_html = browser.html
        
        soup = BeautifulSoup(img_html, 'html.parser')
        
        image_url = main_url + soup.find('img', class_='wide-image')['src']
        
        hemisphere_image_urls.append({"title" : title, "img_url" : image_url})


    return mars_data











