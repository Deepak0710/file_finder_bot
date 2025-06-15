# utils/gmail.py

from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Gmail readonly scope
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None
    token_path = 'credentials/token.json'
    creds_path = 'credentials/credentials.json'

    # Load existing token if available
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    # If no valid credentials, go through OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save token
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def get_starred_email_subjects(max_results=10):
    service = authenticate_gmail()
    results = service.users().messages().list(
        userId='me',
        labelIds=['STARRED'],
        maxResults=max_results
    ).execute()

    messages = results.get('messages', [])
    subjects = []

    for msg in messages:
        msg_detail = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_detail['payload'].get('headers', [])
        for header in headers:
            if header['name'] == 'Subject':
                subjects.append(header['value'])
                break

    return subjects

    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        snippet = msg['snippet']
        print(f"📧 Starred Email: {snippet[:100]}")

