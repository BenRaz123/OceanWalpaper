from manim import *
from random import randint
from numpy import arange

class GridScene(Scene):
    def construct(self):
        
        animate = sys.argv[-1] == "--animate" or sys.argv[-1] == "-a"

        self.camera.background_color = "#0e1019"

        def get_random_square() -> Square:
            colors = [
                "#1D1f28",
                "#1D1f28",
                "#1D1f28",
                "#1D1f28",
                "#0e1019",
                "#0e1019",
                "#0e1019",
                "#c3e88e",
                "#a6accd",
                "#f07177",
                "#89dcff",
                "#c791e9",
                "#80cbc4",
            ]

            return (
                Square(side_length=0.1)
                .set_fill(opacity=1, color=colors[randint(0, len(colors) - 1)])
                .set_stroke(opacity=0)
            )

        group = VGroup()
        for i in arange(0, 18, 0.25):
            for j in arange(0, 10, 0.25):
                shape = get_random_square().set_x(i).set_y(j)
                group.add(shape)
        group.set_x(0).set_y(0).scale(0.8)
    
        if not animate:
            print("I am not animating!")
            self.add(group)
        else:
            print("I am animating!")
            self.play(LaggedStart(*[FadeIn(item, shift=LEFT, scale=0.5) for item in group], lag_ratio=0.005))
