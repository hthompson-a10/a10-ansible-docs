.. _a10_visibility_monitor_secondary_monitor_module:


a10_visibility_monitor_secondary_monitor -- Configures A10 visibility.monitor.secondary-monitor
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure secondary monitoring key






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  secondary_monitoring_key (True, any, None)
    'service'= Monitor traffic to any service;


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  replay_debug_file (False, any, None)
    Field replay_debug_file


    debug_protocol (optional, any, None)
      'TCP'= TCP; 'UDP'= UDP; 'ICMP'= ICMP;


    debug_port (optional, any, None)
      Specify port


    debug_ip_addr (optional, any, None)
      Specify source/dest ip addr



  delete_debug_file (False, any, None)
    Field delete_debug_file


    debug_protocol (optional, any, None)
      'TCP'= TCP; 'UDP'= UDP; 'ICMP'= ICMP;


    debug_port (optional, any, None)
      Specify port


    debug_ip_addr (optional, any, None)
      Specify source/dest ip addr



  mon_entity_topk (False, any, None)
    Enable topk for secondary entities


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  source_entity_topk (False, any, None)
    Enable topk for sources to secondary-entities


  debug_list (False, any, None)
    Field debug_list


    debug_protocol (optional, any, None)
      'TCP'= TCP; 'UDP'= UDP; 'ICMP'= ICMP;


    debug_port (optional, any, None)
      Specify port


    uuid (optional, any, None)
      uuid of the object


    debug_ip_addr (optional, any, None)
      Specify source/dest ip addr



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

