input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    gjennomsnittshøyde = (Per + Pål + Espen + Kongen + Prinsessen) / 5
    basic.showNumber(gjennomsnittshøyde)
    basic.showString("cm")
    basic.clearScreen()
})
let gjennomsnittshøyde = 0
let Per = 178
let Pål = 181
let Espen = 172
let Kongen = 180
let Prinsessen = 162
