import cv2
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import random
from dis_graph2 import vid2dens
#import matplotlib.pyplot as plt


# Deisgning of Traffic for generating multiple data
# define function to develop fuzzy Systems

def fuzzy_sys(d):

   # function to generate still traffic for One direction e.g. North
        #a0 =ini() 
        #print( "car::",a0[0]," ","Motorcycle::",a0[1],"  ","Truck::",a0[2]," ","Bicycle::",a0[3]," ","Bus::",a0[4])

    # calculating density based on experimental results
        #s1=(a0[0]+(int(a0[1]/2))+a0[2]+(int(a0[3]/3))+a0[4])
 
 # function to generate Queue traffic for One direction e.g. North
 # calculating density based on experimental results
        #a1=ini()
        #q1=(a1[0]+(int(a1[1]/2))+a1[2]+(int(a1[3]/3))+a1[4])

        #print( "car::",a1[0]," ","Motorcycle::",a1[1],"  ","Truck::",a1[2]," ","Bicycle::",a1[3]," ","Bus::",a1[4])
        #print(d)
        #vd = vid2dens(d)
        #global i
        if d == "N":
            #pathIn= './images/N/'
            #i=1
            vd = vid2dens(d)
        elif d == "E":
            #pathIn= './images/E/'
            #i=2
            vd = vid2dens(d)
        elif d == "W":
            #pathIn= './images/W/'
            #i=3
            vd = vid2dens(d)

        elif d == "S": 
            #pathIn= './images/S/'
            #i=4
            vd = vid2dens(d)

        
        # Define Fix timing to be set at each signal
        fx=50
        
        s1= vd["s1"]
        q1= vd["q1"]

        # Printing Density of still and Queue traffic
        print("s1::", s1,"Q1::", q1,"FX::", fx)
        
        if s1+q1 <= 0:
            fx=10
            dt1=0
        else :


    # Setting boundaries for membership function for traffic density and delta( change in signal timing increase or decrease)

            stl_traf = ctrl.Antecedent(np.arange(0, 50, 1), 'stl_traf')

            que_traf = ctrl.Antecedent(np.arange(0, 50, 1), 'que_traf')

            dt = ctrl.Consequent(np.arange(-30,30, 1), 'dt')


            stl_traf['few'] = fuzz.trapmf(stl_traf.universe,[0, 5,10, 15])
            stl_traf['small'] = fuzz.trapmf(stl_traf.universe,[11,16,21, 26])
            stl_traf['medium'] = fuzz.trapmf(stl_traf.universe, [23,28,33,38])
            stl_traf['many'] = fuzz.trapmf(stl_traf.universe, [35, 40,45, 50])

            #stl_traf.view()

            que_traf['few'] = fuzz.trapmf(que_traf.universe, [0, 5,10, 15])
            que_traf['small'] = fuzz.trapmf(que_traf.universe, [11,16,21,26])
            que_traf['medium'] = fuzz.trapmf(que_traf.universe, [23,28,33,38])
            que_traf['many'] = fuzz.trapmf(que_traf.universe, [35, 40,45,50])

            #que_traf.view()


            dt['vlow']= fuzz.trimf(dt.universe, [-30, -24,-18])
            dt['zero']= fuzz.trimf(dt.universe, [-20, -13, -5])
            dt['low'] = fuzz.trimf(dt.universe, [-8, 0, 8])
            dt['medium'] = fuzz.trimf(dt.universe, [5, 13, 20])
            dt['high'] = fuzz.trimf(dt.universe, [18, 24, 30])
            #dt.View()			 

    # Generating optimized rules or fuzzy inference sys forgetting accurate delta values

            rule1 = ctrl.Rule(stl_traf['few'] & que_traf['few'] , dt['vlow'])

            rule2 = ctrl.Rule(stl_traf['few'] & que_traf['small'] , dt['vlow'])

            rule3 = ctrl.Rule( stl_traf['small'] & que_traf['few'], dt['vlow'])

            rule4 = ctrl.Rule( stl_traf['few'] & que_traf['medium'], dt['zero'])

            rule5 = ctrl.Rule( stl_traf['small'] & que_traf['small'], dt['zero'])

            rule6 = ctrl.Rule( stl_traf['medium']& que_traf['few'], dt['zero'])


            rule7 = ctrl.Rule( stl_traf['medium'] &  que_traf['small'] , dt['low'])

            rule8 = ctrl.Rule( stl_traf['small'] & que_traf['medium'], dt['low'])

            rule9 = ctrl.Rule(stl_traf['few'] & que_traf['many'], dt['low'])

            rule10 = ctrl.Rule(stl_traf['many'] & que_traf['few'], dt['low'])

            rule11 = ctrl.Rule(stl_traf['small'] & que_traf['many'] , dt['medium'])

            rule12 = ctrl.Rule(stl_traf['medium'] & que_traf['medium'] , dt['medium'])

            rule13 = ctrl.Rule(stl_traf['many'] & que_traf['small'] , dt['medium'])

            rule14 = ctrl.Rule(stl_traf['many'] & que_traf['medium'], dt['high'])

            rule15 = ctrl.Rule( stl_traf['medium'] & que_traf['many'] , dt['high'])

            rule16 = ctrl.Rule( stl_traf['many'] & que_traf['many'] , dt['high'])


    #Setting up fuzzy control system with rules


            dt_ctrl = ctrl.ControlSystem([rule1, rule2, rule3,rule4,rule5,  rule6, rule7,rule8,rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16])

            delta = ctrl.ControlSystemSimulation(dt_ctrl)

            delta.input['stl_traf'] = s1

            delta.input['que_traf'] = q1

            # Crunch the numbers

            delta.compute()

            dt1 = int(delta.output['dt']) 

            #updating Signal timing value or dynamic signal timing
            fx = int(fx+ dt1)

        print("Total Signal Time(Sec)::", fx , " " ,"Delta Change (Sec)::", dt1)
        #dt.view(sim=delta)
        #plt.show()


        # Rteurns the Traffic density, updated signal timing along with delta
        fz = {"s1": s1,
              "q1": q1,
              "fx": fx,
              "dt1":dt1}
        return fz

