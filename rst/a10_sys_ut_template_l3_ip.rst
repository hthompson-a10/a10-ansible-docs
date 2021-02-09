.. _a10_sys_ut_template_l3_ip_module:


a10_sys_ut_template_l3_ip -- Configures A10 sys-ut.template.l3.ip
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IP address






Parameters
----------

  ve (False, any, None)
    Virtual Ethernet interface


  ansible_username (True, any, None)
    Username for AXAPI authentication


  template_name (optional, any, None)
    Key to identify parent object


  ipv6_start_address (False, any, None)
    Ipv6 address


  nat_pool (False, any, None)
    Nat pool


  trunk (False, any, None)
    Trunk number


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  virtual_server (False, any, None)
    vip


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ipv4_start_address (False, any, None)
    IP address


  uuid (False, any, None)
    uuid of the object


  src_dst (True, any, None)
    'dest'= dest; 'src'= src;


  ipv4_end_address (False, any, None)
    IP end address


  ipv6_end_address (False, any, None)
    Ipv6 end address


  state (True, any, None)
    State of the object to be created.


  ethernet (False, any, None)
    Ethernet interface


  ansible_password (True, any, None)
    Password for AXAPI authentication









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

