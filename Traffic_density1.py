
# import all libaray to support functions

from fuzzy_ctrl_sys2 import fuzzy_sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dis_graph1 import dis_sig
import serial
#import concurrent.futures

# Generating multiple list to store all key data

fxx = []

n=50
YLT =2

NTfx = []
NTr = []
NTdt1 = []
NTds =[]
NTs1 = []
NTq1 = []
nf_traf_sat =[]
Ntraffic_sat = []

STfx = []
STr = []
STrbg =[]
STdt1 = []
STds =[]
STs1 = []
STq1 = []
sf_traf_sat =[]
Straffic_sat = []

ETfx = []
ETr = []
ETrbg =[]
ETdt1 = []
ETds =[]
ETs1 = []
ETq1 = []
ef_traf_sat =[]
Etraffic_sat = []

WTfx = []
WTr = []
WTdt1 = []
WTds =[]
WTs1 = []
WTq1 = []
wf_traf_sat =[]
Wtraffic_sat = []

     
    
    
# generating velue for 10 instances
for i in range(1):
     N_T = fuzzy_sys('N')
     E_T = fuzzy_sys('E')
     W_T = fuzzy_sys('W')
     S_T = fuzzy_sys('S')

     fxx.append(n)
     TCT = N_T["fx"]+S_T["fx"]+E_T["fx"]+W_T["fx"]

     NTs1.append(N_T["s1"])
     NTq1.append(N_T["q1"])
     ntds = N_T["s1"]+N_T["q1"]
     ntr = S_T["fx"]+E_T["fx"]+W_T["fx"]+YLT+YLT+YLT
     NTfx.append(N_T["fx"])
     NTr.append(ntr)
     NTdt1.append(N_T["dt1"])  
     NTds.append(ntds)
     NT_sat =  100-(np.sum((np.log(ntds)- np.log(N_T["fx"]))**2))
     nf_t_sat = 100- (np.sum((np.log(ntds)- np.log(n))**2))
     nf_traf_sat.append(nf_t_sat)
     Ntraffic_sat.append(NT_sat)
     

     STs1.append(S_T["s1"])
     STq1.append(S_T["q1"])
     stds = S_T["s1"]+S_T["q1"]
     str = N_T["fx"]+E_T["fx"]+W_T["fx"]++YLT+YLT+YLT
     strbg = N_T["fx"]+YLT
     STfx.append(S_T["fx"])
     STr.append(str)
     STrbg.append(strbg)
     STdt1.append(S_T["dt1"])  
     STds.append(stds)
     ST_sat = 100-( np.sum((np.log(stds)- np.log(S_T["fx"]))**2))
     sf_t_sat = 100-(np.sum((np.log(ntds)- np.log(n))**2))
     sf_traf_sat.append(sf_t_sat)
     Straffic_sat.append(ST_sat)
     
     ETs1.append(E_T["s1"])
     ETq1.append(E_T["q1"])
     etds = E_T["s1"]+E_T["q1"]
     etr = N_T["fx"]+S_T["fx"]+W_T["fx"]++YLT+YLT+YLT
     etrbg = N_T["fx"]++S_T["fx"]+YLT+YLT
     ETfx.append(E_T["fx"])
     ETr.append(etr)
     ETrbg.append(etrbg)
     ETdt1.append(E_T["dt1"])  
     ETds.append(etds)
     ET_sat =  100-(np.sum((np.log(stds)- np.log(E_T["fx"]))**2))
     ef_t_sat = 100-(np.sum((np.log(ntds)- np.log(n))**2))
     ef_traf_sat.append(ef_t_sat)
     Etraffic_sat.append(ET_sat)
     
     WTs1.append(W_T["s1"])
     WTq1.append(W_T["q1"])
     wtds = W_T["s1"]+W_T["q1"]
     wtr = N_T["fx"]+S_T["fx"]+E_T["fx"]++YLT+YLT+YLT
     WTfx.append(W_T["fx"])
     WTr.append(wtr)
     WTdt1.append(W_T["dt1"])  
     WTds.append(wtds)
     WT_sat =  100 - (np.sum((np.log(stds)- np.log(W_T["fx"]))**2))
     wf_t_sat = 100 - (np.sum((np.log(ntds)- np.log(n))**2))
     wf_traf_sat.append(wf_t_sat)
     Wtraffic_sat.append(WT_sat)
     
     
     dis_sig(N_T["fx"],ntr,ntr,S_T["fx"],strbg,str,E_T["fx"],etrbg,etr,W_T["fx"],wtr,wtr)
          
     # For Meaasuring accuracy though 'Q'
     #T_sat = 100 - np.mean(np.abs(N_T["fx"]- ntds)) * 100
     #f_t_sat = 100 - np.mean(np.abs(n- ntds)) * 100
     
     # For Meaasuring accuracy though 'ln(Q)'
     #T_sat =  -np.log(ntds/N_T["fx"])
     #f_t_sat = -np.log(ntds/n)

     # For Meaasuring accuracy though 'sum(ln(Q)**2)'

     
     #T_sat =  np.sum((np.log(ntds/N_T["fx"]))**2)
     #f_t_sat = np.sum((np.log(ntds/n))**2)


