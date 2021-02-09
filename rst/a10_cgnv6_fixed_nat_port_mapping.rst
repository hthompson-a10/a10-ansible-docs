.. _a10_cgnv6_fixed_nat_port_mapping_module:


a10_cgnv6_fixed_nat_port_mapping -- Configures A10 cgnv6.fixed.nat.port-mapping
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Fixed NAT Port Mapping






Parameters
----------

  oper (False, any, None)
    Field oper


    nat_port (optional, any, None)
      Field nat_port


    mapping_list (optional, any, None)
      Field mapping_list


    inside_user_v6 (optional, any, None)
      Field inside_user_v6


    partition (optional, any, None)
      Field partition


    nat_ip (optional, any, None)
      Field nat_ip


    inside_user_v4 (optional, any, None)
      Field inside_user_v4



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

