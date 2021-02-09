.. _a10_dnssec_ds_module:


a10_dnssec_ds -- Configures A10 dnssec.ds
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Delegation Signer(DS) Resource Records of child zones






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  ds_delete (False, any, None)
    Delete the DS file


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  zone_name (False, any, None)
    DNS zone name of the child zone


  a10_partition (False, any, None)
    Destination/target partition for object/command


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

