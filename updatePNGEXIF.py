##----------------------------------------------------------------------------------------
##  Update PNG File EXIF
##----------------------------------------------------------------------------------------
##  Platform: Python 3, Pillow
##  Copyright Pacess Studio, 2020.  All rights reserved.
##----------------------------------------------------------------------------------------

from PIL.PngImagePlugin import PngInfo
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import glob, os

##----------------------------------------------------------------------------------------
print("\n-----------------------------------------");
print("--  Update PNG File EXIF Version 1.00  --")
print("-----------------------------------------\n");

##----------------------------------------------------------------------------------------
##  Prepare new meta data
_meta = PngInfo()
_meta.add_text("Make", "UGFjZXNzIFN0dWRpbw==")
_meta.add_text("MakerNote", "Friends only")

##----------------------------------------------------------------------------------------
for sourceFile in glob.glob("*.png"):
	
	print("Processing "+sourceFile+"...")
	
	##  Load image	
	image = Image.open(sourceFile)

	##  Remove existing
	data = list(image.getdata())
	cleanImage = Image.new(image.mode, image.size)
	cleanImage.putdata(data)

	##  Save it back	
	cleanImage.save(sourceFile, pnginfo=_meta)

print("Done!")
