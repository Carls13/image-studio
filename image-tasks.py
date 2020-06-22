import sys
import os
from PIL import Image 

# Grab first and second argument
mode = sys.argv[1]
from_directory = sys.argv[2]
to_directory = sys.argv[3]


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


def compress_images():
	# Check if folder exists, if not create
	if not os.path.isdir(from_directory):
		print("Directoy doesn't exist")
		return

	if not os.path.isdir(to_directory):
		print("this")
		os.makedirs(to_directory)

	images_to_process = os.listdir(from_directory)
	print(images_to_process)

	for file in images_to_process:
		print(f'Compressing image {file}...')
		img = Image.open(f'{from_directory}{file}')
		if not img.format == 'JPEG':
			print("Not a JPG file")
			continue
		(width, height) = (img.width // 5, img.height // 5)
		img_resized = img.resize((width, height))
		filename, ext = os.path.splitext(file)
		img_resized.save(f'{to_directory}{file}')

if mode == 'compress':
	compress_images()
if mode.lower() == 'jpg-to-png':
	convert_images()
