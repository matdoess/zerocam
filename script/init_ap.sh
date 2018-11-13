#!/bin/bash

## Setup AP
# https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md
# Install Software
sudo apt-get install -y dnsmasq hostapd

# Disable Servicees
sudo systemctl stop dnsmasq
sudo systemctl stop hostapd

# sudo reboot
## TODO: Scriptstatus speichern und nach reboot wieder einsteigen

# Backup Original config files
sudo cp /etc/dhcpcd.conf /etc/dhcpcd.conf.orig
sudo cp /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
sudo cp /etc/default/hostapd /etc/default/hostapd.orig
sudo cp /etc/hosts /etc/hosts.orig
sudo cp /etc/wpa_supplicant/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf.orig
# TODO wpa_supplicant.conf.orig.empty erstellen

# Edit dhcpcd.conf
cat >> /etc/dhcpcd.conf <<'EOF'
interface wlan0
    static ip_address=192.168.4.1/24
    nohook wpa_supplicant
EOF

sudo service dhcpcd restart

# Create dnsmasq.conf
cat > /etc/dnsmasq.conf <<'EOF'
interface=wlan0      # Use the require wireless interface - usually wlan0
  dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
EOF


# Create hostapd.conf
cat > /etc/hostapd/hostapd.conf <<'EOF'
interface=wlan0
driver=nl80211
ssid=zerocamap
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=zerocampw
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
EOF

# edit /etc/default/hostapd
cat >> /etc/default/hostapd <<'EOF'
DAEMON_CONF="/etc/hostapd/hostapd.conf"
EOF

# clear /etc/wpa_supplicant/wpa_supplicant.conf
sudo echo "" > /etc/wpa_supplicant/wpa_supplicant.conf

# edit /etc/hosts
#TODO: edit /etc/hosts with script
echo "add 192.168.4.1 zerocam to /etc/hosts and comment out other zerocam entries"
read -sn1 -p "When ready press key to continue"
echo -e "\n"

# AP Config Backup
sudo cp /etc/dhcpcd.conf /etc/dhcpcd.conf.ap
sudo cp /etc/dnsmasq.conf /etc/dnsmasq.conf.ap
sudo cp /etc/default/hostapd /etc/default/hostapd.ap
sudo cp /etc/hosts /etc/hosts.ap

sudo systemctl start hostapd
sudo systemctl start dnsmasq

sudo reboot

