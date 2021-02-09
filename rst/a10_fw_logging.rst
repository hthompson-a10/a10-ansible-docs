.. _a10_fw_logging_module:


a10_fw_logging -- Configures A10 fw.logging
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Bind a logging template to firewall






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'log_message_sent'= Log Packet Sent; 'log_type_reset'= Log Event Type Reset; 'log_type_deny'= Log Event Type Deny; 'log_type_session_closed'= Log Event Type Session Close; 'log_type_session_opened'= Log Event Type Session Open; 'rule_not_logged'= Firewall Rule Not Logged; 'log-dropped'= Log Packets Dropped; 'tcp-session-created'= TCP Session Created; 'tcp-session-deleted'= TCP Session Deleted; 'udp-session-created'= UDP Session Created; 'udp-session- deleted'= UDP Session Deleted; 'icmp-session-deleted'= ICMP Session Deleted; 'icmp-session-created'= ICMP Session Created; 'icmpv6-session-deleted'= ICMPV6 Session Deleted; 'icmpv6-session-created'= ICMPV6 Session Created; 'other- session-deleted'= Other Session Deleted; 'other-session-created'= Other Session Created; 'http-request-logged'= HTTP Request Logged; 'http-logging-invalid- format'= HTTP Logging Invalid Format Error; 'dcmsg_permit'= Dcmsg Permit; 'alg_override_permit'= Alg Override Permit; 'template_error'= Template Error; 'ipv4-frag-applied'= IPv4 Fragmentation Applied; 'ipv4-frag-failed'= IPv4 Fragmentation Failed; 'ipv6-frag-applied'= IPv6 Fragmentation Applied; 'ipv6-frag-failed'= IPv6 Fragmentation Failed; 'out-of-buffers'= Out of Buffers; 'add-msg-failed'= Add Message to Buffer Failed; 'tcp-logging-conn- established'= TCP Logging Conn Established; 'tcp-logging-conn-create-failed'= TCP Logging Conn Create Failed; 'tcp-logging-conn-dropped'= TCP Logging Conn Dropped; 'log-message-too-long'= Log message too long; 'http-out-of-order- dropped'= HTTP out-of-order dropped; 'http-alloc-failed'= HTTP Request Info Allocation Failed; 'sctp-session-created'= SCTP Session Created; 'sctp-session- deleted'= SCTP Session Deleted; 'log_type_sctp_inner_proto_filter'= Log Event Type SCTP Inner Proto Filter; 'log_type_gtp_message_filtering'= Log Event Type GTP Message Filtering; 'log_type_gtp_apn_filtering'= Log Event Type GTP Apn Filtering; 'tcp-logging-port-allocated'= TCP Logging Port Allocated; 'tcp- logging-port-freed'= TCP Logging Port Freed; 'tcp-logging-port-allocation- failed'= TCP Logging Port Allocation Failed; 'log_type_gtp_invalid_teid'= Log Event Type GTP Invalid TEID; 'log_gtp_type_reserved_ie_present'= Log Event Type GTP Reserved Information Element Present; 'log_type_gtp_mandatory_ie_missing'= Log Event Type GTP Mandatory Information Element Missing;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    log_type_reset (optional, any, None)
      Log Event Type Reset


    other_session_deleted (optional, any, None)
      Other Session Deleted


    icmpv6_session_deleted (optional, any, None)
      ICMPV6 Session Deleted


    log_type_gtp_mandatory_ie_missing (optional, any, None)
      Log Event Type GTP Mandatory Information Element Missing


    log_type_gtp_message_filtering (optional, any, None)
      Log Event Type GTP Message Filtering


    log_type_deny (optional, any, None)
      Log Event Type Deny


    sctp_session_deleted (optional, any, None)
      SCTP Session Deleted


    log_type_gtp_apn_filtering (optional, any, None)
      Log Event Type GTP Apn Filtering


    log_type_session_opened (optional, any, None)
      Log Event Type Session Open


    log_type_session_closed (optional, any, None)
      Log Event Type Session Close


    sctp_session_created (optional, any, None)
      SCTP Session Created


    icmp_session_created (optional, any, None)
      ICMP Session Created


    log_type_sctp_inner_proto_filter (optional, any, None)
      Log Event Type SCTP Inner Proto Filter


    other_session_created (optional, any, None)
      Other Session Created


    http_request_logged (optional, any, None)
      HTTP Request Logged


    tcp_session_deleted (optional, any, None)
      TCP Session Deleted


    udp_session_created (optional, any, None)
      UDP Session Created


    http_logging_invalid_format (optional, any, None)
      HTTP Logging Invalid Format Error


    log_type_gtp_invalid_teid (optional, any, None)
      Log Event Type GTP Invalid TEID


    log_message_sent (optional, any, None)
      Log Packet Sent


    log_dropped (optional, any, None)
      Log Packets Dropped


    udp_session_deleted (optional, any, None)
      UDP Session Deleted


    tcp_session_created (optional, any, None)
      TCP Session Created


    log_gtp_type_reserved_ie_present (optional, any, None)
      Log Event Type GTP Reserved Information Element Present


    rule_not_logged (optional, any, None)
      Firewall Rule Not Logged


    icmp_session_deleted (optional, any, None)
      ICMP Session Deleted


    icmpv6_session_created (optional, any, None)
      ICMPV6 Session Created



  name (False, any, None)
    Logging Template Name


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


  uuid (False, any, None)
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

