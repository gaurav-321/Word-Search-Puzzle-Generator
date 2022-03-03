import random
from word_search_generator import WordSearch
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


RESOLUTION_MULT = 1
BOLD = 1
WHITE, BLACK = ((255, 0, 0), (0, 0, 0))
a4_image_size = (int(816 * RESOLUTION_MULT), int(1056 * RESOLUTION_MULT))  # width, height
MARGIN_PER = 5
WORDS = ["wear", "variable", "print", "minimum", "graduate", "room", "bulk", "advise", "completed", "memory",
         "hello",
         "what", "who", "basket", "tomorrow", "yester", "today", "teacher", "student", "india", "uniteds",
         "france"]


class Puzzle:
    def __init__(self):
        self.img = 255 * np.ones((a4_image_size[1], a4_image_size[0], 3), np.uint8)
        self.pos = []

    def draw_border(self):
        horiz_margin = int(a4_image_size[1] / 100) * MARGIN_PER
        vert_margin = int(a4_image_size[0] / 100) * MARGIN_PER
        cv2.line(self.img, (horiz_margin, vert_margin), (a4_image_size[0] - horiz_margin, 0 + vert_margin), BLACK, 4)
        cv2.line(self.img, (horiz_margin, a4_image_size[1] - vert_margin),
                 (a4_image_size[0] - horiz_margin, a4_image_size[1] - vert_margin), BLACK, 4)
        cv2.line(self.img, (horiz_margin, vert_margin), (horiz_margin, a4_image_size[1] - vert_margin), BLACK, 4)
        cv2.line(self.img, (a4_image_size[0] - horiz_margin, vert_margin),
                 (a4_image_size[0] - horiz_margin, a4_image_size[1] - vert_margin), BLACK, 4)

    def write_text(self, image, x, y, text):
        pil_im = Image.fromarray(image)

        draw = ImageDraw.Draw(pil_im)

        # Choose a font
        font = ImageFont.truetype("Roboto-Regular.ttf", int(35 * RESOLUTION_MULT))
        w, h = draw.textsize(text, font=font)
        max_r_w = draw.textsize("W", font=font)[0]
        width_adjust = int((max_r_w - w) / 2)
        draw.text((x + 8 + width_adjust, y + 8), text, (0, 0, 0), font=font, stroke_width=BOLD)
        cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
        return cv2_im_processed

    def get_pos(self):
        self.pos = []
        horiz_margin = int(a4_image_size[1] / 100) * MARGIN_PER
        vert_margin = int(a4_image_size[0] / 100) * MARGIN_PER
        start_x, start_y = horiz_margin, vert_margin
        end_x, end_y = a4_image_size[0] - horiz_margin, a4_image_size[1] - vert_margin
        horiz_mult = (a4_image_size[0] - 2 * horiz_margin) / 15
        vert_mult = (a4_image_size[1] - 2 * vert_margin) / 15
        temp_x, temp_y = start_x, start_y
        for j in range(15):
            for i in range(15):
                self.pos.append((temp_x, temp_y))
                temp_x += horiz_mult
            temp_x = start_x
            temp_y += vert_mult


if __name__ == '__main__':
    puzzle = Puzzle()
    puzzle.draw_border()
    puzzle.get_pos()
    word_search = WordSearch(",".join(WORDS), size=15)
    puzzle.grid = word_search.grid
    puzzle.solution = word_search.wordPosition
    i = 0
    for row in puzzle.grid:
        for column in row:
            puzzle.img = puzzle.write_text(puzzle.img, puzzle.pos[i][0], puzzle.pos[i][1], column.upper())
            i += 1
    cv2.imwrite(f"output/{random.randint(0, 1000)}test.png", puzzle.img)

    # cv2.imshow("win", puzzle.img)

