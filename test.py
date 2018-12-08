from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

# The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1AoPWgr7YNP3p0PmFYO_qByrrSuKDcmd-ImII1BVMzIA'
SAMPLE_SPREADSHEET_ID = '1894IkSZptgj9hnY7fDO5J4gVLjrZqpkRBSUasS0RgPg'
SAMPLE_RANGE_NAME = 'R11:V75'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    sheet = service.spreadsheets()
    # result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
    #                             range=SAMPLE_RANGE_NAME).execute()
    # values = result.get('values', [])

    cols = []
    with open('values.txt') as f:
        for line in f.readlines():
            row = line.split(' ')
            cols.append(row)
    
    body = {'values': cols, 'majorDimension': 'COLUMNS'}

    result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME, valueInputOption='USER_ENTERED', body=body).execute()

    # col_names = ['R', 'S', 'T', 'U', 'V']
    # start_row = 11
    # for c in range(len(cols)):
    #     col = cols[c]
    #     col_name = col_names[c]
    #     for i in range(len(col)):
    #         row_num = start_row + i + int(i / 10)



if __name__ == '__main__':
    main()