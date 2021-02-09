.. _a10_environment_module:


a10_environment -- Configures A10 environment
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

environment status colletion parameters






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


  threshold_cfg (False, any, None)
    Field threshold_cfg


    high (optional, any, None)
      High threshold value in Celsius - default 1


    medium (optional, any, None)
      Medium threshold value in Celsius - default 1


    low (optional, any, None)
      Low threshold value in Celsius - default 1



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  update_interval (False, any, None)
    Field update_interval


    interval (optional, any, None)
      Interval



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

