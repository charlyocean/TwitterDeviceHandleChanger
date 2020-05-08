# TwitterDeviceHandleChanger
Made with Tweepy, This is how you run it:
# Setup
First off, make sure you have a verified email address linked to your Twitter account.
Right, you need to install Python and Tweepy. Once you have those, go to Twitter's Developer Page and Click "Create an app" then Apply for an account by:

Check "Making a Bot", Next
Fill out the info for country and name, Next
Describe your use of the API. I put "I want to use the Twitter API to get a bot to tweet user input but change the source label so it doesn't show "Twitter for iPhone/Android" This will be done using Python and Tweepy for simplification."
YOU ARE NOT ANALYZING DATA, UNCHECK THE BOX
The app will be tweeting so check the "Will your app tweet, retweet and comment?" box. I put "Tweepy and Python will be used to tweet user input from a custom source label instead of the default tag."
We are not using these:
Do you plan to display Tweets or aggregate data about Twitter content outside of Twitter?
Will your product, service or analysis make Twitter content or derived information available to a government entity?
Next, Review, Looks Good!
Agree to the terms and click submit application.
Once you are approved, you can create app.

Whatever you name the app will be the source tag of the tweet, so choose carefully!
Use this template for ease:
App name (required):
Sack of potatoes

Application description (required)
This is my app that allows user to change device from "Twitter on x" to whatever they please

Website URL (required)
https://github.com/{YOUR NAME}

Allow this application to be used to sign in with Twitter
Enable Sign in with Twitter: No
Callback URLs: None
Terms of Service URL: None
Privacy policy URL: None
Organization name: None
Organization website URL: None

Tell us how this app will be used (required)
My application will be used to change the source device name of the tweet that it will be publishing.

Now click create!
Review and accept.
Click the "Keys and tokens" tab
Click Generate for your keys
Replace the _YOUR_ACCESS_TOKEN_SECRET and others in the python code with the information on screen.
Run the program and input what the tweet will say and hit enter!
