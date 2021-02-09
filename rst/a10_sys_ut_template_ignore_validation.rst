.. _a10_sys_ut_template_ignore_validation_module:


a10_sys_ut_template_ignore_validation -- Configures A10 sys.ut.template.ignore-validation
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Ignore following layers for validation






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  template_name (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  l4 (False, any, None)
    Dont validate L4 header


  l2 (False, any, None)
    Dont validate L2 header


  l3 (False, any, None)
    Dont validate L3 header


  all (False, any, None)
    Skip validation


  l1 (False, any, None)
    Dont validate TX descriptor. This includes Tx port, Len & vlan


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

