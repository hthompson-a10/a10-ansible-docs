.. _a10_cgnv6_fixed_nat_port_mapping_files_module:


a10_cgnv6_fixed_nat_port_mapping_files -- Configures A10 cgnv6.fixed.nat.port-mapping-files
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Fixed NAT Port Mapping Files






Parameters
----------

  oper (False, any, None)
    Field oper


    file_list (optional, any, None)
      Field file_list


    ntype (optional, any, None)
      Field type


    contain_case_sensitive (optional, any, None)
      Field contain_case_sensitive


    contain (optional, any, None)
      Field contain



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

