# Author: Eyong Christopher
# Introduction:
# This script demonstrates how to use Paramiko for automating tasks on remote servers.
# It includes functionalities like establishing SSH connections, transferring files securely
# using SFTP, executing remote commands, and monitoring server status. These tasks are 
# common in DevOps and DevSecOps pipelines for managing infrastructure remotely.

# How to Use:
# 1. Set the appropriate server details (hostname, SSH username, private key, file paths).
#    - Update the 'hostname', 'username', and 'private_key_path' variables with your server details.
# 2. Update the local and remote file paths for file transfer (if required).
# 3. Modify the commands to execute on the remote server as needed.
# 4. Save the script as a .py file (e.g., remote_server_management.py).
# 5. Run the script using Python:
#    python remote_server_management.py
#    The script will:
#    - Establish an SSH connection to the remote server.
#    - Transfer a file from the local machine to the remote server.
#    - Execute a command on the remote server.
#    - Monitor the server's uptime.

import paramiko
import time

# Define SSH parameters
hostname = 'your_remote_server_ip'  # Example: '192.168.1.100'
port = 22
username = 'your_ssh_username'  # Example: 'ec2-user'
private_key_path = '/path/to/your/private/key.pem'  # Example: '/home/user/.ssh/my-key.pem'

# Create SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote server
try:
    print(f"Connecting to {hostname}...")
    client.connect(hostname, port=port, username=username, key_filename=private_key_path)
    print("Connected successfully.")
except Exception as e:
    print(f"Connection failed: {e}")
    exit(1)

# Function to transfer file securely using SFTP
def transfer_file(local_path, remote_path):
    try:
        # Open an SFTP session
        sftp = client.open_sftp()
        print(f"Transferring file from {local_path} to {remote_path}...")
        sftp.put(local_path, remote_path)  # Transfer file
        sftp.close()
        print(f"File transferred successfully to {remote_path}.")
    except Exception as e:
        print(f"File transfer failed: {e}")

# Function to execute remote command
def execute_command(command):
    try:
        print(f"Executing command: {command}")
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')
        
        if output:
            print(f"Output: {output}")
        if error:
            print(f"Error: {error}")
    except Exception as e:
        print(f"Command execution failed: {e}")

# Function to monitor server status
def monitor_server_status():
    command = 'uptime'  # Check server uptime as an example
    execute_command(command)

# Putting everything together
def main():
    # Step 1: SSH Connection Setup
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        print(f"Connecting to {hostname}...")
        client.connect(hostname, port=port, username=username, key_filename=private_key_path)
        print("Connected successfully.")
        
        # Step 2: Transfer File
        local_file = '/path/to/local/config_file.conf'  # Example: '/home/user/config_file.conf'
        remote_file = '/path/to/remote/config_file.conf'  # Example: '/etc/config_file.conf'
        transfer_file(local_file, remote_file)
        
        # Step 3: Execute Commands
        execute_command('sudo apt update && sudo apt install -y apache2')
        
        # Step 4: Monitor Server
        monitor_server_status()

    except Exception as e:
        print(f"Connection failed: {e}")
        exit(1)
    
    finally:
        client.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
