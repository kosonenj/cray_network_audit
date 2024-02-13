# Cray switch config backup script

This script was developed to ease out the configuration backup of the switches in Cray system environment. 

It can be adapted to any system by changing parameters within the script.

This script reads in /etc/hosts file to know what the switches are and connects to the switches that are available in that file.

## Usage

Make folder "network-backup" in a system that can reach the desirable switches.

Copy the script "copy_switch_config.sh" to the folder.

Enable execution of the script by issuing: 

```bash
chmod +X copy_switch_config.sh"
```

Run the script: 

```bash
sh copy_switch_config.sh"
```

The script will save the copied configurations to a folder named "switch_config"

## Additional information

You can automate the running of this script by using cron jobs.

Edit your cron tab: 

```bash
root$ crontab -e 
```

Add line: 

```bash
0 0 * * MON /root/network_backup/copy_switch_config.sh
```

Verify that your newly added cron job is part of the list: 

```bash
root$ crontab -l
```

NOTE: depending on your system/needs you need to adjust the above. It is meant to be just an example.
