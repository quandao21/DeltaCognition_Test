import gdown
import zipfile
import os

# Model's link
gdrive_link = 'https://drive.google.com/uc?id=10mPON4aVF_KBW9hdKrSerpx0Q0rSDqjA&export=download'

# Local file name
local_file_name = './saved_models/downloaded_model.zip'

# Download the file
gdown.download(gdrive_link, local_file_name, quiet=False)

print(f'File "{local_file_name}" has been downloaded.')


with zipfile.ZipFile(local_file_name, 'r') as zip_ref:
    # Extract all the contents to the specified directory
    zip_ref.extractall('./saved_models/model_ver1')

print(f'Contents of "{local_file_name}" have been extracted.')

# Delete the zip file
os.remove(local_file_name)

print(f'File "{local_file_name}" has been deleted.')