all: \
	.env

.env:
	touch $@
	echo "UID=$(shell id -u)" >> $@
	echo "GID=$(shell id -g)" >> $@
