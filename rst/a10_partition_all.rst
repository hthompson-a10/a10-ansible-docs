.. _a10_partition_all_module:


a10_partition_all -- Configures A10 partition-all
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Display all partitions in the system






Parameters
----------

  oper (False, any, None)
    Field oper


    manageable (optional, any, None)
      Field manageable


    partition_list (optional, any, None)
      Field partition_list


    active_partition_count (optional, any, None)
      Field active_partition_count



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

