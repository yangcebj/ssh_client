import paramiko

# SSH connection details
hostname = "192.168.2.132"
port = 22  # Default SSH port
username = "tester"
password = "tester"

# Create an SSH client
ssh_client = paramiko.SSHClient()

# Automatically add the server's host key (if not already known)
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the server
    ssh_client.connect(hostname, port, username, password)
    print(f"Connected to {hostname}")
    
    # Execute a command
    stdin, stdout, stderr = ssh_client.exec_command("hostnamectl")
    
    # Print the output
    print("Command output:")
    print(stdout.read().decode())  # Read and decode the output
    
    # Print errors if any
    error = stderr.read().decode()
    if error:
        print(f"Error: {error}")
except paramiko.AuthenticationException:
    print("Authentication failed, please verify your credentials")
except paramiko.SSHException as ssh_exception:
    print(f"Unable to establish SSH connection: {ssh_exception}")
except Exception as e:
    print(f"Exception occurred: {e}")
finally:
    # Close the connection
    ssh_client.close()
    print("Connection closed")