.. _a10_so_counters_module:


a10_so_counters -- Configures A10 so-counters
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show scaleout statistics






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'so_pkts_conn_in'= Total packets processed for an established connection; 'so_pkts_conn_redirect'= Total packets redirected for an established connection; 'so_pkts_dropped'= Total packets dropped; 'so_pkts_errors'= Total packet errors; 'so_pkts_in'= Total packets in-coming; 'so_pkts_new_conn_in'= Total packets processed for a new connection; 'so_pkts_new_conn_redirect'= Total packets redirected for a new connection; 'so_pkts_out'= Total packets sent out; 'so_pkts_redirect'= Total packets redirected; 'so_pkts_conn_sync_fail'= Total connection sync failures; 'so_pkts_nat_reserve_fail'= Total NAT reserve failures; 'so_pkts_nat_release_fail'= Total NAT release failures; 'so_pkts_conn_l7_sync'= Total L7 connection syncs; 'so_pkts_conn_l4_sync'= Total L4 connection syncs; 'so_pkts_conn_nat_sync'= Total NAT connection syncs; 'so_pkts_conn_xparent_fw_sync'= Total Xparent FW connection syncs; 'so_pkts_redirect_conn_aged_out'= Total redirect conns aged out; 'so_pkts_traffic_map_not_found_drop'= Traffic MAP Not Found Drop; 'so_pkts_scaleout_not_active_drop'= Scaleout Not Active Drop; 'so_pkts_dest_mac_mistmatch_drop'= Destination MAC Mistmatch Drop; 'so_pkts_l2redirect_interface_not_up'= L2redirect Intf is not UP; 'so_fw_internal_rule_count'= FW internal rule count; 'so_pkts_redirect_table_error'= Redirect Table Error; 'so_pkts_mac_zero_drop'= MAC Address zero Drop;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    so_pkts_conn_sync_fail (optional, any, None)
      Total connection sync failures


    so_pkts_nat_reserve_fail (optional, any, None)
      Total NAT reserve failures


    so_pkts_conn_l7_sync (optional, any, None)
      Total L7 connection syncs


    so_pkts_traffic_map_not_found_drop (optional, any, None)
      Traffic MAP Not Found Drop


    so_pkts_conn_redirect (optional, any, None)
      Total packets redirected for an established connection


    so_pkts_redirect (optional, any, None)
      Total packets redirected


    so_pkts_conn_in (optional, any, None)
      Total packets processed for an established connection


    so_pkts_redirect_conn_aged_out (optional, any, None)
      Total redirect conns aged out


    so_pkts_mac_zero_drop (optional, any, None)
      MAC Address zero Drop


    so_pkts_conn_xparent_fw_sync (optional, any, None)
      Total Xparent FW connection syncs


    so_pkts_in (optional, any, None)
      Total packets in-coming


    so_pkts_errors (optional, any, None)
      Total packet errors


    so_pkts_scaleout_not_active_drop (optional, any, None)
      Scaleout Not Active Drop


    so_pkts_new_conn_in (optional, any, None)
      Total packets processed for a new connection


    so_pkts_nat_release_fail (optional, any, None)
      Total NAT release failures


    so_pkts_dropped (optional, any, None)
      Total packets dropped


    so_pkts_redirect_table_error (optional, any, None)
      Redirect Table Error


    so_pkts_out (optional, any, None)
      Total packets sent out


    so_pkts_conn_nat_sync (optional, any, None)
      Total NAT connection syncs


    so_pkts_new_conn_redirect (optional, any, None)
      Total packets redirected for a new connection


    so_fw_internal_rule_count (optional, any, None)
      FW internal rule count


    so_pkts_conn_l4_sync (optional, any, None)
      Total L4 connection syncs


    so_pkts_dest_mac_mistmatch_drop (optional, any, None)
      Destination MAC Mistmatch Drop


    so_pkts_l2redirect_interface_not_up (optional, any, None)
      L2redirect Intf is not UP



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

