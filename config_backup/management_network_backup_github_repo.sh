#!/bin/bash

DATE_CODE=$(date +%Y%m%d-%H%M)
case $(cat /etc/cray/xname | cut -c 1-5) in
        x3108)
                SYSTEM_NAME=ehz1
                REPO_DIR=~/git/switch_configs
                ;;
        x3110)
                SYSTEM_NAME=ehz2
                REPO_DIR=~/git/switch_configs
                ;;
        x310[6-7])
                SYSTEM_NAME=exa
                REPO_DIR=~/hpe/git/switch_configs
                ;;
        x310[8-9])
                SYSTEM_NAME=exb
                REPO_DIR=~/hpe/git/switch_configs
                ;;
        x320[0-1])
                SYSTEM_NAME=exc
                REPO_DIR=~/hpe/git/switch_configs
                ;;
        x330[0-1])
                SYSTEM_NAME=exd
                REPO_DIR=~/hpe/git/switch_configs
                ;;
        *)
                echo "failed, cant determine system - exiting"
                exit 1
                ;;
esac

echo "Running on $SYSTEM"

#Gather list of switches
SWITCHES=$(cat /etc/hosts | grep "sw-.*adm\|sw-.*mgmt\|sw-.*cds\|sw-.*ehz\|sw-.*spine\|sw-*leaf\|sw-.*cdu" | grep -v "hsn\|^#" | grep sw- |  grep -o "sw-.*" | awk 
'{print $1;}')

mkdir -p ${REPO_DIR}/${SYSTEM_NAME}

for SWITCH in $SWITCHES ; do
        ping -c 1 -w 1 $SWITCH > /dev/null
        if [ $? -gt 0 ] ; then
                echo "Error pinging $SWITCH - skipping"
                continue
        fi
        echo "getting configuration of switch - $SWITCH"
        ssh $SWITCH -o StrictHostKeyChecking=no "show running-config" 2>/dev/null | sed "s/ciphertext .*$/ciphertext xxx-removed-xxx/" > 
$REPO_DIR/${SYSTEM_NAME}/${SWITCH}.cfg
done

cd $REPO_DIR
git add *
if [[ `git status --porcelain` ]]; then
        git commit -a -m "commit by $0 at `date`"

        # Dump out changes
        #git diff HEAD^ HEAD

        git push
else
        echo "Nothing to commit - no changes"
fi
