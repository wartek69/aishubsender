# aishubsender
A python application to send ais data from your ais device to ais hub.

## Aishub
Aishub is a platform where ais data can be submitted to. In return they will give you access to their api that contains world wide ais data.
More information can be found on https://www.aishub.net/join-us
## Run
Before this script can be used pyserial needs to be installed.
```pip3 install pyserial```

Once that's done, open `aishub_sender.py` and change the serial_port variable to point to your connected device.
When you successfully become a partner with ais hub, they will esnd you an ip and port where the ais data needs to be published to.
Specify this address and port in the `aishub_address` variable.
Finally, run the script:
```python3 aishub_sender.py```

## Unix users
When running this script on unix, make sure that the user executing the script is part of the `dialout` group. If that's not the case you might get a permission error.

