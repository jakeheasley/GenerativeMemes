# Karen.

An interactive Twitter Bot.

### Python Library Dependencies:
tweepy - python wrapper for Twitter API  
markovify - probability-based text generation algorithm  
mySQL - database of text snippets scraped from elsewhere on twitter  

### Installing
* install dependencies
    * `pip3 install mysql-connector`. Normal `pip` installs an older version not compatible with Python3.
* register for a [Twitter Developer account](https://developer.twitter.com/) - this is necessary to obtain login credentials for the bot and access the Twitter API for scraping and publishing.
* create a MySQL server on locally or on a web service
* make sure to have the python MySQL connector installed on the database so you can connect to it 
* we run on an [Amazon AWS EC2 server.](https://aws.amazon.com/ec2/) You can run locally or from the server of your choice. Clone the repo to your destination.

### Deployment
* populate Login_Settings.py with credentials for your twitter account and SQL server
* run configuration.py. This sets up a SQL database for all tweets that the bot scrapes and populates it with the pre-selected material that gives Karen her personality.
    * configuration also calls Scheduler_Initializer.py. Run only this when you install the bot on a new machine but with a pre-existing database
* you're running!
