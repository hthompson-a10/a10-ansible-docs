.. _a10_fw_tap_monitor_module:


a10_fw_tap_monitor -- Configures A10 fw.tap-monitor
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure tap monitor port






Parameters
----------

  status (False, any, None)
    'enable'= Enable tap monitor mode; 'disable'= Disable tap monitor mode (Default=Disable);


  ansible_port (True, any, None)
    Port for AXAPI authentication


  tap_port_cfg (False, any, None)
    Field tap_port_cfg


    tap_eth (optional, any, None)
      Ethernet interface number


    tap_vlan (optional, any, None)
      Vlan number



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


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

