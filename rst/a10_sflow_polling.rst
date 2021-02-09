.. _a10_sflow_polling_module:


a10_sflow_polling -- Configures A10 sflow.polling
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure sFlow counter polling on specified source






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  cpu_usage (False, any, None)
    Polling CPU usage


  http_counter (False, any, None)
    Polling HTTP counters


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  eth_list (False, any, None)
    Field eth_list


    eth_start (optional, any, None)
      Ethernet interface to sample


    eth_end (optional, any, None)
      Ethernet interface to sample



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ve_list (False, any, None)
    Field ve_list


    ve_start (optional, any, None)
      VE interface to sample


    ve_end (optional, any, None)
      VE interface to sample



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object









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

