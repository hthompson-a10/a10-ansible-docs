.. _a10_fw_limit_entry_module:


a10_fw_limit_entry -- Configures A10 fw.limit-entry
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Rate Limit Information






Parameters
----------

  oper (False, any, None)
    Field oper


    limit_entry_list (optional, any, None)
      Field limit_entry_list


    prefix_len6 (optional, any, None)
      Field prefix_len6


    prefix_len4 (optional, any, None)
      Field prefix_len4


    pps (optional, any, None)
      Field pps


    prefix6 (optional, any, None)
      Field prefix6


    throughput (optional, any, None)
      Field throughput


    prefix4 (optional, any, None)
      Field prefix4


    limit_entry_count (optional, any, None)
      Field limit_entry_count


    user_quota (optional, any, None)
      Field user_quota



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

