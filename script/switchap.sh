#!/bin/bash

# Example Call
# sudo ./switchap.sh wifi 'FRITZ!Box 7590 SR' 1234567890


#mode = ap / wifi
mode=$1
ssid=$2
pw=$3

echo "mode= $1 ssid = $2 pw = $3"
echo "$ssid"

if [ $mode == ap ]
    then
    echo "AP Mode"
    sudo cp /etc/dhcpcd.conf.ap /etc/dhcpcd.conf
    sudo cp /etc/dnsmasq.conf.ap /etc/dnsmasq.conf
    sudo cp /etc/default/hostapd.ap /etc/default/hostapd
    sudo echo "" > /etc/wpa_supplicant/wpa_supplicant.conf
    sudo reboot

elif [ $mode == wifi ]
# https://www.ghacks.net/2009/04/14/connect-to-a-wireless-network-via-command-line/
    then
    echo "Wifi Mode"
    sudo cp /etc/dhcpcd.conf.orig /etc/dhcpcd.conf
    sudo cp /etc/dnsmasq.conf.orig /etc/dnsmasq.conf
    sudo cp /etc/default/hostapd.orig /etc/default/hostapd
    sudo cp /etc/wpa_supplicant/wpa_supplicant.conf.empty /etc/wpa_supplicant/wpa_supplicant.conf
cat >> /etc/wpa_supplicant/wpa_supplicant.conf <<EOF
network={
	ssid="$ssid"
	psk="$pw"
}
EOF
    sudo reboot
else
    echo "please input ap or wifi as parameter"
fi
