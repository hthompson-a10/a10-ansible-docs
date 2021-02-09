.. _a10_slb_common_conn_rate_limit_src_ip_module:


a10_slb_common_conn_rate_limit_src_ip -- Configures A10 slb.common.conn.rate-limit.src-ip
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set connection limit based on source IP address






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  protocol (True, any, None)
    'tcp'= Set TCP connection rate limit; 'udp'= Set UDP packet rate limit;


  log (False, any, None)
    Send log if threshold exceeded


  ansible_username (True, any, None)
    Username for AXAPI authentication


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  limit_period (False, any, None)
    '100'= 100 ms; '1000'= 1000 ms;


  limit (False, any, None)
    Set max connections per period


  shared (False, any, None)
    Set threshold shared amongst all virtual ports


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  exceed_action (False, any, None)
    Set action if threshold exceeded


  lock_out (False, any, None)
    Set lockout period in seconds if threshold exceeded


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

