# **Capstone Project: Automated Security Management System**

As the capstone project for my Python scripting course, I will design and implement an **Automated Security Management System**. This project will demonstrate my ability to use Python to automate security tasks and routine system management processes. The project addresses real-world challenges in IT and DevOps environments, providing a secure, efficient, and scalable solution.

I will also document the challenges encountered during development and the strategies employed to overcome them, showcasing problem-solving and critical thinking skills.

---

## **Project Objectives**
1. **Automation**: Simplify and automate routine security and system tasks.
2. **Scalability**: Manage multiple servers efficiently.
3. **Security**: Detect vulnerabilities and monitor critical resources.
4. **Documentation**: Highlight challenges and solutions during development.

---

## **Project Features**
1. **Remote Server Management**:
   - Automate tasks on remote servers using SSH with `paramiko`.
   - Execute commands, retrieve logs, and perform remote scans.

2. **File Integrity Monitoring**:
   - Ensure the integrity of critical files using cryptographic hashing from the `cryptography` module.
   - Detect and log unauthorized file modifications.

3. **System Health Monitoring**:
   - Monitor disk space, memory usage, and CPU performance using `os` and `psutil`.
   - Generate alerts for resource anomalies.

4. **Vulnerability Scanning**:
   - Integrate tools like `nmap` via `subprocess` to identify potential security vulnerabilities.
   - Optionally incorporate other tools like `nikto` for additional scanning capabilities.

5. **Report and Log Generation**:
   - Log scan results and system health data to a centralized file.
   - Generate actionable reports and send email notifications for critical events.

6. **Task Scheduling**:
   - Automate periodic task execution using Python's `schedule` module or cron jobs.

---

## **Requirements**

### **1. Software Requirements**
- **Python**: Version 3.8 or later.
- **Python Modules**:
  - `os` - For file and system-level operations.
  - `subprocess` - To execute external commands and tools.
  - `paramiko` - For managing SSH connections.
  - `cryptography` - For hashing and encryption.
  - `psutil` - For monitoring system resources.
  - `schedule` - For task scheduling.
  - `json` and `yaml` - For configuration file management.

### **2. External Tools**
- **nmap**: A network scanning tool for identifying vulnerabilities.
- **Optional**: Additional tools like `nikto` or `OpenVAS` for expanded scanning capabilities.

### **3. Hardware Requirements**
- A system with adequate resources to run scans and store logs.
- Access to remote servers for testing and management.

### **4. Configuration Files**
- **servers.json**: Contains details for remote server connections.


## **5. Security Measures**
- Encrypt sensitive data like credentials using the `cryptography` module.
- Apply strict file permissions to configuration files and logs.


## **Challenges and Solutions**

### **Challenge 1: Managing SSH Connections Securely**
- **Problem**: Handling server credentials securely while ensuring seamless automation.  
- **Solution**: Use the `cryptography` module to encrypt and decrypt sensitive data. Store encrypted credentials in configuration files and decrypt them at runtime.

### **Challenge 2: Handling Large Log Files**
- **Problem**: Logs can grow large, impacting performance and storage.  
- **Solution**: Implement log rotation using Python's `logging.handlers` module to archive older logs and limit file sizes.

### **Challenge 3: Ensuring Cross-Platform Compatibility**
- **Problem**: Certain tools or commands may behave differently across operating systems.  
- **Solution**: Use Python's `platform` module to detect the OS and adapt commands accordingly.

### **Challenge 4: Vulnerability Scanner Integration**
- **Problem**: Integrating external tools like `nmap` requires error handling and proper installation.  
- **Solution**: Validate tool availability using `subprocess.run` before executing scans and provide user-friendly error messages.

### **Challenge 5: Scheduling Tasks Reliably**
- **Problem**: Ensuring tasks run at the correct intervals, even if the script is not running continuously.  
- **Solution**: Combine Python's `schedule` module for in-session task scheduling with system-level schedulers like cron for persistent automation.

---

## **Expected Outcomes**
1. A fully functional Python project that automates security tasks and routine management.
2. A comprehensive report documenting challenges and solutions encountered during the project.
3. Enhanced skills in Python scripting, automation, and troubleshooting.

---

## **Directory Structure**


automated_security/
├── main.py
├── modules/
│   ├── ssh_manager.py
│   ├── file_integrity.py
│   ├── system_health.py
│   ├── vulnerability_scanner.py
│   └── report_generator.py
├── config/
│   ├── servers.json
│   └── settings.yaml
└── logs/
    └── scan_logs.txt
