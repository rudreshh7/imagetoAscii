﻿# ImagetoAscii

This Python script is designed to convert an image into ASCII art. Here's a breakdown of what each part of the code does:

1. **Imports**: The script imports necessary modules such as `sys`, `random`, `argparse`, `numpy`, `math`, and `PIL` (Python Imaging Library).

2. **Grayscale Levels**: Two strings, `gscale1` and `gscale2`, are defined. These strings contain characters that represent different levels of gray. `gscale1` has 70 levels of gray, while `gscale2` has 10 levels.

3. **getAverageL Function**: This function takes an image as input and calculates the average brightness level of the image.

4. **convertImagetoASCII Function**: This function takes an image file, the number of columns for the output ASCII art, a scale factor, and a boolean indicating whether to use more levels of gray. It opens the image, converts it to grayscale, and then divides it into small rectangular sections. Each section is replaced with an ASCII character that represents the average brightness of that section. The ASCII characters are chosen from `gscale1` or `gscale2`, depending on the `moreLevels` parameter.

5. **main Function**: This function handles command-line arguments, calls the `convertImagetoASCII` function to generate the ASCII art, and writes the ASCII art to an output file.

6. **Command-Line Arguments**: The script uses the `argparse` module to handle command-line arguments. The user can specify the input image file, the output file, the number of columns for the ASCII art, the scale factor, and whether to use more levels of gray.

7. **Execution**: If the script is run as the main program (not imported as a module), the `main` function is called. This is determined by the `if __name__ == '__main__':` line.

In summary, this script takes an image file as input and generates ASCII art based on the image's brightness levels. The user can customize the output by specifying command-line arguments.

and In terminal u can write  :

python "main.py" --file "11.jpg" --cols 120 --out "out.txt" 

