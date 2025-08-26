extends CharacterBody2D

@export var max_speed: int = 80
@export var friction: int = 500
@export var damage: int = 10
@export var hp: int = 100
@onready var animation_player: AnimationPlayer = $AnimationPlayer

func _physics_process(delta: float) -> void:
	var input_vector = Vector2.ZERO
	input_vector.x = Input.get_axis("left", "right")
	input_vector.y = Input.get_axis("up", "down")
	input_vector = input_vector.normalized()
	
	velocity = max_speed * input_vector
	
	if input_vector != Vector2.ZERO:
		# en movimiento
		animation_player.play("Run")
	else:
		animation_player.play("Idle")
	
	if velocity.x < 0:
		# flip
		$Sprite2D.scale.x = abs($Sprite2D.scale.x) * -1
	if velocity.x > 0:
		$Sprite2D.scale.x = abs($Sprite2D.scale.x)
	move_and_slide()
