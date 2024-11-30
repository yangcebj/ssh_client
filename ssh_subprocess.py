import subprocess

# SSH connection details
hostname = "192.168.2.132"
port = 22  # Default SSH port
username = "tester"
password = "tester"
command = "hostnamectl"  # Command to execute on the remote server

try:
    # Construct the SSH command
    ssh_command = ["ssh", f"{username}@{hostname}", command]
    
    # Execute the SSH command
    result = subprocess.run(ssh_command, capture_output=True, text=True, check=True)
    
    # Print the command output
    print("Command output:")
    print(result.stdout)
    
    # Print errors, if any
    if result.stderr:
        print(f"Error: {result.stderr}")

except subprocess.CalledProcessError as e:
    print(f"SSH command failed with error: {e}")