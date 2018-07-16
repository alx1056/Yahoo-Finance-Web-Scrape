import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime

#Lets you choose which ticker you want to view without having to manually change the URL
ticker = input("Please enter the ticker symbol you want to see stock data for?")
#Sets a date that you are starting to view your data
start_date = datetime.datetime.now().strftime("%m-%d-%y")
#Sets the URL based off of the Ticker you have chosen 
html = urlopen("https://finance.yahoo.com/quote/"+ticker+"/history?p="+ticker) 
#Calls Beautifil Soup Object and converts HTML to lxml
bsObj = BeautifulSoup(html, "lxml")
#Searches for the table in the DOM and then searches for the specified class that the table is within
table = bsObj.findAll("table", {"class": "W(100%) M(0)"})[0]
#Collects and finds all Rows of that table
rows = table.findAll("tr")
#Creates the CSV file and names it based off of the ticker name and Start Date
csvFile = open("Stock history of "+ticker + " "+ start_date+".csv", 'wt', newline='')
#Writes and Creates the CSV file
writer = csv.writer(csvFile)
#Exception Handling to catch only Rows and Coumns (table data)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    #Closes the CSV file
    csvFile.close()
