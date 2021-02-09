.. _a10_vcs_vmaster_take_over_module:


a10_vcs_vmaster_take_over -- Configures A10 vcs.vmaster-take-over
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Forcefully take over mastership






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  vmaster_take_over (False, any, None)
    vMaster take over priority


  state (True, any, None)
    State of the object to be created.


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

