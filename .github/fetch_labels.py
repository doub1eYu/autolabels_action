#!/usr/bin/env python
# coding: utf-8

import toml

dict_toml = toml.load(open('.github/labels.toml'))
dict_toml_f = toml.load(open('.github/labels_first_time.toml'))

for k in dict_toml_f:
    dict_toml[k] = dict_toml_f[k]
    
print(dict_toml)
toml.dump(dict_toml, open('.github/labels.toml', mode='w'))





