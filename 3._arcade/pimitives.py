import arcade

WIDTH = 1000
HEIGHT = 500
TITLE = "primitivas con Arcade"

class PrimitivesView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.ALABAMA_CRIMSON
    
    def on_draw(self):
        self.clear()
        # dibujar un punto (pixel)
        arcade.draw_point(500, 250, arcade.color.RED, 5)
        # dibujar secuencia de puntos
        arcade.draw_points(
            [(v, v) for v in range(100)],
            arcade.color.YELLOW, 2
        )
        #dibujar una linea
        arcade.draw_line(500, 250, 700, 400, arcade.color.CYAN, 4)
        # dibujar un rectangulo
        arcade.draw_lrbt_rectangle_filled(600, 700, 100, 500, arcade.color.GREEN)

def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    game = PrimitivesView()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()