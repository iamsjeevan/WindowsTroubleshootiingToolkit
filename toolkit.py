import subprocess
import platform

def run_command(command):
    """Runs a command and returns the output."""
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def system_health_check():
    """Checks system health (CPU, memory)."""
    os_type = platform.system()
    if os_type == "Windows":
        command = """
        Get-Process | Measure-Object -Property CPU -Sum;
        Get-WmiObject Win32_OperatingSystem | Select-Object @{Name="FreeMemory";Expression={[math]::Round($_.FreePhysicalMemory / 1MB, 2)}}
        """
        return run_command(["powershell", "-Command", command])
    elif os_type == "Darwin":  # macOS
        command = """
        top -l 1 | grep "CPU usage";
        vm_stat | grep "free"
        """
        return run_command(["bash", "-c", command])
    else:
        return "Unsupported OS"

def disk_space_check():
    """Checks disk space usage."""
    os_type = platform.system()
    if os_type == "Windows":
        command = "Get-PSDrive -PSProvider FileSystem | Select-Object Name,Used,Free"
        return run_command(["powershell", "-Command", command])
    elif os_type == "Darwin":  # macOS
        command = "df -h | grep /dev/disk1"
        return run_command(["bash", "-c", command])
    else:
        return "Unsupported OS"

def network_connectivity():
    """Checks network connectivity."""
    os_type = platform.system()
    if os_type == "Windows":
        command = "Test-Connection google.com -Count 2 | Select-Object Address,Status"
        return run_command(["powershell", "-Command", command])
    elif os_type == "Darwin":  # macOS
        command = "ping -c 2 google.com"
        return run_command(["bash", "-c", command])
    else:
        return "Unsupported OS"

def disk_health_check():
    """Checks disk health (Windows and macOS)."""
    os_type = platform.system()
    if os_type == "Windows":
        command = "Get-WmiObject Win32_DiskDrive | Select-Object Model,Status"
        return run_command(["powershell", "-Command", command])
    elif os_type == "Darwin":  # macOS
        command = "diskutil verifyVolume /"
        return run_command(["bash", "-c", command])
    else:
        return "Unsupported OS"

def uptime_check():
    """Checks system uptime."""
    os_type = platform.system()
    if os_type == "Windows":
        command = "systeminfo | findstr /C:\"System Boot Time\""
        return run_command(["powershell", "-Command", command])
    elif os_type == "Darwin":  # macOS
        command = "uptime"
        return run_command(["bash", "-c", command])
    else:
        return "Unsupported OS"

def main():
    print("System Troubleshooting Toolkit")
    print("-" * 40)
    print("1. Check System Health")
    print("2. Check Disk Space")
    print("3. Test Network Connectivity")
    print("4. Check Disk Health")
    print("5. Check System Uptime")
    print("6. Exit")
    
    while True:
        choice = input("\nEnter your choice: ")
        if choice == '1':
            print("\nSystem Health Check:")
            print(system_health_check())
        elif choice == '2':
            print("\nDisk Space Usage:")
            print(disk_space_check())
        elif choice == '3':
            print("\nNetwork Connectivity:")
            print(network_connectivity())
        elif choice == '4':
            print("\nDisk Health Check:")
            print(disk_health_check())
        elif choice == '5':
            print("\nSystem Uptime:")
            print(uptime_check())
        elif choice == '6':
            print("Exiting Toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
