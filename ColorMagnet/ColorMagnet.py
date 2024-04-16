import cv2
import numpy as np
import webcolors
import tkinter as tk
from PIL import Image, ImageTk

# A dictionary of color names and their RGB values
color_names_rgb = {
    "black": (0, 0, 0),
    "blue": (0, 0, 255),
    "red": (255, 0, 0),
    "white": (255, 255, 255),
    "yellow": (255, 255, 0),
    "green": (0, 128, 0),
    "orange": (255, 165, 0),
    "pink": (255, 192, 203),
    "purple": (128, 0, 128),
    "brown": (139, 69, 19),
    "gray": (128, 128, 128),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "navy": (0, 0, 128),
    "olive": (128, 128, 0),
    "teal": (0, 128, 128),
    "lime": (0, 255, 0),
    "maroon": (128, 0, 0),
    "silver": (192, 192, 192),
    "gold": (255, 215, 0),
    "turquoise": (64, 224, 208),
    "lavender": (230, 230, 250),
    "salmon": (250, 128, 114),
    "indigo": (75, 0, 130),
    "violet": (238, 130, 238),
    "peru": (205, 133, 63),
    "coral": (255, 127, 80),
    "crimson": (220, 20, 60),
    "firebrick": (178, 34, 34),
    "forestgreen": (34, 139, 34),
    "darkorchid": (153, 50, 204),
    "deepskyblue": (0, 191, 255),
    "goldenrod": (218, 165, 32),
    "indianred": (205, 92, 92),
    "khaki": (240, 230, 140),
    "lightcoral": (240, 128, 128),
    "mediumseagreen": (60, 179, 113),
    "orangered": (255, 69, 0),
    "rosybrown": (188, 143, 143),
    "sienna": (160, 82, 45),
    "slateblue": (106, 90, 205),
    "tomato": (255, 99, 71),
    "wheat": (245, 222, 179),
    "darkgreen": (0, 100, 0),
    "darkred": (139, 0, 0),
    "darksalmon": (233, 150, 122),
    "deeppink": (255, 20, 147),
    "dodgerblue": (30, 144, 255),
    "darkviolet": (148, 0, 211),
    "olivedrab": (107, 142, 35),
    "slategray": (112, 128, 144),
    "orchid": (218, 112, 214),
    "powderblue": (176, 224, 230),
    "salmon": (250, 128, 114),
    "lightgreen": (144, 238, 144),
    "darkorange": (255, 140, 0),
    "mediumblue": (0, 0, 205),
    "lightpink": (255, 182, 193),
    "saddlebrown": (139, 69, 19),
    "royalblue": (65, 105, 225),
    "darkseagreen": (143, 188, 143),
    "cadetblue": (95, 158, 160),
    "indianred": (205, 92, 92),
    "deepskyblue": (0, 191, 255),
    "limegreen": (50, 205, 50),
    "mediumorchid": (186, 85, 211),
    "lightslategray": (119, 136, 153),
    "lightcoral": (240, 128, 128),
    "mediumspringgreen": (0, 250, 154),
    "palevioletred": (219, 112, 147),
    "slategray": (112, 128, 144),
    "darkslategray": (47, 79, 79),
    "mediumturquoise": (72, 209, 204),
    "cornflowerblue": (100, 149, 237),
    "darkgoldenrod": (184, 134, 11),
    "tomato": (255, 99, 71),
    "chartreuse": (127, 255, 0),
    "darkkhaki": (189, 183, 107),
    "goldenrod": (218, 165, 32),
    "sandybrown": (244, 164, 96),
    "mediumslateblue": (123, 104, 238),
    "lawngreen": (124, 252, 0),
    "lightseagreen": (32, 178, 170),
    "burlywood": (222, 184, 135),
    "cadmiumyellow": (255, 153, 18),
    "chartreuse": (127, 255, 0),
    "darkolivegreen": (85, 107, 47),
    "darkslateblue": (72, 61, 139),
    "darkslategray": (47, 79, 79),
    "darksalmon": (233, 150, 122),
    "darkturquoise": (0, 206, 209),
    "dodgerblue": (30, 144, 255),
    "goldenyellow": (255, 223, 0),
    "hotpink": (255, 105, 180),
    "lightcyan": (224, 255, 255),
    "lightgray": (211, 211, 211),
    "lightskyblue": (135, 206, 250),
    "lightyellow": (255, 255, 224),
    "mediumaquamarine": (102, 205, 170),
    "mediumblue": (0, 0, 205),
    "mediumvioletred": (199, 21, 133),
    "mistyrose": (255, 228, 225),
    "navajowhite": (255, 222, 173),
    "palegreen": (152, 251, 152),
    "paleturquoise": (175, 238, 238),
    "rosybrown": (188, 143, 143),
    "seagreen": (46, 139, 87),
    "thistle": (216, 191, 216),
    "wheat": (245, 222, 179),
    "aliceblue": (240, 248, 255),
    "antiquewhite": (250, 235, 215),
    "aquamarine": (127, 255, 212),
    "azure": (240, 255, 255),
    "beige": (245, 245, 220),
    "bisque": (255, 228, 196),
    "blanchedalmond": (255, 235, 205),
    "blueviolet": (138, 43, 226),
    "burlywood": (222, 184, 135),
    "cadetblue": (95, 158, 160),
    "chocolate": (210, 105, 30),
    "coral": (255, 127, 80),
    "cornsilk": (255, 248, 220),
    "crimson": (220, 20, 60),
    "darkblue": (0, 0, 139),
    "darkcyan": (0, 139, 139),
    "darkgoldenrod": (184, 134, 11),
    "darkgray": (169, 169, 169),
    "darkgreen": (0, 100, 0),
    "darkkhaki": (189, 183, 107),
    "darkmagenta": (139, 0, 139),
    "darkolivegreen": (85, 107, 47),
    "darkorange": (255, 140, 0),
    "darkorchid": (153, 50, 204),
    "darksalmon": (233, 150, 122),
    "darkseagreen": (143, 188, 143),
    "darkslateblue": (72, 61, 139),
    "darkslategray": (47, 79, 79),
    "darkturquoise": (0, 206, 209),
    "darkviolet": (148, 0, 211),
    "deeppink": (255, 20, 147),
    "deepskyblue": (0, 191, 255),
    "dimgray": (105, 105, 105),
    "dodgerblue": (30, 144, 255),
    "firebrick": (178, 34, 34),
    "floralwhite": (255, 250, 240),
    "forestgreen": (34, 139, 34),
    "gainsboro": (220, 220, 220),
    "ghostwhite": (248, 248, 255),
    "goldenrod": (218, 165, 32),
    "greenyellow": (173, 255, 47),
    "honeydew": (240, 255, 240),
    "hotpink": (255, 105, 180),
    "indianred": (205, 92, 92),
    "ivory": (255, 255, 240),
    "khaki": (240, 230, 140),
    "lavenderblush": (255, 240, 245),
    "lemonchiffon": (255, 250, 205),
    "lightblue": (173, 216, 230),
    "lightcoral": (240, 128, 128),
    "lightcyan": (224, 255, 255),
    "lightgoldenrodyellow": (250, 250, 210),
    "lightgray": (211, 211, 211),
    "lightgreen": (144, 238, 144),
    "lightpink": (255, 182, 193),
    "lightsalmon": (255, 160, 122),
    "lightseagreen": (32, 178, 170),
    "lightskyblue": (135, 206, 250),
    "lightsteelblue": (176, 196, 222),
    "lightyellow": (255, 255, 224),
    "limegreen": (50, 205, 50),
    "linen": (250, 240, 230),
    "mediumaquamarine": (102, 205, 170),
    "mediumblue": (0, 0, 205),
    "mediumorchid": (186, 85, 211),
    "mediumpurple": (147, 112, 219),
    "mediumseagreen": (60, 179, 113),
    "mediumslateblue": (123, 104, 238),
    "mediumspringgreen": (0, 250, 154),
    "mediumturquoise": (72, 209, 204),
    "mediumvioletred": (199, 21, 133),
    "midnightblue": (25, 25, 112),
    "mintcream": (245, 255, 250),
    "mistyrose": (255, 228, 225),
    "moccasin": (255, 228, 181),
    "oldlace": (253, 245, 230),
    "orangered": (255, 69, 0),
    "orchid": (218, 112, 214),
    "palegoldenrod": (238, 232, 170),
    "palegreen": (152, 251, 152),
    "paleturquoise": (175, 238, 238),
    "papayawhip": (255, 239, 213),
    "peachpuff": (255, 218, 185),
    "powderblue": (176, 224, 230),
    "rosybrown": (188, 143, 143),
    "royalblue": (65, 105, 225),
    "saddlebrown": (139, 69, 19),
    "sandybrown": (244, 164, 96),
    "seashell": (255, 245, 238),
    "sienna": (160, 82, 45),
    "skyblue": (135, 206, 235),
    "slateblue": (106, 90, 205),
    "slategray": (112, 128, 144),
    "snow": (255, 250, 250),
    "springgreen": (0, 255, 127),
    "steelblue": (70, 130, 180),
    "tan": (210, 180, 140),
    "thistle": (216, 191, 216),
    "tomato": (255, 99, 71),
    "turquoise": (64, 224, 208),
    "violet": (238, 130, 238),
    "wheat": (245, 222, 179),
    "whitesmoke": (245, 245, 245),
    "yellowgreen": (154, 205, 50)

}


