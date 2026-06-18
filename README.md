# GPSTAK

GPSTAK feeds a Linux device's gpsd position to TAK clients as network GPS.
It emits Cursor on Target position events to `COT_URL` and can optionally
fan out raw NMEA sentences for WinTAK.

Typical AryaOS use:

```sh
sudo apt install gpstak cockpit-gpstak
sudo systemctl enable --now gpstak
```

Configuration lives in `/etc/default/gpstak`:

- `COT_URL`: PyTAK destination, default `udp+broadcast://255.255.255.255:4349`
- `NMEA_TARGETS`: optional space-separated `host:port` targets for raw NMEA
- `GPSTAK_RATE`: update interval in seconds
- `GPSTAK_UID`: CoT UID, defaults to `GPSTAK-<hostname>`
- `GPSTAK_SOURCE_NAME`: source name in CoT remarks, defaults to hostname
- `GPSD_HOST` / `GPSD_PORT`: gpsd endpoint

Build packages:

```sh
make deb
```

The Debian package installs:

- `/usr/local/bin/gpstak`
- `/etc/default/gpstak`
- `/lib/systemd/system/gpstak.service`

## License

Apache-2.0.

