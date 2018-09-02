#!/bin/bash
# Title:genesis.sh
# Description:
# Development Environment:OS X 10.13.6
# Legalise:  
# Author:guycole at gmail dot com
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
#psql -d template1 -U gsc -f genesis.sql
psql -d template1 -U postgres -f genesis.sql
#
