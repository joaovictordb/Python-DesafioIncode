import numpy as np
import matplotlib.pyplot as plt

# Temperaturas fixas (em °C) para Sao Luis, Maranhao
temperatures = [28.5, 29.0, 30.0, 29.5, 28.0]  # Exemplo de temperaturas fixas

# Periodo total de tempo em horas (correspondente as medicoes de temperatura)
total_time = 5  # Exemplo de um periodo total de 5 horas

# Perguntar ao usuario se deseja alterar os valores de modulação
alterar_modulacao = input("Deseja alterar os valores de modulação de frequência e amplitude? (s/n): ").lower()

# Valores padrao para frequencia da portadora e desvio de frequencia
carrier_freq = 10  # Frequencia da portadora em Hz (padrao)
am_amplitude = 1    # Amplitude da portadora para AM (padrao)
freq_deviation = 5  # Desvio de frequencia em Hz para FM (padrao)

if alterar_modulacao == 's':
    # Solicitar novos valores se o usuário quiser alterar
    carrier_freq = float(input("Informe a nova frequência da portadora (em Hz): "))
    am_amplitude = float(input("Informe o novo valor de amplitude para a modulação AM: "))
    freq_deviation = float(input("Informe o novo valor de desvio de frequência para a modulação FM (em Hz): "))

# Criar o vetor de tempo baseado no total de horas
sampling_rate = 1000  # Numero de amostras por segundo para precisao do grafico
t = np.linspace(0, total_time, total_time * sampling_rate)

# Expandir a variacao de temperatura para a quantidade de amostras
# Isso e feito para garantir que tenhamos um valor de temperatura para cada ponto no tempo.
temp_variation = np.interp(t, np.linspace(0, total_time, len(temperatures)), temperatures)

# Normalizar a variacao da temperatura em torno de zero
temp_variation = temp_variation - np.mean(temp_variation)

# Onda portadora (senoidal pura) com a frequancia especificada
carrier = np.sin(2 * np.pi * carrier_freq * t)

# Modulacao AM: o sinal e modulado pela variacao da temperatura ajustada pela amplitude
am_signal = (1 + am_amplitude * temp_variation) * carrier

# Modulação FM: a frequencia instantanea e ajustada de acordo com a variacao da temperatura
fm_signal = np.sin(2 * np.pi * (carrier_freq * t + freq_deviation * np.cumsum(temp_variation) / sampling_rate))

# Plotar os sinais
plt.figure(figsize=(12, 8))

# Sinal de temperatura
plt.subplot(3, 1, 1)
plt.plot(t, temp_variation)
plt.title("Variação de Temperatura (Sinal de Mensagem)")
plt.xlabel("Tempo (horas)")
plt.ylabel("Variação de Temperatura (°C)")

# Sinal AM
plt.subplot(3, 1, 2)
plt.plot(t, am_signal)
plt.title("Sinal Modulado em Amplitude (AM)")
plt.xlabel("Tempo (segundos)")
plt.ylabel("Amplitude")

# Sinal FM
plt.subplot(3, 1, 3)
plt.plot(t, fm_signal)
plt.title("Sinal Modulado em Frequência (FM)")
plt.xlabel("Tempo (segundos)")
plt.ylabel("Frequência")

plt.tight_layout()
plt.show()