import math
ang = float(input('Digite o ângulo que você deseja: '))
rad = math.radians(ang)
print('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(ang, math.sin(rad)))
print('O ângulo de {:.1f} tem o COSSENO de {:.2f}'.format(ang, math.cos(rad)))
print('O ângulo de {:.1f} tem a TANGENTE de {:.2f}'.format(ang, math.tan(rad)))
