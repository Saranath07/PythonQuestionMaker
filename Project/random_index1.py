import requests

# Define the Piston API endpoint
url = "https://emkc.org/api/v2/piston/execute"

# Define the code to be executed
code = """
def add(a, b):
    return a + b

if __name__ == "__main__":
    import sys
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    # Capture the function return value and print it
    print(add(a, b))
"""

# Define the function parameters
params = [3, 5]

# Define the payload
payload = {
    "language": "python",
    "version": "3.10.0",
    "files": [
        {
            "name": "main.py",
            "content": code
        }
    ],
    "args": [str(param) for param in params]
}

# Send the request to the Piston API
response = requests.post(url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    result = response.json()
    # Extract the result value from the output
    output = result["run"]["output"]
    # Strip any leading/trailing whitespace
    output = output.strip()
    print("Output:", output)
else:
    print("Failed to execute code:", response.text)
