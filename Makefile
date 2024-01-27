SUBDIRS := $(shell find . -mindepth 1 -maxdepth 1 -type d -exec test -e '{}/Makefile' ';' -print)
INSTALL_TARGETS = SUBDIRS

.PHONY: install $(SUBDIRS)

install: $(SUBDIRS)

$(SUBDIRS):
	@cd $@ && make install

tools:
	@sudo ./install_tools.sh