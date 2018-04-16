The goal is to process the Reddit threads dataset to understand the hot topic people are talking about.

After extracting top 10 news out of your dataset, use Google Api to search through the google and find the most related pictures to the extracted news. 
You should also consider the time in which the topic is related about to find the pictures related to that topic on special time saved on the dataset

For detecting hot topics in the Reddit dataset, you may go for topic detection approach or clustering approach. Refer to this link to read about

Reddit site: https://en.wikipedia.org/wiki/Reddit
Link to the dataset: https://mega.nz/#F!NtsCGTgD!urXdXLJ6yITYdWEdWN-H1w
Headers are:
'text', 'title', 'url', 'id', 'subreddit', 'meta', 'time', 'author', 'ups', 'downs', 'authorlinkkarma', 'authorcommentkarma', 'authorisgold'

Explanations of the dataset:

� text: text of the thread

� title: title of the thread

� url: url of the thread

� id: unique ID of the thread

� subreddit: subreddit that the thread belongs to

� meta: meta tag assigned to the subreddit of the thread in config.json

� time: timestamp of the thread

� author: username of the author of the thread

� ups: number of ups the thread has received

� downs: number of downs the thread has received

� authorlinkkarma: the author's link karma

� authorcommentkarma: the author's comment karma

� authorisgold: 1 if the author has gold status, 0 otherwise

References
https://github.com/linanqiu/reddit-dataset

APPLICATION DEPENDENCIES

1. Web Server
Since this application makes REST calls over HTTP, a web server like Apache is required to run the application.

2. Python version 3.2+
The application uses a python script to parse reddit threads contained in a csv file.
Since we are using an ajax call in javascript to execute this python script, an extra client-server layer is required.
The application uses a lightweight web framework called Flask which requires python version 3.2+

##Youtube Link
https://youtu.be/55gj878KKKg