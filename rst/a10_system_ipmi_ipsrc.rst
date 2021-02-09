.. _a10_system_ipmi_ipsrc_module:


a10_system_ipmi_ipsrc -- Configures A10 system.ipmi.ipsrc
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Source of IP Address






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  static (False, any, None)
    Manually configured static IP address


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  dhcp (False, any, None)
    IP addr obtained by BMC running DHCP


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

