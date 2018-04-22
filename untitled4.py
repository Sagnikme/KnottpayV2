# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 17:17:06 2018

@author: Sagnik
"""
import dropbox
import argparse
import contextlib
import datetime
import os
import six
import sys
import time
import unicodedata


access_token = 'f_hjRlTkx0AAAAAAAAADvBfY5hiVPot6dJqgrMiYNrG1K1NJGUhzkklBLWmg7ITE'
dbx = dropbox.Dropbox(access_token)
path = 'https://www.dropbox.com/home/FaceID/D0SIDF1B?preview=trainningData.yml'
md, res = dbx.files_download(path)

data = res.content
print(len(data), 'bytes; md:', md)
return data