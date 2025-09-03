extends Control

@export var healthbar: TextureProgressBar


func _on_h_slider_value_changed(value: float) -> void:
	healthbar.value = value
