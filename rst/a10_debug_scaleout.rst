.. _a10_debug_scaleout_module:


a10_debug_scaleout -- Configures A10 debug.scaleout
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Debug scaleout






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  config (False, any, None)
    Debug logs for scaleout config change


  ansible_password (True, any, None)
    Password for AXAPI authentication


  packet (False, any, None)
    Debug logs for scaleout packet flow


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  event (False, any, None)
    Debug logs for scaleout events









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

