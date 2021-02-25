Mission to Mars

In this challenge, I scrape data from four different websites that have information about the planet Mars.

To start with, I scrape data from the website https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest and obtain the latest news and descriptions.

Then I got to the website https://www.jpl.nasa.gov/images/?search=&category=Mars to obtain the first image that appears.

Next, I go to the page https://space-facts.com/mars/ and pull out a table, convert the table to a Pandas table, then convert the Pandas table to HTML.

Lastly, I pull the images of four hemispheres of Mars on the website https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars 

Once I have all the information scraped, I set up a Flask app that will display all of the information from MongoDB. I edit the web page using HTML code along with Bootstrap.

The most useful tool I used here was the Splinter app that allowed me to do all of the scraping I needed to complete this assignment.

![](screenshots/screensjot_1.png)
