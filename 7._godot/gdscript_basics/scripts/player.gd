extends CharacterBody2D

# propiedades
var player_name: String = "Mario"

@export var speed: int = 300
@export var health: int = 100

@export_range(0, 500, 10) var jump_force: int = 250

func _ready() -> void:
	print("speed: ", speed)
	print("health: ", health)
	print("jump force: ", jump_force)

func _physics_process(delta: float) -> void:
	var direction = Input.get_axis("ui_left", "ui_right")
	
	if direction:
		velocity.x = direction * speed
	else:
		velocity.x = move_toward(velocity.x, 0, speed)
	
	move_and_slide()
	
func take_damage(amount: int):
	health -= amount
	print("Player took damage! current health: ", health)
	
	if health <= 0:
		print("Player defeated")
		hide()
