.. _a10_interface_lif_ip_rip_module:


a10_interface_lif_ip_rip -- Configures A10 interface.lif.ip.rip
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

RIP






Parameters
----------

  split_horizon_cfg (False, any, None)
    Field split_horizon_cfg


    state (optional, any, None)
      'poisoned'= Perform split horizon with poisoned reverse; 'disable'= Disable split horizon; 'enable'= Perform split horizon without poisoned reverse;



  receive_packet (False, any, None)
    Enable receiving packet through the specified interface


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  receive_cfg (False, any, None)
    Field receive_cfg


    receive (optional, any, None)
      Advertisement reception


    version (optional, any, None)
      '1'= RIP version 1; '2'= RIP version 2; '1-2'= RIP version 1 & 2;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  send_packet (False, any, None)
    Enable sending packets through the specified interface


  ansible_host (True, any, None)
    Host for AXAPI authentication


  authentication (False, any, None)
    Field authentication


    key_chain (optional, any, None)
      Field key_chain


    mode (optional, any, None)
      Field mode


    str (optional, any, None)
      Field str



  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  send_cfg (False, any, None)
    Field send_cfg


    version (optional, any, None)
      '1'= RIP version 1; '2'= RIP version 2; '1-compatible'= RIPv1-compatible; '1-2'= RIP version 1 & 2;


    send (optional, any, None)
      Advertisement transmission



  lif_ifnum (optional, any, None)
    Key to identify parent object









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

