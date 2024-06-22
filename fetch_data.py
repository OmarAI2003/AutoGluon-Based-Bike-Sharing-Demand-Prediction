import subprocess
import zipfile
import os




def fetch_data():
    # Command to download the dataset using Kaggle API
    download_command = "kaggle competitions download -c bike-sharing-demand"

    # Run the command to download the dataset
    process = subprocess.Popen(download_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Print the output and error messages for the download command
    if output:
        print("Output:", output.decode("utf-8"))
    if error:
        print("Error:", error.decode("utf-8"))

    # Unzip the downloaded file
    zip_file = "bike-sharing-demand.zip"
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(".")


    train = pd.read_csv('train.csv')
    test = pd.read_csv('test.csv')
    submission = pd.read_csv('test.csv')

    return train, test, submission

if __name__ == "__main__":
    fetch_data()
