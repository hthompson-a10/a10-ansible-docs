.. _a10_interface_trunk_ip_stateful_firewall_module:


a10_interface_trunk_ip_stateful_firewall -- Configures A10 interface.trunk.ip.stateful-firewall
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Stateful Firewall direction






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


  inside (False, any, None)
    Inside (private) interface for stateful firewall


  trunk_ifnum (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  access_list (False, any, None)
    Access-list for traffic from the outside


  class_list (False, any, None)
    Class List (Class List Name)


  outside (False, any, None)
    Outside (public) interface for stateful firewall


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  acl_id (False, any, None)
    ACL id









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

