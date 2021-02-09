.. _a10_debug_local_log_module:


a10_debug_local_log -- Configures A10 debug.local-log
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Debug LOCAL log






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  group (False, any, None)
    'query'= Debug local log query (axapi).; 'db-mgr'= Debug local log database management.; 'db-write'= Debug local log insert local log into database.; 'queue'= Debug local log generate and inqueue/dequeue.;


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  level (False, any, None)
    Debug level (Level 1-3. 1=error, 2=notice, 3=Info)


  state (True, any, None)
    State of the object to be created.


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

