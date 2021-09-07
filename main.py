import googlesearch
import csv

query = "site:https://www.searchenginejournal.com/ "

# reading the keywords
with open('keywords.txt', 'r', newline="") as f:
    keywords = f.readlines()

# looping through the keywords
for keyword in keywords:
    # for each keyword the result is the first 50 (or however much the num_results is set to) links
    results = googlesearch.search(query + keyword, num_results=50)
    print(results)

    # writing the results to a csv file
    with open('saved_links.csv', 'w', newline="") as f:
        # creating a csv writer object
        writer = csv.writer(f)
        # each keyword has it's own row of subsequent links
        writer.writerow(results)
