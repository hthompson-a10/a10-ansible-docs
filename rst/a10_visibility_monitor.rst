.. _a10_visibility_monitor_module:


a10_visibility_monitor -- Configures A10 visibility.monitor
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure monitoring keys






Parameters
----------

  index_sessions (False, any, None)
    Start indexing associated sessions


  ansible_username (True, any, None)
    Username for AXAPI authentication


  replay_debug_file (False, any, None)
    Field replay_debug_file


    debug_protocol (optional, any, None)
      'TCP'= TCP; 'UDP'= UDP; 'ICMP'= ICMP;


    debug_port (optional, any, None)
      Specify port


    debug_ip_addr (optional, any, None)
      Specify source/dest ip addr



  index_sessions_type (False, any, None)
    'per-cpu'= Use per cpu list;


  delete_debug_file (False, any, None)
    Field delete_debug_file


    debug_protocol (optional, any, None)
      'TCP'= TCP; 'UDP'= UDP; 'ICMP'= ICMP;


    debug_port (optional, any, None)
      Specify port


    debug_ip_addr (optional, any, None)
      Specify source/dest ip addr



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  netflow (False, any, None)
    Field netflow


    template_active_timeout (optional, any, None)
      Configure active timeout of the netflow templates received in mins (Template active timeout(mins)(default 30mins))


    listening_port (optional, any, None)
      Netflow port to receive packets (Netflow port number(default 9996))


    uuid (optional, any, None)
      uuid of the object



  secondary_monitor (False, any, None)
    Field secondary_monitor


    mon_entity_topk (optional, any, None)
      Enable topk for secondary entities


    secondary_monitoring_key (optional, any, None)
      'service'= Monitor traffic to any service;


    uuid (optional, any, None)
      uuid of the object


    source_entity_topk (optional, any, None)
      Enable topk for sources to secondary-entities


    debug_list (optional, any, None)
      Field debug_list


    replay_debug_file (optional, any, None)
      Field replay_debug_file


    delete_debug_file (optional, any, None)
      Field delete_debug_file



  monitor_key (False, any, None)
    'source'= Monitor traffic from all sources; 'dest'= Monitor traffic to any destination; 'service'= Monitor traffic to any service; 'source-nat-ip'= Monitor traffic to all source nat IPs;


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  sflow (False, any, None)
    Field sflow


    listening_port (optional, any, None)
      sFlow port to receive packets (sFlow port number(default 6343))


    uuid (optional, any, None)
      uuid of the object



  agent_list (False, any, None)
    Field agent_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    agent_name (optional, any, None)
      Specify name for the agent


    agent_v4_addr (optional, any, None)
      Configure agent's IPv4 address


    uuid (optional, any, None)
      uuid of the object


    agent_v6_addr (optional, any, None)
      Configure agent's IPv6 address


    user_tag (optional, any, None)
      Customized tag



  a10_partition (False, any, None)
    Destination/target partition for object/command


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



  primary_monitor (True, any, None)
    'traffic'= Mointor traffic;


  ansible_host (True, any, None)
    Host for AXAPI authentication


  mon_entity_topk (False, any, None)
    Enable topk for primary entities


  state (True, any, None)
    State of the object to be created.


  template (False, any, None)
    Field template


    notification (optional, any, None)
      Field notification



  source_entity_topk (False, any, None)
    Enable topk for sources to primary-entities


  ansible_password (True, any, None)
    Password for AXAPI authentication









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

