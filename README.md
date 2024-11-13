## SFTP File Management with Paramiko

This repository contains Python scripts for managing files on an SFTP server using the `paramiko` library. The scripts include functionalities for connecting to an SFTP server, recursively searching for files, downloading files, and uploading files. Environment variables are used to securely store and retrieve SFTP credentials.

### Features

- **SFTP Connection**: Establishes a secure connection to an SFTP server using `paramiko.SSHClient`.
- **Recursive File Search and Download**: Recursively searches for a specified file on the remote server and downloads it to a local directory.
- **File Upload**: Uploads a local file to a specified path on the remote server.
- **Environment Variables**: Uses a `.env` file to securely store and retrieve SFTP credentials.

### Setup

1. **Clone the Repository**:
   ```bash
   git https://github.com/ShahMehraj/SSH-File-Transfer-Protocol.git
   cd sftp-file-management
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` File**:
   Create a `.env` file in the project directory with the following content:
   ```
   SFTP_HOST=your_sftp_host
   SFTP_USERNAME=your_username
   SFTP_PASSWORD=your_password
   ```

### Usage

1. **Connect to SFTP Server**:
   ```python
   sftp = sftp_connect()
   ```

2. **Search and Download File**:
   ```python
   search_and_download(sftp, remote_dir='/', filename='wmr1006.csv', local_dir='./')
   ```

3. **Upload File**:
   ```python
   upload_file(sftp, local_file_path='path/to/local/file.txt', remote_file_path='/path/to/remote/file.txt')
   ```

### Example

```python
import paramiko as pmk
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Establish SFTP connection
sftp = sftp_connect()

# Search and download file
search_and_download(sftp, remote_dir='/', filename='wmr1006.csv', local_dir='./')

# Upload file
upload_file(sftp, local_file_path='path/to/local/file.txt', remote_file_path='/path/to/remote/file.txt')

# Close SFTP connection
sftp.close()
```

---
