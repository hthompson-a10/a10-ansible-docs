.. _a10_axdebug_capture_module:


a10_axdebug_capture -- Configures A10 axdebug.capture
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Dump packets






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  save (False, any, None)
    Save packets into file (Specify filename to save packets)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  brief (False, any, None)
    Print basic packet information


  detail (False, any, None)
    Include packet payload


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  current_slot (False, any, None)
    Only for current-slot of chassis


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