#creating data-frame

df = pd.DataFrame({ 'Fix Time': fxx,
'North Traffic Gr Timing':NTfx,
'North Traffic rd Timing':NTr,		      
'North Traffic Delta':NTdt1,
'North Traffic Density':NTds,
'North Saturation of Traffic':Ntraffic_sat,
'North Sat_Traf_fix':nf_traf_sat ,
  
'South Traffic Gr Timing':STfx,
'South Traffic rd Timing':STr,		      
'South Traffic Delta':STdt1,
'South Traffic Density':STds,
'South Saturation of Traffic':Straffic_sat,
'South Sat_Traf_fix': sf_traf_sat,

'East Traffic Gr Timing':ETfx,
'East Traffic rd Timing':ETr,		      
'East Traffic Delta':ETdt1,
'East Traffic Density':ETds,
'East Saturation of Traffic':Etraffic_sat,
'East Sat_Traf_fix': ef_traf_sat,

'West Traffic Gr Timing':WTfx,
'West Traffic rd Timing':WTr,		      
'West Traffic Delta':WTdt1,
'West Traffic Density':WTds,
'West Saturation of Traffic':Wtraffic_sat,
'West Sat_Traf_fix': wf_traf_sat,

                       })
df1 = pd.DataFrame({ 
'North Traffic Gr Timing':NTfx,
'North Traffic rd Timing1':NTr,
'North Traffic rd Timing':NTr,		      
 
'South Traffic Gr Timing':STfx,
'South Traffic rd Timing Before Green':STrbg,
'South Traffic rd Timing':STr,		      

'East Traffic Gr Timing':ETfx,
'East Traffic rd Timing Before Green':ETrbg,
'East Traffic rd Timing':ETr,
		      

'West Traffic Gr Timing':WTfx,
'West Traffic rd Timing1':WTr,
'West Traffic rd Timing':WTr,

'Yellow Time':YLT,		      

                       })





#sorting data in frame by density 
  
rs=df.sort_values("North Traffic Density", axis=0,ascending=True,inplace=False, kind='quicksort')

# Subpoltting and gca stands for 'get current axis'

#df1.to_csv("my2.csv",index=False)

rs1 = rs.head(1)


d= df1.values.tolist()

print(d[0])
#print(d[1,:])

s = serial.Serial("COM4",115200 , timeout=4)
to_send = d[0]
#[62,120,120,38,64,144,38,104,144,38,144,144,2]

a_var=bytearray(to_send)

s.write(a_var[:])



#for r in d:
#    for t in r:
#        print(hex(t))
plt.figure()

plt.subplot(221)
ax1 = plt.gca()
rs.plot.line("North Traffic Density",'North Sat_Traf_fix',ax=ax1)

rs.plot.line("North Traffic Density",'North Saturation of Traffic',ax=ax1)
plt.grid(True)


plt.subplot(222)
ax2 = plt.gca()

rs.plot.line("South Traffic Density","South Sat_Traf_fix", ax=ax2)

rs.plot.line("South Traffic Density","South Saturation of Traffic" , ax=ax2)
plt.grid(True)

plt.subplot(223)

ax3 = plt.gca()

rs.plot.line("East Traffic Density",'East Sat_Traf_fix', ax=ax3)

rs.plot.line("East Traffic Density",'East Saturation of Traffic', ax=ax3)
plt.grid(True)

plt.subplot(224)

ax4 = plt.gca()

rs.plot.line("West Traffic Density",'West Sat_Traf_fix', ax=ax4)

rs.plot.line("West Traffic Density",'West Saturation of Traffic', ax=ax4)
plt.grid(True)








#print(rs['North Traffic Density'], rs['North Traffic Gr Timing'])


#rs.plot(x= 'North Traffic rd Timing', y=["North Traffic Density", "North Traffic Gr Timing","Fix Time"], kind="bar")



        

plt.tight_layout()
plt.show()