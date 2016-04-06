#!/usr/bin/env python

from fabric.api import env, run, sudo

env.hosts = ['172.31.21.140', '172.31.10.93', '172.31.10.92']
#env.hosts = ['172.31.21.140']
env.key_filename = '~/KeyPair.pem'
def uptime():
  run('mkdir ~/ml')
