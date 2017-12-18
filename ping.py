import os
import commands
import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials
 
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/googlePing/client_secret.json', scope)
client = gspread.authorize(creds)

now = datetime.datetime.now()

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Ping").sheet1

#Get the number of total rows 
allRows = sheet.row_count

hostname = "8.8.8.8"
response = commands.getoutput("ping -c 4 "+ hostname + "| tail -1| awk '{print $4}' | cut -d '/' -f 2")

#Remove values after the .
pingVal = str(response).split('.', 1)[0]

row = [now.strftime("%d-%m-%Y %H:%M"), pingVal]

sheet.insert_row(row, allRows+1)
print 'Script executed correctly '+now.strftime("%d-%m-%Y %H:%M")
