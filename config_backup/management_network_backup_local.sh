#!/bin/bash
cat /etc/hosts | grep "sw-.*adm\|sw-.*mgmt\|sw-.*cds\|sw-.*ehz\|sw-.*spine\|sw-*leaf\|sw-.*cdu" | grep -v "hsn\|#" | grep sw- |  grep -o "sw-.*" | awk '{print $1;}' > 
switches.txt

mkdir -p switch_config
RED='\033[0;31m'
NOCOLOR='\033[0m'

host="switches.txt"
for LINE in `cat $host`
do
        echo -e "${RED}$LINE copying configuration${NOCOLOR}"
        ssh $LINE show run > $LINE.`date +%m-%d-%Y`.txt
        echo -e "${RED}$LINE copy complete${NOCOLOR}"
        mv sw-* ./switch_config/
done

