import arcade
import numpy as np
import random
from game_object_3d import Object3D

# definicion de constantes
WIDTH = 800
HEIGHT = 800
TITLE = "Proyeccion 3d"


def get_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


class App(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.BLACK
        self.cube = Object3D(
            [
                #x, y, z
                (1, 1, 1),
                (1, 1, -1),
                (1, -1, 1),
                (1, -1, -1),
                (-1, 1, 1),
                (-1, 1, -1),
                (-1, -1, 1),
                (-1, -1, -1),
            ],
            [
                (0, 1),
                (1, 3),
                (2, 3),
                (2, 0),
                (4, 5),
                (5, 7),
                (6, 7),
                (6, 4),
                (0, 4),
                (1, 5),
                (2, 6),
                (3, 7)
            ],
            arcade.color.YELLOW
        )
        self.cube.translate(399, 399, 0)
        self.cube.scale(100, 100, 100)
        self.cube.rotate(-0.3, "x")
        self.cube.rotate(0.3, "y")
        self.cube.rotate(0.7, "z")
    
    def on_update(self, delta_time: float):
        self.cube.rotate(delta_time, "y")
        pass

    def on_draw(self):
        self.clear()
        self.cube.draw()
    
    
def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    game = App()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()