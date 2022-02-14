# What does this do ?

This tool converts Noritsu RAWs to linear tiffs to make them easier to use.

# How to use it ?

1. Install Python >= 3.6 and make sure it is added to your PATH during installation
2. Install Imagemagick, make sure to tick the box to install legacy tools during installation
3. Restart your computer
4. Create a folder named "raws" in the same folder as the convert_raws.py and sizes.py files
5. Bring your raw files to the "raws" folder
6. Execute the convert_raws.py script
7. The script will guess the image size and output a linear tiff from the raw file in the "raws" folder, with the ".tiff" extension

# My images look striped, or weird

As Noritsu RAWs do not contain information about the dimensions of the image, the script tries to guess it from the number of pixels (known from the file size). It will try to find a height and a width that matches the number of pixels and will use the closest height/width pair to avoid ridiculous aspect ratios (eg a 3000x2000px image is more likely than 200x60000px).

The script looks for a list of known filesizes/image dimensions in the sizes.py file before trying to guess. This works, as RAWs are uncompressed so images from the same canal and scan settings will always have the same weight. If your files end up looking weird, you should add an entry into this file with your image size (in bits), and its expected dimensions. The script uses the psheight and pswidth parameters for image dimensions. 

The raw files are slightly wider and taller than Noritsu-converted images so it is not possible to use these to guess the raw dimensions.

# The converted images are very dark

That's the way they are. I guess Noritsu does that to prevent clipping.

# Can I get support for this tool ?

You can contact me at    *a d r i e n v e a u @ gmail com* for (paid) support for this tool. I will happily modify it to suit your files, and can create an executable for easier use. It can also be made to work with a simple drag and drop of the folder that contains the images. The code shared here is the quick and dirty thing that worked for my use, it is not really anything final.