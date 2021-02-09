.. _a10_cgnv6_lw_4o6_binding_table_validate_module:


a10_cgnv6_lw_4o6_binding_table_validate -- Configures A10 cgnv6.lw.4o6.binding-table-validate
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Check for errors in LW-4over6 Binding Table






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  binding_name (False, any, None)
    LW-4over6 Binding Table Name


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

