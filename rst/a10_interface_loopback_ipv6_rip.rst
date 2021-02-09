.. _a10_interface_loopback_ipv6_rip_module:


a10_interface_loopback_ipv6_rip -- Configures A10 interface.loopback.ipv6.rip
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

RIP






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  split_horizon_cfg (False, any, None)
    Field split_horizon_cfg


    state (optional, any, None)
      'poisoned'= Perform split horizon with poisoned reverse; 'disable'= Disable split horizon; 'enable'= Perform split horizon without poisoned reverse;



  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  loopback_ifnum (optional, any, None)
    Key to identify parent object


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

