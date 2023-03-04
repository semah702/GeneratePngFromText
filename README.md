# Generate PNG from Text
Generate PNG file from Text.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install Pillow
```

## Usage

```python
from text2Png import text2png

text = "Hello, world!" # You can change text here.
font_path = "ShantellSans-Italic-VariableFont_BNCE,INFM,SPAC,wght.ttf" # You can change font here.

# Save to PNG
image = text2png(text, font_path)
image.save('text.png')
```

*You can use the example in the ```run.py``` file.*

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
