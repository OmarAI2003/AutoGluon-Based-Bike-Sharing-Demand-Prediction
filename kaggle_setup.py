import os

# Define the path to the .kaggle directory in the user's home directory
kaggle_dir = os.path.join(os.getenv('USERPROFILE'), '.kaggle')

# Create the .kaggle directory
os.makedirs(kaggle_dir, exist_ok=True)

# Define the path to the kaggle.json file
kaggle_json_path = os.path.join(kaggle_dir, 'kaggle.json')

# Create an empty kaggle.json file
with open(kaggle_json_path, 'w') as f:
    pass

# Change the permissions of the kaggle.json file to read/write by the owner only
os.chmod(kaggle_json_path, 0o600)

# Fill in your user name and key from creating the kaggle account and API token file

import json

# Define your Kaggle username and API key
kaggle_username = "omarai23"
kaggle_key = "e7b12b21c4ae0a83bc0d3c1800c107e1"

# Define the path to the kaggle.json file
kaggle_json_path = os.path.join(os.getenv('USERPROFILE'), '.kaggle', 'kaggle.json')

# Save API token to the kaggle.json file
with open(kaggle_json_path, "w") as f:
    json.dump({"username": kaggle_username, "key": kaggle_key}, f)