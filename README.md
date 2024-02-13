# Cray network audit

Security hardening of AOS-CX switches in Cray Super Computers.

Usage: python3 cray_network_audit.py
When prompted: enter PATH to the captured switch configuration files. i.e. /root/network/backup.

This program expectes that you have your switch configuration files saved somewhere locally in such folder as /root/network/backup.
This program will loop through all configuration files in the directory and compare it against defined best practices in this script.

If you have not backed up your configuration please navicate to the folder /config_backup and you will have couple pre-made examples on how 
to campure configuration from the switch. 
