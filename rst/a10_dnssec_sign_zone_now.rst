.. _a10_dnssec_sign_zone_now_module:


a10_dnssec_sign_zone_now -- Configures A10 dnssec.sign-zone-now
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

sign zone right now






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


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  zone_name (False, any, None)
    Specify the name for the DNS zone, empty means sign all zones


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

