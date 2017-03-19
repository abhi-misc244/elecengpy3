class cableclass(object):
    def __init__(self,size= 16, core='3c+e', insulation='xlpe', length=0.1, install='conduit'):
        self.size = size
        self.core = core
        self.insulation = insulation
        self.length = length
        self.install = install
        self.updatedata()

    def updatedata(self):
        import elecengpy
        import csv

        #f = elecengpy.datafile.mcore_xlpe_res_data()

        if (self.core == '2c+e' or '3c+e' or'4c+e' or 'multicore') and (self.insulation.lower() == 'xlpe'):
            f = elecengpy.datafile.mcore_xlpe_res_data()
        elif (self.core == '2c+e' or '3c+e' or'4c+e' or 'multicore') and    (self.insulation.lower() == 'pvc'):
            f = elecengpy.datafile.mcore_pvc_res_data()
        elif (self.core == '1c' or 'single core') and (self.insulation.lower() == 'xlpe'):
            f = elecengpy.datafile.score_xlpe_res_data()
        elif (self.core == '1c' or 'single core') and (self.insulation.lower() == 'pvc'):
            f = elecengpy.datafile.score_pvc_res_data()
        elif self.insulation.lower() == 'aerial':
            f = elecengpy.datafile.aerial_res_data()
            self.size = 'Almond'
            #print (f)

        reader = csv.reader(f)
        table = list(reader)
        del table[0]
        del table[0]
        i = 0
        row = 0
        for x in table:
            if str(self.size).lower() == x[0].lower():
                row = i
            i = i+1
        #print (row)
        #print (table)
        self.reactance = float(table[row][1]) * self.length
        self.resistance = float(table[row][2]) * self.length

        if (self.core == '2c+e' or '3c+e' or'4c+e' or 'multicore') and (self.insulation =='pvc') and (self.install == 'unenclosed'):
            f = elecengpy.datafile.mcore_pvc_unenclosed_amp()
        elif (self.core == '2c+e' or '3c+e' or'4c+e' or 'multicore') and (self.insulation =='pvc') and (self.install == 'direct buried'):
            f = elecengpy.datafile.mcore_pvc_dburied_amp()
        elif (self.core == '2c+e' or '3c+e' or'4c+e' or 'multicore') and (self.insulation =='pvc') and (self.install == 'conduit'):
            f = elecengpy.datafile.mcore_pvc_conduit_amp()
        elif (self.core == '2c+e' or '3c+e' or'4c+e' or 'multicore') and (self.insulation =='xlpe') and (self.install == 'unenclosed'):
            f = elecengpy.datafile.mcore_xlpe_unenclosed_amp()
        elif (self.core == '2c+e' or '3c+e' or'4c+e' or 'multicore') and (self.insulation =='xlpe') and (self.install == 'direct buried'):
            f = elecengpy.datafile.mcore_xlpe_dburied_amp()
        elif (self.core == '2c+e' or '3c+e' or'4c+e' or 'multicore') and (self.insulation =='xlpe') and (self.install == 'conduit'):
            f = elecengpy.datafile.mcore_xlpe_conduit_amp()
        elif (self.core == '1c' or 'singlecore') and (self.insulation =='pvc') and (self.install == 'unenclosed'):
            f = elecengpy.datafile.score_pvc_unenclosed_amp()
        elif (self.core == '1c' or 'singlecore') and (self.insulation =='pvc') and (self.install == 'direct buried'):
            f = elecengpy.datafile.score_pvc_dburied_amp()
        elif (self.core == '1c' or 'singlecore') and (self.insulation =='pvc') and (self.install == 'conduit'):
            f = elecengpy.datafile.score_pvc_conduit_amp()
        elif (self.core == '1c' or 'singlecore') and (self.insulation =='xlpe') and (self.install == 'unenclosed'):
            f = elecengpy.datafile.score_xlpe_unenclosed_amp()
        elif (self.core == '1c' or 'singlecore') and (self.insulation =='xlpe') and (self.install == 'direct buried'):
            f = elecengpy.datafile.score_xlpe_dburied_amp()
        elif (self.core == '1c' or 'singlecore') and (self.insulation =='xlpe') and (self.install == 'conduit'):
            f = elecengpy.datafile.score_xlpe_conduit_amp()

        reader = csv.reader(f)
        table = list(reader)
        del table[0]
        i = 0
        row = 0
        for x in table:
            if self.size == float(x[0]):
                self.ampacity = float(x[1])

        f = elecengpy.datafile.earthsize()

        reader = csv.reader(f)
        table = list(reader)
        del table[0]
        del table[0]
        i = 0
        row = 0
        for x in table:
            if self.size == float(x[0]):
                self.earthsize = float(x[1])



    def changesize(self, size):
        '''
        size shall be passed in number
        '''
        self.size = size

        self.updatedata()

    def changelength(self, var):
        #Length shall be passed in kilometers
        print ('something here')
        '''self.length = var
        #self.updatedata()
        print ('the length is ', self.length)'''
    def changecore(self, core):
        '''
        core shall be passed in string
        '''
        self.core = core
        self.updatedata()
    def changeinsulation(self, insulation):
        '''
        insulation shall be passed in string
        '''
        self.insulation = insulation
        if self.insulation == 'aerial':
            self.size = 'Almond'
        self.updatedata()
    def changeinstall(self, install):
        self.install = install
        self.updatedata()
    def currentresize(self, current):
        '''
        resize cable based on current
        '''
        size = [2.5,4,6,10,16,25,35,50,70,95,120,240,300,400,500,630]
        for i in size:
            if float(self.ampacity)<current:
                self.changesize(i)
    def calcvdthree(self, current, pf=0.8):
        import math
        return ((self.resistance*pf+self.reactance*math.sin(math.acos(pf)))* current * 3**.5)
    def vdthreeresize(self, current):
        '''
        resize cable based on current
        '''
        size = [2.5,4,6,10,16,25,35,50,70,95,120,240,300,400,500,630]
        self.changesize(2.5)
        for i in size:
            if self.calcvdthree(current) > 415*.05:
                self.changesize(i)

    def faultloop(self, current):
        '''
        Calculate the fault loop length
        '''
        self.lmax = 0.8* self.size *240*self.earthsize/(current * .0225 *(self.size+self.earthsize))
        return self.lmax

    def faultloopresize(self, current, distance=100):
        '''
        resize cable based on current
        '''
        size = [2.5,4,6,10,16,25,35,50,70,95,120,240,300,400,500,630]
        self.changesize(2.5)
        for i in size:
            if self.faultloop(current) < distance:
                self.changesize(i)


    def printdata(self):
        print (self.size, "mm2 ", self.insulation,  self.core)
        print (self.resistance, "ohm + i* " ,self.reactance)
        print (self.length, "km long")



