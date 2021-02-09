.. _a10_vrrp_a_restart_port_list_module:


a10_vrrp_a_restart_port_list -- Configures A10 vrrp.a.restart-port-list
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Ports to be restarted on standby system after transition






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


  state (True, any, None)
    State of the object to be created.


  vrid_list (False, any, None)
    Field vrid_list


    ethernet_cfg (optional, any, None)
      Field ethernet_cfg


    user_tag (optional, any, None)
      Customized tag


    uuid (optional, any, None)
      uuid of the object


    vrid_val (optional, any, None)
      Specify ha VRRP-A vrid



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

