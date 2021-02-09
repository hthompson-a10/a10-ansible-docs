.. _a10_vpn_log_module:


a10_vpn_log -- Configures A10 vpn.log
=====================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Log






Parameters
----------

  oper (False, any, None)
    Field oper


    vpn_log_offset (optional, any, None)
      Field vpn_log_offset


    vpn_log_over (optional, any, None)
      Field vpn_log_over


    num_lines (optional, any, None)
      Field num_lines


    from_start (optional, any, None)
      Field from_start


    follow (optional, any, None)
      Field follow


    vpn_log_list (optional, any, None)
      Field vpn_log_list



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

