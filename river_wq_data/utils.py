#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:35:52 2024

@author: mike
"""
import matplotlib.pyplot as plt


############################################
### Functions


def gpd_to_feather(gdf, output):
    """

    """
    gdf.to_feather(output, compression='zstd', compression_level=1)


def df_to_feather(df, output):
    """

    """
    df.to_feather(output, compression='zstd', compression_level=1)


def make_figure(df, path):
    """

    """
    fig, ax = plt.subplots(layout='tight', figsize=(10, 6))
    df.plot(ax=ax)

    fig.savefig(path)

    plt.close(fig)

































