.. _a10_visibility_module:


a10_visibility -- Configures A10 visibility
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Display Network statistics






Parameters
----------

  monitored_entity (False, any, None)
    Field monitored_entity


    detail (optional, any, None)
      Field detail


    sessions (optional, any, None)
      Field sessions


    topk (optional, any, None)
      Field topk


    uuid (optional, any, None)
      uuid of the object


    secondary (optional, any, None)
      Field secondary



  debug_files (False, any, None)
    Field debug_files


    uuid (optional, any, None)
      uuid of the object



  ansible_username (True, any, None)
    Username for AXAPI authentication


  initial_learning_interval (False, any, None)
    Initial learning interval (in hours) before processing


  reporting (False, any, None)
    Field reporting


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object


    template (optional, any, None)
      Field template


    telemetry_export_interval (optional, any, None)
      Field telemetry_export_interval



  resource_usage (False, any, None)
    Field resource_usage


    uuid (optional, any, None)
      uuid of the object



  topk (False, any, None)
    Field topk


    sources (optional, any, None)
      Field sources



  file (False, any, None)
    Field file


    metrics (optional, any, None)
      Field metrics



  granularity (False, any, None)
    Granularity for rate based calculations in seconds (default 5)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  monitor (False, any, None)
    Field monitor


    uuid (optional, any, None)
      uuid of the object


    sflow (optional, any, None)
      Field sflow


    agent_list (optional, any, None)
      Field agent_list


    replay_debug_file (optional, any, None)
      Field replay_debug_file


    index_sessions_type (optional, any, None)
      'per-cpu'= Use per cpu list;


    primary_monitor (optional, any, None)
      'traffic'= Mointor traffic;


    delete_debug_file (optional, any, None)
      Field delete_debug_file


    mon_entity_topk (optional, any, None)
      Enable topk for primary entities


    index_sessions (optional, any, None)
      Start indexing associated sessions


    source_entity_topk (optional, any, None)
      Enable topk for sources to primary-entities


    debug_list (optional, any, None)
      Field debug_list


    secondary_monitor (optional, any, None)
      Field secondary_monitor


    netflow (optional, any, None)
      Field netflow


    monitor_key (optional, any, None)
      'source'= Monitor traffic from all sources; 'dest'= Monitor traffic to any destination; 'service'= Monitor traffic to any service; 'source-nat-ip'= Monitor traffic to all source nat IPs;


    template (optional, any, None)
      Field template



  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'mon-entity-limit-exceed'= Total monitor entity limit exceed failures; 'ha-entity-create-sent'= Total montior entity HA create messages sent; 'ha-entity-delete-sent'= Total montior entity HA delete messages sent; 'ha-entity-anomaly-on-sent'= Total anomaly on HA messages sent; 'ha-entity- anomaly-off-sent'= Total anomaly off HA messages sent; 'ha-entity-periodic- sync-sent'= Total monitor entity periodic sync messages sent; 'out-of-memory- alloc-failures'= Out of memory allocation failures; 'lw-mon-entity-created'= Total Light-weight entities created; 'lw-mon-entity-deleted'= Total Light- weight entities deleted; 'lw-mon-entity-limit-exceed'= Light weight limit exceeded errors; 'lw-out-of-memory-alloc-failures'= Light Weight Out-of-memory allocation failures; 'mon-entity-rrd-file-timestamp-err'= Total monitor entity rrd file timestamp errors; 'mon-entity-rrd-update-err'= Total monitor entity rrd update error; 'mon-entity-rrd-last-update-fetch-failed-err'= Total monitor entity rrd last update fetch failed error; 'mon-entity-rrd-tune-err'= Total monitor entity rrd tune error; 'mon-entity-rrd-out-of-memory-err'= Total monitor entity rrd load failed, out of memory error; 'mon-entity-rrd-file- create-err'= Total monitor entity rrd file create error;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    mon_entity_rrd_file_timestamp_err (optional, any, None)
      Total monitor entity rrd file timestamp errors


    mon_entity_rrd_file_create_err (optional, any, None)
      Total monitor entity rrd file create error


    lw_mon_entity_created (optional, any, None)
      Total Light-weight entities created


    mon_entity_rrd_update_err (optional, any, None)
      Total monitor entity rrd update error


    reporting (optional, any, None)
      Field reporting


    mon_entity_limit_exceed (optional, any, None)
      Total monitor entity limit exceed failures


    lw_mon_entity_deleted (optional, any, None)
      Total Light-weight entities deleted


    mon_entity_rrd_tune_err (optional, any, None)
      Total monitor entity rrd tune error


    out_of_memory_alloc_failures (optional, any, None)
      Out of memory allocation failures


    lw_out_of_memory_alloc_failures (optional, any, None)
      Light Weight Out-of-memory allocation failures


    ha_entity_periodic_sync_sent (optional, any, None)
      Total monitor entity periodic sync messages sent


    mon_entity_rrd_out_of_memory_err (optional, any, None)
      Total monitor entity rrd load failed, out of memory error


    ha_entity_anomaly_off_sent (optional, any, None)
      Total anomaly off HA messages sent


    ha_entity_delete_sent (optional, any, None)
      Total montior entity HA delete messages sent


    monitor (optional, any, None)
      Field monitor


    flow_collector (optional, any, None)
      Field flow_collector


    ha_entity_create_sent (optional, any, None)
      Total montior entity HA create messages sent


    lw_mon_entity_limit_exceed (optional, any, None)
      Light weight limit exceeded errors


    ha_entity_anomaly_on_sent (optional, any, None)
      Total anomaly on HA messages sent


    mon_entity_rrd_last_update_fetch_failed_err (optional, any, None)
      Total monitor entity rrd last update fetch failed error


    mon_entity_telemetry_data (optional, any, None)
      Field mon_entity_telemetry_data



  uuid (False, any, None)
    uuid of the object


  flow_collector (False, any, None)
    Field flow_collector


    netflow (optional, any, None)
      Field netflow


    sflow (optional, any, None)
      Field sflow



  state (True, any, None)
    State of the object to be created.


  anomaly_detection (False, any, None)
    Field anomaly_detection


    feature_status (optional, any, None)
      'enable'= Enable anomaly-detection; 'disable'= Disable anomaly detection (default);


    sensitivity (optional, any, None)
      'high'= Highly sensitive anomaly detection. Can lead to false positives; 'low'= Low sensitivity anomaly detection. Can cause delay in detection and might not detect certain attacks. (default);


    logging (optional, any, None)
      'per-entity'= Enable per entity logging; 'per-metric'= Enable per metric logging with threshold details; 'disable'= Disable anomaly notifications (Default);


    uuid (optional, any, None)
      uuid of the object



  source_entity_topk (False, any, None)
    Enable topk for sources


  ansible_password (True, any, None)
    Password for AXAPI authentication


  mon_entity_telemetry_data (False, any, None)
    Field mon_entity_telemetry_data


    sampling_enable (optional, any, None)
      Field sampling_enable


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

