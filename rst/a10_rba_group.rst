.. _a10_rba_group_module:


a10_rba_group -- Configures A10 rba.group
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

RBA configuration for a group






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Name of a RBA group


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  partition_list (False, any, None)
    Field partition_list


    rule_list (optional, any, None)
      Field rule_list


    role_list (optional, any, None)
      Field role_list


    user_tag (optional, any, None)
      Customized tag


    uuid (optional, any, None)
      uuid of the object


    partition_name (optional, any, None)
      partition name



  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ansible_host (True, any, None)
    Host for AXAPI authentication


  a10_partition (False, any, None)
    Destination/target partition for object/command


  user_list (False, any, None)
    Field user_list


    user (optional, any, None)
      Users in the group



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

