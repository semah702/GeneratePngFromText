from text2Png import text2png

# Seçimleri ayarla
text = "Hello, world!"
font_path = "ShantellSans-Italic-VariableFont_BNCE,INFM,SPAC,wght.ttf"

# PNG olarak kaydet
image = text2png(text, font_path)
image.save('text.png')