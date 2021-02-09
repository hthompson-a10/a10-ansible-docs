.. _a10_network_bridge_vlan_group_module:


a10_network_bridge_vlan_group -- Configures A10 network.bridge-vlan-group
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Bridge VLAN Group Settings






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  bridge_vlan_group_number (True, any, None)
    Bridge VLAN Group Number


  name (False, any, None)
    Bridge Group Name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ve (False, any, None)
    Virtual Ethernet Port (Virtual Ethernet Port number)


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  vlan_list (False, any, None)
    Field vlan_list


    vlan_start (optional, any, None)
      VLAN id


    vlan_end (optional, any, None)
      VLAN id



  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  forward_traffic (False, any, None)
    'forward-all-traffic'= Forward all traffic between bridge members; 'forward-ip- traffic'= Forward only IP traffic between bridge members (default);


  uuid (False, any, None)
    uuid of the object









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