# Initialize the camera
cap = cv2.VideoCapture(0)

# Create a GUI window
root = tk.Tk()
root.title("ColorMagnet")

# Create a label to display the recognized color name
color_label = tk.Label(root, text="", font=("Arial", 20))
color_label.pack(pady=20)

# Create a label to display color information (RGB)
color_info_label = tk.Label(root, text="", font=("Arial", 16))
color_info_label.pack(pady=10)

# Function to update the recognized color name and display the camera feed
def update_color_label():
    ret, frame = cap.read()
    if frame is not None:
        # Get the average color in the frame
        avg_color = np.mean(np.mean(frame, axis=0), axis=0).astype(int)

        # Find the closest known color based on RGB values
        closest_color = None
        min_distance = float('inf')

        for color_name, color_rgb in color_names_rgb.items():
            distance = np.linalg.norm(np.array(color_rgb) - np.array(avg_color))
            if distance < min_distance:
                min_distance = distance
                closest_color = color_name

        color_label.config(text=f"Recognized Color: {closest_color}")

        # Display color information (RGB)
        if closest_color in color_names_rgb:
            color_info_label.config(text=f"RGB: {color_names_rgb[closest_color]}")

        # Display the camera feed in a separate window
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        label_img.imgtk = imgtk
        label_img.configure(image=imgtk)
        label_img.after(10, update_color_label)  # Update the image every 10ms

# Create a label to display the camera feed
label_img = tk.Label(root)
label_img.pack()

# Start updating the color label and displaying the camera feed
update_color_label()

# Function to close the camera and exit the GUI
def close_app():
    cap.release()
    root.destroy()

# Create an "Exit" button to exit the application
exit_button = tk.Button(root, text="Exit", command=close_app)
exit_button.pack()

# Start the GUI main loop
root.mainloop()
