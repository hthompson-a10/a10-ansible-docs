.. _a10_system_big_buff_pool_module:


a10_system_big_buff_pool -- Configures A10 system-big-buff-pool
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

System big buff pool config






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  big_buff_pool (False, any, None)
    Configure big I/O buffer pool


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


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

