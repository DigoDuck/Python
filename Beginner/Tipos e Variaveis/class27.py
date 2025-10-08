# Constante = variáveis que não vão mudar

velocidade = 60 # Velocidade do carro
local_carro = 101 # Local em que o carro está

RADAR_1 = 60  # Velocidade máxima do radar
LOCAL_1 = 100 # Local em que o radar está posicionado
RADAR_RANGE = 1 # A distância que o radar pega


vel_carro_pass_rad1 = velocidade > RADAR_1
carro_passou_rad1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado = vel_carro_pass_rad1 and carro_passou_rad1

if vel_carro_pass_rad1:
    print("Carro está acima da velocidade máxima da via")

if carro_passou_rad1:
    print("Carro passou radar 1")

if  carro_multado and vel_carro_pass_rad1:
    print("Carro multado em radar 1")