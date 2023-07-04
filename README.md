## Introduction
The `cut.py` and `together.py` scripts are designed to help you create collages from input images. The `cut.py` script allows you to cut an input image into smaller cropped images, while the `together.py` script combines those cropped images into a single collage image. These scripts utilize the Python Imaging Library (PIL) to handle image manipulation and processing.

## Requirements
- Python 3.x
- PIL (Python Imaging Library)

## Usage

### 1. Cutting the Input Image (cut.py)
1. Ensure that you have the required libraries installed. You can install PIL using pip:
   ```
   pip install pillow
   ```

2. Place the input image you want to cut in the same directory as the `cut.py` script. Ensure that the input image is in a supported format, such as PNG or JPEG.

3. Open the `cut.py` script in a text editor or IDE.

4. Modify the following variables in the script according to your needs:
   - `input_image_path`: Path to the input image file.
   - `output_width`: Width of the output cropped images in pixels.
   - `output_height`: Height of the output cropped images in pixels.
   - `output_dir`: Path to the output directory where the cropped images will be saved.

5. Save the modified script.

6. Run the script using Python:
   ```
   python cut.py
   ```

7. The script will cut the input image into smaller cropped images based on the specified width and height. The cropped images will be saved in the specified output directory. Each cropped image will be named in the format `row-column.png`, indicating its position in the original image.

### 2. Creating the Collage (together.py)
1. Ensure that you have the required libraries installed. You can install PIL using pip:
   ```
   pip install pillow
   ```

2. Place the cropped images you want to use for the collage in the `input` folder. Make sure the folder only contains the cropped images you wish to include.

3. Open the `together.py` script in a text editor or IDE.

4. Modify the following variables in the script according to your needs:
   - `output_width`: Width of the output collage image in pixels.
   - `output_height`: Height of the output collage image in pixels.
   - `resolution`: Resolution of the output collage image in dots per inch (DPI).
   - `rows`: Number of rows in the collage.
   - `columns`: Number of columns in the collage.

5. Save the modified script.

6. Place the desired hand-drawn data images in the `input` folder.

7. Run the script using Python:
   ```
   python together.py
   ```

8. The script will create the collage by combining the cropped images from the `input` folder and save it as multiple output images. Each output image will contain a portion of the collage. The output images will be named as `output_1.png`, `output_2.png`, and so on.

## Notes
- Both scripts assume that the input images are in PNG format. You can modify the scripts to support other image formats if needed.
- The `cut.py` script divides the input image into a grid based on the specified width and height of the output cropped images. The dimensions of the input image should be divisible by the output width and height to ensure equal-sized cropped images.
- The `together.py` script resizes the cropped images to fit into the output collage based on the specified number of rows and columns. The aspect ratio of the cropped images may be adjusted to fit the desired collage dimensions.
- The

 `together.py` script requires the cropped images to be placed in the `input` folder. Ensure that only the desired cropped images are present in the folder before running the script.
- The output images will be saved in the same directory as the script.
