import subprocess

def run_powershell_command(command):
    """Runs a PowerShell command and returns the output."""
    try:
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def system_health_check():
    """Checks system health (CPU, memory)."""
    command = """
    Get-Process | Measure-Object -Property CPU -Sum;
    Get-WmiObject Win32_OperatingSystem | Select-Object @{Name="FreeMemory";Expression={[math]::Round($_.FreePhysicalMemory / 1MB, 2)}}
    """
    return run_powershell_command(command)

def disk_space_check():
    """Checks disk space usage."""
    command = "Get-PSDrive -PSProvider FileSystem | Select-Object Name,Used,Free"
    return run_powershell_command(command)

def network_connectivity():
    """Checks network connectivity."""
    command = "Test-Connection google.com -Count 2 | Select-Object Address,Status"
    return run_powershell_command(command)

def main():
    print("Windows System Troubleshooting Toolkit")
    print("-" * 40)
    print("1. Check System Health")
    print("2. Check Disk Space")
    print("3. Test Network Connectivity")
    print("4. Exit")
    
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
            print("Exiting Toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
