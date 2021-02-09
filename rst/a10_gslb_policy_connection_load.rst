.. _a10_gslb_policy_connection_load_module:


a10_gslb_policy_connection_load -- Configures A10 gslb.policy.connection-load
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Select Service-IP with the lowest connection-load






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  connection_load_fail_break (False, any, None)
    Break when exceed limit


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  connection_load_samples (False, any, None)
    Specify samples for connection-load (Number of samples used to calculate the connection load, default is 5)


  connection_load_enable (False, any, None)
    Enable connection-load


  policy_name (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  limit (False, any, None)
    Limit of maxinum connection load, default is unlimited


  connection_load_interval (False, any, None)
    Interval between two samples, Unit= second (Interval value,default is 5)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  connection_load_limit (False, any, None)
    The value of the connection-load limit, default is unlimited









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

