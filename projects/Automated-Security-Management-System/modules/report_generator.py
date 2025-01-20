from datetime import datetime

def save_to_log(content, log_file="/home/devops/DevOps-Learning-Journey/projects/Automated-Security-Management-System/logs/scan_logs.txt"):
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - {content}\n")
