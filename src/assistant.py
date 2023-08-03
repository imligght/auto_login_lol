import pyautogui as pyag
import time

time.sleep(5)
print(pyag.position())


# não posso continuar me baseando em tempo para executar os comandos, pois,
# isso vai variar muito de computador para computador. Preciso encontrar uma maneira de
# detectar quando a janela foi inicializada.