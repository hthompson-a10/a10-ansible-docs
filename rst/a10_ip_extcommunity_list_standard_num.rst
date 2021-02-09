.. _a10_ip_extcommunity_list_standard_num_module:


a10_ip_extcommunity_list_standard_num -- Configures A10 ip.extcommunity.list.standard-num
=========================================================================================

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


    std_list_action (optional, any, None)
      'deny'= Specify community to reject; 'permit'= Specify community to accept;


    std_list_value (optional, any, None)
      rt Route Target extended community in aa=nn or IPaddr=nn format OR soo Site-of- Origin extended community in aa=nn or IPaddr=nn



  std_list_num (True, any, None)
    Extended Community list number (standard)


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

