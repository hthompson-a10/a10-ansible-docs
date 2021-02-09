.. _a10_debug_monitor_module:


a10_debug_monitor -- Configures A10 debug.monitor
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Monitor debug output






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


  filename (False, any, None)
    Filename to save debug output


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  all_slots (False, any, None)
    Display debug output of both Master and Blade


  cpuid (False, any, None)
    CPU id to debug (0,1,...)


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

