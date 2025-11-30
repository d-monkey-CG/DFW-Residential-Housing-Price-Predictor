import pandas as pd

# DCAD 2021 Joined script

file_path_appr = '/DCAD2021_CURRENT/ACCOUNT_APPRL_YEAR.CSV'
file_path_info = '/DCAD2021_CURRENT/ACCOUNT_INFO.CSV'
file_path_detail = '/DCAD2021_CURRENT/RES_DETAIL.CSV'

cols_needed_appr = ['ACCOUNT_NUM', 'LAND_VAL', 'TOT_VAL']
cols_needed_info = ['ACCOUNT_NUM', 'APPRAISAL_YR', 'STREET_NUM', 'STREET_HALF_NUM', 'FULL_STREET_NAME', 'PROPERTY_ZIPCODE']
cols_needed_detail = ['ACCOUNT_NUM', 'YR_BUILT', 'TOT_MAIN_SF', 'POOL_IND']

df_appr = pd.read_csv(file_path_appr, usecols=cols_needed_appr, low_memory=False)
df_info = pd.read_csv(file_path_info, usecols=cols_needed_info, low_memory=False)
df_detail = pd.read_csv(file_path_detail, usecols=cols_needed_detail, low_memory=False)

df_merged = df_appr.merge(df_info, on='ACCOUNT_NUM', how='left')
df_merged = df_merged.merge(df_detail, on='ACCOUNT_NUM', how='left')

df_merged.to_csv('DCAD_Joined_2021.csv', index=False)

# DCAD 2022 Joined script

file_path_appr = '/DCAD2022_CURRENT/ACCOUNT_APPRL_YEAR.CSV'
file_path_info = '/DCAD2022_CURRENT/ACCOUNT_INFO.CSV'
file_path_detail = '/DCAD2022_CURRENT/RES_DETAIL.CSV'

cols_needed_appr = ['ACCOUNT_NUM', 'LAND_VAL', 'TOT_VAL']
cols_needed_info = ['ACCOUNT_NUM', 'APPRAISAL_YR', 'STREET_NUM', 'STREET_HALF_NUM', 'FULL_STREET_NAME', 'PROPERTY_ZIPCODE']
cols_needed_detail = ['ACCOUNT_NUM', 'YR_BUILT', 'TOT_MAIN_SF', 'POOL_IND']

df_appr = pd.read_csv(file_path_appr, usecols=cols_needed_appr, low_memory=False)
df_info = pd.read_csv(file_path_info, usecols=cols_needed_info, low_memory=False)
df_detail = pd.read_csv(file_path_detail, usecols=cols_needed_detail, low_memory=False)

df_merged = df_appr.merge(df_info, on='ACCOUNT_NUM', how='left')
df_merged = df_merged.merge(df_detail, on='ACCOUNT_NUM', how='left')

df_merged.to_csv('DCAD_Joined_2022.csv', index=False)

# DCAD 2023 Joined script

file_path_appr = '/DCAD2023_CURRENT/ACCOUNT_APPRL_YEAR.CSV'
file_path_info = '/DCAD2023_CURRENT/ACCOUNT_INFO.CSV'
file_path_detail = '/DCAD2023_CURRENT/RES_DETAIL.CSV'

cols_needed_appr = ['ACCOUNT_NUM', 'LAND_VAL', 'TOT_VAL']
cols_needed_info = ['ACCOUNT_NUM', 'APPRAISAL_YR', 'STREET_NUM', 'STREET_HALF_NUM', 'FULL_STREET_NAME', 'PROPERTY_ZIPCODE']
cols_needed_detail = ['ACCOUNT_NUM', 'YR_BUILT', 'TOT_MAIN_SF', 'POOL_IND']

df_appr = pd.read_csv(file_path_appr, usecols=cols_needed_appr, low_memory=False)
df_info = pd.read_csv(file_path_info, usecols=cols_needed_info, low_memory=False)
df_detail = pd.read_csv(file_path_detail, usecols=cols_needed_detail, low_memory=False)

df_merged = df_appr.merge(df_info, on='ACCOUNT_NUM', how='left')
df_merged = df_merged.merge(df_detail, on='ACCOUNT_NUM', how='left')

df_merged.to_csv('DCAD_Joined_2023.csv', index=False)

# DCAD 2024 Joined script

file_path_appr = '/DCAD2024_CURRENT/ACCOUNT_APPRL_YEAR.CSV'
file_path_info = '/DCAD2024_CURRENT/ACCOUNT_INFO.CSV'
file_path_detail = '/DCAD2024_CURRENT/RES_DETAIL.CSV'

cols_needed_appr = ['ACCOUNT_NUM', 'LAND_VAL', 'TOT_VAL']
cols_needed_info = ['ACCOUNT_NUM', 'APPRAISAL_YR', 'STREET_NUM', 'STREET_HALF_NUM', 'FULL_STREET_NAME', 'PROPERTY_ZIPCODE']
cols_needed_detail = ['ACCOUNT_NUM', 'YR_BUILT', 'TOT_MAIN_SF', 'POOL_IND']

df_appr = pd.read_csv(file_path_appr, usecols=cols_needed_appr, low_memory=False)
df_info = pd.read_csv(file_path_info, usecols=cols_needed_info, low_memory=False)
df_detail = pd.read_csv(file_path_detail, usecols=cols_needed_detail, low_memory=False)

df_merged = df_appr.merge(df_info, on='ACCOUNT_NUM', how='left')
df_merged = df_merged.merge(df_detail, on='ACCOUNT_NUM', how='left')

df_merged.to_csv('DCAD_Joined_2024.csv', index=False)

# DCAD 2025 Joined script

file_path_appr = '/DCAD2025_CURRENT/ACCOUNT_APPRL_YEAR.CSV'
file_path_info = '/DCAD2025_CURRENT/ACCOUNT_INFO.CSV'
file_path_detail = '/DCAD2025_CURRENT/RES_DETAIL.CSV'

cols_needed_appr = ['ACCOUNT_NUM', 'LAND_VAL', 'TOT_VAL']
cols_needed_info = ['ACCOUNT_NUM', 'APPRAISAL_YR', 'STREET_NUM', 'STREET_HALF_NUM', 'FULL_STREET_NAME', 'PROPERTY_ZIPCODE']
cols_needed_detail = ['ACCOUNT_NUM', 'YR_BUILT', 'TOT_MAIN_SF', 'POOL_IND']

df_appr = pd.read_csv(file_path_appr, usecols=cols_needed_appr, low_memory=False)
df_info = pd.read_csv(file_path_info, usecols=cols_needed_info, low_memory=False)
df_detail = pd.read_csv(file_path_detail, usecols=cols_needed_detail, low_memory=False)

df_merged = df_appr.merge(df_info, on='ACCOUNT_NUM', how='left')
df_merged = df_merged.merge(df_detail, on='ACCOUNT_NUM', how='left')

df_merged.to_csv('DCAD_Joined_2025.csv', index=False)
