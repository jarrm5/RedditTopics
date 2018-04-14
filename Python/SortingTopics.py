import csv

#Search dataset by title "keyword"
def search(keyword):
    with open("Book1.csv", "r") as incsvfile:
        reader = csv.DictReader(incsvfile)

        with open("Book1write.csv", 'w') as outcsvfile:
            dw = csv.DictWriter(outcsvfile, delimiter=',', fieldnames=reader.fieldnames)
            headers = {}
            for n in dw.fieldnames:
                headers[n] = n
            dw.writerow(headers)
            for row in reader:
                if keyword in row['title']:
                    row['title'] = row['title'].replace(",", "")
                    dw.writerow(row)

#Sort based on highest number of ups count for given keyword

def sort():
    with open("Book1write.csv", "r") as incsvfile:
        reader = csv.DictReader(incsvfile,delimiter=",")
        sortedlist = sorted(reader, key=lambda row: (row['ups']), reverse=False)
        print(sortedlist)
        with open('sorted.csv', 'w') as f:
            #writer = csv.DictWriter(f, fieldnames=reader.fieldnames, quoting=csv.QUOTE_NONNUMERIC)
            writer = csv.DictWriter(f, delimiter=",", fieldnames=reader.fieldnames,quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()
            for row in sortedlist:
                writer.writerow(row)


#Program Starts here

keyword = input("Enter keyword:\n")
search(keyword)
sort()