import subprocess

# SSH connection details
hostname = "192.168.2.132"
port = 22  # Default SSH port
username = "tester"
password = "tester"
command = "hostnamectl"

ssh_command = ["sshpass", "-p", password, "ssh", f"{username}@{hostname}", command]
try:
    result = subprocess.run(ssh_command, capture_output=True, text=True, check=True)
    print(result.stdout)

except subprocess.CalledProcessError as e:
    print(f"SSH command failed with error: {e}")



