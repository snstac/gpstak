.PHONY: deb rpm package clean check

VERSION ?= $(shell sed -n 's/^VERSION = "\(.*\)"/\1/p' gpstak/gpstak.py)

check:
	python3 -m py_compile gpstak/gpstak.py

deb: check
	mkdir -p out
	VERSION="$(VERSION)" nfpm package -f nfpm.yaml -p deb -t out/

rpm: check
	mkdir -p out
	VERSION="$(VERSION)" nfpm package -f nfpm.yaml -p rpm -t out/

package: deb rpm

clean:
	rm -rf out build dist

