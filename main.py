##################################################################################################
# Import Libraries

import datetime
import easyocr
import csv
from dateutil.parser import parse
#import datetime as date_time_obj
#from datetime import datetime

##################################################################################################
# Functions

# Date validate
def is_date(date_time_str):
    done = False
    if done == False:
        try: 
            datetime.datetime.strptime(date_time_str, '%m/%d/%y')
            done = True
        except ValueError:
            done = False
    if done == False:
        try: 
            datetime.datetime.strptime(date_time_str, '%d/%m/%y')
            done = True
        except ValueError:
            done = False
    if done == False:
        try: 
            datetime.datetime.strptime(date_time_str, '%d/%m/%Y')
            done = True
        except ValueError:
            done = False
    return done
    



##################################################################################################

# OCR 
IMAGE_PATH = './images/invoice2.png'
reader = easyocr.Reader(['en'], gpu=False)
bound = reader.readtext(IMAGE_PATH)

text = ''
for i in range(len(bound)):
    text = text + bound[i][1] + '\n'

lower_text = text.lower()
res = lower_text.split() # put in to list
print(res)

# Get total
total = 0
date = "YYYY-MM-DD"
Currency = "Currency"
for index, value in enumerate(res):
    # Get Total
    if value == 'total':
        tot_str = res[index + 1]
        if tot_str[0] == 's':
            Currency = "Doller"
            total = tot_str[1:]
        print("Total: " + total)
    # Get Date
    if is_date(value):
        date = value
        print("Date: " + date)




""" for index, val in enumerate(res):
    if val==val:
        print("true") """
        
    

header = ['Total', 'Date', 'Currency']
data = [
    [total, date, Currency]
]

with open('outputs.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

