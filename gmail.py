from __future__ import print_function
import pickle
import os.path
import re
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API to get the labels
    results = service.users().messages().list(userId='me',labelIds = ['INBOX']).execute()
    messages = results.get('messages', [])

    if not messages:
        print('No messages found.')
    else:
        i = 0
        message = messages[0]
        scheduleMessage = ''
        while scheduleMessage == '':
            message = messages[i]
            msg = service.users().messages().get(userId='me', id=message['id'], format='metadata').execute()
            for header in msg['payload']['headers']:
                if header['name'] == 'From':
                    if header['value'] == 'Craig Colucci <craig@dbatvirginiabeach.com>':
                        scheduleMessage = message['id']
                        print(header['value'])
                        print(scheduleMessage)

                        schedule = service.users().messages().attatchments.get(userId='me', id=message['id']).execute()
                        print("moo")

            i = i + 1

if __name__ == '__main__':
    main()