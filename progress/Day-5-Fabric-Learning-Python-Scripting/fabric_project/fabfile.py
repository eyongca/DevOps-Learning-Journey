"""
Fabric Project for Automating Remote Server Management

Author: Eyong Christopher

Description:
This script uses Fabric to automate common tasks on a remote server, such as updating packages, 
checking logs, managing services, and deploying applications.

How to Use:
1. Install Fabric:
   pip install fabric

2. Create an SSH key pair (if not already created):
   ssh-keygen -t rsa -b 2048

3. Add your public key to the remote server:
   ssh-copy-id -i /path/to/your/public_key user@server_ip

4. Update the variables `REMOTE_USER`, `REMOTE_HOST`, and `KEY_FILE` in the script to match your setup.

5. Run tasks using the `fab` command:
   - Test connection: `fab connect`
   - Update system: `fab update_system`
   - Check logs: `fab check_logs --log-file=/path/to/logfile`
   - Manage a service: `fab manage_service --service-name=nginx --action=status`
   - Deploy an app: `fab deploy_app`
   - Deploy and monitor logs: `fab deploy_and_monitor`

"""

from fabric import Connection, task

# Define global configuration
REMOTE_USER = "your_user"
REMOTE_HOST = "your_server_ip_or_hostname"
KEY_FILE = "/path/to/your/private_key"

@task
def connect(ctx):
    """
    Test the connection to the remote server.
    """
    conn = Connection(
        host=REMOTE_HOST,
        user=REMOTE_USER,
        connect_kwargs={"key_filename": KEY_FILE},
    )
    conn.run("uname -a")
    print("Connection successful!")


@task
def update_system(ctx):
    """
    Update the system packages on the remote server.
    """
    conn = Connection(
        host=REMOTE_HOST,
        user=REMOTE_USER,
        connect_kwargs={"key_filename": KEY_FILE},
    )
    print("Updating system packages...")
    conn.sudo("apt-get update && apt-get upgrade -y")
    print("System update completed!")


@task
def check_logs(ctx, log_file="/var/log/syslog"):
    """
    Check the specified log file on the remote server.
    """
    conn = Connection(
        host=REMOTE_HOST,
        user=REMOTE_USER,
        connect_kwargs={"key_filename": KEY_FILE},
    )
    print(f"Displaying the last 20 lines of {log_file}...")
    conn.run(f"tail -n 20 {log_file}")


@task
def manage_service(ctx, service_name, action):
    """
    Manage a service (start, stop, restart, status) on the remote server.
    :param service_name: Name of the service to manage.
    :param action: Action to perform (start, stop, restart, status).
    """
    conn = Connection(
        host=REMOTE_HOST,
        user=REMOTE_USER,
        connect_kwargs={"key_filename": KEY_FILE},
    )
    print(f"{action.capitalize()}ing the service: {service_name}")
    conn.sudo(f"systemctl {action} {service_name}")


@task
def deploy_app(ctx):
    """
    Deploy a sample web application to the remote server.
    """
    conn = Connection(
        host=REMOTE_HOST,
        user=REMOTE_USER,
        connect_kwargs={"key_filename": KEY_FILE},
    )
    print("Deploying the web application...")

    # Clone the repository
    repo_url = "https://github.com/your-repo/sample-web-app.git"
    conn.run(f"git clone {repo_url} ~/sample-web-app")

    # Install dependencies
    conn.sudo("apt-get install -y python3-pip")
    conn.run("pip3 install -r ~/sample-web-app/requirements.txt")

    # Start the application
    conn.run("python3 ~/sample-web-app/app.py &")
    print("Web application deployed and started!")


@task
def deploy_and_monitor(ctx):
    """
    Deploy the application and monitor its logs.
    """
    deploy_app(ctx)
    check_logs(ctx, log_file="~/sample-web-app/logs/app.log")
