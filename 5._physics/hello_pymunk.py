import pymunk

# crear space
space = pymunk.Space()
space.gravity = (0, -9)

# crear body
body = pymunk.Body()
body.position = (50, 100)
body.mass = 1

# Crear shape
shape = pymunk.Poly.create_box(body)

# agregar al space
space.add(body, shape)

print_options = pymunk.SpaceDebugDrawOptions()

for _ in range(100):
    space.step(0.02) # 50FPS
    space.debug_draw(print_options)