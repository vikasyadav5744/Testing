import streamlit as st
import pandas as pd

rest = {'calloi':[2500,6500,7600,8700,10000,6700,6200,7700,5500],
       'callvol':[6000,6700,4300,6500,6600,6700,15000,7600,7800],
        'strike':[25000,25050,25100,25150,25200,25250,25300,25350,25400],
         'spot':[25187,25187,25187,25187,25187,25187,25187,25187,25187],
       }
data= pd.DataFrame(rest)
data['cemax']=data['calloi'].max()
data['volcemax']=data['calloi'].max()
data['volcemaxstr']=data.loc[data['callvol']==data['callvol'].max(),'strike']
data['cemaxstr']=data.loc[data['calloi']==data['calloi'].max(),'strike']

conds=[data['spot']<data['cemaxstr']<data['volcemaxstr']]

choice=['OI ressistace at']

data['status']= np.select(conds,choice, default='strong')


st.write(data)
