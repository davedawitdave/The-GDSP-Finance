import requests

# Set the API key
api_token = "YOUR_API_KEY"

# Set the endpoint and query parameters
endpoint = "https://api.worldtradingdata.com/api/v1/stock"
params = {
    "symbol": "AAPL",
    "api_token": api_token
}

# Make the API request
response = requests.get(endpoint, params=params)

# Get the JSON data from the response
data = response.json()

# Print the data
print(data)