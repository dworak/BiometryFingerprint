This Python set of script provides functionality for thinning fingerprint images using a set of predefined structures. Additionally, it calculates minutiae points on the thinned image. The script uses the Python Imaging Library (PIL) and various image processing techniques.

## Usage

1. Ensure you have the required dependencies installed: PIL.
2. Run the script by executing `python thining.py`.

## Features

- Thinning: The script applies a set of predefined structures to thin the input fingerprint image.
- Minutiae Calculation: After thinning, the script calculates minutiae points on the thinned image.

## Example

```python
im = Image.open("images/fingerprint.png")
im = im.convert("L")
im.show()

make_thin(im)

result = calculate_minutiaes(im)
result.show()
