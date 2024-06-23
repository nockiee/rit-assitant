from PIL import Image, ImageDraw, ImageFont

def draw_text_with_outline(draw, position, text, font, text_color, outline_color, outline_width):
    x, y = position
    for dx in range(-outline_width, outline_width+1):
        for dy in range(-outline_width, outline_width+1):
            if dx != 0 or dy != 0:
                draw.text((x + dx, y + dy), text, font=font, fill=outline_color)
    draw.text(position, text, font=font, fill=text_color)

name = str(input("Введите имя\n| -> "))
size = int(input("Введите размера текста\n| -> "))

with Image.open("dub.png") as original:
    draw = ImageDraw.Draw(original)
    
    font_path = "arial.ttf"
    try:
        font = ImageFont.truetype(font_path, size)
    except IOError:
        print("Не удалось загрузить шрифт. Убедитесь, что путь к шрифту указан правильно.")
        exit()
    

    rip_text = "RIP"
    rip_bbox = draw.textbbox((0, 0), rip_text, font=font)
    rip_width, rip_height = rip_bbox[2] - rip_bbox[0], rip_bbox[3] - rip_bbox[1]
    
    name_bbox = draw.textbbox((0, 0), name, font=font)
    name_width, name_height = name_bbox[2] - name_bbox[0], name_bbox[3] - name_bbox[1]
    

    text_color = (255, 255, 255)
    outline_color = (0, 0, 0)
    outline_width = 2

    draw_text_with_outline(draw, ((original.width - rip_width) / 2, 20), rip_text, font, text_color, outline_color, outline_width)
    draw_text_with_outline(draw, ((original.width - name_width) / 2, original.height - name_height - 20), name, font, text_color, outline_color, outline_width)

    original_4b = original.convert("L")
    original_4b.save("rip.jpg")
    original_4b.show()
