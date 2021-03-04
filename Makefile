
MKFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
CURRENT_DIR := $(patsubst %/,%,$(dir $(MKFILE_PATH)))

TMP := /tmp/ansible_docs

.ONESHELL:
.PHONY: install
install:
	cd ~
	git clone https://github.com/a10networks/sdkgenerator.git
	~/sdkgenerator
	sudo pip3 install -e .
	cd ~
	git clone https://github.com/a10networks/ansible-doc-extractor.git
	cd ~/ansible-doc-extractor
	sudo pip3 install -e .
	cd $(CURRENT_DIR)
	sudo pip3 install -e .

.PHONY: build
build:
	$(MAKE) generate
	$(MAKE) extract
	$(MAKE) migrate 
	$(MAKE) docs

.PHONY: migrate
migrate:
	migrate_rst $(TMP) $(CURRENT_DIR)/a10_ansible_docs/axapi_collection/$(ACOS_VERSION)

.PHONY: extract
extract:
	mkdir $(TMP)
	ansible-doc-extractor $(TMP) $(INSTALL_PATH)/a10-acos-axapi/plugins/modules/*.py

.ONESHELL: 
.PHONY: generate
generate:
	cd $(CURRENT_DIR)
	cd ..
	sdkgenerator --output-strategy ansible_web_doc --acos-version $(ACOS_VERSION) $(SCHEMA_PATH) . 

.PHONY: docs
docs:
	mkdir $(CURRENT_DIR)/a10_ansible_docs/$(ACOS_VERSION)
	sphinx-build $(CURRENT_DIR)/a10_ansible_docs/axapi_collection $(CURRENT_DIR)/a10_ansible_docs/$(ACOS_VERSION)/axapi_html
