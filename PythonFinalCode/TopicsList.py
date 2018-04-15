# Import statements
import csv
import re


# Add Header to the csv file threads.csv and store this new file in file.csv
def addHeader():
    seen = []
    with open('threads.csv', 'r') as f1:
        try:
            r = csv.reader(f1)
            data = [line for line in r]
            datalist = list(data)
            with open('file.csv', 'w') as f2:
                try:
                    w = csv.writer(f2)
                    w.writerow(['text', 'title', 'url', 'id', 'subreddit', 'meta', 'time', 'author', 'ups', 'downs',
                                'authorlinkkarma', 'authorcommentkarma', 'authorisgold'])
                    for row in datalist:
                        if row[1] not in seen:
                            seen.append(row[1])
                            w.writerow(row)
                except IOError:
                    print "Error: Cannot perform write operation."
                    return 0
        except IOError:
            print "Error: File does not appear to exist."
            return 0


# Search for user entered keyword and stores in searchresult.csv
def search(keyword):
    with open("file.csv", "rt") as incsvfile:
        try:
            reader = csv.DictReader(incsvfile)
            with open('searchresult.csv', 'wt') as outcsvfile:
                try:
                    dw = csv.DictWriter(outcsvfile, delimiter=',', fieldnames=reader.fieldnames)
                    headers = {}
                    for n in dw.fieldnames:
                        headers[n] = n
                    dw.writerow(headers)
                    for row in reader:
                        if keyword in row['title']:
                            row['title'] = row['title'].replace(",", "")
                            dw.writerow(row)
                except IOError:
                    print "Error: Cannot perform write operation."
                    return 0
        except IOError:
            print "Error: File does not appear to exist."
            return 0


# Sorts searchresult.csv, removes redundant and unwanted information and stores top 10 news based on time and ups count
# in finaldata.csv file
def sort():
    newtopics = []
    topicsList = []
    with open("searchresult.csv", "r") as incsvfile:
        try:
            datarows = csv.DictReader(incsvfile, delimiter=',')
            newlist = list(datarows)
            sorted_data = sorted(newlist, key=lambda k: (k['time'], k['ups']), reverse=True)

            with open('finaldata.csv', 'w') as f:
                try:
                    writer = csv.DictWriter(f, delimiter=",", fieldnames=['title', 'url', 'time', 'ups'])
                    writer.writeheader()
                    j = 1
                    flag = False
                    for q in sorted_data:
                        if q['title'] not in newtopics:
                            newtopics.append(q['title'])
                            if j <= 10:
                                j = j + 1
                                result = re.sub(r'[^a-zA-Z0-9]', " ", q['title'])
                                result = " ".join(result.split())
                                writer.writerow({'title': result,
                                                 'url': q['url'],
                                                 'time': q['time'],
                                                 'ups': q['ups']
                                                 })
                                #List of top 10 topics after sorting
                                topicsList.append(result)
                            else:
                                flag = True
                                break
                        elif flag:
                            break
                    # Print List of top 10 topics after sorting
                    print "Topic List:\n",topicsList
                except IOError:
                    print "Error: Cannot perform write operation."
                    return 0
        except IOError:
            print "Error: File does not appear to exist."
            return 0


# Call addheader to add headers
addHeader()

# Enter keyword
keyword = raw_input("Enter keyword:\n")

# Search for keyword
search(keyword)

# Sort the data based on time and ups
sort()