.. _a10_netflow_monitor_sample_nat_pool_module:


a10_netflow_monitor_sample_nat_pool -- Configures A10 netflow.monitor.sample.nat-pool
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Select nat pool to monitor






Parameters
----------

  pool_name (True, any, None)
    Name of nat pool


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  monitor_name (optional, any, None)
    Key to identify parent object


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

