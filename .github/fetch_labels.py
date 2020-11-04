#!/usr/bin/env python
# coding: utf-8

import toml
import sys
import os
import subprocess

try:
    dict_toml_f = toml.load(open('.github/labels_first_time.toml'))
except Exception:
    sys.exit()
dict_toml = toml.load(open('.github/labels.toml'))

cmd = "labels fetch -f .github/labels.toml"
runcmd = subprocess.check_output(cmd.split())
print(runcmd)

for k in dict_toml_f:
    dict_toml[k] = dict_toml_f[k]
print(dict_toml)
toml.dump(dict_toml, open('.github/labels.toml', mode='w'))
os.remove('.github/labels_first_time.toml')




