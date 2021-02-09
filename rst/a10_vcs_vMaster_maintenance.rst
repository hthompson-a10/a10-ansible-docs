.. _a10_vcs_vMaster_maintenance_module:


a10_vcs_vMaster_maintenance -- Configures A10 vcs.vMaster-maintenance
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

During this period, vMaster can leave and come back to be vMaster again






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  vMaster_maintenance (False, any, None)
    the seconds vMaster will be maintained, 60 by default


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

