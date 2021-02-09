.. _a10_slb_server_group_module:


a10_slb_server_group -- Configures A10 slb.server-group
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

server-group






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    dummy_conn (optional, any, None)
      Current established connections


    name (optional, any, None)
      server-group name



  name (True, any, None)
    server-group name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  member_list (False, any, None)
    Field member_list


    name (optional, any, None)
      Member name


    uuid (optional, any, None)
      uuid of the object



  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


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

