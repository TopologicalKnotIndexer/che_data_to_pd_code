# 读入一个分子数据文件，返回一个 PD_CODE
import os
from to_pd_code       import to_pd_code
from to_spatial_coord import to_spatial_coord

def che_data_to_pd_code(che_data_file_path: str) -> list:
    assert os.path.isfile(che_data_file_path)
    spatial_coord = to_spatial_coord(che_data_file_path)
    pd_code       = to_pd_code(spatial_coord)
    return pd_code
