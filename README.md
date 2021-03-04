# Overview

This is tool is designed to automate documentation of A10's Ansible modules

## Installation

The following command will install the sdkgenerator and A10's version of the ansible-doc-extractor tool

`make install`

## Usage

### Requirements
The json schema files have been dowloaded from one of the build servers.

The a10-acos-axapi repo has been cloned from github (https://github.com/a10networks/a10-acos-axapi.git)

### Build command
`make build ACOS_VERSION=<acos-version> SCHEMA_PATH=<path-to-schema-files> INSTALL_PATH=<path-to-axapi-collection>`

`ACOS_VERSION` - Can be either acos_4_1_4, acos_5_1_0, or acos_5_2_0

`SCHEMA_PATH` - Path to the json-schema files downloaded from build server. (Tutorial for this can be found under the Tutorial folders on the internal Openstack Team's channel)

`INSTALL_PATH` - Installation path to `a10-acos-axapi` github repo on local machine

## Result

* A document containing the html and static files can be found under `a10-ansible-docs/a10_ansible_docs/axapi_html`
* A document contining the rst files can be found under `a10-ansible-docs/a10_ansible_docs/axapi_collection/ACOS_VERSION`