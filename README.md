# bill_reader


## Python 
version 3.7* or (3.8)

## Install Easyocr 
```python3 -m pip install --upgrade pip```
```pip install easyocr```

## csv entries
Received date	Supplier Name	Invoice Number	Invoice Date	Currency	Sub total	Vat/Tax	Total

## Date and time validate format
```"Jun 28 2018 at 7:40AM" -> "%b %d %Y at %I:%M%p"```
```"September 18, 2017, 22:19:55" -> "%B %d, %Y, %H:%M:%S"```
```"Sun,05/12/99,12:30PM" -> "%a,%d/%m/%y,%I:%M%p"```
```"Mon, 21 March, 2015" -> "%a, %d %B, %Y"```
```"2018-03-12T10:12:45Z" -> "%Y-%m-%dT%H:%M:%SZ"```
https://stackabuse.com/converting-strings-to-datetime-in-python
```dtime = datetime.datetime.now()```
