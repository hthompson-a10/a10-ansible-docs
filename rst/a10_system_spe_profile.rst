.. _a10_system_spe_profile_module:


a10_system_spe_profile -- Configures A10 system.spe-profile
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set Security Policy Engine Profile






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  action (False, any, None)
    'ipv4-only'= Enable IPv4 HW forward entries only; 'ipv6-only'= Enable IPv6 HW forward entries only; 'ipv4-ipv6'= Enable Both IPv4/IPv6 HW forward entries (shared);


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

