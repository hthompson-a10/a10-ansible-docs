.. _a10_gslb_policy_active_rdt_module:


a10_gslb_policy_active_rdt -- Configures A10 gslb.policy.active-rdt
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Select SLB device with the shortest round delay time to local DNS






Parameters
----------

  keep_tracking (False, any, None)
    Keep tracking client even round-delay-time samples are ready


  enable (False, any, None)
    Enable the active rdt


  fail_break (False, any, None)
    Break when no valid RDT


  ansible_username (True, any, None)
    Username for AXAPI authentication


  proto_rdt_enable (False, any, None)
    Enable the round-delay-time to the controller


  policy_name (optional, any, None)
    Key to identify parent object


  controller (False, any, None)
    Active round-delay-time by controller


  skip (False, any, None)
    Skip query if round-delay-time samples are not ready (Specify maximum skip count,default is 3)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  difference (False, any, None)
    The difference between the round-delay-time, default is 0


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  single_shot (False, any, None)
    Single Shot RDT


  ansible_password (True, any, None)
    Password for AXAPI authentication


  timeout (False, any, None)
    Specify timeout if round-delay-time samples are not ready (Specify timeout, unit=sec,default is 3)


  state (True, any, None)
    State of the object to be created.


  limit (False, any, None)
    Limit of allowed RDT, default is 16383 (Limit, unit= millisecond)


  samples (False, any, None)
    Specify samples number for round-delay-time (Number of samples,default is 5)


  ignore_id (False, any, None)
    Ignore IP Address specified in IP List by ID


  tolerance (False, any, None)
    The difference percentage between the round-delay-time, default is 10 (Tolerance)









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

