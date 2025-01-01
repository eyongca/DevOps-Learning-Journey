import os
import subprocess
import sys
import time
import requests


# Configuration
REPO_URL = "https://github.com/eyongca/DevOps-Learning-Journey.git"
CLONE_DIR = "/home/devops/DevOps-Learning-Journey"
APP_PORT = 5000
DOCKER_IMAGE_NAME = "day-1"
DOCKER_CONTAINER_NAME = "day-1-container"
VENV_DIR = os.path.join(CLONE_DIR, "venv")


# Step 0: Ensure prerequisites are installed
def ensure_prerequisites():
    print("Ensuring prerequisites are installed...")

    # Check if python pip is installed
    try:
        subprocess.run(["pip", "--version"], check=True)
    except FileNotFoundError:
        print("pip is not installed. Installing pip...")
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "python3-pip"], check=True)

    # Check if git is installed
    try:
        subprocess.run(["git", "--version"], check=True, stdout=subprocess.DEVNULL)
    except FileNotFoundError:
        print("Git is not installed. Installing git...")
        subprocess.run(["sudo", "apt", "install", "-y", "git"], check=True)

    # Check if docker is installed
    try:
        subprocess.run(["docker", "--version"], check=True, stdout=subprocess.DEVNULL)
    except FileNotFoundError:
        print("Docker is not installed. Installing docker...")
        subprocess.run(["sudo", "apt", "install", "-y", "docker.io"], check=True)
        subprocess.run(["sudo", "systemctl", "start", "docker"], check=True)
        subprocess.run(["sudo", "systemctl", "enable", "docker"], check=True)

    print("Prerequisites are installed.")


# Step 1: Clone the git repository
def clone_repo():
    from git import Repo
    if not os.path.exists(CLONE_DIR):
        print("Cloning the git repository...")
        Repo.clone_from(REPO_URL, CLONE_DIR)
    else:
        print("Git repository already cloned. Skipping this step.")


# Step 2: Install the application dependencies
def install_app_dependencies():
    print("Installing the application dependencies...")

    # Check for requirements.txt file and install python dependencies
    requirements_file = os.path.join(CLONE_DIR, "requirements.txt")
    if os.path.exists(requirements_file):
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)

        subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_file], check=True)
    else:
        print("No requirements.txt file found. Skipping this step.")

    # Check for package.json file and install node dependencies
    package_json_file = os.path.join(CLONE_DIR, "package.json")
    if os.path.exists(package_json_file):
        subprocess.run(["npm", "install"], check=True, cwd=CLONE_DIR)
    else:
        print("No package.json file found. Skipping this step.")


# Step 3: Build the docker image
def deploy_with_docker():
    print("Building the docker image...")
    subprocess.run(["docker", "build", "-t", DOCKER_IMAGE_NAME, CLONE_DIR], check=True)

    print("Running the docker container...")
    subprocess.run(["docker", "run", "-d", "-p", f"{APP_PORT}:{APP_PORT}", "--name", DOCKER_CONTAINER_NAME, DOCKER_IMAGE_NAME], check=True)


# Step 4: Monitor the application is running
def monitor_appplication():
    url = f"http://localhost:{APP_PORT}"
    print("Monitoring the application...")
    try:
        while True:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"Application is running with status code {response.status_code}")
                else:
                    print(f"Application is not running with status code {response.status_code}")
            except requests.exceptions.ConnectionError:
                print("Application is not running. Connection error.")
            time.sleep(10)

    except KeyboardInterrupt:
        print("Monitoring stopped.")


# Step 5: Install python libraries required for the script to run
def install_script_dependencies():
    print("Installing the script dependencies...")
    try:
        import git
    except ImportError:
        print("Installing gitpython...")
        subprocess.run([sys.executable, "-m", "pip", "install", "gitpython"], check=True)


# Step 6: Install pip in virtual environment if not found
def install_pip_in_venv():
    if not os.path.exists(os.path.join(VENV_DIR, "bin", "pip")):
        print("pip not found in virtual environment. Installing pip...")

        # Download get-pip.py script
        subprocess.run(["curl", "https://bootstrap.pypa.io/get-pip.py", "-o", "get-pip.py"], check=True)

        # Install pip in the virtual environment
        subprocess.run([sys.executable, "get-pip.py"], check=True)

        # Clean up
        os.remove("get-pip.py")
    else:
        print("pip is already installed in the virtual environment.")


# Step 7: Main function
if __name__ == "__main__":
    ensure_prerequisites()
    install_script_dependencies()

    # Create virtual environment if it doesn't exist
    if not os.path.exists(VENV_DIR):
        print(f"Creating virtual environment in {VENV_DIR}...")
        subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True)

    # Install pip in the virtual environment if necessary
    install_pip_in_venv()

    clone_repo()
    install_app_dependencies()
    deploy_with_docker()
    monitor_appplication()
