import os  # Importing os module for directory and file operations
import csv  # Importing csv module for reading CSV files
import requests  # Importing requests module for making HTTP requests

def download_images_from_csv(csv_file, save_directory):
    # Create the save directory if it doesn't exist
    os.makedirs(save_directory, exist_ok=True)

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader) # Skip header row
        for row in reader:
            # Assuming the URL is in the last column of each row
            image_url = row[-1]
            print(image_url)
            # Extract the filename from the URL
            filename = image_url.split('/')[-1]
            # Download the image
            response = requests.get(image_url)
            if response.status_code == 200:
                # Save the image locally
                with open(os.path.join(save_directory, filename), 'wb') as img_file:
                    img_file.write(response.content)
                print(f"Downloaded: {filename}")
            else:
                print(f"Failed to download: {filename}")

# Example usage
csv_file = 'faculty.csv'
save_directory = 'downloaded_images'
download_images_from_csv(csv_file, save_directory)
