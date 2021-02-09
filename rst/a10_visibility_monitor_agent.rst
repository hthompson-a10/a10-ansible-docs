.. _a10_visibility_monitor_agent_module:


a10_visibility_monitor_agent -- Configures A10 visibility.monitor.agent
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure xflow agent






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'sflow-packets-received'= sFlow Packets Received; 'sflow-samples- received'= sFlow Samples Received; 'sflow-samples-bad-len'= sFlow Samples Bad Length; 'sflow-samples-non-std'= sFlow Samples Non-standard; 'sflow-samples- skipped'= sFlow Samples Skipped; 'sflow-sample-record-bad-len'= sFlow Sample Records Bad Length; 'sflow-samples-sent-for-detection'= sFlow Samples Processed For Detection; 'sflow-sample-record-invalid-layer2'= sFlow Sample Records Unknown Layer-2; 'sflow-sample-ipv6-hdr-parse-fail'= sFlow Sample IPv6 Record Header Parse Failures; 'sflow-disabled'= sFlow Packet Samples Processing Disabled; 'netflow-disabled'= Netflow Flow Samples Processing Disabled; 'netflow-v5-packets-received'= Netflow v5 Packets Received; 'netflow-v5-samples-received'= Netflow v5 Samples Received; 'netflow-v5-samples-sent-for-detection'= Netflow v5 Samples Processed For Detection; 'netflow-v5-sample-records-bad-len'= Netflow v5 Sample Records Bad Length; 'netflow-v5-max-records-exceed'= Netflow v5 Sample Max Records Error; 'netflow-v9-packets-received'= Netflow v9 Packets Received; 'netflow-v9-samples-received'= Netflow v9 Samples Received; 'netflow-v9-samples-sent-for-detection'= Netflow v9 Samples Processed For Detection; 'netflow-v9-sample-records-bad-len'= Netflow v9 Sample Records Bad Length; 'netflow-v9-max-records-exceed'= Netflow v9 Sample Max Records Error; 'netflow-v10-packets-received'= Netflow v10 Packets Received; 'netflow-v10-samples-received'= Netflow v10 Samples Received; 'netflow-v10-samples-sent-for-detection'= Netflow v10 Samples Procssed For Detection; 'netflow-v10-sample-records-bad-len'= Netflow v10 Sample Records Bad Length; 'netflow-v10-max-records-exceed'= Netflow v10 Sample Max records Error; 'netflow-tcp-sample-received'= Netflow TCP Samples Received; 'netflow-udp- sample-received'= Netflow UDP Samples received; 'netflow-icmp-sample-received'= Netflow ICMP Samples Received; 'netflow-other-sample-received'= Netflow OTHER Samples Received; 'netflow-record-copy-oom-error'= Netflow Data Record Copy Fail OOM; 'netflow-record-rse-invalid'= Netflow Data Record Reduced Size Invalid; 'netflow-sample-flow-dur-error'= Netflow Sample Flow Duration Error;



  agent_name (True, any, None)
    Specify name for the agent


  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    agent_name (optional, any, None)
      Specify name for the agent


    sflow_samples_skipped (optional, any, None)
      sFlow Samples Skipped


    netflow_udp_sample_received (optional, any, None)
      Netflow UDP Samples received


    netflow_record_rse_invalid (optional, any, None)
      Netflow Data Record Reduced Size Invalid


    netflow_sample_flow_dur_error (optional, any, None)
      Netflow Sample Flow Duration Error


    netflow_v9_max_records_exceed (optional, any, None)
      Netflow v9 Sample Max Records Error


    netflow_v9_samples_sent_for_detection (optional, any, None)
      Netflow v9 Samples Processed For Detection


    netflow_v5_packets_received (optional, any, None)
      Netflow v5 Packets Received


    netflow_v10_samples_sent_for_detection (optional, any, None)
      Netflow v10 Samples Procssed For Detection


    sflow_disabled (optional, any, None)
      sFlow Packet Samples Processing Disabled


    netflow_v10_sample_records_bad_len (optional, any, None)
      Netflow v10 Sample Records Bad Length


    sflow_sample_record_bad_len (optional, any, None)
      sFlow Sample Records Bad Length


    netflow_v5_samples_sent_for_detection (optional, any, None)
      Netflow v5 Samples Processed For Detection


    netflow_v10_max_records_exceed (optional, any, None)
      Netflow v10 Sample Max records Error


    netflow_tcp_sample_received (optional, any, None)
      Netflow TCP Samples Received


    netflow_v5_samples_received (optional, any, None)
      Netflow v5 Samples Received


    netflow_v5_sample_records_bad_len (optional, any, None)
      Netflow v5 Sample Records Bad Length


    sflow_samples_bad_len (optional, any, None)
      sFlow Samples Bad Length


    netflow_v9_sample_records_bad_len (optional, any, None)
      Netflow v9 Sample Records Bad Length


    netflow_record_copy_oom_error (optional, any, None)
      Netflow Data Record Copy Fail OOM


    netflow_disabled (optional, any, None)
      Netflow Flow Samples Processing Disabled


    sflow_samples_non_std (optional, any, None)
      sFlow Samples Non-standard


    netflow_v9_packets_received (optional, any, None)
      Netflow v9 Packets Received


    netflow_v9_samples_received (optional, any, None)
      Netflow v9 Samples Received


    sflow_sample_ipv6_hdr_parse_fail (optional, any, None)
      sFlow Sample IPv6 Record Header Parse Failures


    sflow_packets_received (optional, any, None)
      sFlow Packets Received


    netflow_icmp_sample_received (optional, any, None)
      Netflow ICMP Samples Received


    sflow_samples_sent_for_detection (optional, any, None)
      sFlow Samples Processed For Detection


    netflow_v10_samples_received (optional, any, None)
      Netflow v10 Samples Received


    sflow_samples_received (optional, any, None)
      sFlow Samples Received


    sflow_sample_record_invalid_layer2 (optional, any, None)
      sFlow Sample Records Unknown Layer-2


    netflow_v5_max_records_exceed (optional, any, None)
      Netflow v5 Sample Max Records Error


    netflow_v10_packets_received (optional, any, None)
      Netflow v10 Packets Received


    netflow_other_sample_received (optional, any, None)
      Netflow OTHER Samples Received



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  agent_v6_addr (False, any, None)
    Configure agent's IPv6 address


  state (True, any, None)
    State of the object to be created.


  agent_v4_addr (False, any, None)
    Configure agent's IPv4 address


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

