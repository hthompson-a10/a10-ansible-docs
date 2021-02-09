.. _a10_vrrp_a_peer_group_module:


a10_vrrp_a_peer_group -- Configures A10 vrrp.a.peer-group
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

VRRP-A peer group






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


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  peer (False, any, None)
    Field peer


    ipv6_peer_address_cfg (optional, any, None)
      Field ipv6_peer_address_cfg


    ip_peer_address_cfg (optional, any, None)
      Field ip_peer_address_cfg



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

