import tkinter as tk
from dollarpy import Recognizer, Template, Point


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")

        self.is_drawing = False
        self.points = []

        # Create a canvas
        self.canvas = tk.Canvas(root, bg="white", width=400, height=400)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        # Play button
        self.play_button = tk.Button(root, text="Play", command=self.start_drawing)
        self.play_button.pack(side=tk.LEFT, padx=5)

        # Pause button
        self.pause_button = tk.Button(root, text="Pause", command=self.stop_drawing)
        self.pause_button.pack(side=tk.LEFT, padx=5)

        # Clear button
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        tmpl_triangle = Template(
            "triangle",
            [
                Point(137, 139),
                Point(135, 141),
                Point(133, 144),
                Point(132, 146),
                Point(130, 149),
                Point(128, 151),
                Point(126, 155),
                Point(123, 160),
                Point(120, 166),
                Point(116, 171),
                Point(112, 177),
                Point(107, 183),
                Point(102, 188),
                Point(100, 191),
                Point(95, 195),
                Point(90, 199),
                Point(86, 203),
                Point(82, 206),
                Point(80, 209),
                Point(75, 213),
                Point(73, 213),
                Point(70, 216),
                Point(67, 219),
                Point(64, 221),
                Point(61, 223),
                Point(60, 225),
                Point(62, 226),
                Point(65, 225),
                Point(67, 226),
                Point(74, 226),
                Point(77, 227),
                Point(85, 229),
                Point(91, 230),
                Point(99, 231),
                Point(108, 232),
                Point(116, 233),
                Point(125, 233),
                Point(134, 234),
                Point(145, 233),
                Point(153, 232),
                Point(160, 233),
                Point(170, 234),
                Point(177, 235),
                Point(179, 236),
                Point(186, 237),
                Point(193, 238),
                Point(198, 239),
                Point(200, 237),
                Point(202, 239),
                Point(204, 238),
                Point(206, 234),
                Point(205, 230),
                Point(202, 222),
                Point(197, 216),
                Point(192, 207),
                Point(186, 198),
                Point(179, 189),
                Point(174, 183),
                Point(170, 178),
                Point(164, 171),
                Point(161, 168),
                Point(154, 160),
                Point(148, 155),
                Point(143, 150),
                Point(138, 148),
                Point(136, 148),
            ],
        )

        tmpl_x = Template(
            "x",
            [
                Point(87, 142, 1),
                Point(89, 145, 1),
                Point(91, 148, 1),
                Point(93, 151, 1),
                Point(96, 155, 1),
                Point(98, 157, 1),
                Point(100, 160, 1),
                Point(102, 162, 1),
                Point(106, 167, 1),
                Point(108, 169, 1),
                Point(110, 171, 1),
                Point(115, 177, 1),
                Point(119, 183, 1),
                Point(123, 189, 1),
                Point(127, 193, 1),
                Point(129, 196, 1),
                Point(133, 200, 1),
                Point(137, 206, 1),
                Point(140, 209, 1),
                Point(143, 212, 1),
                Point(146, 215, 1),
                Point(151, 220, 1),
                Point(153, 222, 1),
                Point(155, 223, 1),
                Point(157, 225, 1),
                Point(158, 223, 1),
                Point(157, 218, 1),
                Point(155, 211, 1),
                Point(154, 208, 1),
                Point(152, 200, 1),
                Point(150, 189, 1),
                Point(148, 179, 1),
                Point(147, 170, 1),
                Point(147, 158, 1),
                Point(147, 148, 1),
                Point(147, 141, 1),
                Point(147, 136, 1),
                Point(144, 135, 1),
                Point(142, 137, 1),
                Point(140, 139, 1),
                Point(135, 145, 1),
                Point(131, 152, 1),
                Point(124, 163, 1),
                Point(116, 177, 1),
                Point(108, 191, 1),
                Point(100, 206, 1),
                Point(94, 217, 1),
                Point(91, 222, 1),
                Point(89, 225, 1),
                Point(87, 226, 1),
                Point(87, 224, 1),
            ],
        )

        tmpl_rect = Template(
            "rectangle",
            [
                Point(78, 149, 1),
                Point(78, 153, 1),
                Point(78, 157, 1),
                Point(78, 160, 1),
                Point(79, 162, 1),
                Point(79, 164, 1),
                Point(79, 167, 1),
                Point(79, 169, 1),
                Point(79, 173, 1),
                Point(79, 178, 1),
                Point(79, 183, 1),
                Point(80, 189, 1),
                Point(80, 193, 1),
                Point(80, 198, 1),
                Point(80, 202, 1),
                Point(81, 208, 1),
                Point(81, 210, 1),
                Point(81, 216, 1),
                Point(82, 222, 1),
                Point(82, 224, 1),
                Point(82, 227, 1),
                Point(83, 229, 1),
                Point(83, 231, 1),
                Point(85, 230, 1),
                Point(88, 232, 1),
                Point(90, 233, 1),
                Point(92, 232, 1),
                Point(94, 233, 1),
                Point(99, 232, 1),
                Point(102, 233, 1),
                Point(106, 233, 1),
                Point(109, 234, 1),
                Point(117, 235, 1),
                Point(123, 236, 1),
                Point(126, 236, 1),
                Point(135, 237, 1),
                Point(142, 238, 1),
                Point(145, 238, 1),
                Point(152, 238, 1),
                Point(154, 239, 1),
                Point(165, 238, 1),
                Point(174, 237, 1),
                Point(179, 236, 1),
                Point(186, 235, 1),
                Point(191, 235, 1),
                Point(195, 233, 1),
                Point(197, 233, 1),
                Point(200, 233, 1),
                Point(201, 235, 1),
                Point(201, 233, 1),
                Point(199, 231, 1),
                Point(198, 226, 1),
                Point(198, 220, 1),
                Point(196, 207, 1),
                Point(195, 195, 1),
                Point(195, 181, 1),
                Point(195, 173, 1),
                Point(195, 163, 1),
                Point(194, 155, 1),
                Point(192, 145, 1),
                Point(192, 143, 1),
                Point(192, 138, 1),
                Point(191, 135, 1),
                Point(191, 133, 1),
                Point(191, 130, 1),
                Point(190, 128, 1),
                Point(188, 129, 1),
                Point(186, 129, 1),
                Point(181, 132, 1),
                Point(173, 131, 1),
                Point(162, 131, 1),
                Point(151, 132, 1),
                Point(149, 132, 1),
                Point(138, 132, 1),
                Point(136, 132, 1),
                Point(122, 131, 1),
                Point(120, 131, 1),
                Point(109, 130, 1),
                Point(107, 130, 1),
                Point(90, 132, 1),
                Point(81, 133, 1),
                Point(76, 133, 1),
            ],
        )

        tmpl_circle = Template(
            "circle",
            [
                Point(127, 141, 1),
                Point(124, 140, 1),
                Point(120, 139, 1),
                Point(118, 139, 1),
                Point(116, 139, 1),
                Point(111, 140, 1),
                Point(109, 141, 1),
                Point(104, 144, 1),
                Point(100, 147, 1),
                Point(96, 152, 1),
                Point(93, 157, 1),
                Point(90, 163, 1),
                Point(87, 169, 1),
                Point(85, 175, 1),
                Point(83, 181, 1),
                Point(82, 190, 1),
                Point(82, 195, 1),
                Point(83, 200, 1),
                Point(84, 205, 1),
                Point(88, 213, 1),
                Point(91, 216, 1),
                Point(96, 219, 1),
                Point(103, 222, 1),
                Point(108, 224, 1),
                Point(111, 224, 1),
                Point(120, 224, 1),
                Point(133, 223, 1),
                Point(142, 222, 1),
                Point(152, 218, 1),
                Point(160, 214, 1),
                Point(167, 210, 1),
                Point(173, 204, 1),
                Point(178, 198, 1),
                Point(179, 196, 1),
                Point(182, 188, 1),
                Point(182, 177, 1),
                Point(178, 167, 1),
                Point(170, 150, 1),
                Point(163, 138, 1),
                Point(152, 130, 1),
                Point(143, 129, 1),
                Point(140, 131, 1),
                Point(129, 136, 1),
                Point(126, 139, 1),
            ],
        )

        tmpl_check = Template(
            "check",
            [
                Point(91, 185, 1),
                Point(93, 185, 1),
                Point(95, 185, 1),
                Point(97, 185, 1),
                Point(100, 188, 1),
                Point(102, 189, 1),
                Point(104, 190, 1),
                Point(106, 193, 1),
                Point(108, 195, 1),
                Point(110, 198, 1),
                Point(112, 201, 1),
                Point(114, 204, 1),
                Point(115, 207, 1),
                Point(117, 210, 1),
                Point(118, 212, 1),
                Point(120, 214, 1),
                Point(121, 217, 1),
                Point(122, 219, 1),
                Point(123, 222, 1),
                Point(124, 224, 1),
                Point(126, 226, 1),
                Point(127, 229, 1),
                Point(129, 231, 1),
                Point(130, 233, 1),
                Point(129, 231, 1),
                Point(129, 228, 1),
                Point(129, 226, 1),
                Point(129, 224, 1),
                Point(129, 221, 1),
                Point(129, 218, 1),
                Point(129, 212, 1),
                Point(129, 208, 1),
                Point(130, 198, 1),
                Point(132, 189, 1),
                Point(134, 182, 1),
                Point(137, 173, 1),
                Point(143, 164, 1),
                Point(147, 157, 1),
                Point(151, 151, 1),
                Point(155, 144, 1),
                Point(161, 137, 1),
                Point(165, 131, 1),
                Point(171, 122, 1),
                Point(174, 118, 1),
                Point(176, 114, 1),
                Point(177, 112, 1),
                Point(177, 114, 1),
                Point(175, 116, 1),
                Point(173, 118, 1),
            ],
        )

        tmpl_caret = Template(
            "caret",
            [
                Point(79, 245, 1),
                Point(79, 242, 1),
                Point(79, 239, 1),
                Point(80, 237, 1),
                Point(80, 234, 1),
                Point(81, 232, 1),
                Point(82, 230, 1),
                Point(84, 224, 1),
                Point(86, 220, 1),
                Point(86, 218, 1),
                Point(87, 216, 1),
                Point(88, 213, 1),
                Point(90, 207, 1),
                Point(91, 202, 1),
                Point(92, 200, 1),
                Point(93, 194, 1),
                Point(94, 192, 1),
                Point(96, 189, 1),
                Point(97, 186, 1),
                Point(100, 179, 1),
                Point(102, 173, 1),
                Point(105, 165, 1),
                Point(107, 160, 1),
                Point(109, 158, 1),
                Point(112, 151, 1),
                Point(115, 144, 1),
                Point(117, 139, 1),
                Point(119, 136, 1),
                Point(119, 134, 1),
                Point(120, 132, 1),
                Point(121, 129, 1),
                Point(122, 127, 1),
                Point(124, 125, 1),
                Point(126, 124, 1),
                Point(129, 125, 1),
                Point(131, 127, 1),
                Point(132, 130, 1),
                Point(136, 139, 1),
                Point(141, 154, 1),
                Point(145, 166, 1),
                Point(151, 182, 1),
                Point(156, 193, 1),
                Point(157, 196, 1),
                Point(161, 209, 1),
                Point(162, 211, 1),
                Point(167, 223, 1),
                Point(169, 229, 1),
                Point(170, 231, 1),
                Point(173, 237, 1),
                Point(176, 242, 1),
                Point(177, 244, 1),
                Point(179, 250, 1),
                Point(181, 255, 1),
                Point(182, 257, 1),
            ],
        )

        tmpl_zigzag = Template(
            "zig-zag",
            [
                Point(307, 216, 1),
                Point(333, 186, 1),
                Point(356, 215, 1),
                Point(375, 186, 1),
                Point(399, 216, 1),
                Point(418, 186, 1),
            ],
        )

        tmpl_arrow = Template(
            "arrow",
            [
                Point(68, 222, 1),
                Point(70, 220, 1),
                Point(73, 218, 1),
                Point(75, 217, 1),
                Point(77, 215, 1),
                Point(80, 213, 1),
                Point(82, 212, 1),
                Point(84, 210, 1),
                Point(87, 209, 1),
                Point(89, 208, 1),
                Point(92, 206, 1),
                Point(95, 204, 1),
                Point(101, 201, 1),
                Point(106, 198, 1),
                Point(112, 194, 1),
                Point(118, 191, 1),
                Point(124, 187, 1),
                Point(127, 186, 1),
                Point(132, 183, 1),
                Point(138, 181, 1),
                Point(141, 180, 1),
                Point(146, 178, 1),
                Point(154, 173, 1),
                Point(159, 171, 1),
                Point(161, 170, 1),
                Point(166, 167, 1),
                Point(168, 167, 1),
                Point(171, 166, 1),
                Point(174, 164, 1),
                Point(177, 162, 1),
                Point(180, 160, 1),
                Point(182, 158, 1),
                Point(183, 156, 1),
                Point(181, 154, 1),
                Point(178, 153, 1),
                Point(171, 153, 1),
                Point(164, 153, 1),
                Point(160, 153, 1),
                Point(150, 154, 1),
                Point(147, 155, 1),
                Point(141, 157, 1),
                Point(137, 158, 1),
                Point(135, 158, 1),
                Point(137, 158, 1),
                Point(140, 157, 1),
                Point(143, 156, 1),
                Point(151, 154, 1),
                Point(160, 152, 1),
                Point(170, 149, 1),
                Point(179, 147, 1),
                Point(185, 145, 1),
                Point(192, 144, 1),
                Point(196, 144, 1),
                Point(198, 144, 1),
                Point(200, 144, 1),
                Point(201, 147, 1),
                Point(199, 149, 1),
                Point(194, 157, 1),
                Point(191, 160, 1),
                Point(186, 167, 1),
                Point(180, 176, 1),
                Point(177, 179, 1),
                Point(171, 187, 1),
                Point(169, 189, 1),
                Point(165, 194, 1),
                Point(164, 196, 1),
            ],
        )

        tmpl_left_square_bracket = Template(
            "left square bracket",
            [
                Point(140, 124, 1),
                Point(138, 123, 1),
                Point(135, 122, 1),
                Point(133, 123, 1),
                Point(130, 123, 1),
                Point(128, 124, 1),
                Point(125, 125, 1),
                Point(122, 124, 1),
                Point(120, 124, 1),
                Point(118, 124, 1),
                Point(116, 125, 1),
                Point(113, 125, 1),
                Point(111, 125, 1),
                Point(108, 124, 1),
                Point(106, 125, 1),
                Point(104, 125, 1),
                Point(102, 124, 1),
                Point(100, 123, 1),
                Point(98, 123, 1),
                Point(95, 124, 1),
                Point(93, 123, 1),
                Point(90, 124, 1),
                Point(88, 124, 1),
                Point(85, 125, 1),
                Point(83, 126, 1),
                Point(81, 127, 1),
                Point(81, 129, 1),
                Point(82, 131, 1),
                Point(82, 134, 1),
                Point(83, 138, 1),
                Point(84, 141, 1),
                Point(84, 144, 1),
                Point(85, 148, 1),
                Point(85, 151, 1),
                Point(86, 156, 1),
                Point(86, 160, 1),
                Point(86, 164, 1),
                Point(86, 168, 1),
                Point(87, 171, 1),
                Point(87, 175, 1),
                Point(87, 179, 1),
                Point(87, 182, 1),
                Point(87, 186, 1),
                Point(88, 188, 1),
                Point(88, 195, 1),
                Point(88, 198, 1),
                Point(88, 201, 1),
                Point(88, 207, 1),
                Point(89, 211, 1),
                Point(89, 213, 1),
                Point(89, 217, 1),
                Point(89, 222, 1),
                Point(88, 225, 1),
                Point(88, 229, 1),
                Point(88, 231, 1),
                Point(88, 233, 1),
                Point(88, 235, 1),
                Point(89, 237, 1),
                Point(89, 240, 1),
                Point(89, 242, 1),
                Point(91, 241, 1),
                Point(94, 241, 1),
                Point(96, 240, 1),
                Point(98, 239, 1),
                Point(105, 240, 1),
                Point(109, 240, 1),
                Point(113, 239, 1),
                Point(116, 240, 1),
                Point(121, 239, 1),
                Point(130, 240, 1),
                Point(136, 237, 1),
                Point(139, 237, 1),
                Point(144, 238, 1),
                Point(151, 237, 1),
                Point(157, 236, 1),
                Point(159, 237, 1),
            ],
        )

        tmpl_right_square_bracket = Template(
            "right square bracket",
            [
                Point(112, 138, 1),
                Point(112, 136, 1),
                Point(115, 136, 1),
                Point(118, 137, 1),
                Point(120, 136, 1),
                Point(123, 136, 1),
                Point(125, 136, 1),
                Point(128, 136, 1),
                Point(131, 136, 1),
                Point(134, 135, 1),
                Point(137, 135, 1),
                Point(140, 134, 1),
                Point(143, 133, 1),
                Point(145, 132, 1),
                Point(147, 132, 1),
                Point(149, 132, 1),
                Point(152, 132, 1),
                Point(153, 134, 1),
                Point(154, 137, 1),
                Point(155, 141, 1),
                Point(156, 144, 1),
                Point(157, 152, 1),
                Point(158, 161, 1),
                Point(160, 170, 1),
                Point(162, 182, 1),
                Point(164, 192, 1),
                Point(166, 200, 1),
                Point(167, 209, 1),
                Point(168, 214, 1),
                Point(168, 216, 1),
                Point(169, 221, 1),
                Point(169, 223, 1),
                Point(169, 228, 1),
                Point(169, 231, 1),
                Point(166, 233, 1),
                Point(164, 234, 1),
                Point(161, 235, 1),
                Point(155, 236, 1),
                Point(147, 235, 1),
                Point(140, 233, 1),
                Point(131, 233, 1),
                Point(124, 233, 1),
                Point(117, 235, 1),
                Point(114, 238, 1),
                Point(112, 238, 1),
            ],
        )

        tmpl_v = Template(
            "v",
            [
                Point(89, 164, 1),
                Point(90, 162, 1),
                Point(92, 162, 1),
                Point(94, 164, 1),
                Point(95, 166, 1),
                Point(96, 169, 1),
                Point(97, 171, 1),
                Point(99, 175, 1),
                Point(101, 178, 1),
                Point(103, 182, 1),
                Point(106, 189, 1),
                Point(108, 194, 1),
                Point(111, 199, 1),
                Point(114, 204, 1),
                Point(117, 209, 1),
                Point(119, 214, 1),
                Point(122, 218, 1),
                Point(124, 222, 1),
                Point(126, 225, 1),
                Point(128, 228, 1),
                Point(130, 229, 1),
                Point(133, 233, 1),
                Point(134, 236, 1),
                Point(136, 239, 1),
                Point(138, 240, 1),
                Point(139, 242, 1),
                Point(140, 244, 1),
                Point(142, 242, 1),
                Point(142, 240, 1),
                Point(142, 237, 1),
                Point(143, 235, 1),
                Point(143, 233, 1),
                Point(145, 229, 1),
                Point(146, 226, 1),
                Point(148, 217, 1),
                Point(149, 208, 1),
                Point(149, 205, 1),
                Point(151, 196, 1),
                Point(151, 193, 1),
                Point(153, 182, 1),
                Point(155, 172, 1),
                Point(157, 165, 1),
                Point(159, 160, 1),
                Point(162, 155, 1),
                Point(164, 150, 1),
                Point(165, 148, 1),
                Point(166, 146, 1),
            ],
        )

        tmpl_delete = Template(
            "delete",
            [
                Point(123, 129, 1),
                Point(123, 131, 1),
                Point(124, 133, 1),
                Point(125, 136, 1),
                Point(127, 140, 1),
                Point(129, 142, 1),
                Point(133, 148, 1),
                Point(137, 154, 1),
                Point(143, 158, 1),
                Point(145, 161, 1),
                Point(148, 164, 1),
                Point(153, 170, 1),
                Point(158, 176, 1),
                Point(160, 178, 1),
                Point(164, 183, 1),
                Point(168, 188, 1),
                Point(171, 191, 1),
                Point(175, 196, 1),
                Point(178, 200, 1),
                Point(180, 202, 1),
                Point(181, 205, 1),
                Point(184, 208, 1),
                Point(186, 210, 1),
                Point(187, 213, 1),
                Point(188, 215, 1),
                Point(186, 212, 1),
                Point(183, 211, 1),
                Point(177, 208, 1),
                Point(169, 206, 1),
                Point(162, 205, 1),
                Point(154, 207, 1),
                Point(145, 209, 1),
                Point(137, 210, 1),
                Point(129, 214, 1),
                Point(122, 217, 1),
                Point(118, 218, 1),
                Point(111, 221, 1),
                Point(109, 222, 1),
                Point(110, 219, 1),
                Point(112, 217, 1),
                Point(118, 209, 1),
                Point(120, 207, 1),
                Point(128, 196, 1),
                Point(135, 187, 1),
                Point(138, 183, 1),
                Point(148, 167, 1),
                Point(157, 153, 1),
                Point(163, 145, 1),
                Point(165, 142, 1),
                Point(172, 133, 1),
                Point(177, 127, 1),
                Point(179, 127, 1),
                Point(180, 125, 1),
            ],
        )

        tmpl_left_curly_brace = Template(
            "left curly brace",
            [
                Point(150, 116, 1),
                Point(147, 117, 1),
                Point(145, 116, 1),
                Point(142, 116, 1),
                Point(139, 117, 1),
                Point(136, 117, 1),
                Point(133, 118, 1),
                Point(129, 121, 1),
                Point(126, 122, 1),
                Point(123, 123, 1),
                Point(120, 125, 1),
                Point(118, 127, 1),
                Point(115, 128, 1),
                Point(113, 129, 1),
                Point(112, 131, 1),
                Point(113, 134, 1),
                Point(115, 134, 1),
                Point(117, 135, 1),
                Point(120, 135, 1),
                Point(123, 137, 1),
                Point(126, 138, 1),
                Point(129, 140, 1),
                Point(135, 143, 1),
                Point(137, 144, 1),
                Point(139, 147, 1),
                Point(141, 149, 1),
                Point(140, 152, 1),
                Point(139, 155, 1),
                Point(134, 159, 1),
                Point(131, 161, 1),
                Point(124, 166, 1),
                Point(121, 166, 1),
                Point(117, 166, 1),
                Point(114, 167, 1),
                Point(112, 166, 1),
                Point(114, 164, 1),
                Point(116, 163, 1),
                Point(118, 163, 1),
                Point(120, 162, 1),
                Point(122, 163, 1),
                Point(125, 164, 1),
                Point(127, 165, 1),
                Point(129, 166, 1),
                Point(130, 168, 1),
                Point(129, 171, 1),
                Point(127, 175, 1),
                Point(125, 179, 1),
                Point(123, 184, 1),
                Point(121, 190, 1),
                Point(120, 194, 1),
                Point(119, 199, 1),
                Point(120, 202, 1),
                Point(123, 207, 1),
                Point(127, 211, 1),
                Point(133, 215, 1),
                Point(142, 219, 1),
                Point(148, 220, 1),
                Point(151, 221, 1),
            ],
        )

        tmpl_right_curly_brace = Template(
            "right curly brace",
            [
                Point(117, 132, 1),
                Point(115, 132, 1),
                Point(115, 129, 1),
                Point(117, 129, 1),
                Point(119, 128, 1),
                Point(122, 127, 1),
                Point(125, 127, 1),
                Point(127, 127, 1),
                Point(130, 127, 1),
                Point(133, 129, 1),
                Point(136, 129, 1),
                Point(138, 130, 1),
                Point(140, 131, 1),
                Point(143, 134, 1),
                Point(144, 136, 1),
                Point(145, 139, 1),
                Point(145, 142, 1),
                Point(145, 145, 1),
                Point(145, 147, 1),
                Point(145, 149, 1),
                Point(144, 152, 1),
                Point(142, 157, 1),
                Point(141, 160, 1),
                Point(139, 163, 1),
                Point(137, 166, 1),
                Point(135, 167, 1),
                Point(133, 169, 1),
                Point(131, 172, 1),
                Point(128, 173, 1),
                Point(126, 176, 1),
                Point(125, 178, 1),
                Point(125, 180, 1),
                Point(125, 182, 1),
                Point(126, 184, 1),
                Point(128, 187, 1),
                Point(130, 187, 1),
                Point(132, 188, 1),
                Point(135, 189, 1),
                Point(140, 189, 1),
                Point(145, 189, 1),
                Point(150, 187, 1),
                Point(155, 186, 1),
                Point(157, 185, 1),
                Point(159, 184, 1),
                Point(156, 185, 1),
                Point(154, 185, 1),
                Point(149, 185, 1),
                Point(145, 187, 1),
                Point(141, 188, 1),
                Point(136, 191, 1),
                Point(134, 191, 1),
                Point(131, 192, 1),
                Point(129, 193, 1),
                Point(129, 195, 1),
                Point(129, 197, 1),
                Point(131, 200, 1),
                Point(133, 202, 1),
                Point(136, 206, 1),
                Point(139, 211, 1),
                Point(142, 215, 1),
                Point(145, 220, 1),
                Point(147, 225, 1),
                Point(148, 231, 1),
                Point(147, 239, 1),
                Point(144, 244, 1),
                Point(139, 248, 1),
                Point(134, 250, 1),
                Point(126, 253, 1),
                Point(119, 253, 1),
                Point(115, 253, 1),
            ],
        )

        tmpl_star = Template(
            "star",
            [
                Point(75, 250, 1),
                Point(75, 247, 1),
                Point(77, 244, 1),
                Point(78, 242, 1),
                Point(79, 239, 1),
                Point(80, 237, 1),
                Point(82, 234, 1),
                Point(82, 232, 1),
                Point(84, 229, 1),
                Point(85, 225, 1),
                Point(87, 222, 1),
                Point(88, 219, 1),
                Point(89, 216, 1),
                Point(91, 212, 1),
                Point(92, 208, 1),
                Point(94, 204, 1),
                Point(95, 201, 1),
                Point(96, 196, 1),
                Point(97, 194, 1),
                Point(98, 191, 1),
                Point(100, 185, 1),
                Point(102, 178, 1),
                Point(104, 173, 1),
                Point(104, 171, 1),
                Point(105, 164, 1),
                Point(106, 158, 1),
                Point(107, 156, 1),
                Point(107, 152, 1),
                Point(108, 145, 1),
                Point(109, 141, 1),
                Point(110, 139, 1),
                Point(112, 133, 1),
                Point(113, 131, 1),
                Point(116, 127, 1),
                Point(117, 125, 1),
                Point(119, 122, 1),
                Point(121, 121, 1),
                Point(123, 120, 1),
                Point(125, 122, 1),
                Point(125, 125, 1),
                Point(127, 130, 1),
                Point(128, 133, 1),
                Point(131, 143, 1),
                Point(136, 153, 1),
                Point(140, 163, 1),
                Point(144, 172, 1),
                Point(145, 175, 1),
                Point(151, 189, 1),
                Point(156, 201, 1),
                Point(161, 213, 1),
                Point(166, 225, 1),
                Point(169, 233, 1),
                Point(171, 236, 1),
                Point(174, 243, 1),
                Point(177, 247, 1),
                Point(178, 249, 1),
                Point(179, 251, 1),
                Point(180, 253, 1),
                Point(180, 255, 1),
                Point(179, 257, 1),
                Point(177, 257, 1),
                Point(174, 255, 1),
                Point(169, 250, 1),
                Point(164, 247, 1),
                Point(160, 245, 1),
                Point(149, 238, 1),
                Point(138, 230, 1),
                Point(127, 221, 1),
                Point(124, 220, 1),
                Point(112, 212, 1),
                Point(110, 210, 1),
                Point(96, 201, 1),
                Point(84, 195, 1),
                Point(74, 190, 1),
                Point(64, 182, 1),
                Point(55, 175, 1),
                Point(51, 172, 1),
                Point(49, 170, 1),
                Point(51, 169, 1),
                Point(56, 169, 1),
                Point(66, 169, 1),
                Point(78, 168, 1),
                Point(92, 166, 1),
                Point(107, 164, 1),
                Point(123, 161, 1),
                Point(140, 162, 1),
                Point(156, 162, 1),
                Point(171, 160, 1),
                Point(173, 160, 1),
                Point(186, 160, 1),
                Point(195, 160, 1),
                Point(198, 161, 1),
                Point(203, 163, 1),
                Point(208, 163, 1),
                Point(206, 164, 1),
                Point(200, 167, 1),
                Point(187, 172, 1),
                Point(174, 179, 1),
                Point(172, 181, 1),
                Point(153, 192, 1),
                Point(137, 201, 1),
                Point(123, 211, 1),
                Point(112, 220, 1),
                Point(99, 229, 1),
                Point(90, 237, 1),
                Point(80, 244, 1),
                Point(73, 250, 1),
                Point(69, 254, 1),
                Point(69, 252, 1),
            ],
        )

        tmpl_pigtail = Template(
            "pigtail",
            [
                Point(81, 219, 1),
                Point(84, 218, 1),
                Point(86, 220, 1),
                Point(88, 220, 1),
                Point(90, 220, 1),
                Point(92, 219, 1),
                Point(95, 220, 1),
                Point(97, 219, 1),
                Point(99, 220, 1),
                Point(102, 218, 1),
                Point(105, 217, 1),
                Point(107, 216, 1),
                Point(110, 216, 1),
                Point(113, 214, 1),
                Point(116, 212, 1),
                Point(118, 210, 1),
                Point(121, 208, 1),
                Point(124, 205, 1),
                Point(126, 202, 1),
                Point(129, 199, 1),
                Point(132, 196, 1),
                Point(136, 191, 1),
                Point(139, 187, 1),
                Point(142, 182, 1),
                Point(144, 179, 1),
                Point(146, 174, 1),
                Point(148, 170, 1),
                Point(149, 168, 1),
                Point(151, 162, 1),
                Point(152, 160, 1),
                Point(152, 157, 1),
                Point(152, 155, 1),
                Point(152, 151, 1),
                Point(152, 149, 1),
                Point(152, 146, 1),
                Point(149, 142, 1),
                Point(148, 139, 1),
                Point(145, 137, 1),
                Point(141, 135, 1),
                Point(139, 135, 1),
                Point(134, 136, 1),
                Point(130, 140, 1),
                Point(128, 142, 1),
                Point(126, 145, 1),
                Point(122, 150, 1),
                Point(119, 158, 1),
                Point(117, 163, 1),
                Point(115, 170, 1),
                Point(114, 175, 1),
                Point(117, 184, 1),
                Point(120, 190, 1),
                Point(125, 199, 1),
                Point(129, 203, 1),
                Point(133, 208, 1),
                Point(138, 213, 1),
                Point(145, 215, 1),
                Point(155, 218, 1),
                Point(164, 219, 1),
                Point(166, 219, 1),
                Point(177, 219, 1),
                Point(182, 218, 1),
                Point(192, 216, 1),
                Point(196, 213, 1),
                Point(199, 212, 1),
                Point(201, 211, 1),
            ],
        )

        all_templates = [tmpl_triangle, tmpl_x, tmpl_rect, tmpl_circle, tmpl_check, tmpl_caret, tmpl_zigzag, tmpl_arrow, tmpl_left_square_bracket, tmpl_right_square_bracket, tmpl_v, tmpl_delete, tmpl_left_curly_brace, tmpl_right_curly_brace, tmpl_star, tmpl_pigtail]

        # Gesture recognizer
        self.recognizer = Recognizer(all_templates)

        # Event bindings
        self.canvas.bind("<Button-1>", self.start_line)
        self.canvas.bind("<B1-Motion>", self.draw_line)
        self.canvas.bind("<ButtonRelease-1>", self.end_line)

    def start_drawing(self):
        self.is_drawing = True

    def stop_drawing(self):
        self.is_drawing = False

    def start_line(self, event):
        self.points = []
        self.points.append(Point(event.x, event.y))

    def draw_line(self, event):
        if self.is_drawing:
            x, y = event.x, event.y
            self.points.append(Point(x, y))
            self.canvas.create_oval(x, y, x + 2, y + 2, fill="black", width=2)

    def end_line(self, event):
        if self.is_drawing:
            self.is_drawing = False
            gesture_name = self.recognizer.recognize(self.points)
            print("Recognized Gesture:", gesture_name)

    def clear_canvas(self):
        self.canvas.delete("all")


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()