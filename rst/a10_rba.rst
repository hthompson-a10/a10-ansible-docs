.. _a10_rba_module:


a10_rba -- Configures A10 rba
=============================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Role Based Access configuration






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


  group_list (False, any, None)
    Field group_list


    user_list (optional, any, None)
      Field user_list


    user_tag (optional, any, None)
      Customized tag


    uuid (optional, any, None)
      uuid of the object


    name (optional, any, None)
      Name of a RBA group


    partition_list (optional, any, None)
      Field partition_list



  ansible_host (True, any, None)
    Host for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  action (False, any, None)
    'enable'= Enable RBA; 'disable'= Disable RBA;


  role_list (False, any, None)
    Field role_list


    rule_list (optional, any, None)
      Field rule_list


    default_privilege (optional, any, None)
      'no-access'= no-access; 'read'= read; 'write'= write;


    name (optional, any, None)
      Name for the RBA role


    partition_only (optional, any, None)
      Partition RBA Role


    user_tag (optional, any, None)
      Customized tag


    uuid (optional, any, None)
      uuid of the object



  a10_partition (False, any, None)
    Destination/target partition for object/command


  user_list (False, any, None)
    Field user_list


    uuid (optional, any, None)
      uuid of the object


    user_tag (optional, any, None)
      Customized tag


    name (optional, any, None)
      Name of a user account


    partition_list (optional, any, None)
      Field partition_list










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

