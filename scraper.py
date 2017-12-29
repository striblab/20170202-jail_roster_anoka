# 0. LOAD LIBRARIES
import urllib2
from urllib2 import urlopen
from datetime import datetime
import csv
import json
import sys

# 1. SCRAPE RAW DATA
rawData = urllib2.urlopen("http://www.anok.co/JailInfoForPublic/inmates_json.aspx").read()

print(rawData)

# 2. CONVERT TO CSV
data_parsed = json.loads(rawData)

inmate_data = data_parsed['inmates']

# 3. TIMESTAMP THE CSV
FORMAT = '%Y%m%d%H%M%S'
path = 'roster.json'
new_path = '%s_%s' % (datetime.now().strftime(FORMAT), path)

# 4. WRITE TO ARCHIVE
text_file = open(new_path, 'w')
text_file.write(rawData)
# csvwriter = csv.writer(text_file)

# count = 0

# for inmate in inmate_data:

#       if count == 0:

#              header = inmate.keys()

#              csvwriter.writerow(header)

#              count += 1

#       csvwriter.writerow(inmate.values())

text_file.close()


# 5. SEARCH CSV FOR HIT
f = open('names.csv')
csv_f = csv.reader(f)
text_file2 = open('hits.txt',"a")

# import re
# def string_found(string1, string2):
#    if re.search(r"\b" + string1 + r"\b", string2):
#       return True
#    return False

# 6. RECORD HITS IN MASTER HIT FILE
for row in csv_f:
	print(str('"' + row[0] + '","' + row[1] + '"'))
	# if str(row[0]) in str(inmate_data) != -1 and str(row[1]) in str(inmate_data) != -1:
	if str('["' + row[0] + '","' + row[1] + '",') in str(rawData) != -1:
		text_file2.write('Found on %s - %s\n' % (datetime.now().strftime(FORMAT), str(row)))

f.close();
text_file2.close();