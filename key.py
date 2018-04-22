# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 14:37:44 2018

@author: Sagnik
"""

import random, string
x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
print(x)