import os
from dotenv import load_dotenv
from sftp_module.connection import sftp_connect
from sftp_module.download import search_and_download
from sftp_module.upload import upload_file

load_dotenv()

host = os.getenv('SFTP_HOST')
username = os.getenv('SFTP_USERNAME')
password = os.getenv('SFTP_PASSWORD')

sftp = sftp_connect(host, username, password)
if sftp:
    remote_dir = '/'
    filename = 'wmr1006.csv'
    local_dir = './'
    found = search_and_download(sftp, remote_dir, filename, local_dir)
    if not found:
        print(f"File {filename} not found on the server.")
    sftp.close()
