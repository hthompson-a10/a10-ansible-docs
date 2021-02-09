.. _a10_debug_vector_module:


a10_debug_vector -- Configures A10 debug.vector
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Debug vector flow






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  trace (False, any, None)
    Debug logs for vector callbacks


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  packet (False, any, None)
    Debug logs for vector packet flow


  state (True, any, None)
    State of the object to be created.


  error (False, any, None)
    Debug logs for vector errors


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

