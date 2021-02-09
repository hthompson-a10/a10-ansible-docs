.. _a10_dnssec_key_rollover_module:


a10_dnssec_key_rollover -- Configures A10 dnssec.key-rollover
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

DNSSEC Key rollover






Parameters
----------

  ds_ready_in_parent_zone (False, any, None)
    DS RR is already ready in the parent zone


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ksk_start (False, any, None)
    start KSK rollover in emergency mode


  ansible_username (True, any, None)
    Username for AXAPI authentication


  zsk_start (False, any, None)
    start ZSK rollover in emergency mode


  dnssec_key_type (False, any, None)
    'ZSK'= Zone Signing Key; 'KSK'= Key Signing Key;


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  zone_name (False, any, None)
    Specify the name for the DNS zone


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