class loadclass():
    def __init__(self,power='100kva', voltage='415v', pf=0.8):
        self.power = power
        self.voltage = voltage
        self.pf = pf
        self.updatepower(power)
        self.updatevoltage(voltage)
    def updatevoltage(self, voltage):
        import re
        v = re.split('(\d+)',voltage)
        v_units = v[2]
        if v_units.lower() == 'kv':
            voltage = float(v[1])*1000
        elif v_units.lower() == 'v':
            voltage = float(v[1])

        self.voltage = voltage
    def updatepower(self, power):
        import re
        p = re.split('(\d+)',power)
        p_units = p[2]
        if p_units.lower() == 'kw':
            power = float(p[1])*1000
        elif p_units.lower() == 'mw':
            power = float(p[1])*1000000
        elif p_units.lower() == 'w':
            power = float(p[1])
        elif p_units.lower() == 'mva':
            power = float(p[1])*1000000*self.pf
        elif p_units.lower() == 'kva':
            power = float(p[1])*1000*self.pf
        elif p_units.lower() == 'va':
            power = float(p[1])*self.pf
        self.power = power

class transformerclass():
    def __init__(self, power=2500, vhv=11000,vlv=415, xdp=0.05):
        self.power = power #power in kva
        self.vhv = vhv # voltage in volts
        self.vlv = vlv # voltage in volts
        self.xdp = xdp
        self.update()
    def update(self):
        self.scpower = self.power / self.xdp
        self.imphv = self.vhv**2 / self.power
        self.puimplv = self.vlv**2 / self.power
        self.hvi = self.power / (self.vhv * 3**.5) *1000
        self.lvi = self.power / (self.vlv * 3**.5) * 1000
        self.schvi = self.hvi / self.xdp
        self.sclvi = self.lvi / self.xdp
        def updatepower(self, power):
            '''
            Power shall be passed in in kva
            '''
            self.power = power
            self.update()
        def updatevhv(self, vhv):
            '''
            Voltage shall be passed in in Volts
            '''
            self.vhv = vhv
            self.update()
        def updatevlv(self, vlv):
            '''
            Voltage shall be passed in in Volts
            '''
            self.vlv = vlv
            self.update()
        def updatexdp(self, xdp):
            '''
            Percentage Impedance shall be passed in percentage. For example 5 Percent shall be passed as 0.05
            '''
            self.xdp = xdp
            self.update()
