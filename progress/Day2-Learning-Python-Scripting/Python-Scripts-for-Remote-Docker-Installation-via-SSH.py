"""
Script Name: install_docker.py
Description: Script to check and install Docker if not already installed using SSH for secure automation.

Author: [Eyong Christopher]
Version: 1.1
"""

import subprocess

# Define the remote server and SSH details
REMOTE_USER = "ubuntu"
REMOTE_HOST = "3.89.93.62"
SSH_KEY_PATH = "/home/devops/Downloads/devops.pem"  # Path to your SSH private key

def run_remote_command(command):
    """
    Runs a command on a remote server via SSH.
    """
    try:
        ssh_command = [
            "ssh",
            "-i", SSH_KEY_PATH,
            f"{REMOTE_USER}@{REMOTE_HOST}",
            command
        ]
        result = subprocess.run(ssh_command, check=True, text=True, capture_output=True)
        print(result.stdout)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Remote command failed: {e}")
        print(e.stderr)
        return None

def is_docker_installed():
    """
    Checks if Docker is installed on the remote server.
    """
    check_command = "command -v docker"
    result = run_remote_command(check_command)
    return result is not None

def install_docker_remotely():
    """
    Installs Docker on a remote server if not already installed.
    """
    if is_docker_installed():
        print("Docker is already installed on the remote server.")
    else:
        print("Docker is not installed on the remote server. Installing Docker...")
        try:
            install_script_command = "curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh"
            run_remote_command(install_script_command)
            print("Docker installed successfully on the remote server.")
        except Exception as e:
            print(f"An unexpected error occurred during installation: {e}")

def main():
    """
    Main function to execute the script logic.
    """
    install_docker_remotely()

if __name__ == "__main__":
    main()
