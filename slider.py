
import albumentations as A
import cv2
import os
import tkinter as tk

blur_limit=1
brightness_limit=0.0
contrast_limit=0.0
gauss_variance=0.0
gauss_mean=0.0
gauss_scale=0.1
clip_limit=1.0
grid_limit=1
alpha_limit=0.0
lightness_limit=0.1


image = cv2.imread("example.png") #example image to show filters

path_to_save = 'path/to/save'
isExist = os.path.exists(path_to_save)
if not isExist:

   # Create a new directory because it does not exist
   os.makedirs(path_to_save)

path_to_augmant='path/to/augmant'

# slider for deciding to blur value
def update_label(value):
    # Convert value to integer if necessary
    value = int(value)
    if value % 2 == 0:
        value += 1
    label.config(text=f"Slider Value: {value}")
    blr_img=blur(image, value)
    cv2.imshow("blur_image", blr_img)
    cv2.waitKey(3)
    global blur_limit
    blur_limit=value

def set_blur():
    global blur_limit
    # Record the current slider value in the recorded_blur_limit
    recorded_blur_limit = int(slider.get())
    if recorded_blur_limit % 2 == 0:
        recorded_blur_limit += 1
    print(f"Blur limit recorded: {recorded_blur_limit}")


def blur(image, blur_lmt):
    transform = A.Compose([
        A.Blur(blur_limit=(blur_lmt,blur_lmt), p=1.0), ])
    transformed = transform(image=image)
    blur_image = transformed["image"]
    return blur_image

# Create the main window
root = tk.Tk()
root.title("Tkinter Slider Example")

# Create a label to display the slider value
label = tk.Label(root, text="Slider Value: 1")
label.pack(pady=10)

# Create a slider (Scale widget)
slider = tk.Scale(root, from_=1, to=100, orient="horizontal", length=600, command=update_label)
slider.pack(pady=10)
tk.Button(root, text='Set the value', command=set_blur).pack()

# Run the application
root.mainloop()
cv2.destroyAllWindows()


#slider for contrast and brighnetss
def update_bright(value):
    value =float(value)
    brightness_label.config(text=f"Slider Value: {value}")
    global brightness_limit 
    brightness_limit=value
    img=filter_try()
    cv2.imshow("bright_image", img)
    cv2.waitKey(3)

def update_contrast(value):
    value =float(value)
    contrast_label.config(text=f"Slider Value: {value}")
    global contrast_limit 
    contrast_limit=value
    img=filter_try()
    cv2.imshow("bright_image", img)
    cv2.waitKey(3)

def filter_try():
    global brightness_limit
    global contrast_limit
    return brightness(image, brightness_limit, contrast_limit)


def set_brightness_contrast():
    global brightness_limit
    global contrast_limit
    recorded_brightness_limit = float(brightness_slider.get())
    recorded_contrast_limit = float(contrast_slider.get())
    print(f"Brightness limit recorded: {recorded_brightness_limit:.1f}")
    print(f"Contrast limit recorded: {recorded_contrast_limit:.1f}")

def brightness(image,brightness,contrast):
    transform = A.Compose([
        A.RandomBrightnessContrast(brightness_limit=(brightness, brightness), contrast_limit=(contrast, contrast) ,p=1.0),])
    transformed = transform(image=image)
    bright_image = transformed["image"]
    return bright_image


# Create the main window
root = tk.Tk()
root.title("Brightness and Contrast Slider")

# Create a label to display the slider value
brightness_label = tk.Label(root, text="Brightness Value: 0.0")
brightness_label.pack(pady=10)

# Create a slider (Scale widget)
brightness_slider = tk.Scale(root, from_=-1.0, to=1.0, resolution=0.1, orient="horizontal", length=600, command=update_bright)
brightness_slider.pack(pady=10)

contrast_label = tk.Label(root, text="Contrast Value: 0.0")
contrast_label.pack(pady=10)

contrast_slider = tk.Scale(root, from_=-1.0, to=1.0, resolution=0.1, orient="horizontal", length=600, command=update_contrast)
contrast_slider.pack(pady=10)

tk.Button(root, text='Record Brightness and Contrast Limits', command=set_brightness_contrast).pack(pady=10)

# Run the application
root.mainloop()

# Close OpenCV windows when Tkinter application is closed
cv2.destroyAllWindows()



#slider for gauss noise 

def update_variance(value):
    value =float(value)
    variance_label.config(text=f"Slider Value: {value}")
    global gauss_variance
    gauss_variance=value
    img=filter_try_gauss()
    cv2.imshow("gauss_noise_image", img)
    cv2.waitKey(3)

def update_mean(value):
    value =float(value)
    mean_label.config(text=f"Slider Value: {value}")
    global gauss_mean 
    gauss_mean=value
    img=filter_try_gauss()
    cv2.imshow("gauss_noise_image", img)
    cv2.waitKey(3)

