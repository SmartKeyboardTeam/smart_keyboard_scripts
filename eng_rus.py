import pyautogui as pg

# language switcher
# pg.hotkey('ctrl', 'a')
# pg.PAUSE = 2
# pg.hotkey('ctrl', 'c')
# pg.PAUSE = 2
pg.hotkey('Win')
pg.PAUSE = 0.5
pg.typewrite('Google\n', 0.1)
pg.typewrite('https://gsgen.ru/tools/perevod-raskladki-online/\n')
pg.moveTo(800,500)
pg.click()
pg.hotkey('ctrl', 'v')
pg.moveTo(900,650)
pg.click()
