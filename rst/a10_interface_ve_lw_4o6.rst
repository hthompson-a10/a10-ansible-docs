.. _a10_interface_ve_lw_4o6_module:


a10_interface_ve_lw_4o6 -- Configures A10 interface.ve.lw-4o6
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure LW-4over6 interface






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ve_ifnum (optional, any, None)
    Key to identify parent object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  inside (False, any, None)
    Configure LW-4over6 outside interface


  state (True, any, None)
    State of the object to be created.


  outside (False, any, None)
    Configure LW-4over6 inside interface


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


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

