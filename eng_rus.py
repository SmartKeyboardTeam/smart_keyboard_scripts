import pyautogui as pg

# language switcher
# pg.hotkey('ctrl', 'a')
# pg.PAUSE = 2
# pg.hotkey('ctrl', 'c')
# pg.PAUSE = 2
pg.hotkey('Win')
pg.PAUSE = 0.5
pg.typewrite('https://gsgen.ru/tools/perevod-raskladki-online/\n', 0.01)
pg.moveTo(800, 600)
pg.click()
pg.PAUSE = 0.5
pg.hotkey('ctrl', 'v')
pg.moveTo(900, 650)
pg.click()
