nome = str(input('Digite seu nome completo: ')).strip().split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[-1]))
#O [-1] significa o ultimo elemento da lista.
#O [-2] significa o penultimo e assim vai..
#O [0] representa o primeiro.