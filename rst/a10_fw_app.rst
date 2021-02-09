.. _a10_fw_app_module:


a10_fw_app -- Configures A10 fw.app
===================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show application firewall supported protocols






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'dummy'= Entry for a10countergen;



  oper (False, any, None)
    Field oper


    category (optional, any, None)
      Field category


    contains (optional, any, None)
      Field contains


    related (optional, any, None)
      Field related


    group_list (optional, any, None)
      Field group_list



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    dummy (optional, any, None)
      Entry for a10countergen



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

