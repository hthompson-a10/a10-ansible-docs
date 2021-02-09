.. _a10_gslb_policy_auto_map_module:


a10_gslb_policy_auto_map -- Configures A10 gslb.policy.auto-map
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Auto Mapping Options






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


  all (False, any, None)
    All modules


  policy_name (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  module_type (False, any, None)
    Field module_type


  ttl (False, any, None)
    Specify Auto Map TTL (TTL, default is 300)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  module_disable (False, any, None)
    Specify Disable Auto Map Module


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

