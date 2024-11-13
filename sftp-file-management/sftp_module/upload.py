import os

def upload_file(sftp, local_file_path, remote_file_path):
    """
    Uploads a local file to a specified remote server path.

    Args:
        sftp (paramiko.SFTPClient): An active SFTP client connection.
        local_file_path (str): The path to the local file to be uploaded.
        remote_file_path (str): The path on the remote server where the file will be uploaded.

    Returns:
        bool: True if the file is successfully uploaded, False otherwise.

    Raises:
        FileNotFoundError: If the local file does not exist.
        Exception: For any other unexpected errors during the upload process.
    """
    try:
        if not os.path.isfile(local_file_path):
            raise FileNotFoundError(f"Local file {local_file_path} does not exist.")
        
        sftp.put(local_file_path, remote_file_path)
        print(f"File {local_file_path} uploaded to {remote_file_path}")
        return True
    except FileNotFoundError as e:
        print(f"Error during upload: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
