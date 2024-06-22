import os
import json

def setup_kaggle_api():
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

    # Define your Kaggle username and API key
    kaggle_username = os.environ.get('kaggle_username')
    kaggle_key = os.environ.get('kaggle_key')

    # Save API token to the kaggle.json file
    with open(kaggle_json_path, "w") as f:
        json.dump({"username": kaggle_username, "key": kaggle_key}, f)


setup_kaggle_api()