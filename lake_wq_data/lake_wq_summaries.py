#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 16:30:33 2022

@author: mike
"""
import pandas as pd
import geopandas as gpd
import utils, params

pd.options.display.max_columns = 10


############################################
### Summaries

date = pd.Timestamp.now().strftime('%Y-%m-%d')

ts_data0 = pd.read_feather(params.ts_data_feather_path)
stn_data0 = gpd.read_file(params.stn_data_path)

## Check timestamps
ts_data1 = ts_data0.dropna(subset=['RawValue'])[['LawaSiteID', 'Indicator', 'SampleDateTime']].copy()
ts_data2 = pd.merge(stn_data0[['LawaSiteID', 'Agency']], ts_data1, on='LawaSiteID').drop('LawaSiteID', axis=1)
ts_data2['hour'] = ts_data2.SampleDateTime.dt.hour

# datetimes at 00:00:00
midnight0 = ts_data2[ts_data2['SampleDateTime'].dt.time.apply(lambda x: x.isoformat()) == '00:00:00'].copy()
grp1 = midnight0.groupby(['Agency', 'Indicator'])['SampleDateTime']

midnight_count = grp1.count()
midnight_count.name = 'sample_count'
midnight_min = grp1.min()
midnight_min.name = 'sample_min_date'
midnight_max = grp1.max()
midnight_max.name = 'sample_max_date'

midnight1 = pd.concat([midnight_min, midnight_max, midnight_count], axis=1)

# sample dates that are outside the realistic time for sampling
# >= 19:00 to 7:00, <= 5:00 to 17:00
grp2 = ts_data2.groupby(['Agency', 'Indicator', 'hour'])['SampleDateTime']
hour_count = grp2.count()
hour_count.name = 'sample_count'

outside0 = ts_data2[(ts_data2['SampleDateTime'].dt.hour >= 19) | (ts_data2['SampleDateTime'].dt.hour <= 5)].copy()

grp3 = outside0.groupby(['Agency', 'Indicator'])['SampleDateTime']

outside_count = grp3.count()
outside_count.name = 'sample_count'
outside_min = grp3.min()
outside_min.name = 'sample_min_date'
outside_max = grp3.max()
outside_max.name = 'sample_max_date'

outside1 = pd.concat([outside_min, outside_max, outside_count], axis=1)


### Save summaries
midnight1.to_csv(params.midnight_summ_csv)
hour_count.to_csv(params.hour_summ_csv)
outside1.to_csv(params.outside_summ_csv)











