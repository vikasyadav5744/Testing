import pandas as pd
import streamlit as st
import numpy as np

rest = {
    'calloi': [2500, 6500, 7600, 8700, 6000, 6700, 6200, 7700, 5500],
    'callvol': [6000, 6700, 4300, 6500, 18000, 6700, 15000, 7600, 7800],
    'strike': [25000, 25050, 25100, 25150, 25200, 25250, 25300, 25350, 25400],
    'spot': [25187] * 9,
}
data = pd.DataFrame(rest)

# FIX: Use .iloc[0] or .max() to get the scalar value instead of a Series
cemax_strike = data.loc[data['calloi'] == data['calloi'].max(), 'strike'].iloc[0]
volmax_strike = data.loc[data['callvol'] == data['callvol'].max(), 'strike'].iloc[0]

# Assigning these to the dataframe for reference
data['cemaxstr'] = cemax_strike
data['volcemaxstr'] = volmax_strike

# Define conditions
conds = [
    (data['spot'] < data['cemaxstr']) & (data['spot'] < data['volcemaxstr']) & (data['cemaxstr'] > data['volcemaxstr']),
    (data['spot'] < data['cemaxstr']) & (data['spot'] < data['volcemaxstr']) & (data['cemaxstr'] < data['volcemaxstr'])
]

choice = ['Volume is resistance', 'OI is resistance']

# Apply np.select
data['status'] = np.select(conds, choice, default='No Clear Resistance')
st.write(data)
