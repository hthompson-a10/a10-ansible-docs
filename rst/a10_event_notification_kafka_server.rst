.. _a10_event_notification_kafka_server_module:


a10_event_notification_kafka_server -- Configures A10 event.notification.kafka.server
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set remote kafka server ip address






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'pr-acos-harmony-topic'= PR topic counter from acos to harmony; 'avro-device-status-topic'= AVRO device status from acos to harmony; 'avro- partition-metrics-topic'= AVRO partition metrics from acos to harmony; 'avro- generic-sent'= Telemetry exported via avro; 'pr-acos-harmony-topic-enqueue- err'= PR topic to harmony enqueue error; 'pr-acos-harmony-topic-dequeue-err'= PR topic to harmony  dequeue error; 'avro-generic-failed-encoding'= Telemetry exported via avro failed encoding; 'avro-generic-failed-sending'= Telemetry exported via avro failed sending; 'avro-device-status-topic-enqueue-err'= AVRO device status enqueue error; 'avro-device-status-topic-dequeue-err'= AVRO device status dequeue error; 'avro-partition-metrics-topic-enqueue-err'= Part metrics dropped,enq error on acos queues; 'avro-partition-metrics-topic- dequeue-err'= Part metrics dropped,enq error analytics queues; 'kafka-unknown- topic-dequeue-err'= Unknown type dropped,enq error analytics queues; 'kafka- broker-down'= Telemetry drop because kafka broker is down; 'kafka-queue-full- err'= Telemetry drop because kafka Queue is full; 'pr-throttle-drop'= L7 PR dropped,log throttling; 'pr-not-allowed-drop'= PR drop because not allowed to log; 'pr-be-ttfb-anomaly'= PR back-end ttfb is negative; 'pr-be-ttlb-anomaly'= PR back-end ttlb is negative; 'pr-in-latency-threshold-exceed'= PR in latency threshold exceeded; 'pr-out-latency-threshold-exceed'= PR out latency threshold exceeded; 'pr-out-latency-anomaly'= PR out latency negative; 'pr-in-latency- anomaly'= PR in latency negative; 'kafka-topic-error'= Telemetry dropped because kafka topic not created; 'pc-encoding-failed'= Telemetry exported via avro failed encoding; 'pc-acos-harmony-topic'= PC topic counter from acos to harmony; 'pc-acos-harmony-topic-dequeue-err'= PC topic to harmony  dequeue error; 'cgn-pc-acos-harmony-topic'= CGN PC topic counter from acos to harmony; 'cgn-pc-acos-harmony-topic-dequeue-err'= CGN PC topic to harmony dequeue error; 'cgn-pe-acos-harmony-topic'= CGN PE topic counter from acos to harmony; 'cgn- pe-acos-harmony-topic-dequeue-err'= CGN PE topic to harmony dequeue error; 'fw- pc-acos-harmony-topic'= FW PC topic counter from acos to harmony; 'fw-pc-acos- harmony-topic-dequeue-err'= FW PC topic to harmony dequeue error; 'fw-deny-pc- acos-harmony-topic'= FW DENY PC topic counter from acos to harmony; 'fw-deny- pc-acos-harmony-topic-dequeue-err'= FW DENY PC logs dropped,enq error analytics queues; 'fw-rst-pc-acos-harmony-topic'= FW RST PC topic counter from acos to harmony; 'fw-rst-pc-acos-harmony-topic-dequeue-err'= FW RST PC topic to harmony dequeue error; 'cgn-summary-error-acos-harmony-topic'= CGN Summary PE topic counter from acos to harmony; 'cgn-summary-error-acos-harmony-topic-dequeue- err'= CGN Summary PE topic to harmony dequeue error; 'rule-set-application- metrics-topic'= AppFW metrics from acos to harmony; 'rule-set-application- metrics-topic-dequeue-err'= AppFW metrics dequeue error; 'slb-ssl-stats- metrics-topic'= SSL stats metrics from acos to harmony; 'slb-ssl-stats-metrics- topic-dequeue-err'= SSL stats metrics dequeue error; 'slb-client-ssl-counters- metrics-topic'= Client SSL counters metrics from acos to harmony; 'slb-client- ssl-counters-metrics-topic-dequeue-err'= Cilent SSL metrics dropped,enq error analytics qs; 'slb-server-ssl-counters-metrics-topic'= Server SSL counters metrics from acos to harmony; 'slb-server-ssl-counters-metrics-topic-dequeue- err'= Server SSL metrics dropped,enq error analytics qs; 'pc-throttle-drop'= PC drop due to throttling; 'metrics-dropped-pt-missing'= Partition-Tenant mapping not saved on HC; 'ssli-pc-acos-harmony-topic'= SSLi PC topic counter from acos to harmony; 'ssli-pc-acos-harmony-topic-dequeue-err'= SSLi PC topic to harmony dequeue error; 'ssli-pe-acos-harmony-topic'= SSLi PE topic counter from acos to harmony; 'ssli-pe-acos-harmony-topic-dequeue-err'= SSLi PE topic to harmony dequeue error; 'analytics-bus-restart'= Analytics bus restart count;



  oper (False, any, None)
    Field oper


    kafka_broker_state (optional, any, None)
      Field kafka_broker_state



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    ssli_pe_acos_harmony_topic (optional, any, None)
      SSLi PE topic counter from acos to harmony


    pc_acos_harmony_topic (optional, any, None)
      PC topic counter from acos to harmony


    pr_in_latency_threshold_exceed (optional, any, None)
      PR in latency threshold exceeded


    pc_throttle_drop (optional, any, None)
      PC drop due to throttling


    ssli_pe_acos_harmony_topic_dequeue_err (optional, any, None)
      SSLi PE topic to harmony dequeue error


    pr_throttle_drop (optional, any, None)
      L7 PR dropped,log throttling


    pc_encoding_failed (optional, any, None)
      Telemetry exported via avro failed encoding


    avro_device_status_topic (optional, any, None)
      AVRO device status from acos to harmony


    slb_ssl_stats_metrics_topic (optional, any, None)
      SSL stats metrics from acos to harmony


    pr_acos_harmony_topic_enqueue_err (optional, any, None)
      PR topic to harmony enqueue error


    ssli_pc_acos_harmony_topic (optional, any, None)
      SSLi PC topic counter from acos to harmony


    fw_pc_acos_harmony_topic_dequeue_err (optional, any, None)
      FW PC topic to harmony dequeue error


    pr_not_allowed_drop (optional, any, None)
      PR drop because not allowed to log


    kafka_unknown_topic_dequeue_err (optional, any, None)
      Unknown type dropped,enq error analytics queues


    avro_generic_failed_encoding (optional, any, None)
      Telemetry exported via avro failed encoding


    rule_set_application_metrics_topic_dequeue_err (optional, any, None)
      AppFW metrics dequeue error


    avro_device_status_topic_dequeue_err (optional, any, None)
      AVRO device status dequeue error


    cgn_pc_acos_harmony_topic_dequeue_err (optional, any, None)
      CGN PC topic to harmony dequeue error


    pr_acos_harmony_topic (optional, any, None)
      PR topic counter from acos to harmony


    kafka_queue_full_err (optional, any, None)
      Telemetry drop because kafka Queue is full


    avro_generic_sent (optional, any, None)
      Telemetry exported via avro


    pr_acos_harmony_topic_dequeue_err (optional, any, None)
      PR topic to harmony  dequeue error


    metrics_dropped_pt_missing (optional, any, None)
      Partition-Tenant mapping not saved on HC


    slb_client_ssl_counters_metrics_topic (optional, any, None)
      Client SSL counters metrics from acos to harmony


    fw_pc_acos_harmony_topic (optional, any, None)
      FW PC topic counter from acos to harmony


    cgn_summary_error_acos_harmony_topic (optional, any, None)
      CGN Summary PE topic counter from acos to harmony


    slb_server_ssl_counters_metrics_topic_dequeue_err (optional, any, None)
      Server SSL metrics dropped,enq error analytics qs


    pr_out_latency_threshold_exceed (optional, any, None)
      PR out latency threshold exceeded


    slb_server_ssl_counters_metrics_topic (optional, any, None)
      Server SSL counters metrics from acos to harmony


    slb_client_ssl_counters_metrics_topic_dequeue_err (optional, any, None)
      Cilent SSL metrics dropped,enq error analytics qs


    kafka_topic_error (optional, any, None)
      Telemetry dropped because kafka topic not created


    avro_partition_metrics_topic (optional, any, None)
      AVRO partition metrics from acos to harmony


    pr_in_latency_anomaly (optional, any, None)
      PR in latency negative


    pc_acos_harmony_topic_dequeue_err (optional, any, None)
      PC topic to harmony  dequeue error


    analytics_bus_restart (optional, any, None)
      Analytics bus restart count


    fw_rst_pc_acos_harmony_topic (optional, any, None)
      FW RST PC topic counter from acos to harmony


    avro_partition_metrics_topic_enqueue_err (optional, any, None)
      Part metrics dropped,enq error on acos queues


    fw_deny_pc_acos_harmony_topic_dequeue_err (optional, any, None)
      FW DENY PC logs dropped,enq error analytics queues


    cgn_pc_acos_harmony_topic (optional, any, None)
      CGN PC topic counter from acos to harmony


    slb_ssl_stats_metrics_topic_dequeue_err (optional, any, None)
      SSL stats metrics dequeue error


    avro_device_status_topic_enqueue_err (optional, any, None)
      AVRO device status enqueue error


    rule_set_application_metrics_topic (optional, any, None)
      AppFW metrics from acos to harmony


    kafka_broker_down (optional, any, None)
      Telemetry drop because kafka broker is down


    pr_out_latency_anomaly (optional, any, None)
      PR out latency negative


    avro_partition_metrics_topic_dequeue_err (optional, any, None)
      Part metrics dropped,enq error analytics queues


    cgn_summary_error_acos_harmony_topic_dequeue_err (optional, any, None)
      CGN Summary PE topic to harmony dequeue error


    cgn_pe_acos_harmony_topic (optional, any, None)
      CGN PE topic counter from acos to harmony


    fw_rst_pc_acos_harmony_topic_dequeue_err (optional, any, None)
      FW RST PC topic to harmony dequeue error


    pr_be_ttfb_anomaly (optional, any, None)
      PR back-end ttfb is negative


    avro_generic_failed_sending (optional, any, None)
      Telemetry exported via avro failed sending


    ssli_pc_acos_harmony_topic_dequeue_err (optional, any, None)
      SSLi PC topic to harmony dequeue error


    fw_deny_pc_acos_harmony_topic (optional, any, None)
      FW DENY PC topic counter from acos to harmony


    cgn_pe_acos_harmony_topic_dequeue_err (optional, any, None)
      CGN PE topic to harmony dequeue error


    pr_be_ttlb_anomaly (optional, any, None)
      PR back-end ttlb is negative



  host_ipv4 (False, any, None)
    Set kafka Broker ip address or hostname


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  use_mgmt_port (False, any, None)
    Use management port for connections


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (False, any, None)
    Set remote kafka port number (Remote kafka port number 1-32767, default is 9092)


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

