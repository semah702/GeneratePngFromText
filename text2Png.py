from PIL import Image, ImageDraw, ImageFont

def text2png(text, font_path):
    # Font ayarlarını yap
    font = ImageFont.truetype(font_path, 250)

    # Text stilini ayarla
    text_color = (0,0,0) # Pembe
    text_position = (0,0)
    text_width = font.getbbox(text)[2] # Yazı genişliği
    text_height = font.getbbox(text)[3] # Yazı yüksekliği

    # Yeni bir resim oluştur ve üzerine texti ekle
    background_plan = (255, 255, 255, 0) # Şeffaf arkaplan
    image = Image.new('RGBA', (text_width, text_height), color = background_plan)
    draw = ImageDraw.Draw(image)
    draw.text(text_position, text, fill=text_color, font=font)
    return image