.. _a10_cgnv6_lsn_port_overloading_port_overloading_status_module:


a10_cgnv6_lsn_port_overloading_port_overloading_status -- Configures A10 cgnv6.lsn.port.overloading.port-overloading-status
===========================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show port-overloading-status






Parameters
----------

  oper (False, any, None)
    Field oper


    tcp_list (optional, any, None)
      Field tcp_list


    unique (optional, any, None)
      Field unique


    udp_list (optional, any, None)
      Field udp_list



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

