.. _a10_visibility_monitor_delete_debug_file_module:


a10_visibility_monitor_delete_debug_file -- Configures A10 visibility.monitor.delete-debug-file
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Delete the debug entity file






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


  debug_ip_addr (True, any, None)
    Specify source/dest ip addr


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  debug_protocol (False, any, None)
    'TCP'= TCP; 'UDP'= UDP; 'ICMP'= ICMP;


  debug_port (False, any, None)
    Specify port


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

