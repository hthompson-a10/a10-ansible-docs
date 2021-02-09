.. _a10_debug_cgn_module:


a10_debug_cgn -- Configures A10 debug.cgn
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

CGN packet debugging






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


  state (True, any, None)
    State of the object to be created.


  error (False, any, None)
    Debug logs for errors in CGN


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  drops (False, any, None)
    Debug logs for packet drops in CGN


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

