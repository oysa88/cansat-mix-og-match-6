def on_button_pressed_a():
    global gjennomsnittshøyde
    gjennomsnittshøyde = (Per + Pål + Espen + Kongen + Prinsessen) / 5
    basic.show_number(gjennomsnittshøyde)
    basic.show_string("cm")
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

gjennomsnittshøyde = 0
Per = 178
Pål = 181
Espen = 172
Kongen = 180
Prinsessen = 162


