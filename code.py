
import pandas as pd 
import numpy as np
import streamlit as st

df1 = {
    'Spot_Price': [25187]*4, 
    'cemaxstr': [25250]*4, 
    'volcemaxstr': [25250]*4, 
    'volcesevent5str': [25400]*4, 
    'cesevent5str': [25450]*4
}
df = pd.DataFrame(df1)

# Base logic used in many conditions
base_res = (df['Spot_Price'] < df['cemaxstr']) & (df['Spot_Price'] < df['volcemaxstr']) & (df['cemaxstr'] == df['volcemaxstr'])

# REORDERED: Most specific (complex) conditions first
conditions = [
    # 6. Both WTT, OI75 > VOL75
    base_res & (df['cemaxstr'] < df['cesevent5str']) & (df['cesevent5str'] > df['volcesevent5str']) & (df['volcemaxstr'] < df['volcesevent5str']),
    
    # 5. Both WTT, OI75 < VOL75
    base_res & (df['cemaxstr'] < df['cesevent5str']) & (df['cesevent5str'] < df['volcesevent5str']) & (df['volcemaxstr'] < df['volcesevent5str']),
    
    # 4. Both WTT (General)
    base_res & (df['cemaxstr'] < df['cesevent5str']) & (df['volcemaxstr'] < df['volcesevent5str']),
    
    # 3. Only OI WTT
    base_res & (df['cemaxstr'] < df['cesevent5str']),
    
    # 2. Only Vol WTT
    base_res & (df['volcemaxstr'] < df['volcesevent5str']),
    
    # 1. Simple Strong Resistance (The "Catch-all" for the base case)
    base_res
]

choices = [
    'Resistance is WTT- (OI and vol both WTT OI7t5 > Vol7t5)',
    'Resistance is WTT- (OI and vol both WTT OI7t5 < Vol7t5)',
    'Resistance is WTT- (OI and vol both WTT)',
    'OI and VOLUME both is resistance- (OI WTT)',
    'OI and VOLUME both is resistance- (vol WTT)',
    'OI and VOLUME both is resistance'
]

# Apply np.select
df['resistance_status'] = np.select(conditions, choices, default='No clear Resistance')

st.dataframe(df)


# Base logic used in many conditions
base_res = (df['Spot_Price'] < df['cemaxstr']) & (df['Spot_Price'] < df['volcemaxstr']) & (df['cemaxstr'] == df['volcemaxstr'])

# REORDERED: Most specific (complex) conditions first
conditions = [
    # 6. Both WTT, OI75 > VOL75
    base_res & (df['cemaxstr'] < df['cesevent5str']) & (df['cesevent5str'] > df['volcesevent5str']) & (df['volcemaxstr'] < df['volcesevent5str']),
    
    # 5. Both WTT, OI75 < VOL75
    base_res & (df['cemaxstr'] < df['cesevent5str']) & (df['cesevent5str'] < df['volcesevent5str']) & (df['volcemaxstr'] < df['volcesevent5str']),
    
    # 4. Both WTT (General)
    base_res & (df['cemaxstr'] < df['cesevent5str']) & (df['volcemaxstr'] < df['volcesevent5str']),
    
    # 3. Only OI WTT
    base_res & (df['cemaxstr'] < df['cesevent5str']),
    
    # 2. Only Vol WTT
    base_res & (df['volcemaxstr'] < df['volcesevent5str']),
    
    # 1. Simple Strong Resistance (The "Catch-all" for the base case)
    base_res
]

choices = [
    'Resistance is WTT- (OI and vol both WTT OI7t5 > Vol7t5)',
    'Resistance is WTT- (OI and vol both WTT OI7t5 < Vol7t5)',
    'Resistance is WTT- (OI and vol both WTT)',
    'OI and VOLUME both is resistance- (OI WTT)',
    'OI and VOLUME both is resistance- (vol WTT)',
    'OI and VOLUME both is resistance'
]

# Apply np.select
df['resistance_status'] = np.select(conditions, choices, default='No clear Resistance')

