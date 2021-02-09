.. _a10_gslb_group_module:


a10_gslb_group -- Configures A10 gslb.group
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

GSLB Group






Parameters
----------

  auto_map_primary (False, any, None)
    Primary Controller's IP address


  enable (False, any, None)
    Join GSLB Group


  suffix (False, any, None)
    Set DNS Suffix (Name)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  dns_discover (False, any, None)
    Discover member via DNS Protocol


  config_anywhere (False, any, None)
    Every member can do config


  config_merge (False, any, None)
    Merge old master's config when new one take over


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  auto_map_smart (False, any, None)
    Choose Best IP address


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  data_interface (False, any, None)
    Data Interface IP Address


  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  primary_list (False, any, None)
    Field primary_list


    primary (optional, any, None)
      Specify Primary controller's IP address



  standalone (False, any, None)
    Run GSLB Group in standalone mode


  ansible_password (True, any, None)
    Password for AXAPI authentication


  name (True, any, None)
    Specify Group domain name


  priority (False, any, None)
    Specify Local Priority, default is 100


  config_save (False, any, None)
    Accept config-save message from master


  state (True, any, None)
    State of the object to be created.


  learn (False, any, None)
    Learn neighbour information from other controllers


  auto_map_learn (False, any, None)
    IP Address learned from other controller


  user_tag (False, any, None)
    Customized tag


  mgmt_interface (False, any, None)
    Management Interface IP Address









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

