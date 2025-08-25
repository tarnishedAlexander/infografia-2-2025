extends Node2D

# GAME STATE
@export var time_limit: int = 15

var score: int = 0
var time_left: int = 0
var total_coins: int = 0

# Node references
@export var player: CharacterBody2D
@export var coins_container: Node2D
@export var score_label: Label
@export var timer_label: Label
@export var message_label: Label
@export var game_timer: Timer

# initialization
func _ready() -> void:
	total_coins = coins_container.get_child_count()
	
	# connect coinst signals
	for coin in coins_container.get_children():
		coin.collected.connect(on_coin_collected)
		
	game_timer.timeout.connect(on_game_timer_timeout)
	
	start_game()
	
func start_game():
	score = 0
	time_left = time_limit
	score_label.text = "Score: " + str(score)
	timer_label.text = "Time: " + str(time_left)
	message_label.hide()
	
	game_timer.start(time_limit)
	get_tree().paused = false
	
# signal handlers
func on_coin_collected():
	score += 1
	score_label.text = "Score: " + str(score)
	
	if score == total_coins:
		message_label.text = "You Win!"
		message_label.show()
		game_timer.stop()
		get_tree().paused = true
		
func on_game_timer_timeout():
	message_label.text = "Game Over"
	message_label.show()
	get_tree().paused = true
	
func _process(delta: float) -> void:
	if not get_tree().paused:
		timer_label.text = "Time: " + str(int(game_timer.time_left))
