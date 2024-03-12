#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:34:11 2024

@author: mike
"""
import pathlib
import os


#################################################3
### Parameters

script_path = pathlib.Path(os.path.realpath(os.path.dirname(__file__)))
base_path = script_path.parent.joinpath('data')

river_wq_files = ['lawa-riverwqmonitoringdata_north-island-2004-2022_1of2.csv.zip', 'lawa-riverwq_monitoringdata_north-island-2004-2022-2of2.csv.zip', 'lawa-riverwq_monitoringdata_south-island-2004-2022.csv.zip']

lawa_to_nzseg_path = base_path.joinpath('lawa_to_nzsegment.csv')

## RAW data
stn_data_raw_path = base_path.joinpath('lawa_river_wq_field_samples_sites_raw.gpkg')
ts_data_raw_csv_path = base_path.joinpath('lawa_river_wq_field_samples_ts_raw.csv.zip')
ds_data_raw_path = base_path.joinpath('lawa_river_wq_field_samples_sites_mtypes_raw.csv')
ts_data_raw_feather_path = base_path.joinpath('lawa_river_wq_field_samples_ts_raw.feather')

## Summaries
midnight_summ_csv = base_path.joinpath('lawa_river_wq_field_samples_midnight.csv')
hour_summ_csv = base_path.joinpath('lawa_river_wq_field_samples_hour_count.csv')
outside_summ_csv = base_path.joinpath('lawa_river_wq_field_samples_outside.csv')

## Cleaned data
stn_data_path = base_path.joinpath('lawa_river_wq_field_samples_sites.gpkg')
ts_data_csv_path = base_path.joinpath('lawa_river_wq_field_samples_ts.csv.zip')
ds_data_path = base_path.joinpath('lawa_river_wq_field_samples_sites_mtypes.csv')
ts_data_feather_path = base_path.joinpath('lawa_river_wq_field_samples_ts.feather')











































