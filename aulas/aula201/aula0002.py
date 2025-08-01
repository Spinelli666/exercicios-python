# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton('Clique aqui!')
botao.setStyleSheet('background-color: red; color: white; font-size: 20px;')
botao.show() # Adiciona o widget na hierarquia e exibe a janela

# botao2 = QPushButton('Clique aqui também!')
# botao2.show()

app.exec() # O loop da aplicação