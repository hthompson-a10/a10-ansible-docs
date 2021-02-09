.. _a10_cgnv6_logging_module:


a10_cgnv6_logging -- Configures A10 cgnv6.logging
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

CGNV6 Logging Statistics






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'tcp-session-created'= TCP Session Created; 'tcp-session-deleted'= TCP Session Deleted; 'tcp-port-allocated'= TCP Port Allocated; 'tcp-port- freed'= TCP Port Freed; 'tcp-port-batch-allocated'= TCP Port Batch Allocated; 'tcp-port-batch-freed'= TCP Port Batch Freed; 'udp-session-created'= UDP Session Created; 'udp-session-deleted'= UDP Session Deleted; 'udp-port- allocated'= UDP Port Allocated; 'udp-port-freed'= UDP Port Freed; 'udp-port- batch-allocated'= UDP Port Batch Allocated; 'udp-port-batch-freed'= UDP Port Batch Freed; 'icmp-session-created'= ICMP Session Created; 'icmp-session- deleted'= ICMP Session Deleted; 'icmp-resource-allocated'= ICMP Resource Allocated; 'icmp-resource-freed'= ICMP Resource Freed; 'icmpv6-session- created'= ICMPV6 Session Created; 'icmpv6-session-deleted'= ICMPV6 Session Deleted; 'icmpv6-resource-allocated'= ICMPV6 Resource Allocated; 'icmpv6-resource-freed'= ICMPV6 Resource Freed; 'gre-session-created'= GRE Session Created; 'gre-session-deleted'= GRE Session Deleted; 'gre-resource- allocated'= GRE Resource Allocated; 'gre-resource-freed'= GRE Resource Freed; 'esp-session-created'= ESP Session Created; 'esp-session-deleted'= ESP Session Deleted; 'esp-resource-allocated'= ESP Resource Allocated; 'esp-resource- freed'= ESP Resource Freed; 'fixed-nat-user-ports'= Fixed NAT Inside User Port Mapping; 'fixed-nat-disable-config-logged'= Fixed NAT Periodic Configs Logged; 'fixed-nat-disable-config-logs-sent'= Fixed NAT Periodic Config Logs Sent; 'fixed-nat-periodic-config-logs-sent'= Fixed NAT Disabled Configs Logged; 'fixed-nat-periodic-config-logged'= Fixed NAT Disabled Config Logs Sent; 'fixed-nat-interim-updated'= Fixed NAT Interim Updated; 'enhanced-user-log'= Enhanced User Log; 'log-sent'= Log Packets Sent; 'log-dropped'= Log Packets Dropped; 'conn-tcp-established'= TCP Connection Established; 'conn-tcp- dropped'= TCP Connection Lost; 'tcp-port-overloading-allocated'= TCP Port Overloading Allocated; 'tcp-port-overloading-freed'= TCP Port Overloading Freed; 'udp-port-overloading-allocated'= UDP Port Overloading Allocated; 'udp- port-overloading-freed'= UDP Port Overloading Freed; 'http-request-logged'= HTTP Request Logged; 'reduced-logs-by-destination'= Reduced Logs by Destination Protocol and Port; 'out-of-buffers'= Out of Buffers; 'add-msg-failed'= Add Message to Buffer Failed; 'rtsp-port-allocated'= RTSP UDP Port Allocated; 'rtsp-port-freed'= RTSP UDP Port Freed; 'conn-tcp-create-failed'= TCP Connection Failed; 'ipv4-frag-applied'= IPv4 Fragmentation Applied; 'ipv4-frag- failed'= IPv4 Fragmentation Failed; 'ipv6-frag-applied'= IPv6 Fragmentation Applied; 'ipv6-frag-failed'= IPv6 Fragmentation Failed; 'interim-update- scheduled'= Port Allocation Interim Update Scheduled; 'interim-update-schedule- failed'= Port Allocation Interim Update Failed; 'interim-update-terminated'= Port Allocation Interim Update Terminated; 'interim-update-memory-freed'= Port Allocation Interim Update Memory Freed; 'interim-update-no-buff-retried'= Port Allocation Interim Update Memory Freed; 'tcp-port-batch-interim-updated'= TCP Port Batch Interim Updated; 'udp-port-batch-interim-updated'= UDP Port Batch Interim Updated; 'port-block-accounting-freed'= Port Allocation Accounting Freed; 'port-block-accounting-allocated'= Port Allocation Accounting Allocated; 'log-message-too-long'= Log message too long; 'http-out-of-order-dropped'= HTTP out-of-order dropped; 'http-alloc-failed'= HTTP Request Info Allocation Failed; 'http-frag-merge-failed-dropped'= HTTP frag merge failed dropped; 'http- malloc'= HTTP mem allocate; 'http-mfree'= HTTP mem free; 'http-spm-alloc- type0'= HTTP Conn SPM Type 0 allocate; 'http-spm-alloc-type1'= HTTP Conn SPM Type 1 allocate; 'http-spm-alloc-type2'= HTTP Conn SPM Type 2 allocate; 'http- spm-alloc-type3'= HTTP Conn SPM Type 3 allocate; 'http-spm-alloc-type4'= HTTP Conn SPM Type 4 allocate; 'http-spm-free-type0'= HTTP Conn SPM Type 0 free; 'http-spm-free-type1'= HTTP Conn SPM Type 1 free; 'http-spm-free-type2'= HTTP Conn SPM Type 2 free; 'http-spm-free-type3'= HTTP Conn SPM Type 3 free; 'http- spm-free-type4'= HTTP Conn SPM Type 4 free;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    tcp_port_overloading_freed (optional, any, None)
      TCP Port Overloading Freed


    udp_port_freed (optional, any, None)
      UDP Port Freed


    tcp_port_allocated (optional, any, None)
      TCP Port Allocated


    esp_resource_allocated (optional, any, None)
      ESP Resource Allocated


    udp_port_batch_allocated (optional, any, None)
      UDP Port Batch Allocated


    esp_session_created (optional, any, None)
      ESP Session Created


    icmpv6_resource_freed (optional, any, None)
      ICMPV6 Resource Freed


    udp_port_overloading_allocated (optional, any, None)
      UDP Port Overloading Allocated


    fixed_nat_interim_updated (optional, any, None)
      Fixed NAT Interim Updated


    icmp_session_created (optional, any, None)
      ICMP Session Created


    reduced_logs_by_destination (optional, any, None)
      Reduced Logs by Destination Protocol and Port


    gre_session_deleted (optional, any, None)
      GRE Session Deleted


    icmpv6_resource_allocated (optional, any, None)
      ICMPV6 Resource Allocated


    esp_session_deleted (optional, any, None)
      ESP Session Deleted


    udp_session_created (optional, any, None)
      UDP Session Created


    enhanced_user_log (optional, any, None)
      Enhanced User Log


    udp_port_overloading_freed (optional, any, None)
      UDP Port Overloading Freed


    fixed_nat_periodic_config_logs_sent (optional, any, None)
      Fixed NAT Disabled Configs Logged


    fixed_nat_user_ports (optional, any, None)
      Fixed NAT Inside User Port Mapping


    gre_session_created (optional, any, None)
      GRE Session Created


    tcp_session_created (optional, any, None)
      TCP Session Created


    tcp_port_batch_freed (optional, any, None)
      TCP Port Batch Freed


    udp_port_batch_freed (optional, any, None)
      UDP Port Batch Freed


    icmp_resource_freed (optional, any, None)
      ICMP Resource Freed


    udp_port_allocated (optional, any, None)
      UDP Port Allocated


    http_request_logged (optional, any, None)
      HTTP Request Logged


    fixed_nat_disable_config_logs_sent (optional, any, None)
      Fixed NAT Periodic Config Logs Sent


    fixed_nat_disable_config_logged (optional, any, None)
      Fixed NAT Periodic Configs Logged


    gre_resource_freed (optional, any, None)
      GRE Resource Freed


    esp_resource_freed (optional, any, None)
      ESP Resource Freed


    gre_resource_allocated (optional, any, None)
      GRE Resource Allocated


    icmp_resource_allocated (optional, any, None)
      ICMP Resource Allocated


    tcp_port_overloading_allocated (optional, any, None)
      TCP Port Overloading Allocated


    udp_port_batch_interim_updated (optional, any, None)
      UDP Port Batch Interim Updated


    tcp_session_deleted (optional, any, None)
      TCP Session Deleted


    tcp_port_batch_allocated (optional, any, None)
      TCP Port Batch Allocated


    conn_tcp_established (optional, any, None)
      TCP Connection Established


    fixed_nat_periodic_config_logged (optional, any, None)
      Fixed NAT Disabled Config Logs Sent


    conn_tcp_dropped (optional, any, None)
      TCP Connection Lost


    tcp_port_batch_interim_updated (optional, any, None)
      TCP Port Batch Interim Updated


    tcp_port_freed (optional, any, None)
      TCP Port Freed


    log_dropped (optional, any, None)
      Log Packets Dropped


    log_sent (optional, any, None)
      Log Packets Sent


    udp_session_deleted (optional, any, None)
      UDP Session Deleted


    icmpv6_session_deleted (optional, any, None)
      ICMPV6 Session Deleted


    icmp_session_deleted (optional, any, None)
      ICMP Session Deleted


    icmpv6_session_created (optional, any, None)
      ICMPV6 Session Created



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  source_address (False, any, None)
    Field source_address


    uuid (optional, any, None)
      uuid of the object



  ansible_password (True, any, None)
    Password for AXAPI authentication


  nat_resource_exhausted (False, any, None)
    Field nat_resource_exhausted


    uuid (optional, any, None)
      uuid of the object


    level (optional, any, None)
      'warning'= Log level Warning; 'critical'= Log level Critical (Default); 'notice'= Log level Notice;



  state (True, any, None)
    State of the object to be created.


  nat_quota_exceeded (False, any, None)
    Field nat_quota_exceeded


    uuid (optional, any, None)
      uuid of the object


    level (optional, any, None)
      'warning'= Log level Warning (Default); 'critical'= Log level Critical; 'notice'= Log level Notice;



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  tcp_svr_status (False, any, None)
    Field tcp_svr_status


    uuid (optional, any, None)
      uuid of the object










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

