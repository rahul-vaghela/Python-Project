
# import all libaray to support functions

from fuzzy_ctrl_sys import fuzzy_sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dis_graph import dis_sig
import serial

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
STdt1 = []
STds =[]
STs1 = []
STq1 = []
sf_traf_sat =[]
Straffic_sat = []

ETfx = []
ETr = []
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
for i in range(10):
     N_T = fuzzy_sys('N')
     S_T = fuzzy_sys('S')
     W_T = fuzzy_sys('W')
     E_T = fuzzy_sys('E')

     fxx.append(n)
     TCT = N_T["fx"]+S_T["fx"]+E_T["fx"]+W_T["fx"]

     NTs1.append(N_T["s1"])
     NTq1.append(N_T["q1"])
     ntds = N_T["s1"]+N_T["q1"]
     ntr = (TCT - N_T["fx"])+(YLT*3)
     NTfx.append(N_T["fx"])
     NTr.append(ntr)
     NTdt1.append(N_T["dt1"])  
     NTds.append(ntds)
     NT_sat =  100- (np.sum((np.log(ntds)- np.log(N_T["fx"]))**2))
     nf_t_sat = 100 - (np.sum((np.log(ntds)- np.log(n))**2))
     nf_traf_sat.append(nf_t_sat)
     Ntraffic_sat.append(NT_sat)
     
     STs1.append(S_T["s1"])
     STq1.append(S_T["q1"])
     stds = S_T["s1"]+S_T["q1"]
     str = (TCT - S_T["fx"])+(YLT*3)
     STfx.append(S_T["fx"])
     STr.append(str)
     STdt1.append(S_T["dt1"])  
     STds.append(stds)
     ST_sat = 100-( np.sum((np.log(stds)- np.log(S_T["fx"]))**2))
     sf_t_sat = 100-(np.sum((np.log(stds)- np.log(n))**2))
     sf_traf_sat.append(sf_t_sat)
     Straffic_sat.append(ST_sat)
     
     ETs1.append(E_T["s1"])
     ETq1.append(E_T["q1"])
     etds = E_T["s1"]+E_T["q1"]
     etr = (TCT - E_T["fx"])+(YLT*3)
     ETfx.append(E_T["fx"])
     ETr.append(etr)
     ETdt1.append(E_T["dt1"])  
     ETds.append(etds)
     ET_sat =  100-(np.sum((np.log(etds)- np.log(E_T["fx"]))**2))
     ef_t_sat = 100-(np.sum((np.log(etds)- np.log(n))**2))
     ef_traf_sat.append(ef_t_sat)
     Etraffic_sat.append(ET_sat)
     
     WTs1.append(W_T["s1"])
     WTq1.append(W_T["q1"])
     wtds = W_T["s1"]+W_T["q1"]
     wtr = (TCT - W_T["fx"])+(YLT*3)
     WTfx.append(W_T["fx"])
     WTr.append(wtr)
     WTdt1.append(W_T["dt1"])  
     WTds.append(wtds)
     WT_sat =  100 - (np.sum((np.log(wtds)- np.log(W_T["fx"]))**2))
     wf_t_sat = 100 - (np.sum((np.log(wtds)- np.log(n))**2))
     wf_traf_sat.append(wf_t_sat)
     Wtraffic_sat.append(WT_sat)
     
     
     dis_sig(N_T["fx"],ntr,N_T["dt1"],S_T["fx"],str,S_T["dt1"],E_T["fx"],etr,E_T["dt1"],W_T["fx"],wtr,W_T["dt1"])
          
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
'Nyello time': YLT,
'North Traffic rd Timing':NTr,		      
 
'South Traffic Gr Timing':STfx,
'Syello time': YLT,
'South Traffic rd Timing':STr,		      

'East Traffic Gr Timing':ETfx,
'Eyello time': YLT,
'East Traffic rd Timing':ETr,		      

'West Traffic Gr Timing':WTfx,
'Wyello time': YLT,
'West Traffic rd Timing':WTr,		      

                       })





#sorting data in frame by density 
  
rs=df.sort_values("North Traffic Density", axis=0,ascending=True,inplace=False, kind='quicksort')

# Subpoltting and gca stands for 'get current axis'

df.to_csv("my7.csv",index=False)

rs1 = rs.head(1)




print(df1)
plt.figure()

plt.subplot(221)
ax1 = plt.gca()
rs.plot.line("North Traffic Density",'North Sat_Traf_fix',ax=ax1)

rs.plot.line("North Traffic Density",'North Saturation of Traffic',ax=ax1)
plt.grid(True)

rs=df.sort_values("South Traffic Density", axis=0,ascending=True,inplace=False, kind='quicksort')

plt.subplot(222)
ax2 = plt.gca()

rs.plot.line("South Traffic Density","South Sat_Traf_fix", ax=ax2)

rs.plot.line("South Traffic Density","South Saturation of Traffic" , ax=ax2)
plt.grid(True)

rs=df.sort_values("East Traffic Density", axis=0,ascending=True,inplace=False, kind='quicksort')

plt.subplot(223)

ax3 = plt.gca()

rs.plot.line("East Traffic Density",'East Sat_Traf_fix', ax=ax3)

rs.plot.line("East Traffic Density",'East Saturation of Traffic', ax=ax3)
plt.grid(True)

rs=df.sort_values("West Traffic Density", axis=0,ascending=True,inplace=False, kind='quicksort')

plt.subplot(224)

ax4 = plt.gca()

rs.plot.line("West Traffic Density",'West Sat_Traf_fix', ax=ax4)

rs.plot.line("West Traffic Density",'West Saturation of Traffic', ax=ax4)
plt.grid(True)


#plt.figure()
#rs=df.sort_values("North Traffic Density", axis=0,ascending=True,inplace=False, kind='quicksort')

#plt.subplot(221)
#ax1 = plt.gca()
#rs.plot.line("North Traffic Density",'North Traffic Delta',ax=ax1)
#rs.plot.line("North Traffic Density",'North Traffic Gr Timing',ax=ax1)

#plt.grid(True)






#print(rs['North Traffic Density'], rs['North Traffic Gr Timing'])


#rs.plot(x= 'North Traffic rd Timing', y=["North Traffic Density", "North Traffic Gr Timing","Fix Time"], kind="bar")



        

plt.tight_layout()
plt.show()