def update_scale(value):
    value =float(value)
    scale_label.config(text=f"Slider Value: {value}")
    global gauss_scale 
    gauss_scale=value
    img=filter_try_gauss()
    cv2.imshow("gauss_noise_image", img)
    cv2.waitKey(3)


def filter_try_gauss():
    global gauss_variance
    global gauss_mean
    global gauss_scale
    return gauss_noise(image, gauss_variance, gauss_mean, gauss_scale)


def set_values():
    global gauss_variance
    global gauss_mean
    global gauss_scale
    recorded_variance = float(variance_slider.get())
    recorded_mean = float(mean_slider.get())
    recorded_scale=float(scale_slider.get())
    print(f"Brightness limit recorded: {recorded_variance:.1f}")
    print(f"Contrast limit recorded: {recorded_mean:.1f}")
    print(f"Contrast limit recorded: {recorded_scale:.1f}")

def gauss_noise(image, var, mean, scale):
    transform = A.Compose([
        A.GaussNoise(var_limit=(var, var),  mean=mean,  per_channel=False, #var_limit=Variance range for noise 
                    noise_scale_factor=scale, p=1.0 ),])
    transformed = transform(image=image)
    gauss_noise_image = transformed["image"]
    return gauss_noise_image


# Create the main window
root = tk.Tk()
root.title("Gauss Noise Slider")

# Create a label to display the slider value
variance_label = tk.Label(root, text="Variance Value: 0.0")
variance_label.pack(pady=10)

# Create a slider (Scale widget)
variance_slider = tk.Scale(root, from_=0.0, to=100.0, resolution=0.1, orient="horizontal", length=600, command=update_variance)
variance_slider.pack(pady=10)

mean_label = tk.Label(root, text="Mean Value: 0.0")
mean_label.pack(pady=10)

mean_slider = tk.Scale(root, from_=0.0, to=100.0, resolution=0.1, orient="horizontal", length=600, command=update_mean)
mean_slider.pack(pady=10)

scale_label = tk.Label(root, text="Scale Value: 0.0")
scale_label.pack(pady=10)

scale_slider = tk.Scale(root, from_=0.1, to=1.0, resolution=0.1, orient="horizontal", length=600, command=update_scale)
scale_slider.pack(pady=10)

tk.Button(root, text='Record Values', command=set_values).pack(pady=10)

# Run the application
root.mainloop()

# Close OpenCV windows when Tkinter application is closed
cv2.destroyAllWindows()

#slider for Clahe

def update_clip(value):
    value =float(value)
    clip_label.config(text=f"Slider Value: {value}")
    global clip_limit 
    clip_limit=value
    img=filter_clahe()
    cv2.imshow("clahe_image", img)
    cv2.waitKey(3)

def update_grid(value):
    value =int(value)
    grid_label.config(text=f"Slider Value: {value}")
    global grid_limit 
    grid_limit=value
    img=filter_clahe()
    cv2.imshow("clahe_image", img)
    cv2.waitKey(3)

def filter_clahe():
    global clip_limit
    global grid_limit
    return clahe(image, clip_limit, grid_limit)


def set_clip_grid():
    global clip_limit
    global grid_limit
    recorded_clip_limit = float(clip_slider.get())
    recorded_grid_limit = float(grid_slider.get())
    print(f"Clip limit recorded: {recorded_clip_limit:.1f}")
    print(f"Grid limit recorded: {recorded_grid_limit:.1f}")


def clahe(image, clip_limit, grid_limit):
    transform = A.Compose([
        A.CLAHE(
            clip_limit=(clip_limit,clip_limit),  # ScaleFloatType
            tile_grid_size=(grid_limit, grid_limit),  # tuple[int, int]
            always_apply=None,  # bool | None
            p=1.0,  # float
        ),])
    transformed = transform(image=image)
    clahe_image = transformed["image"]
    return clahe_image


# Create the main window
root = tk.Tk()
root.title("Clahe Filter Slider")

# Create a label to display the slider value
clip_label = tk.Label(root, text="Clip Value: 0.0")
clip_label.pack(pady=10)

# Create a slider (Scale widget)
clip_slider = tk.Scale(root, from_=1.0, to=100.0, resolution=0.1, orient="horizontal", length=600, command=update_clip)
clip_slider.pack(pady=10)

grid_label = tk.Label(root, text="Grid Value: 0")
grid_label.pack(pady=10)

grid_slider = tk.Scale(root, from_=1, to=100,  orient="horizontal", length=600, command=update_grid)
grid_slider.pack(pady=10)

tk.Button(root, text='Record Clip and Grid Limits', command=set_clip_grid).pack(pady=10)


# Run the application
root.mainloop()
cv2.destroyAllWindows()

# slider for sharpen filter

def update_alpha(value):
    # Convert value to integer if necessary
    value =float(value)
    alpha_label.config(text=f"Slider Value: {value}")
    # Use the slider value in your function here
    global alpha_limit 
    alpha_limit=value
    img=filter_sharpen()
    cv2.imshow("sharpen_image", img)
    cv2.waitKey(3)


