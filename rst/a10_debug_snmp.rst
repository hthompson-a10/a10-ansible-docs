.. _a10_debug_snmp_module:


a10_debug_snmp -- Configures A10 debug.snmp
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

SNMP module parameters






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


  all (False, any, None)
    SNMP all debug switch


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  error (False, any, None)
    SNMP debug error switch


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  event (False, any, None)
    SNMP debug event switch









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

