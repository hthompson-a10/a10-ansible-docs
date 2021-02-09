.. _a10_delete_cgnv6_module:


a10_delete_cgnv6 -- Configures A10 delete.cgnv6
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Delete cgnv6 related files






Parameters
----------

  lw_4o6_binding_table_validation_log (False, any, None)
    LW-4O6 Binding Table validation log File


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  lw_filename (False, any, None)
    LW-4O6 Binding Table Validation Log File Name


  filename (False, any, None)
    Specify the port-mapping-file to be deleted


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  fixed_nat (False, any, None)
    Delete fixed-nat port-mapping-file


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

