// As discussed at Code Club on 13-06-2024
input.onButtonPressed(Button.A, function () {
    trigger_number += -50
})
function Decide_whether_to_water () {
    // Problem - keeps calling the watering function so it never stops.
    if (moisture_measure > trigger_number) {
        water_the_plant()
    }
}
function water_the_plant () {
    for (let index = 0; index < 4; index++) {
        pins.servoWritePin(AnalogPin.P0, 80)
        basic.pause(2000)
        pins.servoWritePin(AnalogPin.P0, 0)
        basic.pause(2000)
    }
}
input.onSound(DetectedSound.Loud, function () {
    led.plotBarGraph(
    moisture_measure,
    1023
    )
})
input.onButtonPressed(Button.AB, function () {
    moisture_measure = pins.analogReadPin(AnalogPin.P1)
    basic.showString("M ")
    basic.showNumber(moisture_measure)
    Decide_whether_to_water()
})
input.onButtonPressed(Button.B, function () {
    trigger_number += 50
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showString("T ")
    basic.showNumber(trigger_number)
})
let moisture_measure = 0
let trigger_number = 0
trigger_number = 700
basic.forever(function () {
    moisture_measure = pins.analogReadPin(AnalogPin.P1)
    Decide_whether_to_water()
    basic.pause(300000)
})
