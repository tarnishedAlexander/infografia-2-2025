extends CharacterBody2D

@export var target: Node2D = null
@export var max_speed = 50

func setup():
	await get_tree().physics_frame

func _ready() -> void:
	call_deferred("setup")
	
func _physics_process(delta: float) -> void:
	
	move_and_slide()
