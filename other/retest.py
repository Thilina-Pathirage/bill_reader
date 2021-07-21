import datetime

import easyocr
import csv

IMAGE_PATH = '../images/invoice.png'

reader = easyocr.Reader(['en'], gpu=False)

bound = reader.readtext(IMAGE_PATH)

text = ''
for i in range(len(bound)):
    text = text + bound[i][1] + '\n'

lower_text = text.lower()
res = lower_text.split()

print(res)

# Get total
total = 0
for index, i in enumerate(res):
    if i == 'total':
        print("The Total: " + res[index + 1])
        total = res[index + 1]

# Date validate


def date_validate(date_string):
    date_date = str(date_string)
    try:
        if date_string == datetime.datetime.strptime(date_date, '%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        return False


date = ""
for index, i in enumerate(res):
    if date_validate(res[index]):
        print("true")
        date = res[index]

header = ['Total', 'Date']
data = [
    [total, date]
]

with open('../outputs.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
