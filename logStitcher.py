import os
import collections
from PIL import Image
import math

target_dir = r"O:\Well Files Operated\Cline 1-14\Core\Pictures"
# target_dir = r"C:\Users\wnixon\Documents\GitHub\stitchLogImages\testImages"
out_folder = r"C:\Users\wnixon\Documents\GitHub\stitchLogImages"
chunk_size = 50
##FIGURE OUT A WAY TO DO THIS IN 50 PICTURE CHUNKS

for root, dirs, files in os.walk(target_dir):
	print('''Reading Files From:
				ROOT = {0}
				DIRS = {1}
				FILES = {2}'''.format(root, dirs, files))

images = {}
for item in files:
	print ("Item = {0}".format(item))
	filename, ext = os.path.splitext(os.path.basename(item))
	print("Filename = {0} Ext = {1}".format(filename, ext))
	if ext.lower() == ".jpg":
		filekey = int(filename.split('_')[1])
		images.setdefault(filekey, os.path.join(root,item))

orderedImages = collections.OrderedDict(sorted(images.items()))
	
number_of_chunks = int(math.ceil(len(files) / chunk_size))
print("Number of Chunks = {0}".format(number_of_chunks))

imageList = []
for v in orderedImages.values():
	imageList.append(v)

def chunks(l,n):
	for i in xrange(0, len(l), n):
		return [l[i:i+n] for i in range(0, len(l), n)]

chunked_list = chunks(imageList, chunk_size)
print(chunked_list)

i=0
for chunk in chunked_list:
	filename = "mergeLogImage{0}.png".format(i)
	out_file = os.path.join(out_folder, filename)
	i += 1

	ImgM = {"height": 0, "width": 0, "mode": ""}

	for item in chunk:
		print("ITEM = {0}".format(item))
		img = Image.open(item)
		ImgM['width'] += img.size[0]
		if img.size[1] > ImgM['height']:
			ImgM['height'] = img.size[1]
		ImgM['mode'] = img.mode
		# if ImgM['mode'] != img.mode:
			# print("ImgM['height'] = {0} != img.mode = {1}".format(ImgM['mode'],img.mode))
		del img
	
	bigIm = Image.new(ImgM['mode'], (ImgM['width'],ImgM['height']))

	upperLeftX = 0
	upperLeftY = 0

	for item2 in chunk:
		img2 = Image.open(item2)

		bigIm.paste(img2,(upperLeftX,upperLeftY))
		upperLeftX += img2.size[0]
		 
		del img2

	bigIm.save(out_file)
	print("{0} saved".format(out_file))
	del bigIm