def update_lightness(value):
    # Convert value to integer if necessary
    value =float(value)
    lightness_label.config(text=f"Slider Value: {value}")
    # Use the slider value in your function here
    global lightness_limit 
    lightness_limit=value
    img=filter_sharpen()
    cv2.imshow("sharpen_image", img)
    cv2.waitKey(3)

def filter_sharpen():
    global alpha_limit
    global lightness_limit
    return sharpen(image, alpha_limit, lightness_limit)


def set_sharpen():
    global alpha_limit
    global lightness_limit
    recorded_alpha_limit = float(alpha_slider.get())
    recorded_lightness_limit = float(lightness_slider.get())
    print(f"Clip limit recorded: {recorded_alpha_limit:.1f}")
    print(f"Grid limit recorded: {recorded_lightness_limit:.1f}")


def sharpen(image, alpha, light):
    transform = A.Compose([
        A.Sharpen(
            alpha=(alpha, alpha),  # tuple[float, float]
            lightness=(light, light),  # tuple[float, float]
            always_apply=None,  # bool | None
            p=1.0,  # float
        )
        ])
    transformed = transform(image=image)
    sharpen_image = transformed["image"]
    return sharpen_image

# Create the main window
root = tk.Tk()
root.title("Sharpen Filter Slider")

# Create a label to display the slider value
alpha_label = tk.Label(root, text="Alpha Value: 0.0")
alpha_label.pack(pady=10)

# Create a slider (Scale widget)
alpha_slider = tk.Scale(root, from_=0.0, to=1.0, resolution=0.1, orient="horizontal", length=600, command=update_alpha)
alpha_slider.pack(pady=10)

lightness_label = tk.Label(root, text="Lightness Value: 0")
lightness_label.pack(pady=10)

lightness_slider = tk.Scale(root, from_=0.1, to=100.0, resolution=0.1,   orient="horizontal", length=600, command=update_lightness)
lightness_slider.pack(pady=10)

tk.Button(root, text='Record Sharpen Limits', command=set_sharpen).pack(pady=10)

# Create a button to apply the recorded brightness and contrast limits
#tk.Button(root, text='Apply Recorded Brightness & Contrast', command=apply_brightness_contrast).pack(pady=10)

# Run the application
root.mainloop()
cv2.destroyAllWindows()


def horizontal(image):
    transform = A.Compose([
        A.HorizontalFlip(p=1.0),])
    transformed = transform(image=image)
    horizontal_image = transformed["image"]
    return horizontal_image

def channel_shuffel(image):
    transform = A.Compose([
        A.ChannelShuffle(p=1.0),])
    transformed = transform(image=image)
    channel_shuffel_image = transformed["image"]
    return channel_shuffel_image


def vertical_flip(image):
    transform = A.Compose([
        A.VerticalFlip(p=1.0), ])
    transformed = transform(image=image)
    vertical_flip_image = transformed["image"]
    return vertical_flip_image

def random_rotate90(image):
    transform = A.Compose([
        A.RandomRotate90(p=1.0) ,])
    transformed = transform(image=image)
    random_rotate90_image = transformed["image"]
    return random_rotate90_image


# Get a list of all files in the folder
files = os.listdir(path_to_augmant)


# Loop through all files
for file_name in files:
    print(file_name[:-4])

    # Build the full file path
    file_path = os.path.join(path_to_augmant, file_name)
    image = cv2.imread(file_path)
    horizontal_img=horizontal(image)
    cv2.imwrite(os.path.join(path_to_save , f"horizontal_{file_name[:-4]}.png"), horizontal_img)
    blur_img=blur(image, blur_limit)
    cv2.imwrite(os.path.join(path_to_save , f"blur_{file_name[:-4]}.png"), blur_img)
    brightness_img=brightness(image,brightness_limit,contrast_limit)
    cv2.imwrite(os.path.join(path_to_save , f"bright_{file_name[:-4]}.png"), brightness_img)
    chanel_img=channel_shuffel(image)
    cv2.imwrite(os.path.join(path_to_save , f"chanel_shuffel_{file_name[:-4]}.png"), chanel_img)
    vertical_img= vertical_flip(image)
    cv2.imwrite(os.path.join(path_to_save , f"vertical_{file_name[:-4]}.png"), vertical_img)
    rotate_img=random_rotate90(image)
    cv2.imwrite(os.path.join(path_to_save , f"rotate_{file_name[:-4]}.png"), rotate_img)
    gauss_img=gauss_noise(image, gauss_variance, gauss_mean, gauss_scale)
    cv2.imwrite(os.path.join(path_to_save , f"gauss_{file_name[:-4]}.png"), gauss_img)
    clahe_img=clahe(image,clip_limit,grid_limit)
    cv2.imwrite(os.path.join(path_to_save , f"clahe_{file_name[:-4]}.png"), clahe_img)
    sharpen_img =sharpen(image, alpha_limit, lightness_limit)
    cv2.imwrite(os.path.join(path_to_save , f"sharpen_{file_name[:-4]}.png"), sharpen_img)