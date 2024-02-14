import os

config_folder = input ('Please specify the path to the folder: ')  # Update with the path to your configuration files folder

# Define the best practice configuration line items to check
best_practices = {
    #General system check
    "!Version ArubaOS-CX": "Software version not up to date",
    "banner exec": "No exec banner found",
    #General features
    "no ip icmp redirect": "ICMP redirect not disabled",
    "ntp enable": "No NTP server configured",
    "vlan 1": "Default VLAN not configured (vlan 1)",
    "vlan 2": "NMN VLAN not configured (vlan 2)",
    "vlan 4": "HSM VLAN not configured (vlan 4)",
    "vlan 7": "CMN VLAN not configured (vlan 7)",
    "spanning-tree": "No spanning-tree configured",
    "spanning-tree forward-delay 4": "No spanning-tree forward-delay configured",
    "spanning-tree config-name": "No spanning-tree config-name configured",
    "spanning-tree config-revision": "No spanning-tree config-revision configured",
    #Security
    "aaa authentication limit-login-attempts": "No AAA authentication limit-login-attempts configured",
    "ssh certified-algorithms-only": "Strict certified-algorithms-only is not enabled",
    "session-timeout": "no session time out configured",
    "radius-server host": "No Radius server conrigured",
    "aaa authentication login": "No AAA authentication login configured",
    "tacacs-server host": "No Tacacs-server configured",
    "snmp-server community": "SNMPv2 server community enabled, should be disabled in secure systems and use SNMPv3",
    "snmp-server vrf": "SNMPv2 enabled in VRF, should be disabled in secure systems and use SNMPv3",
    #Security - internal networks
    "vrf Customer": "VRF customer not configured",
    "vrf keepalive": "VRF keepalive not configured",
    "ntp enable": "No NTP server configured",
    "password plaitext": "No plaintext passwords found in configuration",
    "ssh server vrf Customer": "SSH access not configured for VRF Customer",
    "ssh server vrf default": "SSH access not configured for VRF default",
    "ssh server vrf keepalive": "SSH access not configured for VRF keepalive",
    "ssh server vrf mgmt": "SSH access not configured for VRF mgmt",
    "access-list ip cmn-can": "Access-list cmn-can not configured",
    "access-list ip mgmt": "Access-list mgmt not configured",
    "access-list ip nmn-hmn": "Access-list nmn-hmn not configured",
    "https-server vrf Customer": "HTTPS access not allowed from VRF Customer",
    "https-server vrf default": "HTTPS access not allowed from VRF default",
    "https-server vrf mgmt": "HTTPS access not allowed from VRF mgmt",
}

minimum_version = "10.09.0010"  # Update with the minimum software version

for config_file in os.listdir(config_folder):
    file_path = os.path.join(config_folder, config_file)
    if not config_file.endswith(".cfg"):
        continue

    with open(file_path, "r") as f:
        config_lines = f.readlines()

    # Check for best practice configuration line items
    config_errors = []
    for line_item, error_message in best_practices.items():
        found = False
        for line in config_lines:
            if line_item in line:
                found = True
                break
        if not found:
            config_errors.append(error_message)

    # Get current software version from configuration file
    version_line = "!Version ArubaOS-CX"
    for line in config_lines:
        if version_line in line:
            version = line.strip().split(maxsplit=1)[1][14:]
            if version < minimum_version:
                config_errors.append(f"Software version ({version}) does not meet the minimum requirement of ({minimum_version})")
            else :
                print (f"This switch is currently running software version:", line[9:] )
            break

    # Print results for each configuration file
    print("Configuration file:", config_file)
    
    if config_errors:
        for error in config_errors:
            print("  -", error)
    else:
        print("No configuration errors found.")
    
    print("--")
