"""
System Management Utility Script

Author: Eyong Christopher

This script provides a set of utilities for system management tasks, 
including disk space checks, directory listing, file copying, 
directory archiving, and running shell commands.

Usage Examples:
-----------------
1. Check disk space:
   python system_management.py --disk

2. List directory contents:
   python system_management.py --list /path/to/directory

3. Copy a file:
   python system_management.py --copy source.txt destination.txt

4. Create a directory archive:
   python system_management.py --archive /path/to/source /path/to/archive

5. Run a shell command:
   python system_management.py --command ls -la
"""

import os
import subprocess
import shutil
import argparse


def check_disk_space():
    """Check disk space usage."""
    print("\nChecking disk space...")
    subprocess.run(["df", "-h"], check=True)


def list_directory_contents(directory):
    """List the contents of a directory."""
    print(f"\nContents of directory: {directory}")
    for item in os.listdir(directory):
        print(item)


def copy_file(source, destination):
    """Copy a file to a new location."""
    print(f"\nCopying {source} to {destination}...")
    shutil.copy(source, destination)
    print("File copied successfully.")


def create_archive(source, destination):
    """Create an archive of a directory."""
    print(f"\nCreating an archive of {source} at {destination}...")
    shutil.make_archive(destination, 'zip', source)
    print("Archive created successfully.")


def run_command(command):
    """Run a shell command and capture output."""
    print(f"\nRunning command: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)
    print(f"Output:\n{result.stdout}")
    if result.stderr:
        print(f"Errors:\n{result.stderr}")


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="System Management Utility")
    parser.add_argument("--disk", action="store_true", help="Check disk space")
    parser.add_argument("--list", type=str, help="List directory contents")
    parser.add_argument("--copy", nargs=2, metavar=('source', 'destination'), help="Copy a file")
    parser.add_argument("--archive", nargs=2, metavar=('source', 'destination'), help="Create a directory archive")
    parser.add_argument("--command", nargs='+', help="Run a shell command")
    return parser.parse_args()


def main():
    """Main function to handle user requests."""
    args = parse_arguments()

    if args.disk:
        check_disk_space()
    if args.list:
        list_directory_contents(args.list)
    if args.copy:
        copy_file(args.copy[0], args.copy[1])
    if args.archive:
        create_archive(args.archive[0], args.archive[1])
    if args.command:
        run_command(args.command)


if __name__ == "__main__":
    main()