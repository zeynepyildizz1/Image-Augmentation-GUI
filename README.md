# Image Augmentation GUI

This is a Tkinter-based image augmentation tool that allows users to apply and fine-tune various augmentation filters using sliders. It utilizes the [Albumentations](https://albumentations.ai/) library for high-performance image transformations.

## ✨ Features

- Blur filter with adjustable kernel size
- Brightness and contrast adjustment
- Gaussian noise with variance, mean, and scale sliders
- CLAHE (Adaptive Histogram Equalization)
- Sharpen filter with alpha and lightness control
- Horizontal & vertical flips, channel shuffle, random 90° rotation
- Batch processing for a folder of images

## 🧰 Requirements

- Python 3.7+
- OpenCV (`opencv-python`)
- Albumentations
- Tkinter (comes with standard Python installation)

Install requirements:
```bash
pip install -r requirements.txt


## 🚀 Usage
Edit the path_to_augmant and path_to_save variables in slider.py to match your image input/output folders.

Run the script:

python slider.py

Use sliders to preview filters and apply them to all images in the folder.

