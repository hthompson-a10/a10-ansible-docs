.. _a10_license_manager_overage_module:


a10_license_manager_overage -- Configures A10 license.manager.overage
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set overage parameters






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  seconds (False, any, None)
    Number of seconds


  hours (False, any, None)
    Number of hours


  gb (False, any, None)
    Number of GB


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  kb (False, any, None)
    Number of KB


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  mb (False, any, None)
    Number of MB


  ansible_password (True, any, None)
    Password for AXAPI authentication


  bytes (False, any, None)
    Number of bytes


  days (False, any, None)
    Number of days


  state (True, any, None)
    State of the object to be created.


  minutes (False, any, None)
    Number of minutes









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

