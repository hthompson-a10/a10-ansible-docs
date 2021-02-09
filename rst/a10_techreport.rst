.. _a10_techreport_module:


a10_techreport -- Configures A10 techreport
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure show tech






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


  max_partitions (False, any, None)
    Field max_partitions


    uuid (optional, any, None)
      uuid of the object


    value (optional, any, None)
      Maximum partions to show in per periodic techsupport (default is 30)



  interval (False, any, None)
    Field interval


    uuid (optional, any, None)
      uuid of the object


    value (optional, any, None)
      Showtech interval in minutes (default is 15)



  max_logfile_size (False, any, None)
    Field max_logfile_size


    uuid (optional, any, None)
      uuid of the object


    value (optional, any, None)
      Log file size for periodic techsupport (default is 1)



  state (True, any, None)
    State of the object to be created.


  disable (False, any, None)
    Disable the polling techreport


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ansible_host (True, any, None)
    Host for AXAPI authentication


  a10_partition (False, any, None)
    Destination/target partition for object/command


  priority_partition_list (False, any, None)
    Field priority_partition_list


    uuid (optional, any, None)
      uuid of the object


    part_name (optional, any, None)
      Name of partition always want to show in showtech (shared is always shown by default)










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

