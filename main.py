# As discussed at Code Club on 13-06-2024

def on_button_pressed_a():
    global trigger_number
    trigger_number += -50
input.on_button_pressed(Button.A, on_button_pressed_a)

def Decide_whether_to_water():
    # Problem - keeps calling the watering function so it never stops.
    if moisture_measure > trigger_number:
        water_the_plant()
def water_the_plant():
    for index in range(4):
        pins.servo_write_pin(AnalogPin.P0, 80)
        basic.pause(2000)
        pins.servo_write_pin(AnalogPin.P0, 0)
        basic.pause(2000)

def on_sound_loud():
    led.plot_bar_graph(moisture_measure, 1023)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_button_pressed_ab():
    global moisture_measure
    moisture_measure = pins.analog_read_pin(AnalogPin.P1)
    basic.show_string("M ")
    basic.show_number(moisture_measure)
    Decide_whether_to_water()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global trigger_number
    trigger_number += 50
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    basic.show_string("T ")
    basic.show_number(trigger_number)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

moisture_measure = 0
trigger_number = 0
trigger_number = 700

def on_forever():
    global moisture_measure
    moisture_measure = pins.analog_read_pin(AnalogPin.P1)
    Decide_whether_to_water()
    basic.pause(300000)
basic.forever(on_forever)
