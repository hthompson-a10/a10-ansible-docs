.. _a10_gslb_policy_capacity_module:


a10_gslb_policy_capacity -- Configures A10 gslb.policy.capacity
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Select Service-IP for the device having highest available connection capacity






Parameters
----------

  capacity_enable (False, any, None)
    Enable capacity


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  policy_name (optional, any, None)
    Key to identify parent object


  capacity_fail_break (False, any, None)
    Break when exceed threshold


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  threshold (False, any, None)
    Specify capacity threshold, default is 90


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

