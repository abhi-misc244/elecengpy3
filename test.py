import elecengpy
c = elecengpy.elementfile.cableclass()
print ('size is ',c.size)
print ('core is ',c.core)
print ('insulation is ', c.insulation)
print('resistance is ', c.resistance)
print ('reactance is ', c.reactance)
print('nominal diameter is ', c.ndiameter)
print ('Ampacity is ', c.ampacity)
print ('------------------------\n-----------------')
print('Changing size')
c.changesize(25)
print ('size is ',c.size)
print ('core is ',c.core)
print ('insulation is ', c.insulation)
print('resistance is ', c.resistance)
print ('reactance is ', c.reactance)
print('nominal diameter is ', c.ndiameter)
print ('Ampacity is ', c.ampacity)
print ('------------------------\n-----------------')

print('changing insulation')
c.changeinsulation('pvc')
print ('size is ',c.size)
print ('core is ',c.core)
print ('insulation is ', c.insulation)
print('resistance is ', c.resistance)
print ('reactance is ', c.reactance)
print('nominal diameter is ', c.ndiameter)
print ('Ampacity is ', c.ampacity)
print ('------------------------\n-----------------')
