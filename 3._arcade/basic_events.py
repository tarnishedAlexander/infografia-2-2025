import arcade

WIDTH = 1280
HEIGHT = 720
TITLE = "eventos arcade"

class CircleCharacter:
    def __init__(self, x0, y0, r=50, color=arcade.color.RED):
        self.x = x0
        self.y = y0
        self.r = r
        self.color = color
    
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.color)

class EventsView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.YELLOW
        # estado de la app
        self.char = CircleCharacter(WIDTH // 2, HEIGHT // 2)
        self.speed = 4
        self.stroke_points = []

    # 1. atencion de eventos
    def on_key_press(self, symbol, modifiers):
        ## teclado / joystick
        if symbol == arcade.key.UP:
            # 2. actualizacion del estado
            self.char.y += self.speed
        elif symbol == arcade.key.DOWN:
            self.char.y -= self.speed

    def on_mouse_press(self, x, y, button, modifiers):
        print(f"boton presionado! {button} en posicion: {x}, {y}")
        self.stroke_points = []
        # self.char.x = x
        # self.char.y = y
    def on_mouse_drag(self, x, y, dx, dy, _buttons, _modifiers):
        # print(f"arrastrando! {_buttons} en posicion: {x},{y}, con velocidad: {dx},{dy}")
        self.stroke_points.append((x, y))

    def on_mouse_release(self, x, y, button, modifiers):
        self.char.x = x
        self.char.y = y
        

    def draw_stroke(self):
        arcade.draw_line_strip(self.stroke_points, arcade.color.GREEN, 3)
    # 3. renderizacion
    def on_draw(self):
        self.clear()
        self.char.draw()
        self.draw_stroke()
    


def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    game = EventsView()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()