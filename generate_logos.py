import os
from PIL import Image, ImageDraw, ImageFont

def make_logos():
    os.makedirs('image', exist_ok=True)

    # Generate Logo.png
    img = Image.new('RGBA', (400, 120), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Balance scale icon
    draw.line([(60, 30), (60, 85)], fill=(30, 41, 59, 255), width=4)
    draw.line([(40, 85), (80, 85)], fill=(30, 41, 59, 255), width=5)
    draw.line([(30, 45), (90, 45)], fill=(30, 41, 59, 255), width=4)
    draw.line([(30, 45), (20, 65)], fill=(30, 41, 59, 255), width=2)
    draw.line([(30, 45), (40, 65)], fill=(30, 41, 59, 255), width=2)
    draw.arc([(15, 60), (45, 75)], 0, 180, fill=(30, 41, 59, 255), width=3)
    draw.line([(90, 45), (80, 65)], fill=(30, 41, 59, 255), width=2)
    draw.line([(90, 45), (100, 65)], fill=(30, 41, 59, 255), width=2)
    draw.arc([(75, 60), (105, 75)], 0, 180, fill=(30, 41, 59, 255), width=3)

    try:
        font_large = ImageFont.truetype('arial.ttf', 36)
        font_small = ImageFont.truetype('arial.ttf', 14)
    except Exception:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    draw.text((115, 30), 'LegalEase', fill=(15, 23, 42, 255), font=font_large)
    draw.text((118, 72), 'AI Legal Document Generator', fill=(99, 102, 241, 255), font=font_small)

    img.save('image/Logo.png')

    # Generate inverseLogo.png
    img_inv = Image.new('RGBA', (400, 120), (255, 255, 255, 0))
    draw_inv = ImageDraw.Draw(img_inv)

    draw_inv.line([(60, 30), (60, 85)], fill=(241, 245, 249, 255), width=4)
    draw_inv.line([(40, 85), (80, 85)], fill=(241, 245, 249, 255), width=5)
    draw_inv.line([(30, 45), (90, 45)], fill=(241, 245, 249, 255), width=4)
    draw_inv.line([(30, 45), (20, 65)], fill=(241, 245, 249, 255), width=2)
    draw_inv.line([(30, 45), (40, 65)], fill=(241, 245, 249, 255), width=2)
    draw_inv.arc([(15, 60), (45, 75)], 0, 180, fill=(241, 245, 249, 255), width=3)
    draw_inv.line([(90, 45), (80, 65)], fill=(241, 245, 249, 255), width=2)
    draw_inv.line([(90, 45), (100, 65)], fill=(241, 245, 249, 255), width=2)
    draw_inv.arc([(75, 60), (105, 75)], 0, 180, fill=(241, 245, 249, 255), width=3)

    draw_inv.text((115, 30), 'LegalEase', fill=(255, 255, 255, 255), font=font_large)
    draw_inv.text((118, 72), 'AI Legal Document Generator', fill=(129, 140, 248, 255), font=font_small)

    img_inv.save('image/inverseLogo.png')
    print("Logos saved successfully.")

if __name__ == '__main__':
    make_logos()
