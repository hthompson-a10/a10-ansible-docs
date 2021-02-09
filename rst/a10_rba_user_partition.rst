.. _a10_rba_user_partition_module:


a10_rba_user_partition -- Configures A10 rba.user.partition
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

RBA configuration for the access privilege of a user within one partition






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


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  user_name (optional, any, None)
    Key to identify parent object


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  role_list (False, any, None)
    Field role_list


    role (optional, any, None)
      Role in a given partition



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  partition_name (True, any, None)
    partition name









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

