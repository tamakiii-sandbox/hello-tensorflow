all: \
	.env

.env:
	touch $@
	echo "UNAME=$(shell whoami)" >> $@
	echo "UID=$(shell id -u)" >> $@
	echo "GID=$(shell id -g)" >> $@

clean:
	rm -rf .env
