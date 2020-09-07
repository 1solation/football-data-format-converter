from urllib import request
import csv
import sys

my_list = []  # instantiate list for insertion of values
url = sys.argv[1]
response = request.urlopen(url)
lines = [line.decode("utf-8") for line in response.readlines()]
cr = csv.reader(lines)

next(cr)  # skips header row of CSV file
for row in cr:
    # create data structure to populate for each record in CSV file
    my_list.append(
        {
            "Div": row[0],
            "Date": row[1],
            "Time": row[2],
            "HomeTeam": row[3],
            "AwayTeam": row[4],
            "FTHG": row[5],
            "FTAG": row[6],
        }
    )
    print(my_list)  # output to console
# save data to file for easy access at a later date
with open("results.txt", "w") as f:
    for item in my_list:
        f.write("%s\n" % item)
# print(lines)
