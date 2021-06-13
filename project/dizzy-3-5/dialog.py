#
# class Dialog(object):
#     def __init__(self, text, width, color="white"):
#         self._width = width
#         self._color = color
#
#         self._lines = []
#         line = ""
#         for word in text.split():
#             if len(line) + len(word) < self._width:
#                 line = f"{line} {word}"
#             else:
#                 self._lines.append(line.center(self._width))
#                 line = word
#
#     def draw(self):
#         # count the position first
#         y_offset = HEIGHT / 2 - 16 * len(self._lines) / 2
#         x_offset = WIDTH / 2 - 16 * self._width / 2
#
#         # print line by line
#         counter = 0
#         for line in self._lines:
#             screen.draw.text(
#                 line,
#                 (x_offset, counter * 20 + y_offset),
#                 fontname="dizzy-iii-fantasy-world-dizzy-spectrum.ttf",
#                 fontsize=16,
#                 color=self._color,
#             )
#             counter += 1
