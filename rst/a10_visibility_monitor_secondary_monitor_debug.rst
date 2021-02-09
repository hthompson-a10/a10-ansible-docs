.. _a10_visibility_monitor_secondary_monitor_debug_module:


a10_visibility_monitor_secondary_monitor_debug -- Configures A10 visibility.monitor.secondary.monitor.debug
===========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enable store and replay for the entitites






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


  debug_ip_addr (True, any, None)
    Specify source/dest ip addr


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  debug_protocol (True, any, None)
    'TCP'= TCP; 'UDP'= UDP; 'ICMP'= ICMP;


  debug_port (True, any, None)
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

