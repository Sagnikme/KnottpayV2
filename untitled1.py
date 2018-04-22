# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 15:23:56 2018

@author: Sagnik
"""

import os
import shutil

home_dir = (r'''C:\Users\Sagnik\Desktop\Project\dataSet''')   
if not os.path.isdir(home_dir):
    os.makedirs(home_dir)
    print('done')
    
shutil.rmtree(home_dir, ignore_errors=True)