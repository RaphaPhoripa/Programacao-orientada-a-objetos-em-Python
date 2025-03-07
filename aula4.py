import pyautogui
import time
import subprocess

# Passo 1: Abrir o Bloco de Notas
subprocess.Popen(['notepad.exe'])

# Passo 2: Esperar um pouco para garantir que o Bloco de Notas abriu
time.sleep(2)

# Passo 3: Digitar a mensagem
pyautogui.write('Meu robo esta vivo e esta fazendo analises de dados', interval=0.1)

# Passo 4: Aguardar 5 segundos para visualizar
time.sleep(5)

# Passo 5: Fechar o Bloco de Notas
#pyautogui.hotkey('alt', 'f4'
# )

# Passo 6: Confirmar para não salvar, se necessário
time.sleep(1)
pyautogui.press('left')  # Seleciona "Não salvar"
pyautogui.press('enter')