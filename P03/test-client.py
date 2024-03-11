from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# Parameters of the server to talk to
IP = "127.0.0.1"  # your IP address
PORT = 8080

# Create a client object
c = Client(IP, PORT)

# Test the ping method
print("* Testing PING...")
response = c.talk("PING")
print(response)

# Test the get method
print("\n* Testing GET...")
for i in range(5):
    response_get = c.talk(f"GET {i}")
    print(f"GET {i}:", response_get)
    if i == 0:
        sequence_get_0 = response_get


# Test the INFO method using the sequence obtained from GET 0
print("\n* Testing INFO...")
response_info = c.talk(f"INFO {sequence_get_0}")
print(response_info)

# Test the COMP method using the sequence obtained from GET 0
print("\n* Testing COMP...")
response_comp = c.talk(f"COMP {sequence_get_0}")
print(response_comp)

# Test the REV method using the sequence obtained from GET 0
print("\n* Testing REV...")
response_rev = c.talk(f"REV {sequence_get_0}")
print(response_rev)
