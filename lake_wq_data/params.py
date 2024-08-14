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

nzrec_data_path = base_path.joinpath('nzrec')
rec_rivers_feather = nzrec_data_path.joinpath('rec25_rivers_clean.feather')

lake_wq_files = ['lawa-lakewq-monitoring-data_2004-2022_statetrend-results_sep2023.csv.zip']

# lakes_poly_gpkg = base_path.joinpath('lakes_polygons_fenz.gpkg')

# lawa_to_nzseg_path = base_path.joinpath('lawa_to_nzsegment.csv')

## RAW data
stn_data_raw_path = base_path.joinpath('lawa_lake_wq_field_samples_sites_raw.gpkg')
ts_data_raw_csv_path = base_path.joinpath('lawa_lake_wq_field_samples_ts_raw.csv.zip')
ds_data_raw_path = base_path.joinpath('lawa_lake_wq_field_samples_sites_mtypes_raw.csv')
ts_data_raw_feather_path = base_path.joinpath('lawa_lake_wq_field_samples_ts_raw.feather')

## Summaries
midnight_summ_csv = base_path.joinpath('lawa_lake_wq_field_samples_midnight.csv')
hour_summ_csv = base_path.joinpath('lawa_lake_wq_field_samples_hour_count.csv')
outside_summ_csv = base_path.joinpath('lawa_lake_wq_field_samples_outside.csv')

## Cleaned data
stn_data_path = base_path.joinpath('lawa_lake_wq_field_samples_sites.gpkg')
ts_data_csv_path = base_path.joinpath('lawa_lake_wq_field_samples_ts.csv.zip')
ds_data_path = base_path.joinpath('lawa_lake_wq_field_samples_sites_mtypes.csv')
ts_data_feather_path = base_path.joinpath('lawa_lake_wq_field_samples_ts.feather')
# stn_poly_gpkg = base_path.joinpath('lawa_lake_polygons_fenz.gpkg')










































