.. _a10_slb_ipv6_class_list_module:


a10_slb_ipv6_class_list -- Configures A10 slb.ipv6-class-list
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IPv6 subnet add remove config






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ipv6_list (False, any, None)
    Field ipv6_list


    lid (optional, any, None)
      Use Limit ID defined in template (Specify LID index)


    action (optional, any, None)
      'add'= Add the entry; 'delete'= Delete the entry;


    ipv6_addr (optional, any, None)
      Specify IPv6 host or subnet


    glid (optional, any, None)
      Use global Limit ID (Specify global LID index)


    lsn_radius_profile (optional, any, None)
      LSN RADIUS Profile Index


    lsn_lid (optional, any, None)
      LSN Limit ID (LID index)



  name (True, any, None)
    Specify name of the class list


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


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

