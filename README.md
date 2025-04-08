# 🎨 Word Search Puzzle Generator

## ✨ Description

The Word Search Puzzle Generator is a Python program designed to create customizable word search puzzles. It utilizes OpenCV for displaying the puzzle and provides flexibility through various configuration options, making it an ideal tool for both educators and enthusiasts.

## ⚡️ Features

- **Customizable Puzzle Size**: Generate puzzles of any size from 10x10 to larger grids.
- **Multiple Difficulty Levels**: Choose from different levels of difficulty to suit your needs.
- **Random Word Placement**: Words are randomly placed within the grid, ensuring a unique puzzle each time.
- **Color Customization**: Adjust font colors and background for better visibility and aesthetics.
- **Output Options**: Save puzzles as images or display them in real-time using OpenCV.

## 🛠️ Installation

To get started with the Word Search Puzzle Generator, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/gag3301v/Word-Search-Puzzle-Generator.git
   cd Word-Search-Puzzle-Generator
   ```

2. **Install Dependencies**:
   ```sh
   pip install opencv-python numpy pillow word_search_generator
   ```

## 📦 Usage

### Example 1: Display a Puzzle in Real-Time

```python
from word_search_generator import WordSearch, Puzzle
import cv2

# Initialize the puzzle with predefined words and size
wordsearch = WordSearch(['hello', 'world'], size=15)
puzzle = Puzzle(wordsearch)

# Generate and display the puzzle using OpenCV
cv2.imshow('Word Search Puzzle', puzzle.draw())
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Example 2: Save a Puzzle as an Image

```python
from word_search_generator import WordSearch, Puzzle
import cv2

# Initialize the puzzle with predefined words and size
wordsearch = WordSearch(['hello', 'world'], size=15)
puzzle = Puzzle(wordsearch)

# Generate and save the puzzle as an image
cv2.imwrite('output/word_search_puzzle.png', puzzle.draw())
```

### Example 3: Print a Puzzle to the Console

```python
from word_search_generator import WordSearch, Puzzle

# Initialize the puzzle with predefined words and size
wordsearch = WordSearch(['hello', 'world'], size=15)
puzzle = Puzzle(wordsearch)

# Print the puzzle to the console
print(puzzle.generate())
```

## 🔧 Configuration (if applicable)

The program uses a set of constants for customization:

- `RESOLUTION_MULT`: Multiplier for the base resolution.
- `BOLD`: Font style for bold text.
- `WHITE`, `BLACK`: Colors used in the puzzle.

You can modify these constants to change the appearance and size of the puzzles.

## 🧪 Tests

Tests are not currently available for this project. If you wish to contribute, feel free to add them!

## 📁 Project Structure

```
Word-Search-Puzzle-Generator/
├── README.md
├── page_gen.py
├── temp.py
└── temp2.py
```

## 👥 Contributing

Contributions are welcome! Please read our [CONTRIBUTING](https://github.com/gag3301v/Word-Search-Puzzle-Generator/blob/main/CONTRIBUTING.md) file for details on how to contribute.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/gag3301v/Word-Search-Puzzle-Generator/blob/main/LICENSE) file for details.

---
**Owner**: gag3301v  
**GitHub Repo**: [Word-Search-Puzzle-Generator](https://github.com/gag3301v/Word-Search-Puzzle-Generator)