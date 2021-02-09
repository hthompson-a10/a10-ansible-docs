.. _a10_vrrp_a_restart_port_list_vrid_module:


a10_vrrp_a_restart_port_list_vrid -- Configures A10 vrrp-a.restart.port.list.vrid
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify VRRP-A vrid






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


  vrid_val (True, any, None)
    Specify ha VRRP-A vrid


  state (True, any, None)
    State of the object to be created.


  ethernet_cfg (False, any, None)
    Field ethernet_cfg


    flap_ethernet_end (optional, any, None)
      Ethernet Port


    flap_ethernet_start (optional, any, None)
      Ethernet Port



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  user_tag (False, any, None)
    Customized tag









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

