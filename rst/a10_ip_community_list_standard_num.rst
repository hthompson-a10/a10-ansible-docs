.. _a10_ip_community_list_standard_num_module:


a10_ip_community_list_standard_num -- Configures A10 ip.community.list.standard-num
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Standard number Community-list






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


  rules_list (False, any, None)
    Field rules_list


    std_list_comm_value (optional, any, None)
      community value in the format 1-4294967295|AA=NN|internet|local-AS|no- advertise|no-export


    std_list_action (optional, any, None)
      'deny'= Specify community to reject; 'permit'= Specify community to accept;



  std_list_num (True, any, None)
    Community list number (standard)


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

