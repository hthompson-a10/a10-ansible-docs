.. _a10_snmp_server_slb_data_cache_timeout_module:


a10_snmp_server_slb_data_cache_timeout -- Configures A10 snmp.server.slb-data-cache-timeout
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure the SLB data cache time-out in seconds






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


  slblimit (False, any, None)
    Cache time-out in seconds, default as 60 seconds


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

