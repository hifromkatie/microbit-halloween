input.onButtonPressed(Button.A, function () {
    ghost.showColor(neopixel.colors(NeoPixelColors.Red))
})
input.onButtonPressed(Button.B, function () {
    ghost.showColor(neopixel.colors(NeoPixelColors.Blue))
})
input.onButtonPressed(Button.AB, function () {
    ghost.showColor(neopixel.colors(NeoPixelColors.Green))
})
input.onGesture(Gesture.Shake, function () {
    ghost.showColor(neopixel.colors(NeoPixelColors.Yellow))
})
input.onGesture(Gesture.ScreenDown, function () {
    ghost.showColor(neopixel.colors(NeoPixelColors.Purple))
})
let ghost: neopixel.Strip = null
ghost = neopixel.create(DigitalPin.P0, 1, NeoPixelMode.RGB_RGB)
ghost.showColor(neopixel.colors(NeoPixelColors.White))
basic.forever(function () {

})
