import paramiko as pmk

def sftp_connect(host, username, password):
    try:
        ssh = pmk.SSHClient()
        ssh.set_missing_host_key_policy(pmk.AutoAddPolicy())
        ssh.connect(hostname=host, username=username, password=password)
        sftp_client = ssh.open_sftp()
        return sftp_client
    except Exception as e:
        print(f"Connection failed: {e}")
        return None
