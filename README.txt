The goal is to process the Reddit threads dataset to understand the hot topic people are talking about.

After extracting top 10 news out of your dataset, use Google Api to search through the google and find the most related pictures to the extracted news. 
You should also consider the time in which the topic is related about to find the pictures related to that topic on special time saved on the dataset

For detecting hot topics in the Reddit dataset, you may go for topic detection approach or clustering approach. Refer to this link to read about

Reddit site: https://en.wikipedia.org/wiki/Reddit
Link to the dataset: https://mega.nz/#F!NtsCGTgD!urXdXLJ6yITYdWEdWN-H1w
Headers are:
'text', 'title', 'url', 'id', 'subreddit', 'meta', 'time', 'author', 'ups', 'downs', 'authorlinkkarma', 'authorcommentkarma', 'authorisgold'

Explanations of the dataset:

· text: text of the thread

· title: title of the thread

· url: url of the thread

· id: unique ID of the thread

· subreddit: subreddit that the thread belongs to

· meta: meta tag assigned to the subreddit of the thread in config.json

· time: timestamp of the thread

· author: username of the author of the thread

· ups: number of ups the thread has received

· downs: number of downs the thread has received

· authorlinkkarma: the author's link karma

· authorcommentkarma: the author's comment karma

· authorisgold: 1 if the author has gold status, 0 otherwise

References
https://github.com/linanqiu/reddit-dataset