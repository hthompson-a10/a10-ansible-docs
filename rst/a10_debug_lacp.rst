.. _a10_debug_lacp_module:


a10_debug_lacp -- Configures A10 debug.lacp
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

lacp - LACP commands






Parameters
----------

  all (False, any, None)
    all - turn on all debugging


  ansible_username (True, any, None)
    Username for AXAPI authentication


  sync (False, any, None)
    sync - echo synchronization to console


  packet (False, any, None)
    packet - echo packet contents to console


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ha (False, any, None)
    ha - echo High availability events to console


  a10_partition (False, any, None)
    Destination/target partition for object/command


  event (False, any, None)
    event - echo events to console


  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  cli (False, any, None)
    cli - echo commands to console


  detail (False, any, None)
    detail - echo timer start/stop to console


  timer (False, any, None)
    timer - echo timer expiry to console


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


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

