from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from dotenv import load_dotenv

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = 'supersecretkey'
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'pdf', 'txt'}
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_credentials():
    """Handles OAuth login and token saving."""
    creds = None
    if os.path.exists('token.pkl'):
        with open('token.pkl', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials_oauth.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pkl', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def upload_to_drive(filepath, filename):
    """Uploads a file to Google Drive using OAuth credentials."""
    creds = get_credentials()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {'name': filename}
    media = MediaFileUpload(filepath, resumable=True)

    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"✅ File uploaded successfully, ID: {file.get('id')}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part!')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No selected file!')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            upload_to_drive(filepath, filename)
            flash('File uploaded successfully to your Google Drive!')
        except Exception as e:
            flash(f'Error uploading to Google Drive: {e}')

        return redirect(url_for('index'))
    else:
        flash('Invalid file type! Allowed: pdf, txt')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
