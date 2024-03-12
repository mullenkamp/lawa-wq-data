#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 16:30:33 2022

@author: mike
"""
import pandas as pd
import os
import geopandas as gpd

import utils, params

pd.options.display.max_columns = 10


############################################
### Summaries

date = pd.Timestamp.now().strftime('%Y-%m-%d')

ts_data0 = pd.read_feather(params.ts_data_raw_feather_path)
stn_data0 = gpd.read_file(params.stn_data_raw_path)
stn_mtype_data0 = pd.read_csv(params.ds_data_raw_path)

## Remove duplicates
ts_data0 = pd.merge(stn_data0[['LawaSiteID', 'Agency']], ts_data0.dropna(subset=['RawValue']), on='LawaSiteID')

grp = ts_data0.groupby(['LawaSiteID', 'Indicator', 'SampleDateTime'])

other1 = grp[['Agency', 'QCRaw', 'QCNumber', 'QCNEMSEquivalent', 'Symbol', 'RawValue']].first()
values1 = grp['Value (numeric)'].mean()
values1.name = 'Value (numeric)'

ts_data1 = pd.concat([other1, values1], axis=1).reset_index()

## Remove datetimes at 00:00:00
ts_data2 = ts_data1[ts_data1['SampleDateTime'].dt.time.apply(lambda x: x.isoformat()) != '00:00:00'].copy()

## Correct time shifting issues
bad_rcs = ['Auckland Council', 'Bay of Plenty Regional Council', 'Waikato Regional Council']
bad_rcs_bool = ts_data2.Agency.isin(bad_rcs)

ts_data2.loc[bad_rcs_bool, 'SampleDateTime'] = ts_data2.loc[bad_rcs_bool, 'SampleDateTime'] + pd.DateOffset(hours=12)

# Samples outside of normal sampling times
late_times_bool = ts_data2['SampleDateTime'].dt.hour >= 19
ts_data2.loc[late_times_bool, 'SampleDateTime'] = ts_data2.loc[late_times_bool, 'SampleDateTime'] - pd.DateOffset(hours=12)

early_times_bool = ts_data2['SampleDateTime'].dt.hour <= 5
ts_data2.loc[early_times_bool, 'SampleDateTime'] = ts_data2.loc[early_times_bool, 'SampleDateTime'] + pd.DateOffset(hours=12)

### Save data
ts_data3 = ts_data2.drop('Agency', axis=1).reset_index(drop=True)

stn_data1 = stn_data0[stn_data0.LawaSiteID.isin(ts_data3.LawaSiteID.unique())]
stn_mtype_data1 = pd.merge(ts_data3[['LawaSiteID', 'Indicator']].drop_duplicates(['LawaSiteID', 'Indicator']), stn_mtype_data0, on=['LawaSiteID', 'Indicator'])

stn_data1.to_file(params.stn_data_path)
stn_mtype_data1.to_csv(params.ds_data_path, index=False)
ts_data3.to_csv(params.ts_data_csv_path, index=False, compression='zip')
utils.df_to_feather(ts_data3, params.ts_data_feather_path)









