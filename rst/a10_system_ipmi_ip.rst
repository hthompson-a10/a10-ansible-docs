.. _a10_system_ipmi_ip_module:


a10_system_ipmi_ip -- Configures A10 system.ipmi.ip
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set IP address for IPMI interface






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  default_gateway (False, any, None)
    Default gateway address


  ipv4_address (False, any, None)
    IP address


  state (True, any, None)
    State of the object to be created.


  ipv4_netmask (False, any, None)
    IP subnet mask


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

