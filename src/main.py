# * LIBRARIES#####################################################
import time
import flet as ft
from flet import *
# * FONT #########################################################
def main(page: Page):
    page.fonts = {"RubikGlitch": "/fonts/RubikGlitch-Regular.ttf"}
    page.theme = Theme(font_family="RubikGlitch")
# * PAGE #########################################################
    page.title = "R E L O J"
    page.theme_mode = 'light'
    page.vertical_alignment = "center"
    page.window_min_width = 1200
    page.window_min_height = 400
    page.window_full_screen = False
# * THEME ########################################################
    def change_theme_on_keyboard(e: KeyboardEvent):
        if e.key == 'D':
            page.theme_mode = 'dark'
            page.update()
        
        elif e.key == 'L':
            page.theme_mode = 'light'
            page.update()

    page.on_keyboard_event = change_theme_on_keyboard
# * FULL SCREEN ##################################################
    def on_keyboard(e: KeyboardEvent):
        if e.key == 'F11':
            page.window_full_screen = True
            page.update()
        elif e.key == 'Escape' and page.window_full_screen == True:
            page.window_full_screen = False
            page.update()
    page.on_keyboard_event = on_keyboard
# * ITEMS ########################################################
    hora = Text(
        f"", size=200,
        # bgcolor="#000000",
        )
    minutos = Text(f"", size=200)
    segundos = Text(f"", size=200)
    PmOAm = Text(f"", size=200)
    Fecha = Text(f"", size=50)
# * PAGE ADD #####################################################
    page.add(
        Container(
            Row(
                controls=[
                    hora,
                    minutos,
                    segundos,
                    PmOAm,
                    
                ],alignment="center",
            )
        ),
        Row(
            controls=[
                Fecha,
            ],alignment="center",
        ),
    )
# * LOOP #########################################################
    while True:
        hrs = time.strftime("%I:", time.localtime())
        mint = time.strftime("%M:", time.localtime())
        segs = time.strftime("%S", time.localtime())
        pm_am = time.strftime(" %p", time.localtime())
        FechaUpdate = time.strftime("%A, %d/%m/%Y", time.localtime())
        
        hora.value = f"{hrs}"
        minutos.value = f"{mint}"
        segundos.value = f"{segs}"
        PmOAm.value = f"{pm_am}"
        Fecha.value = f"{FechaUpdate}"

        page.update()
        time.sleep(1)
# * RUN #########################################################
ft.app(target=main, assets_dir="assets")