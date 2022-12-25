# Word Search Puzzle Generator
This program generates a word search puzzle and displays it in a window using the OpenCV library. It uses the WordSearch class from the word_search_generator module to generate the puzzle, and it uses the Puzzle class to draw the puzzle onto an image and display it.

## Requirements
This program requires the following libraries:

- OpenCV
- NumPy
- Pillow
## Usage
To use the program, simply run the script using Python. The generated puzzle will be displayed in a window.

## Customization
There are several constants at the top of the script that can be adjusted to customize the puzzle:

- RESOLUTION_MULT: A multiplier for the resolution of the generated puzzle. Higher values will result in a larger puzzle.
- BOLD: The stroke width for the text in the puzzle. Higher values will result in bolder text.
- WHITE: The color of the background of the puzzle.
- BLACK: The color of the border and text of the puzzle.
- a4_image_size: The size of the generated puzzle in pixels.
- MARGIN_PER: The percentage of the image size to use as a margin around the puzzle.
- WORDS: A list of words to include in the puzzle.
## Notes
The font used in the puzzle is "Roboto-Regular.ttf", which must be placed in the same directory as the script.

The word_search_generator module is not provided in this repository. It must be obtained separately.
