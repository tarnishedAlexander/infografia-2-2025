extends CharacterBody2D

# SIGNALS
signal health_changed(new_health: int)
signal power_activated()
signal power_deactivated()
signal power_time_updated(time_left: float)

# PROPERTIES
@export var speed: float = 300.0
@export var jump_velocity: float = -400.0
@export var max_health: int = 100

var gravity: float = ProjectSettings.get_setting("physics/2d/default_gravity")
@onready var state_machine = $AnimationTree.get("parameters/playback")

var health: int
var has_gem: bool = false
var has_key: bool = false
var gem_timer: Timer

enum {
	WALK,
	DUCK,
	JUMP,
	IDLE
}

var state = IDLE

func _ready() -> void:
	health = max_health
	add_to_group("player")
	print("Player initialized. has_gem: ", has_gem, ", has_key: ", has_key)
	
	# Create gem timer
	gem_timer = Timer.new()
	gem_timer.wait_time = 2.0  # 2 seconds
	gem_timer.one_shot = true
	gem_timer.timeout.connect(_on_gem_timer_timeout)
	add_child(gem_timer)

func _physics_process(delta: float) -> void:
	# Test key for health system - press H to take damage
	if Input.is_action_just_pressed("ui_down"):
		take_damage(10)
		print("Manual damage test - Health: ", health)
	
	# add gravity
	if not is_on_floor():
		velocity.y += gravity * delta
		state_machine.travel("Jump")
		
	if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		velocity.y = jump_velocity
		state_machine.travel("Jump")
		
	var direction = Input.get_axis("ui_left", "ui_right")
	if direction:
		velocity.x = direction * speed
		state_machine.travel("Walk")
		if direction < 0:
			$Sprite2D.scale.x = abs($Sprite2D.scale.x) * -1
		elif direction > 0:
			$Sprite2D.scale.x = abs($Sprite2D.scale.x)
	else:
		velocity.x = move_toward(velocity.x, 0, speed)
		state_machine.travel("Idle")
		
	move_and_slide()


func _process(delta: float) -> void:
	# Update power timer display
	if has_gem and gem_timer.time_left > 0:
		power_time_updated.emit(gem_timer.time_left)

func _on_hurtbox_area_entered(area: Area2D) -> void:
	print("OUCH!")

func take_damage(amount: int) -> void:
	health -= amount
	print("Player health: ", health)
	health_changed.emit(health)
	if health <= 0:
		die()

func die() -> void:
	print("Player died!")
	# Reset position or restart level
	global_position = Vector2(100, 100)  # Reset to starting position
	health = max_health
	health_changed.emit(health)

func can_stomp_enemies() -> bool:
	return has_gem

func collect_gem() -> void:
	has_gem = true
	gem_timer.start()
	power_activated.emit()
	print("Gem collected! Can now stomp enemies for 2 seconds! has_gem = ", has_gem)

func _on_gem_timer_timeout() -> void:
	has_gem = false
	power_deactivated.emit()
	print("Gem power expired! can no longer stomp enemies")

func collect_key() -> void:
	has_key = true
	print("Key collected! Can now open doors! has_key = ", has_key)

func can_open_doors() -> bool:
	return has_key
