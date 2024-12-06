
# Windows System Troubleshooting Toolkit

This toolkit, built using Python and PowerShell, provides a convenient way to streamline system diagnostics and resolve common Windows system issues. It leverages the power of PowerShell commands and Python's simplicity to create a command-line interface for performing key troubleshooting tasks.

## Features

- **System Health Check**:
  - Monitors CPU usage and free physical memory.

- **Disk Space Check**:
  - Displays used and free space for all drives on the system.

- **Network Connectivity Test**:
  - Tests internet connectivity by pinging a reliable external server.

## Requirements

1. **Python** (3.7 or later)
2. **PowerShell** (Windows built-in tool)
3. **Git** (for version control, optional)

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/windows-toolkit.git
   cd windows-toolkit
   ```

2. Run the script directly using Python:
   ```bash
   python toolkit.py
   ```

## Usage

1. Run the script and choose an option from the menu:
   - Option 1: Check system health.
   - Option 2: View disk space usage.
   - Option 3: Test network connectivity.
   - Option 4: Exit the program.

2. Follow the on-screen prompts for results.

## Example Output

```plaintext
Windows System Troubleshooting Toolkit
----------------------------------------
1. Check System Health
2. Check Disk Space
3. Test Network Connectivity
4. Exit

Enter your choice: 1

System Health Check:
CPU Usage: 23%
Free Memory: 4.5 GB
```

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the toolkit.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- [Python](https://www.python.org/)
- [PowerShell](https://docs.microsoft.com/en-us/powershell/)

---

Happy troubleshooting!
