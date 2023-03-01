from PIL import Image, ImageDraw, ImageFont

# Font ayarlarını yap
font_path = "ShantellSans-Italic-VariableFont_BNCE,INFM,SPAC,wght.ttf"
font = ImageFont.truetype(font_path, 36)

# Text stilini ayarla
text = "Hello, world!"
text_color = (255, 192, 203) # Pembe
text_position = (0,0)
text_width, text_height = font.getsize(text) # Text boyutu

# Yeni bir resim oluştur ve üzerine texti ekle
background_plan = (255, 255, 255, 0) # Şeffaf arkaplan
image = Image.new('RGBA', (text_width, text_height), color = background_plan)
draw = ImageDraw.Draw(image)
draw.text(text_position, text, fill=text_color, font=font)

# PNG olarak kaydet
image.save('text.png')
