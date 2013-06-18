import os
import collections
from PIL import Image

target_dir = r"O:\Well Files Operated\Cline 1-14\Core\Pictures"

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

print(images)

orderedImages = collections.OrderedDict(sorted(images.items()))

ImgM = {"height": 0, "width": 0, "mode": ""}

for key, item in orderedImages.iteritems():
	print("KEY = {0} : ITEM = {1} ".format(key, item))
	img = Image.open(item)
	ImgM['width'] += img.size[0]
	if img.size[1] > ImgM['height']:
		ImgM['height'] = img.size[1]

print ImgM