.. _a10_scaleout_status_module:


a10_scaleout_status -- Configures A10 scaleout.status
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Field status






Parameters
----------

  oper (False, any, None)
    Field oper


    l2redirect_vlan (optional, any, None)
      Field l2redirect_vlan


    device_list (optional, any, None)
      Field device_list


    l2redirect_eth (optional, any, None)
      Field l2redirect_eth


    l2redirect_valid (optional, any, None)
      Field l2redirect_valid


    l2redirect_operational (optional, any, None)
      Field l2redirect_operational


    role (optional, any, None)
      Field role


    l2redirect (optional, any, None)
      Field l2redirect


    l2redirect_trunk (optional, any, None)
      Field l2redirect_trunk


    db_role (optional, any, None)
      Field db_role



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

