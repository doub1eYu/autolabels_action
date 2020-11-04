#!/usr/bin/env python
# coding: utf-8

import toml
import sys
import subprocess

try:
    dict_toml_f = toml.load(open('.github/labels_first_time.toml'))
except Exception:
    sys.exit()

cmd = "labels fetch -f .github/labels.toml"
runcmd = subprocess.check_output(cmd.split())
print(runcmd)
dict_toml = toml.load(open('.github/labels.toml'))

for k in dict_toml_f:
    dict_toml[k] = dict_toml_f[k]
print(dict_toml)
toml.dump(dict_toml, open('.github/labels.toml', mode='w'))

cmd = "git rm .github/labels_first_time.toml"
runcmd = subprocess.check_output(cmd.split())
print(runcmd)




