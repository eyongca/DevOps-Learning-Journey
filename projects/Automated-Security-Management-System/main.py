import json
from modules.ssh_manager import SSHManager
from modules.system_health import get_disk_usage, get_memory_usage, get_cpu_usage
from modules.vulnerability_scanner import run_nmap_scan
from modules.report_generator import save_to_log
from modules.nmap import check_and_install_nmap

def main():
    try:
        # Load server details
        with open("/home/devops/DevOps-Learning-Journey/projects/Automated-Security-Management-System/config/servers.json") as f:
            servers = json.load(f)

        # Loop through servers
        for server in servers:
            ssh = SSHManager(server['hostname'], server['username'], server['password'])
            try:
                ssh.connect()
                stdout, stderr = ssh.execute_command("uptime")
                save_to_log(f"Server {server['hostname']} uptime: {stdout}")
                print(f"[SUCCESS] SSH connected successfully to {server['hostname']}")
                save_to_log(f"[SUCCESS] SSH connected successfully to {server['hostname']}")

            except Exception as e:
                print(f"[ERROR] Error connecting to {server['hostname']}: {e}")
                save_to_log(f"[ERROR] Error connecting to {server['hostname']}: {e}")
            finally:
                ssh.close()

        # Local system health check
        disk = get_disk_usage()
        memory = get_memory_usage()
        cpu = get_cpu_usage()
        save_to_log(f"Disk Usage: {disk.percent}%, Memory Usage: {memory.percent}%, CPU Usage: {cpu}%")
        print(f"[SUCCESS] System health check completed successfully.")
        save_to_log("[SUCCESS] System health check completed successfully.")

        # Vulnerability scan
        scan_result = run_nmap_scan("127.0.0.1")
        save_to_log(f"Nmap Scan Result: {scan_result}")
        print(f"[SUCCESS] Vulnerability scan completed successfully.")
        save_to_log("[SUCCESS] Vulnerability scan completed successfully.")

        # Display final success message
        print("[SUCCESS] All tasks executed successfully.")
        save_to_log("[SUCCESS] All tasks executed successfully.")

    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
        save_to_log(f"[ERROR] An unexpected error occurred: {e}")

if __name__ == "__main__":
    check_and_install_nmap()
    main()
