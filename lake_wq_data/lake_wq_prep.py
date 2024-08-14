#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 16:30:33 2022

@author: mike
"""
import pandas as pd
import numpy as np
from gistools import vector
import geopandas as gpd

import utils, params

pd.options.display.max_columns = 10


############################################
### Summaries

date = pd.Timestamp.now().strftime('%Y-%m-%d')

ts_combo_list = []
stn_combo_list = []
stn_mtype_combo_list = []
for file in params.lake_wq_files:
    data = pd.read_csv(params.base_path.joinpath(file), compression='zip')

    stn_data0 = data[['Region', 'Agency', 'LawaSiteID', 'SiteID', 'CouncilSiteID', 'Latitude', 'Longitude', 'LFENZID', 'GeomorphicLType', 'LType']].drop_duplicates(subset=['LawaSiteID']).copy()
    stn_data_geo = vector.xy_to_gpd('LawaSiteID', 'Longitude', 'Latitude', stn_data0, 4326)
    stn_data = stn_data_geo.merge(stn_data0.drop(['Latitude', 'Longitude'], axis=1), on='LawaSiteID')
    stn_combo_list.append(stn_data)

    stn_mtype = data[['LawaSiteID', 'Indicator', 'Units', 'RawValue']].groupby(['LawaSiteID', 'Indicator', 'Units']).RawValue.count()
    stn_mtype.name = 'value_count'
    stn_mtype = stn_mtype.reset_index()
    stn_mtype_combo_list.append(stn_mtype)

    ## Process the TS data
    ts_data0 = data[['LawaSiteID', 'Indicator', 'SampleDateTime', 'RawValue', 'QCRaw', 'QCNumber', 'QCNEMSEquivalent', 'Symbol', 'Value']].copy()

    ## Convert values to numeric
    ts_data0['Value'] = pd.to_numeric(ts_data0['Value'], errors='coerce')

    ## Convert RawValue to string
    ts_data0['RawValue'] = ts_data0['RawValue'].astype(str)

    ## convert timestamps
    ts_data0['SampleDateTime'] = pd.to_datetime(ts_data0['SampleDateTime'], dayfirst=True, infer_datetime_format=True)

    ## Save data
    ts_combo_list.append(ts_data0)

ts_data0 = pd.concat(ts_combo_list).sort_values(['LawaSiteID', 'Indicator', 'SampleDateTime']).reset_index(drop=True)

# ts_data0['RawValue'] = ts_data0.RawValue.astype(str)
ts_data0['QCRaw'] = pd.to_numeric(ts_data0['QCRaw'], errors='coerce')
ts_data0['QCNumber'] = pd.to_numeric(ts_data0['QCNumber'], errors='coerce')
ts_data0['QCNEMSEquivalent'] = pd.to_numeric(ts_data0['QCNEMSEquivalent'], errors='coerce')

stn_data0 = pd.concat(stn_combo_list).sort_values(['LawaSiteID'])
stn_data0.loc[stn_data0['LFENZID'] < 1, 'LFENZID'] = None

stn_mtype_data0 = pd.concat(stn_mtype_combo_list).sort_values(['LawaSiteID', 'Indicator']).drop_duplicates(['LawaSiteID', 'Indicator'])

## Add in the nzsegment values
# segs_df = pd.read_csv(params.lawa_to_nzseg_path).rename(columns={'wq_lawa_site_id': 'LawaSiteID'})
# stn_data1 = stn_data0.merge(segs_df, on='LawaSiteID', how='inner')

## Lakes polygons
lakes_poly0 = gpd.read_file(params.lakes_poly_gpkg)
lakes_poly1 = lakes_poly0.drop(['OBJECTID', 'Shape_Length', 'Shape_Area'], axis=1).rename(columns={'LID': 'LFENZID'}).copy()

### Save data
stn_data0.to_file(params.stn_data_raw_path)
stn_mtype_data0.to_csv(params.ds_data_raw_path, index=False)
ts_data0.to_csv(params.ts_data_raw_csv_path, index=False, compression='zip')
utils.df_to_feather(ts_data0, params.ts_data_raw_feather_path)
lakes_poly1.to_file(params.stn_poly_gpkg)








