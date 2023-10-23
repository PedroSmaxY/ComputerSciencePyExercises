met = float(input('Uma distância em metros: '))
km = met/1000
hm = met/100
dam = met/10
dm = met*10
cm = met*100
mm = met*1000
print('A medida de {}m corresponde a:'.format(met))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))
