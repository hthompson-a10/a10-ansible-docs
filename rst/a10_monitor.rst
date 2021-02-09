.. _a10_monitor_module:


a10_monitor -- Configures A10 monitor
=====================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

System monitor configuration






Parameters
----------

  ctrl_cpu (False, any, None)
    Monitor control CPU threshold (Threshold value in percentage, default 90)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  warn_temp (False, any, None)
    Monitor warning system temperature threshold (Threshold value in Celsius, default 68)


  buffer_drop (False, any, None)
    Monitor buffer drop threshold (Threshold value)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  conn_type1 (False, any, None)
    Conn resource type 1 (Threshold value, default 32767)


  conn_type0 (False, any, None)
    Conn resource type 0 (Threshold value, default 32767)


  conn_type3 (False, any, None)
    Conn resource type 3 (Threshold value, default 32767)


  conn_type2 (False, any, None)
    Conn resource type 2 (Threshold value, default 32767)


  conn_type4 (False, any, None)
    Conn resource type 4 (Threshold value, default 32767)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  disk (False, any, None)
    Monitor hard disk usage threshold (Threshold value in percentage, default 85)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  smp_type0 (False, any, None)
    SMP resource type 0 (Threshold value, default 32767)


  smp_type1 (False, any, None)
    SMP resource type 1 (Threshold value, default 32767)


  smp_type2 (False, any, None)
    SMP resource type 2 (Threshold value, default 32767)


  smp_type3 (False, any, None)
    SMP resource type 3 (Threshold value, default 32767)


  smp_type4 (False, any, None)
    SMP resource type 4 (Threshold value, default 32767)


  uuid (False, any, None)
    uuid of the object


  state (True, any, None)
    State of the object to be created.


  buffer_usage (False, any, None)
    Monitor IO buffer usage threshold (Threshold value)


  memory (False, any, None)
    Monitor memory usage threshold (Threshold value in percentage, default 95)


  data_cpu (False, any, None)
    Monitor data CPU threshold (Threshold value in percentage, default 90)


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

