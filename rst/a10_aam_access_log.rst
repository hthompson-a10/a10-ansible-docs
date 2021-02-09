.. _a10_aam_access_log_module:


a10_aam_access_log -- Configures A10 aam.access-log
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Access Log Info






Parameters
----------

  oper (False, any, None)
    Field oper


    last (optional, any, None)
      Field last


    target (optional, any, None)
      Field target


    top (optional, any, None)
      Field top


    tail (optional, any, None)
      Field tail


    host_name (optional, any, None)
      Field host_name


    access_status (optional, any, None)
      Field access_status


    total (optional, any, None)
      Field total


    log_list (optional, any, None)
      Field log_list



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

