.. _a10_network_lldp_module:


a10_network_lldp -- Configures A10 network.lldp
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure LLDP






Parameters
----------

  system_name (False, any, None)
    Configure lldp system name


  ansible_port (True, any, None)
    Port for AXAPI authentication


  tx_set (False, any, None)
    Field tx_set


    reinit_delay (optional, any, None)
      Configure lldp tx reinit delay (The lldp tx reinit_delay value, default is 2)


    hold (optional, any, None)
      Configure lldp tx hold multiplier (The lldp tx hold value, default is 4)


    fast_count (optional, any, None)
      Configure lldp tx fast count value (The lldp tx fast count value, default is 4)


    fast_interval (optional, any, None)
      Configure lldp tx fast interval value (The lldp tx fast interval value, default is 1)


    tx_interval (optional, any, None)
      Configure lldp tx interval (The lldp tx interval value, default is 30)



  uuid (False, any, None)
    uuid of the object


  system_description (False, any, None)
    Configure lldp system description


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  notification_cfg (False, any, None)
    Field notification_cfg


    notification (optional, any, None)
      Enable lldp notification


    interval (optional, any, None)
      Configure lldp notification interval, default is 30 (The lldp notification interval value, default is 30)



  enable_cfg (False, any, None)
    Field enable_cfg


    enable (optional, any, None)
      Enable lldp


    rx (optional, any, None)
      Enable lldp rx


    tx (optional, any, None)
      Enable lldp tx



  state (True, any, None)
    State of the object to be created.


  management_address (False, any, None)
    Field management_address


    dns_list (optional, any, None)
      Field dns_list


    ipv6_addr_list (optional, any, None)
      Field ipv6_addr_list


    ipv4_addr_list (optional, any, None)
      Field ipv4_addr_list



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

