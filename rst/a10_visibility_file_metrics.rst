.. _a10_visibility_file_metrics_module:


a10_visibility_file_metrics -- Configures A10 visibility.file.metrics
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Persistent storage for metrics






Parameters
----------

  oper (False, any, None)
    Field oper


    sec_l4_proto (optional, any, None)
      Field sec_l4_proto


    pri_ipv4_addr (optional, any, None)
      Field pri_ipv4_addr


    sec_ipv6_addr (optional, any, None)
      Field sec_ipv6_addr


    pri_l4_proto (optional, any, None)
      Field pri_l4_proto


    pri_type (optional, any, None)
      Field pri_type


    sec_l4_port (optional, any, None)
      Field sec_l4_port


    proc_metric_list (optional, any, None)
      Field proc_metric_list


    sec_type (optional, any, None)
      Field sec_type


    file_name (optional, any, None)
      Field file_name


    sec_ipv4_addr (optional, any, None)
      Field sec_ipv4_addr


    pri_ipv6_addr (optional, any, None)
      Field pri_ipv6_addr


    monitor_type (optional, any, None)
      Field monitor_type


    pri_l4_port (optional, any, None)
      Field pri_l4_port



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  action (False, any, None)
    'enable'= Enable persistent storage(default); 'disable'= Disable persistent storage;


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

