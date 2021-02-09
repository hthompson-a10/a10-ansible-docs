.. _a10_import_periodic_dnssec_dnskey_module:


a10_import_periodic_dnssec_dnskey -- Configures A10 import-periodic.dnssec-dnskey
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

DNSSEC DNSKEY(KSK) file for child zone






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  a10_partition (False, any, None)
    Destination/target partition for object/command


  period (False, any, None)
    Specify the period in second


  remote_file (False, any, None)
    profile name for remote url


  state (True, any, None)
    State of the object to be created.


  use_mgmt_port (False, any, None)
    Use management port as source port


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  dnssec_dnskey (True, any, None)
    DNSSEC DNSKEY(KSK) file for child zone


  ansible_host (True, any, None)
    Host for AXAPI authentication









Examples
--------

.. code-block:: yaml+jinja

    





Status
------




- This module is not guaranteed to have a backwards compatible interface. *[preview]*


- This module is maintained by community.



Authors
~~~~~~~

- A10 Networks 2018

