import os
import subprocess
import platform

try:
    import distro  # For identifying Linux distributions
except ImportError:
    print("[INFO] Installing 'distro' package for Linux distribution detection...")
    subprocess.run(["pip3", "install", "distro"], check=True)
    import distro


def check_and_install_nmap():
    """
    Checks if nmap is installed. If not, attempts to install it based on the OS.
    """
    try:
        # Check if nmap is installed
        subprocess.run(["nmap", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print("[INFO] Nmap is already installed.")
    except FileNotFoundError:
        print("[INFO] Nmap is not found. Attempting to install...")
        os_type = platform.system()

        if os_type == "Linux":
            # Use the distro module for Linux distribution detection
            distribution = distro.id()
            if distribution in ["ubuntu", "debian"]:
                subprocess.run(["sudo", "apt", "update"], check=True)
                subprocess.run(["sudo", "apt", "install", "-y", "nmap"], check=True)
            elif distribution in ["centos", "rhel", "fedora"]:
                subprocess.run(["sudo", "yum", "install", "-y", "nmap"], check=True)
            else:
                print(f"[ERROR] Unsupported Linux distribution: {distribution}. Please install nmap manually.")
        elif os_type == "Darwin":
            # Use Homebrew for macOS
            try:
                subprocess.run(["brew", "install", "nmap"], check=True)
            except FileNotFoundError:
                print("[ERROR] Homebrew is not installed. Please install Homebrew and try again.")
        elif os_type == "Windows":
            print("[INFO] Please download and install Nmap manually from https://nmap.org/download.html.")
        else:
            print(f"[ERROR] Unsupported operating system: {os_type}. Please install nmap manually.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")


# Call the function to check and install nmap
if __name__ == "__main__":
    check_and_install_nmap()
