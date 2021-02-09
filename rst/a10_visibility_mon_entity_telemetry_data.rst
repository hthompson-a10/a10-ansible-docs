.. _a10_visibility_mon_entity_telemetry_data_module:


a10_visibility_mon_entity_telemetry_data -- Configures A10 visibility.mon-entity-telemetry-data
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

dummy schema for sflow exports






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'in_pkts'= Monitored Entity telemetry Metric IN pkts; 'out_pkts'= Monitored Entity telemetry Metric OUT pkts; 'in_bytes'= Monitored Entity telemetry Metric IN bytes; 'out_bytes'= Monitored Entity telemetry Metric OUT bytes; 'errors'= Monitored Entity telemetry Metric ERRORS; 'in_small_pkt'= Monitored Entity telemetry Metric IN SMALL pkt; 'in_frag'= Monitored Entity telemetry Metric IN frag; 'out_small_pkt'= Monitored Entity telemetry Metric OUT SMALL pkt; 'out_frag'= Monitored Entity telemetry Metric OUT frag; 'new- conn'= Monitored Entity telemetry Metric New Sessions; 'concurrent-conn'= concurrent-conn; 'in_bytes_per_out_bytes'= Monitored Entity telemetry Metric IN bytes per OUT bytes; 'drop_pkts_per_pkts'= Monitored Entity telemetry Metric Drop pkts per pkts; 'tcp_in_syn'= Monitored Entity telemetry Metric TCP IN syn; 'tcp_out_syn'= Monitored Entity telemetry Metric TCP OUT syn; 'tcp_in_fin'= Monitored Entity telemetry Metric TCP IN fin; 'tcp_out_fin'= Monitored Entity telemetry Metric TCP OUT fin; 'tcp_in_payload'= Monitored Entity telemetry Metric TCP IN payload; 'tcp_out_payload'= Monitored Entity telemetry Metric TCP OUT payload; 'tcp_in_rexmit'= Monitored Entity telemetry Metric TCP IN rexmit; 'tcp_out_rexmit'= Monitored Entity telemetry Metric TCP OUT rexmit; 'tcp_in_rst'= Monitored Entity telemetry Metric TCP IN rst; 'tcp_out_rst'= Monitored Entity telemetry Metric TCP OUT rst; 'tcp_in_empty_ack'= Monitored Entity telemetry Metric TCP_IN EMPTY ack; 'tcp_out_empty_ack'= Monitored Entity telemetry Metric TCP OUT EMPTY ack; 'tcp_in_zero_wnd'= Monitored Entity telemetry Metric TCP IN ZERO wnd; 'tcp_out_zero_wnd'= Monitored Entity telemetry Metric TCP OUT ZERO wnd; 'tcp_fwd_syn_per_fin'= Monitored Entity telemetry Metric TCP FWD SYN per FIN;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    tcp_out_syn (optional, any, None)
      Monitored Entity telemetry Metric TCP OUT syn


    in_bytes (optional, any, None)
      Monitored Entity telemetry Metric IN bytes


    tcp_out_rexmit (optional, any, None)
      Monitored Entity telemetry Metric TCP OUT rexmit


    tcp_in_empty_ack (optional, any, None)
      Monitored Entity telemetry Metric TCP_IN EMPTY ack


    in_small_pkt (optional, any, None)
      Monitored Entity telemetry Metric IN SMALL pkt


    tcp_out_empty_ack (optional, any, None)
      Monitored Entity telemetry Metric TCP OUT EMPTY ack


    concurrent_conn (optional, any, None)
      Field concurrent_conn


    tcp_in_fin (optional, any, None)
      Monitored Entity telemetry Metric TCP IN fin


    out_pkts (optional, any, None)
      Monitored Entity telemetry Metric OUT pkts


    tcp_fwd_syn_per_fin (optional, any, None)
      Monitored Entity telemetry Metric TCP FWD SYN per FIN


    out_frag (optional, any, None)
      Monitored Entity telemetry Metric OUT frag


    tcp_in_rst (optional, any, None)
      Monitored Entity telemetry Metric TCP IN rst


    tcp_out_rst (optional, any, None)
      Monitored Entity telemetry Metric TCP OUT rst


    in_pkts (optional, any, None)
      Monitored Entity telemetry Metric IN pkts


    tcp_out_zero_wnd (optional, any, None)
      Monitored Entity telemetry Metric TCP OUT ZERO wnd


    tcp_in_syn (optional, any, None)
      Monitored Entity telemetry Metric TCP IN syn


    new_conn (optional, any, None)
      Monitored Entity telemetry Metric New Sessions


    out_bytes (optional, any, None)
      Monitored Entity telemetry Metric OUT bytes


    errors (optional, any, None)
      Monitored Entity telemetry Metric ERRORS


    out_small_pkt (optional, any, None)
      Monitored Entity telemetry Metric OUT SMALL pkt


    in_frag (optional, any, None)
      Monitored Entity telemetry Metric IN frag


    drop_pkts_per_pkts (optional, any, None)
      Monitored Entity telemetry Metric Drop pkts per pkts


    tcp_in_rexmit (optional, any, None)
      Monitored Entity telemetry Metric TCP IN rexmit


    tcp_out_fin (optional, any, None)
      Monitored Entity telemetry Metric TCP OUT fin


    tcp_out_payload (optional, any, None)
      Monitored Entity telemetry Metric TCP OUT payload


    tcp_in_zero_wnd (optional, any, None)
      Monitored Entity telemetry Metric TCP IN ZERO wnd


    in_bytes_per_out_bytes (optional, any, None)
      Monitored Entity telemetry Metric IN bytes per OUT bytes


    tcp_in_payload (optional, any, None)
      Monitored Entity telemetry Metric TCP IN payload



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

