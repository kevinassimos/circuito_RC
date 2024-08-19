# SPDX-FileCopyrightText: 2024-present kevinassimos <kevin.assimos@acad.ufsm.br>
#
# SPDX-License-Identifier: MIT
import numpy as np
import matplotlib.pyplot as plt

def calcular_tensao_corrente(V0, R, C, tempo_final, dt):
    t = np.arange(0, tempo_final, dt)
    Vt = V0 * np.exp(-t / (R * C))
    It = (V0 / R) * np.exp(-t / (R * C))
    return t, Vt, It

def plotar_resultado(t, Vt, It):
    plt.figure(figsize=(10, 6))
    
    plt.subplot(2, 1, 1)
    plt.plot(t, Vt, label="Tensão (V)")
    plt.title("Resposta do Circuito RC")
    plt.ylabel("Tensão (V)")
    plt.grid(True)
    
    plt.subplot(2, 1, 2)
    plt.plot(t, It, label="Corrente (A)", color='r')
    plt.xlabel("Tempo (s)")
    plt.ylabel("Corrente (A)")
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
