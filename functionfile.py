def flc_three(voltage, power, pf=.8):
    '''
    This function calculates the currrent of a load using voltage and power asuming 3 phase load.
    Power factor is assumed to be 0.8 in case kW is entered by default(if pf variable is not passed). 
    Voltage variable shall contain value such as 415v or 3.3kV. Voltage shall be limited to kV or V.
    Power variable shall contain value such as 120kVA or 200kW. The function will automatically calculate the current based on the units kw or kva. Power shall be limited to kVA, mVA, kW, MW, VA and W.
    The current is returned in Amperes.
    '''
    
    import re 
    v = re.split('(\d+)',voltage) # Spliting the alpha numeric variable into numbers and units
    p = re.split('(\d+)',power) # Spliting the alpha numeric variable into numbers and units
    v_units = v[2]
    p_units = p[2]
    
    if v_units.lower() == 'kv':
        voltage = float(v[1])*1000
    elif v_units.lower() == 'v':
        voltage = float(v[1])
    
    if p_units.lower() == 'kw':
        power = float(p[1])*1000
    elif p_units.lower() == 'mw':
        power = float(p[1])*1000000
    elif p_units.lower() == 'w':
        power = float(p[1])
        
    elif p_units.lower() == 'mva':
        power = float(p[1])*1000000
        pf = 1
    elif p_units.lower() == 'kva':
        power = float(p[1])*1000
        pf = 1
    elif p_units.lower() == 'va':
        power = float(p[1])
        pf = 1
    current = power/(voltage*pf*3**.5) #Current calculation formula for three phase
    return current


def flc_one(voltage, power, pf=.8):
    '''
    This function calculates the currrent of a load using voltage and power asuming 1 phase load.
    Power factor is assumed to be 0.8 in case kW is entered by default(if pf variable is not passed). 
    Voltage variable shall contain value such as 415v or 3.3kV. Voltage shall be limited to kV or V.
    Power variable shall contain value such as 120kVA or 200kW. The function will automatically calculate the current based on the units kw or kva. Power shall be limited to kVA, mVA, kW, MW, VA and W.
    The current is returned in Amperes.
    '''
    import re
    v = re.split('(\d+)',voltage) # Spliting the alpha numeric variable into numbers and units
    p = re.split('(\d+)',power) # Spliting the alpha numeric variable into numbers and units
    v_units = v[2]
    p_units = p[2]
    
    if v_units.lower() == 'kv':
        voltage = float(v[1])*1000
    elif v_units.lower() == 'v':
        voltage = float(v[1])
    
    if p_units.lower() == 'kw':
        power = float(p[1])*1000
    elif p_units.lower() == 'mw':
        power = float(p[1])*1000000
    elif p_units.lower() == 'w':
        power = float(p[1])
        
    elif p_units.lower() == 'mva':
        power = float(p[1])*1000000
        pf = 1
    elif p_units.lower() == 'kva':
        power = float(p[1])*1000
        pf = 1
    elif p_units.lower() == 'va':
        power = float(p[1])
        pf = 1
    current = power/(voltage*pf) #Current calculation formula for 1 phase
    return current 

#print flc_three('415v', '100kva',.9)


def vd_three(resistance, reactance, current, pf=0.8):
    import math
    vd = (resistance*pf+reactance*math.sin(math.acos(pf)))* current * 3**.5
    return vd #three phase voltage drop in phase to phase volts


def vd_one(resistance, reactance, current, pf=0.8):
    import math
    vd = (resistance*pf+reactance*math.sin(math.acos(pf)))* current
    return vd #single phase votage drop








'''
This is a calculation template of 3 phase symetrical fault

This requires Y matrix, number of buses, faulted bus where 3 phase fault is located and voltage at the bus before fault.
At first Z matririx is calculated using Y matrix.
Following this V before fault is calculated and stored in Vd
Then 3 phase faulted current is calculated and stored in If matrix
Following that Vafter fault and I after fault is calculated and stored in V_after_fault and I matrix
'''
def three_fault_cal(Ybus, faulted_bus):
   import numpy
   number_of_bus = int(Ybus.size**.5)
   Z = numpy.linalg.inv(Ybus)
   '''    
   #Example specific Y bus, Change after test run
   Y = numpy.empty([4,4],'complex')

   Y[0,0] = complex(0,-16.212)
   Y[0,1] = complex(0,5)
   Y[0,2] = complex(0,0)
   Y[0,3] = complex(0,6.667)

   Y[1,0] = complex(0,5)
   Y[1,1] = complex(0,-12.5)
   Y[1,2] = complex(0,5)
   Y[1,3] = complex(0,2.5)

   Y[2,0] = complex(0,0)
   Y[2,1] = complex(0,5)
   Y[2,2] = complex(0,-13.33)
   Y[2,3] = complex(0,5)

   Y[3,0] = complex(0,6.667)
   Y[3,1] = complex(0,2.5)
   Y[3,2] = complex(0,5)
   Y[3,3] = complex(0,-14.167)
   '''
   #example specific variables, add as function later
   faulted_bus = 2 # Where the fault is located
   v_before_fault = 1.00 #in per unit for faulted bus only
   number_of_bus = int( Ybus.size**.5)
       
   #Calculation of Vdelta
   Vd =  numpy.zeros([number_of_bus,1],'complex')
   Vd[ faulted_bus-1]= v_before_fault

   #Calculation of Impedance matrix
   Z = numpy.linalg.inv( Ybus)

   #Calculation of fault current
   If = numpy.zeros([number_of_bus,1],'complex')
   If[ faulted_bus-1] = Vd[ faulted_bus-1]/Z[ faulted_bus-1, faulted_bus-1]

   #Calculation of voltage matrix after fault
   V_after_fault = numpy.zeros([number_of_bus,1],'complex')
   for i in range(0, number_of_bus):
      V_after_fault[i] = (1-Z[i, faulted_bus-1]/Z[ faulted_bus-1, faulted_bus-1])*Vd[ faulted_bus-1]
      if i ==  faulted_bus-1:
          V_after_fault[i] = complex(0,0)

   #Calculation of I after fault
   I = numpy.zeros([number_of_bus,number_of_bus],'complex')

   for i in range(0,number_of_bus-1):
      for j in range(0,number_of_bus-1):
          I[i,j] = - Ybus[i,j]*(V_after_fault[i,0]-V_after_fault[j,0])

   If = I
   Vf = V_after_fault
   return  If       





















