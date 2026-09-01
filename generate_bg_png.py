import os
import math
from PIL import Image, ImageDraw

DESKTOP_ICONS_DIR = "/Users/basel/Desktop/icons"
os.makedirs(DESKTOP_ICONS_DIR, exist_ok=True)

# Resolution for HD PNG background asset (1920 x 600 px)
width, height = 1920, 600

# Create base canvas with smooth linear mesh gradient (135 deg: #eff6ff to #f5f3ff to #fdf2f8)
image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

# Create smooth gradient background
for y in range(height):
    for x in range(width):
        # Diagonal factor (135 degrees)
        t = (x / width + y / height) / 2.0
        
        # Interpolate between 3 brand light stops:
        # Stop 0: #eff6ff (239, 246, 255)
        # Stop 0.5: #f5f3ff (245, 243, 255)
        # Stop 1.0: #fdf2f8 (253, 242, 248)
        if t < 0.5:
            factor = t / 0.5
            r = int(239 + (245 - 239) * factor)
            g = int(246 + (243 - 246) * factor)
            b = int(255 + (255 - 255) * factor)
        else:
            factor = (t - 0.5) / 0.5
            r = int(245 + (253 - 245) * factor)
            g = int(243 + (242 - 243) * factor)
            b = int(255 + (248 - 255) * factor)

        image.putpixel((x, y), (r, g, b, 255))

# Draw soft ambient radial glow spheres matching SMARTVISION logo colors
def draw_radial_glow(img, center_x, center_y, radius, color_rgb, max_alpha=50):
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    for r in range(radius, 0, -2):
        alpha = int(max_alpha * (1.0 - (r / radius) ** 1.8))
        if alpha <= 0:
            continue
        bbox = [center_x - r, center_y - r, center_x + r, center_y + r]
        draw.ellipse(bbox, fill=(color_rgb[0], color_rgb[1], color_rgb[2], alpha))
    
    return Image.alpha_composite(img, overlay)

# Add 1. Blue Ambient Sphere (top-left)
image = draw_radial_glow(image, center_x=200, center_y=50, radius=400, color_rgb=(0, 102, 255), max_alpha=65)

# Add 2. Purple Ambient Sphere (bottom-middle)
image = draw_radial_glow(image, center_x=1200, center_y=550, radius=450, color_rgb=(124, 58, 237), max_alpha=55)

# Add 3. Pink Ambient Sphere (top-right)
image = draw_radial_glow(image, center_x=1700, center_y=100, radius=380, color_rgb=(236, 72, 253), max_alpha=55)

# Add 4. Cyan Ambient Sphere (left-center)
image = draw_radial_glow(image, center_x=400, center_y=350, radius=350, color_rgb=(6, 182, 212), max_alpha=45)

# Save PNG output files to /Users/basel/Desktop/icons
output_path_1 = os.path.join(DESKTOP_ICONS_DIR, "hero_background.png")
output_path_2 = os.path.join(DESKTOP_ICONS_DIR, "smartvision_hero_bg_hd.png")

image.save(output_path_1, "PNG")
image.save(output_path_2, "PNG")

print(f"Successfully generated hero background PNG assets:")
print(f" - {output_path_1}")
print(f" - {output_path_2}")
