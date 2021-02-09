.. _a10_cgnv6_scaleout_address_mapping_module:


a10_cgnv6_scaleout_address_mapping -- Configures A10 cgnv6.scaleout.address-mapping
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Field address_mapping






Parameters
----------

  oper (False, any, None)
    Field oper


    ip_list (optional, any, None)
      Field ip_list


    ip (optional, any, None)
      Field ip


    ipv6 (optional, any, None)
      Field ipv6


    nat_ip (optional, any, None)
      Field nat_ip


    active_node (optional, any, None)
      Field active_node


    nat_pool (optional, any, None)
      Field nat_pool


    user_group (optional, any, None)
      Field user_group


    standby_node (optional, any, None)
      Field standby_node



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

