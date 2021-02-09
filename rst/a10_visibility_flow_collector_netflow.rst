.. _a10_visibility_flow_collector_netflow_module:


a10_visibility_flow_collector_netflow -- Configures A10 visibility.flow.collector.netflow
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

NetFlow/IPFIX collector






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'pkts-rcvd'= Total nflow packets received; 'v9-templates-created'= Total v9 templates created; 'v9-templates-deleted'= Total v9 templates deleted; 'v10-templates-created'= Total v10(IPFIX) templates created; 'v10-templates- deleted'= Total v10(IPFIX) templates deleted; 'template-drop-exceeded'= Total templates dropped because of maximum limit; 'template-drop-out-of-memory'= Total templates dropped becuase of out of memory; 'frag-dropped'= Total nflow fragment packets droppped; 'agent-not-found'= nflow pkts from not configured agents; 'version-not-supported'= nflow version not supported; 'unknown-dir'= nflow sample direction is unknown;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    v9_templates_created (optional, any, None)
      Total v9 templates created


    pkts_rcvd (optional, any, None)
      Total nflow packets received


    frag_dropped (optional, any, None)
      Total nflow fragment packets droppped


    agent_not_found (optional, any, None)
      nflow pkts from not configured agents


    version_not_supported (optional, any, None)
      nflow version not supported


    v9_templates_deleted (optional, any, None)
      Total v9 templates deleted


    template_drop_out_of_memory (optional, any, None)
      Total templates dropped becuase of out of memory


    v10_templates_created (optional, any, None)
      Total v10(IPFIX) templates created


    unknown_dir (optional, any, None)
      nflow sample direction is unknown


    v10_templates_deleted (optional, any, None)
      Total v10(IPFIX) templates deleted


    template_drop_exceeded (optional, any, None)
      Total templates dropped because of maximum limit


    template (optional, any, None)
      Field template



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  template (False, any, None)
    Field template


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object


    detail (optional, any, None)
      Field detail



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

