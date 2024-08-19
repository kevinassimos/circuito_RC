# SPDX-FileCopyrightText: 2024-present kevinassimos <kevin.assimos@acad.ufsm.br>
#
# SPDX-License-Identifier: MIT
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
from circuito import calcular_tensao_corrente, plotar_resultado
import csv
from PyQt5.QtWidgets import QFileDialog

class CircuitoRCApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Simulação Circuito RC")
        layout = QVBoxLayout()

        # Labels e caixas de entrada para parâmetros
        self.label_v0 = QLabel("Tensão Inicial (V0):")
        self.input_v0 = QLineEdit()

        self.label_r = QLabel("Resistência (R) [Ω]:")
        self.input_r = QLineEdit()

        self.label_c = QLabel("Capacitância (C) [F]:")
        self.input_c = QLineEdit()

        self.label_tempo = QLabel("Tempo Final (s):")
        self.input_tempo = QLineEdit()

        self.label_dt = QLabel("Intervalo de Tempo (dt) [s]:")
        self.input_dt = QLineEdit()

        # Botão para executar a simulação
        self.btn_simular = QPushButton("Simular")
        self.btn_simular.clicked.connect(self.simular)
        
        self.save_button = QPushButton("Salvar CSV")
        layout.addWidget(self.save_button)
        self.save_button.clicked.connect(self.salvar_csv)

        # Layout
        layout.addWidget(self.label_v0)
        layout.addWidget(self.input_v0)
        layout.addWidget(self.label_r)
        layout.addWidget(self.input_r)
        layout.addWidget(self.label_c)
        layout.addWidget(self.input_c)
        layout.addWidget(self.label_tempo)
        layout.addWidget(self.input_tempo)
        layout.addWidget(self.label_dt)
        layout.addWidget(self.input_dt)
        layout.addWidget(self.btn_simular)

        self.setLayout(layout)

    def simular(self):
        V0 = float(self.input_v0.text())
        R = float(self.input_r.text())
        C = float(self.input_c.text())
        tempo_final = float(self.input_tempo.text())
        dt = float(self.input_dt.text())

        self.t, self.Vt, self.It = calcular_tensao_corrente(V0, R, C, tempo_final, dt)
        plotar_resultado(self.t, self.Vt, self.It)
        
    def salvar_csv(self):
        # Diálogo para escolher onde salvar o arquivo
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo CSV", "", "CSV Files (*.csv);;All Files (*)", options=options)
    
        if file_path:  # Verifique se o caminho foi definido corretamente
            # Dados que serão salvos
            headers = ["Tempo (s)", "Tensão (V)", "Corrente (A)"]
            rows = list(zip(self.t, self.Vt, self.It))

            # Escrevendo os dados no arquivo CSV
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(rows)
        
            print(f"Dados salvos em {file_path}")
        else:
            print("Caminho do arquivo não foi definido.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircuitoRCApp()
    ex.show()
    sys.exit(app.exec_())
