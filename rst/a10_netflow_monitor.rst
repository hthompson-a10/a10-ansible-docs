.. _a10_netflow_monitor_module:


a10_netflow_monitor -- Configures A10 netflow.monitor
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure NetFlow Monitor






Parameters
----------

  disable_log_by_destination (False, any, None)
    Field disable_log_by_destination


    ip_list (optional, any, None)
      Field ip_list


    ip6_list (optional, any, None)
      Field ip6_list


    others (optional, any, None)
      Disable logging for other L4 protocols


    tcp_list (optional, any, None)
      Field tcp_list


    icmp (optional, any, None)
      Disable logging for icmp traffic


    udp_list (optional, any, None)
      Field udp_list


    uuid (optional, any, None)
      uuid of the object



  protocol (False, any, None)
    'v9'= Netflow version 9; 'v10'= Netflow version 10 (IPFIX);


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  sample (False, any, None)
    Field sample


    ethernet_list (optional, any, None)
      Field ethernet_list


    nat_pool_list (optional, any, None)
      Field nat_pool_list


    ve_list (optional, any, None)
      Field ve_list



  disable (False, any, None)
    Disable this netflow monitor


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  name (True, any, None)
    Name of netflow monitor


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'packets-sent'= Sent Packets Count; 'bytes-sent'= Sent Bytes Count; 'nat44-records-sent'= NAT44 Flow Records Sent; 'nat44-records-sent-failure'= NAT44 Flow Records Failed; 'nat64-records-sent'= NAT64 Flow Records Sent; 'nat64-records-sent-failure'= NAT64 Flow Records Failed; 'dslite-records-sent'= Dslite Flow Records Sent; 'dslite-records-sent-failure'= Dslite Flow Records Failed; 'session-event-nat44-records-sent'= Nat44 Session Event Records Sent; 'session-event-nat44-records-sent-failure'= Nat44 Session Event Records Failed; 'session-event-nat64-records-sent'= Nat64 Session Event Records Sent; 'session- event-nat64-records-sent-failure'= Nat64 Session Event Records Falied; 'session-event-dslite-records-sent'= Dslite Session Event Records Sent; 'session-event-dslite-records-sent-failure'= Dslite Session Event Records Failed; 'session-event-fw4-records-sent'= FW4 Session Event Records Sent; 'session-event-fw4-records-sent-failure'= FW4 Session Event Records Failed; 'session-event-fw6-records-sent'= FW6 Session Event Records Sent; 'session- event-fw6-records-sent-failure'= FW6 Session Event Records Failed; 'port- mapping-nat44-records-sent'= Port Mapping Nat44 Event Records Sent; 'port- mapping-nat44-records-sent-failure'= Port Mapping Nat44 Event Records Failed; 'port-mapping-nat64-records-sent'= Port Mapping Nat64 Event Records Sent; 'port-mapping-nat64-records-sent-failure'= Port Mapping Nat64 Event Records Failed; 'port-mapping-dslite-records-sent'= Port Mapping Dslite Event Records Sent; 'port-mapping-dslite-records-sent-failure'= Port Mapping Dslite Event Records failed; 'netflow-v5-records-sent'= Netflow v5 Records Sent; 'netflow-v5-records-sent-failure'= Netflow v5 Records Failed; 'netflow-v5-ext- records-sent'= Netflow v5 Ext Records Sent; 'netflow-v5-ext-records-sent- failure'= Netflow v5 Ext Records Failed; 'port-batching-nat44-records-sent'= Port Batching Nat44 Records Sent; 'port-batching-nat44-records-sent-failure'= Port Batching Nat44 Records Failed; 'port-batching-nat64-records-sent'= Port Batching Nat64 Records Sent; 'port-batching-nat64-records-sent-failure'= Port Batching Nat64 Records Failed; 'port-batching-dslite-records-sent'= Port Batching Dslite Records Sent; 'port-batching-dslite-records-sent-failure'= Port Batching Dslite Records Failed; 'port-batching-v2-nat44-records-sent'= Port Batching V2 Nat44 Records Sent; 'port-batching-v2-nat44-records-sent-failure'= Port Batching V2 Nat44 Records Failed; 'port-batching-v2-nat64-records-sent'= Port Batching V2 Nat64 Records Sent; 'port-batching-v2-nat64-records-sent- failure'= Port Batching V2 Nat64 Records Failed; 'port-batching-v2-dslite- records-sent'= Port Batching V2 Dslite Records Sent; 'port-batching-v2-dslite- records-sent-failure'= Port Batching V2 Dslite Records Falied; 'custom-session- event-nat44-creation-records-sent'= Custom Nat44 Session Creation Records Sent; 'custom-session-event-nat44-creation-records-sent-failure'= Custom Nat44 Session Creation Records Failed; 'custom-session-event-nat64-creation-records- sent'= Custom Nat64 Session Creation Records Sent; 'custom-session-event- nat64-creation-records-sent-failure'= Custom Nat64 Session Creation Records Failed; 'custom-session-event-dslite-creation-records-sent'= Custom Dslite Session Creation Records Sent; 'custom-session-event-dslite-creation-records- sent-failure'= Custom Dslite Session Creation Records Failed; 'custom-session- event-nat44-deletion-records-sent'= Custom Nat44 Session Deletion Records Sent; 'custom-session-event-nat44-deletion-records-sent-failure'= Custom Nat44 Session Deletion Records Failed; 'custom-session-event-nat64-deletion-records- sent'= Custom Nat64 Session Deletion Records Sent; 'custom-session-event- nat64-deletion-records-sent-failure'= Custom Nat64 Session Deletion Records Failed; 'custom-session-event-dslite-deletion-records-sent'= Custom Dslite Session Deletion Records Sent; 'custom-session-event-dslite-deletion-records- sent-failure'= Custom Dslite Session Deletion Records Failed; 'custom-session- event-fw4-creation-records-sent'= Custom FW4 Session Creation Records Sent; 'custom-session-event-fw4-creation-records-sent-failure'= Custom FW4 Session Creation Records Failed; 'custom-session-event-fw6-creation-records-sent'= Custom FW6 Session Creation Records Sent; 'custom-session-event-fw6-creation- records-sent-failure'= Custom FW6 Session Creation Records Failed; 'custom- session-event-fw4-deletion-records-sent'= Custom FW4 Session Deletion Records Sent; 'custom-session-event-fw4-deletion-records-sent-failure'= Custom FW4 Session Deletion Records Failed; 'custom-session-event-fw6-deletion-records- sent'= Custom FW6 Session Deletion Records Sent; 'custom-session-event- fw6-deletion-records-sent-failure'= Custom FW6 Session Deletion Records Failed; 'custom-deny-reset-event-fw4-records-sent'= Custom FW4 Deny/Reset Event Records Sent; 'custom-deny-reset-event-fw4-records-sent-failure'= Custom FW4 Deny/Reset Event Records Failed; 'custom-deny-reset-event-fw6-records-sent'= Custom FW6 Deny/Reset Event Records Sent; 'custom-deny-reset-event-fw6-records-sent- failure'= Custom FW6 Deny/Reset Event Records Failed; 'custom-port-mapping- nat44-creation-records-sent'= Custom Nat44 Port Map Creation Records Sent; 'custom-port-mapping-nat44-creation-records-sent-failure'= Custom Nat44 Port Map Creation Records Failed; 'custom-port-mapping-nat64-creation-records-sent'= Custom Nat64 Port Map Creation Records Sent; 'custom-port-mapping- nat64-creation-records-sent-failure'= Custom Nat64 Port Map Creation Records Failed; 'custom-port-mapping-dslite-creation-records-sent'= Custom Dslite Port Map Creation Records Sent; 'custom-port-mapping-dslite-creation-records-sent- failure'= Custom Dslite Port Map Creation Records Failed; 'custom-port-mapping- nat44-deletion-records-sent'= Custom Nat44 Port Map Deletion Records Sent; 'custom-port-mapping-nat44-deletion-records-sent-failure'= Custom Nat44 Port Map Deletion Records Failed; 'custom-port-mapping-nat64-deletion-records-sent'= Custom Nat64 Port Map Deletion Records Sent; 'custom-port-mapping- nat64-deletion-records-sent-failure'= Custom Nat64 Port Map Deletion Records Failed; 'custom-port-mapping-dslite-deletion-records-sent'= Custom Dslite Port Map Deletion Records Sent; 'custom-port-mapping-dslite-deletion-records-sent- failure'= Custom Dslite Port Map Deletion Records Failed; 'custom-port- batching-nat44-creation-records-sent'= Custom Nat44 Port Batch Creation Records Sent; 'custom-port-batching-nat44-creation-records-sent-failure'= Custom Nat44 Port Batch Creation Records Failed; 'custom-port-batching-nat64-creation- records-sent'= Custom Nat64 Port Batch Creation Records Sent; 'custom-port- batching-nat64-creation-records-sent-failure'= Custom Nat64 Port Batch Creation Records Failed; 'custom-port-batching-dslite-creation-records-sent'= Custom Dslite Port Batch Creation Records Sent; 'custom-port-batching-dslite-creation- records-sent-failure'= Custom Dslite Port Batch Creation Records Failed; 'custom-port-batching-nat44-deletion-records-sent'= Custom Nat44 Port Batch Deletion Records Sent; 'custom-port-batching-nat44-deletion-records-sent- failure'= Custom Nat44 Port Batch Deletion Records Failed; 'custom-port- batching-nat64-deletion-records-sent'= Custom Nat64 Port Batch Deletion Records Sent; 'custom-port-batching-nat64-deletion-records-sent-failure'= Custom Nat64 Port Batch Deletion Records Failed; 'custom-port-batching-dslite-deletion- records-sent'= Custom Dslite Port Batch Deletion Records Sent; 'custom-port- batching-dslite-deletion-records-sent-failure'= Custom Dslite Port Batch Deletion Records Failed; 'custom-port-batching-v2-nat44-creation-records-sent'= Custom Nat44 Port Batch V2 Creation Records Sent;


    counters2 (optional, any, None)
      'custom-port-batching-v2-nat44-creation-records-sent-failure'= Custom Nat44 Port Batch V2 Creation Records Failed; 'custom-port-batching-v2-nat64-creation- records-sent'= Custom Nat64 Port Batch V2 Creation Records Sent; 'custom-port- batching-v2-nat64-creation-records-sent-failure'= Custom Nat64 Port Batch V2 Creation Records Failed; 'custom-port-batching-v2-dslite-creation-records- sent'= Custom Dslite Port Batch V2 Creation Records Sent; 'custom-port- batching-v2-dslite-creation-records-sent-failure'= Custom Dslite Port Batch V2 Creation Records Failed; 'custom-port-batching-v2-nat44-deletion-records-sent'= Custom Nat44 Port Batch V2 Deletion Records Sent; 'custom-port- batching-v2-nat44-deletion-records-sent-failure'= Custom Nat44 Port Batch V2 Deletion Records Failed; 'custom-port-batching-v2-nat64-deletion-records-sent'= Custom Nat64 Port Batch V2 Deletion Records Sent; 'custom-port- batching-v2-nat64-deletion-records-sent-failure'= Custom Nat64 Port Batch V2 Deletion Records Failed; 'custom-port-batching-v2-dslite-deletion-records- sent'= Custom Dslite Port Batch V2 Deletion Records Sent; 'custom-port- batching-v2-dslite-deletion-records-sent-failure'= Custom Dslite Port Batch V2 Deletion Records Failed; 'reduced-logs-by-destination'= Reduced Logs by Destination Protocol and Port;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    custom_session_event_dslite_deletion_records_sent_failure (optional, any, None)
      Custom Dslite Session Deletion Records Failed


    custom_session_event_fw4_deletion_records_sent (optional, any, None)
      Custom FW4 Session Deletion Records Sent


    session_event_nat64_records_sent (optional, any, None)
      Nat64 Session Event Records Sent


    port_mapping_nat44_records_sent (optional, any, None)
      Port Mapping Nat44 Event Records Sent


    nat44_records_sent_failure (optional, any, None)
      NAT44 Flow Records Failed


    custom_port_mapping_nat44_deletion_records_sent (optional, any, None)
      Custom Nat44 Port Map Deletion Records Sent


    reduced_logs_by_destination (optional, any, None)
      Reduced Logs by Destination Protocol and Port


    custom_port_mapping_dslite_deletion_records_sent (optional, any, None)
      Custom Dslite Port Map Deletion Records Sent


    custom_session_event_fw6_creation_records_sent_failure (optional, any, None)
      Custom FW6 Session Creation Records Failed


    custom_port_batching_nat64_creation_records_sent_failure (optional, any, None)
      Custom Nat64 Port Batch Creation Records Failed


    port_mapping_dslite_records_sent (optional, any, None)
      Port Mapping Dslite Event Records Sent


    custom_session_event_fw6_creation_records_sent (optional, any, None)
      Custom FW6 Session Creation Records Sent


    custom_deny_reset_event_fw4_records_sent_failure (optional, any, None)
      Custom FW4 Deny/Reset Event Records Failed


    custom_port_batching_v2_nat64_creation_records_sent (optional, any, None)
      Custom Nat64 Port Batch V2 Creation Records Sent


    port_batching_v2_nat44_records_sent (optional, any, None)
      Port Batching V2 Nat44 Records Sent


    custom_port_mapping_dslite_creation_records_sent_failure (optional, any, None)
      Custom Dslite Port Map Creation Records Failed


    custom_session_event_nat44_deletion_records_sent (optional, any, None)
      Custom Nat44 Session Deletion Records Sent


    custom_port_batching_nat44_creation_records_sent (optional, any, None)
      Custom Nat44 Port Batch Creation Records Sent


    session_event_dslite_records_sent_failure (optional, any, None)
      Dslite Session Event Records Failed


    port_batching_v2_nat44_records_sent_failure (optional, any, None)
      Port Batching V2 Nat44 Records Failed


    custom_port_batching_v2_nat44_deletion_records_sent_failure (optional, any, None)
      Custom Nat44 Port Batch V2 Deletion Records Failed


    session_event_fw6_records_sent_failure (optional, any, None)
      FW6 Session Event Records Failed


    port_batching_nat64_records_sent_failure (optional, any, None)
      Port Batching Nat64 Records Failed


    nat64_records_sent (optional, any, None)
      NAT64 Flow Records Sent


    custom_session_event_dslite_creation_records_sent (optional, any, None)
      Custom Dslite Session Creation Records Sent


    port_mapping_nat64_records_sent (optional, any, None)
      Port Mapping Nat64 Event Records Sent


    custom_port_batching_nat64_deletion_records_sent (optional, any, None)
      Custom Nat64 Port Batch Deletion Records Sent


    custom_port_batching_dslite_deletion_records_sent (optional, any, None)
      Custom Dslite Port Batch Deletion Records Sent


    custom_deny_reset_event_fw6_records_sent_failure (optional, any, None)
      Custom FW6 Deny/Reset Event Records Failed


    port_batching_nat44_records_sent (optional, any, None)
      Port Batching Nat44 Records Sent


    custom_port_mapping_nat64_creation_records_sent (optional, any, None)
      Custom Nat64 Port Map Creation Records Sent


    custom_session_event_nat44_creation_records_sent_failure (optional, any, None)
      Custom Nat44 Session Creation Records Failed


    session_event_fw4_records_sent (optional, any, None)
      FW4 Session Event Records Sent


    custom_port_mapping_nat64_deletion_records_sent (optional, any, None)
      Custom Nat64 Port Map Deletion Records Sent


    session_event_nat64_records_sent_failure (optional, any, None)
      Nat64 Session Event Records Falied


    port_mapping_nat44_records_sent_failure (optional, any, None)
      Port Mapping Nat44 Event Records Failed


    packets_sent (optional, any, None)
      Sent Packets Count


    name (optional, any, None)
      Name of netflow monitor


    custom_port_batching_v2_nat64_creation_records_sent_failure (optional, any, None)
      Custom Nat64 Port Batch V2 Creation Records Failed


    port_batching_nat64_records_sent (optional, any, None)
      Port Batching Nat64 Records Sent


    custom_session_event_nat64_creation_records_sent (optional, any, None)
      Custom Nat64 Session Creation Records Sent


    nat64_records_sent_failure (optional, any, None)
      NAT64 Flow Records Failed


    port_batching_dslite_records_sent_failure (optional, any, None)
      Port Batching Dslite Records Failed


    custom_port_mapping_nat64_deletion_records_sent_failure (optional, any, None)
      Custom Nat64 Port Map Deletion Records Failed


    custom_session_event_nat44_deletion_records_sent_failure (optional, any, None)
      Custom Nat44 Session Deletion Records Failed


    port_mapping_nat64_records_sent_failure (optional, any, None)
      Port Mapping Nat64 Event Records Failed


    custom_session_event_fw4_deletion_records_sent_failure (optional, any, None)
      Custom FW4 Session Deletion Records Failed


    custom_port_batching_nat44_creation_records_sent_failure (optional, any, None)
      Custom Nat44 Port Batch Creation Records Failed


    custom_port_mapping_nat44_creation_records_sent (optional, any, None)
      Custom Nat44 Port Map Creation Records Sent


    custom_port_mapping_dslite_creation_records_sent (optional, any, None)
      Custom Dslite Port Map Creation Records Sent


    custom_port_batching_dslite_deletion_records_sent_failure (optional, any, None)
      Custom Dslite Port Batch Deletion Records Failed


    custom_session_event_nat64_creation_records_sent_failure (optional, any, None)
      Custom Nat64 Session Creation Records Failed


    bytes_sent (optional, any, None)
      Sent Bytes Count


    custom_port_mapping_nat64_creation_records_sent_failure (optional, any, None)
      Custom Nat64 Port Map Creation Records Failed


    custom_port_batching_v2_dslite_deletion_records_sent_failure (optional, any, None)
      Custom Dslite Port Batch V2 Deletion Records Failed


    dslite_records_sent_failure (optional, any, None)
      Dslite Flow Records Failed


    custom_port_batching_v2_dslite_creation_records_sent (optional, any, None)
      Custom Dslite Port Batch V2 Creation Records Sent


    custom_port_mapping_nat44_deletion_records_sent_failure (optional, any, None)
      Custom Nat44 Port Map Deletion Records Failed


    netflow_v5_ext_records_sent (optional, any, None)
      Netflow v5 Ext Records Sent


    session_event_fw4_records_sent_failure (optional, any, None)
      FW4 Session Event Records Failed


    netflow_v5_records_sent_failure (optional, any, None)
      Netflow v5 Records Failed


    dslite_records_sent (optional, any, None)
      Dslite Flow Records Sent


    session_event_nat44_records_sent_failure (optional, any, None)
      Nat44 Session Event Records Failed


    custom_session_event_dslite_creation_records_sent_failure (optional, any, None)
      Custom Dslite Session Creation Records Failed


    session_event_nat44_records_sent (optional, any, None)
      Nat44 Session Event Records Sent


    custom_session_event_fw4_creation_records_sent (optional, any, None)
      Custom FW4 Session Creation Records Sent


    custom_port_batching_dslite_creation_records_sent (optional, any, None)
      Custom Dslite Port Batch Creation Records Sent


    custom_port_batching_v2_dslite_creation_records_sent_failure (optional, any, None)
      Custom Dslite Port Batch V2 Creation Records Failed


    custom_port_batching_v2_nat44_creation_records_sent_failure (optional, any, None)
      Custom Nat44 Port Batch V2 Creation Records Failed


    netflow_v5_records_sent (optional, any, None)
      Netflow v5 Records Sent


    custom_deny_reset_event_fw6_records_sent (optional, any, None)
      Custom FW6 Deny/Reset Event Records Sent


    custom_port_batching_nat64_deletion_records_sent_failure (optional, any, None)
      Custom Nat64 Port Batch Deletion Records Failed


    nat44_records_sent (optional, any, None)
      NAT44 Flow Records Sent


    custom_session_event_fw4_creation_records_sent_failure (optional, any, None)
      Custom FW4 Session Creation Records Failed


    custom_session_event_fw6_deletion_records_sent_failure (optional, any, None)
      Custom FW6 Session Deletion Records Failed


    custom_port_batching_v2_dslite_deletion_records_sent (optional, any, None)
      Custom Dslite Port Batch V2 Deletion Records Sent


    custom_session_event_fw6_deletion_records_sent (optional, any, None)
      Custom FW6 Session Deletion Records Sent


    custom_port_batching_v2_nat44_deletion_records_sent (optional, any, None)
      Custom Nat44 Port Batch V2 Deletion Records Sent


    session_event_fw6_records_sent (optional, any, None)
      FW6 Session Event Records Sent


    port_batching_nat44_records_sent_failure (optional, any, None)
      Port Batching Nat44 Records Failed


    custom_session_event_dslite_deletion_records_sent (optional, any, None)
      Custom Dslite Session Deletion Records Sent


    custom_deny_reset_event_fw4_records_sent (optional, any, None)
      Custom FW4 Deny/Reset Event Records Sent


    custom_port_batching_nat44_deletion_records_sent_failure (optional, any, None)
      Custom Nat44 Port Batch Deletion Records Failed


    custom_port_batching_nat44_deletion_records_sent (optional, any, None)
      Custom Nat44 Port Batch Deletion Records Sent


    port_mapping_dslite_records_sent_failure (optional, any, None)
      Port Mapping Dslite Event Records failed


    custom_port_batching_nat64_creation_records_sent (optional, any, None)
      Custom Nat64 Port Batch Creation Records Sent


    custom_session_event_nat64_deletion_records_sent_failure (optional, any, None)
      Custom Nat64 Session Deletion Records Failed


    port_batching_v2_dslite_records_sent_failure (optional, any, None)
      Port Batching V2 Dslite Records Falied


    custom_port_mapping_nat44_creation_records_sent_failure (optional, any, None)
      Custom Nat44 Port Map Creation Records Failed


    port_batching_v2_dslite_records_sent (optional, any, None)
      Port Batching V2 Dslite Records Sent


    custom_session_event_nat64_deletion_records_sent (optional, any, None)
      Custom Nat64 Session Deletion Records Sent


    session_event_dslite_records_sent (optional, any, None)
      Dslite Session Event Records Sent


    netflow_v5_ext_records_sent_failure (optional, any, None)
      Netflow v5 Ext Records Failed


    port_batching_v2_nat64_records_sent_failure (optional, any, None)
      Port Batching V2 Nat64 Records Failed


    custom_port_batching_v2_nat44_creation_records_sent (optional, any, None)
      Custom Nat44 Port Batch V2 Creation Records Sent


    port_batching_dslite_records_sent (optional, any, None)
      Port Batching Dslite Records Sent


    custom_port_batching_v2_nat64_deletion_records_sent (optional, any, None)
      Custom Nat64 Port Batch V2 Deletion Records Sent


    port_batching_v2_nat64_records_sent (optional, any, None)
      Port Batching V2 Nat64 Records Sent


    custom_port_batching_v2_nat64_deletion_records_sent_failure (optional, any, None)
      Custom Nat64 Port Batch V2 Deletion Records Failed


    custom_session_event_nat44_creation_records_sent (optional, any, None)
      Custom Nat44 Session Creation Records Sent


    custom_port_mapping_dslite_deletion_records_sent_failure (optional, any, None)
      Custom Dslite Port Map Deletion Records Failed


    custom_port_batching_dslite_creation_records_sent_failure (optional, any, None)
      Custom Dslite Port Batch Creation Records Failed



  uuid (False, any, None)
    uuid of the object


  user_tag (False, any, None)
    Customized tag


  destination (False, any, None)
    Field destination


    service_group (optional, any, None)
      Service-group for load balancing between multiple collector servers


    ipv6_cfg (optional, any, None)
      Field ipv6_cfg


    uuid (optional, any, None)
      uuid of the object


    ip_cfg (optional, any, None)
      Field ip_cfg



  source_ip_use_mgmt (False, any, None)
    Use management interface's IP address for source ip of netflow packets


  custom_record (False, any, None)
    Field custom_record


    custom_cfg (optional, any, None)
      Field custom_cfg


    uuid (optional, any, None)
      uuid of the object



  record (False, any, None)
    Field record


    port_mapping_dslite (optional, any, None)
      'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


    nat44 (optional, any, None)
      NAT44 Flow Record Template


    nat64 (optional, any, None)
      NAT64 Flow Record Template


    port_batch_v2_nat64 (optional, any, None)
      'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


    port_batch_nat44 (optional, any, None)
      'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


    port_batch_v2_dslite (optional, any, None)
      'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


    sesn_event_nat64 (optional, any, None)
      'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


    port_batch_dslite (optional, any, None)
      'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


    port_batch_v2_nat44 (optional, any, None)
      'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


    uuid (optional, any, None)
      uuid of the object


    port_batch_nat64 (optional, any, None)
      'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


    sesn_event_fw6 (optional, any, None)
      'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


    netflow_v5_ext (optional, any, None)
      Extended NetFlow V5 Flow Record Template, supports ipv6


    sesn_event_fw4 (optional, any, None)
      'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


    sesn_event_dslite (optional, any, None)
      'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


    dslite (optional, any, None)
      DS-Lite Flow Record Template


    sesn_event_nat44 (optional, any, None)
      'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


    port_mapping_nat44 (optional, any, None)
      'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


    netflow_v5 (optional, any, None)
      NetFlow V5 Flow Record Template


    port_mapping_nat64 (optional, any, None)
      'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;



  state (True, any, None)
    State of the object to be created.


  flow_timeout (False, any, None)
    Configure timeout value to export flow records periodically for long-live session ( Number of minutes= default is 10, 0 means only send flow record when session is deleted)


  source_address (False, any, None)
    Field source_address


    ip (optional, any, None)
      Specify source IP address


    uuid (optional, any, None)
      uuid of the object


    ipv6 (optional, any, None)
      Specify source IPv6 address



  resend_template (False, any, None)
    Field resend_template


    records (optional, any, None)
      To resend template once for each number of records (Number of records= default is 1000, 0 means disable template resend based on record-count)


    uuid (optional, any, None)
      uuid of the object


    timeout (optional, any, None)
      To set time interval to resend template (number of seconds= default is 1800, 0 means disable template resend based on timeout)










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

