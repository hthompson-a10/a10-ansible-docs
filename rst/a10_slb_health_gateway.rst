.. _a10_slb_health_gateway_module:


a10_slb_health_gateway -- Configures A10 slb.health-gateway
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure gateway health-check






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'total_sent'= Number of Total health-check sent; 'total_retry_sent'= Number of Total health-check retry sent; 'total_timeout'= Number of Total health-check timeout;



  oper (False, any, None)
    Field oper


    interval (optional, any, None)
      Field interval


    enabled (optional, any, None)
      Field enabled


    timeout (optional, any, None)
      Field timeout



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    total_sent (optional, any, None)
      Number of Total health-check sent


    total_retry_sent (optional, any, None)
      Number of Total health-check retry sent


    total_timeout (optional, any, None)
      Number of Total health-check timeout



  uuid (False, any, None)
    uuid of the object


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

