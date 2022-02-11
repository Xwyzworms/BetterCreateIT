#%%
from fpdf import FPDF
from PIL import Image
from typing import List 
import os

# %%
PDF : FPDF = FPDF()
images : List = []


folderLocation : str = "" #/* Enter the folder location here */
nameOfPdf : str = "" #/* Enter the name of the pdf here */

def getTheImages(folderLocation: str, nameOfPdf) -> List :
	for directoryPath, directoryNames, filenames in os.walk(folderLocation):
		for filename in [file for file in filenames if file.endswith(".jpg")]:
			full_path : str = os.path.join(directoryPath, filename)
			images.append(full_path)
	images.sort()
	print("Here's what I found:")
	for i in range(len(images)):
		print(images[i])

	return images


# Rotating Image if the image is landscape
def checkImage():
	pass

def rotateImage():
	pass
# %%
