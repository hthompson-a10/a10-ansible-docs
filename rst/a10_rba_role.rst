.. _a10_rba_role_module:


a10_rba_role -- Configures A10 rba.role
=======================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Role configuration for RBA support






Parameters
----------

  rule_list (False, any, None)
    Field rule_list


    operation (optional, any, None)
      'no-access'= no-access; 'read'= read; 'oper'= oper; 'write'= write;


    object (optional, any, None)
      Lineage of object class for permitted operation



  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  name (True, any, None)
    Name for the RBA role


  ansible_username (True, any, None)
    Username for AXAPI authentication


  partition_only (False, any, None)
    Partition RBA Role


  state (True, any, None)
    State of the object to be created.


  default_privilege (False, any, None)
    'no-access'= no-access; 'read'= read; 'write'= write;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  uuid (False, any, None)
    uuid of the object









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

