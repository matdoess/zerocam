#!/bin/bash



















# Create ~/.asoundrc

## Create ladspa Device in alsa to use with picam
# https://github.com/mpromonet/v4l2rtspserver/issues/94#issuecomment-378788356

apt-get install ladspa-sdk

cat >> ~/.asoundrc <<'EOF'

pcm.pluglp {
    type ladspa
    slave.pcm "plughw:1,0"
    path "/usr/lib/ladspa"
    capture_plugins [
	{	
		label hpf
		id 1042
	}
        {
                label amp_mono
                id 1048
                input {
                    controls [ 30 ]
                }
        }
    ]
}

pcm.lp {
    type plug
    slave.pcm pluglp
}
EOF
