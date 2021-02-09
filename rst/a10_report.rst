.. _a10_report_module:


a10_report -- Configures A10 report
===================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Report configurations






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  debug (False, any, None)
    Field debug


    log (optional, any, None)
      Enable Report module's normal logs


    sflow (optional, any, None)
      Enable debugging logs of sFlow parser



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

