import sys
import os
from PIL import Image 

# Grab first and second argument
from_directory = sys.argv[1]
to_directory = sys.argv[2]


def convert_images():
	# Check if folder exists, if not create
	if not os.path.isdir(from_directory):
		print("Directoy doesn't exist")
		return

	if not os.path.isdir(to_directory):
		os.makedirs(to_directory)

	images_to_process = os.listdir(from_directory)
	print(images_to_process)

	for file in images_to_process:
		print(f'Converting {file} to PNG...')
		img = Image.open(f'{from_directory}{file}')
		if not img.format == 'JPEG':
			print("Not a JPG file")
			continue
		filename = os.path.splitext(file)[0]
		img.save(f'{to_directory}{filename}', 'png')

convert_images()

# Loop through folder
# Convert images to ping
# Save to the new folder