.. _a10_interface_ethernet_trunk_group_module:


a10_interface_ethernet_trunk_group -- Configures A10 interface.ethernet.trunk-group
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Trunk Group Settings






Parameters
----------

  trunk_number (True, any, None)
    Trunk Number


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ntype (False, any, None)
    'static'= Static (default); 'lacp'= lacp; 'lacp-udld'= lacp-udld;


  port_priority (False, any, None)
    Set LACP priority for a port (LACP port priority)


  admin_key (False, any, None)
    LACP admin key (Admin key value)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  user_tag (False, any, None)
    Customized tag


  state (True, any, None)
    State of the object to be created.


  ethernet_ifnum (optional, any, None)
    Key to identify parent object


  timeout (False, any, None)
    'long'= Set LACP long timeout (default); 'short'= Set LACP short timeout;


  udld_timeout_cfg (False, any, None)
    Field udld_timeout_cfg


    slow (optional, any, None)
      slow timeout in unit of seconds


    fast (optional, any, None)
      fast timeout in unit of milli-seconds(default 1000)



  ansible_password (True, any, None)
    Password for AXAPI authentication


  mode (False, any, None)
    'active'= enable initiation of LACP negotiation on a port(default); 'passive'= disable initiation of LACP negotiation on a port;









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

