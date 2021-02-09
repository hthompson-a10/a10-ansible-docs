.. _a10_zone_vlan_module:


a10_zone_vlan -- Configures A10 zone.vlan
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Vlan






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


  vlan_list (False, any, None)
    Field vlan_list


    vlan_start (optional, any, None)
      VLAN ID


    vlan_end (optional, any, None)
      Field vlan_end



  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  zone_name (optional, any, None)
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

