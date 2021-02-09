.. _a10_system_trunk_load_balance_module:


a10_system_trunk_load_balance -- Configures A10 system.trunk.load-balance
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Trunk load balancing options






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


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  use_l4 (False, any, None)
    Layer-3/4 Header based load balancing


  a10_partition (False, any, None)
    Destination/target partition for object/command


  use_l3 (False, any, None)
    Layer-3 Header based load balancing









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

