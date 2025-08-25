extends Area2D

# SIGNAL DEFINITION
signal coin_collected(value)

@export var coin_value: int = 10

func _on_body_entered(body):
	# body sea un player
	print("touched!")
	if body.player_name == "Mario":
		print("coin touched by player")
		emit_signal("coin_collected", coin_value)
		queue_free()
