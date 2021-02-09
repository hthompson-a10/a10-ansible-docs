.. _a10_visibility_flow_collector_sflow_module:


a10_visibility_flow_collector_sflow -- Configures A10 visibility.flow.collector.sflow
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

sFlow collector






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'pkts-received'= Total sflow pkts received; 'frag-dropped'= Total sflow fragment packets droppped; 'agent-not-found'= sflow pkts from not configured agents; 'version-not-supported'= sflow version not supported; 'unknown-dir'= sflow sample direction is unknown;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    version_not_supported (optional, any, None)
      sflow version not supported


    unknown_dir (optional, any, None)
      sflow sample direction is unknown


    agent_not_found (optional, any, None)
      sflow pkts from not configured agents


    pkts_received (optional, any, None)
      Total sflow pkts received


    frag_dropped (optional, any, None)
      Total sflow fragment packets droppped



  uuid (False, any, None)
    uuid of the object


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

