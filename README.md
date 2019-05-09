# Karen.

An interactive Twitter Bot using python3.

### Python Library Dependencies:
tweepy - python wrapper for Twitter API  
markovify - probability-based text generation algorithm  
mySQL - database of text snippets scraped from elsewhere on twitter  
Other libraries we use:
    re
    datetime
    literal_eval from ast
### Installing
* Install dependencies
    * `pip3 install mysql-connector`. Normal `pip` installs an older version not compatible with Python3.
* Register for a [Twitter Developer account](https://developer.twitter.com/) - this is necessary to obtain login credentials for the bot and access the Twitter API for scraping and publishing. 
* Set up a mySQL server to store tweets. You can run the database locally or with a server
* We run the bot on an [Amazon AWS EC2 server.](https://aws.amazon.com/ec2/). You can run locally or from the server of your choice. Clone the repo to your destination. 

### Deployment
* Create a file called Login_Settings.py in the Login_Settings_General folder (Login_Settings_Template shows how the file should be organized).
* Fill the appropriate strings in the file with Twitter Developer credentials as well as database credentials.
    * NOTE: the "port" section of the file should be an int, not a string.
* Change the "handle" variable in Bot.py to be the username of your bot. For example, ours is @karen_the_bot.
* Run configuration.py. This sets up a SQL database for all tweets that the bot scrapes, and populates it with the pre-selected material that gives Karen her personality.
    * Configuration also calls Scheduler_Initializer.py. 
    * If you are trying to set up the bot with an SQL server that has already been arranged for the bot (like if you're 
    running a preexisting bot on a new machine), run Scheduler_Initializer by itself as it will set up files that Scheduler.py will read.
* Finally, when you want to start your bot, run Scheduler and the bot will run indefinitely. It is recommended to set up some other
  scripts to check if your bot has stopped running and jumpstart the bot again. The scripts we use are in the "Helper Scripts"
  file and can be used as a reference, but may not work on your device.
  
### Issues you might run into while creating and customizing your bot:
* You can customize how often your bot runs, or how many tweets it scrapes, but Twitter does limit how often you can do this
  if you don't have a paying developer account. To ensure that you don't go over the limit, check the Twitter API. There
  is also a function in Bot.py called rate_status that will let you know how many uses you have left for every single Twitter 
  API function.