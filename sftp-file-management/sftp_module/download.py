import os
import stat

def search_and_download(sftp, remote_dir, filename, local_dir='./'):
    """
    Recursively searches for a specified file in a remote directory and downloads it to a local directory.

    Args:
        sftp (paramiko.SFTPClient): An active SFTP client connection.
        remote_dir (str): The remote directory to start the search from.
        filename (str): The name of the file to search for.
        local_dir (str): The local directory to download the file to.

    Returns:
        bool: True if the file is found and downloaded, False otherwise.

    Raises:
        FileNotFoundError: If the specified file or directory is not found.
        PermissionError: If there are permission issues accessing the file or directory.
        Exception: For any other unexpected errors during the search and download process.
    """
    try:
        print(f"Searching in directory: {remote_dir}")
        for entry in sftp.listdir_attr(remote_dir):
            remote_path = os.path.join(remote_dir, entry.filename).replace('\\', '/')
            if stat.S_ISDIR(entry.st_mode):
                print(f"Entering directory: {remote_path}")
                if search_and_download(sftp, remote_path, filename, local_dir):
                    return True
            elif entry.filename == filename:
                local_path = os.path.join(local_dir, filename)
                print(f"File found: {remote_path}")
                sftp.get(remote_path, local_path)
                print(f"File {filename} downloaded to {local_path}")
                return True
        return False
    except FileNotFoundError as e:
        print(f"Error during search and download: {e}")
        return False
    except PermissionError as e:
        print(f"Permission error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
