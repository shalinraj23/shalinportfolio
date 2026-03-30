import sys
import subprocess

def install(pkg):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

try:
    import cv2
    import numpy as np
    from rembg import remove
except ImportError:
    print("Installing required packages via pip...")
    install("rembg[cli]")
    install("opencv-python")
    install("numpy")
    import cv2
    import numpy as np
    from rembg import remove

print("Loading image...")
input_path = 'profile.jpeg'
output_path = 'profile_professional.jpeg'

with open(input_path, 'rb') as f:
    input_data = f.read()

print("Applying AI background removal to create depth mask...")
out_data = remove(input_data)
nparr = np.frombuffer(out_data, np.uint8)
rgba = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

img = cv2.imread(input_path)

if rgba.shape[:2] != img.shape[:2]:
    rgba = cv2.resize(rgba, (img.shape[1], img.shape[0]))

mask = rgba[:, :, 3] / 255.0
mask_blurred = cv2.GaussianBlur(mask, (5, 5), 0)
mask_3d = np.dstack([mask_blurred]*3)

print("Applying DSLR-style Gaussian Blur to background...")
bg_blurred = cv2.GaussianBlur(img, (61, 61), 0)

final = img * mask_3d + bg_blurred * (1 - mask_3d)

cv2.imwrite(output_path, final)
print("Professional portrait created successfully!")
