import arcade

WIDTH = 1280
HEIGHT = 720
TITLE = "hola game loop"

class HelloView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.YELLOW
        self.a_pressed = False
        self.r_pressed = False

    def on_draw(self):
        self.clear()
        if self.a_pressed and self.r_pressed:
            self.background_color = arcade.color.MAGENTA
        elif self.a_pressed and not self.r_pressed:
            self.background_color = arcade.color.YELLOW
        elif not self.a_pressed and self.r_pressed:
            self.background_color = arcade.color.BLUE
        else:
            self.background_color = arcade.color.RED

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.A:
            self.a_pressed = True
        elif symbol == arcade.key.R:
            self.r_pressed = True

    
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.A:
            self.a_pressed = False
        elif symbol == arcade.key.R:
            self.r_pressed = False

            


def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    game = HelloView()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()