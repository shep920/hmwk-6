import time
from socket import *

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Set a timeout of 2 seconds
clientSocket.settimeout(2)

serverName = '127.0.0.1'
serverPort = 12000

for i in range(1, 11):
    # Current time for sending the packet
    sendTime = time.time()
    message = f"Ping {i} {sendTime}"
    
    try:
        # Send the UDP packet to the server
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        
        # Receive the server's response
        responseMessage, serverAddress = clientSocket.recvfrom(1024)
        
        # Calculate RTT
        rtt = time.time() - sendTime
        print(f"Received from server: {responseMessage.decode()}")
        print(f"RTT: {rtt:.6f} seconds")
    except timeout:
        # No response within 2 seconds
        print("Request timed out")

clientSocket.close()
