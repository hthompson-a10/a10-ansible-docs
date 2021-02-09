.. _a10_file_inspection_global_stat_module:


a10_file_inspection_global_stat -- Configures A10 file.inspection.global-stat
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

global stats






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'download_bad_blocked'= Download malware blocked; 'download_bad_allowed'= Download malware allowed; 'download_bad_ext_inspect'= Download malware extrnal inspect; 'download_suspect_blocked'= Download suspect blocked; 'download_suspect_ext_inspect'= Download suspect extrnal inspect; 'download_suspect_allowed'= Download suspect allowed; 'download_good_blocked'= Download safe blocked; 'download_good_allowed'= Download safe external inspect; 'download_good_ext_inspect'= Download safe allowed; 'upload_bad_blocked'= Upload malware blocked; 'upload_bad_allowed'= Upload malware allowed; 'upload_bad_ext_inspect'= Upload malware extrnal inspect; 'upload_suspect_blocked'= Upload suspect blocked; 'upload_suspect_ext_inspect'= Upload suspect extrnal inspect; 'upload_suspect_allowed'= Upload suspect allowed; 'upload_good_blocked'= Upload safe blocked; 'upload_good_ext_inspect'= Upload safe external inspect; 'upload_good_allowed'= Upload safe allowed; 'icap_200'= Receive icap status 200; 'icap_204'= Receive icap status 204; 'icap_500'= Receive icap status 500; 'icap_other_status_code'= Receive icap other status code; 'icap_connect_fail'= Icap connect fail; 'icap_connection_created'= Icap connection created; 'icap_connection_established'= Icap connection established; 'icap_connection_closed'= Icap connection closed; 'icap_connection_rst'= Icap connection rst; 'icap_bytes_sent'= Icap bytes sent; 'icap_bytes_received'= Icap bytes received; 'bypass_aflex'= Bypassed by aflex; 'bypass_large_file'= Bypassed - large file size; 'bypass_service_disabled'= Bypassed - Internal service disabled; 'bypass_service_down'= Bypassed - Internal service down; 'reset_service_down'= Reset - Internal service down; 'bypass_max_concurrent_files_reached'= Bypassed - max concurrent files on server reached; 'bypass_non_inspection'= Bypassed non inspection data; 'non_supported_file'= Non supported file type; 'transactions_alloc'= Total transactions allocated; 'transactions_free'= Total transactions freed; 'transactions_failure'= Total transactions failure; 'transactions_aborted'= Total transactions aborted; 'orig_conn_bytes_received'= Original connection bytes received; 'orig_conn_bytes_sent'= Original connection bytes sent; 'orig_conn_bytes_bypassed'= Original connection bytes bypassed; 'bypass_buffered_overlimit'= Total Bytes Buffered Overlimit; 'total_bandwidth'= Total File Bytes; 'total_suspect_bandwidth'= Total Suspected Files Bytes; 'total_bad_bandwidth'= Total Bad Files Bytes; 'total_good_bandwidth'= Total Good Files Bytes; 'total_file_size_less_1m'= Total Files Less than 1Mb; 'total_file_size_1_5m'= Total Files Between 1-5Mb; 'total_file_size_5_8m'= Total Files Between 5-8Mb; 'total_file_size_8_32m'= Total Files Between 8-32Mb; 'total_file_size_over_32m'= Total Files over 32Mb; 'suspect_file_size_less_1m'= Suspect Files Less than 1Mb; 'suspect_file_size_1_5m'= Suspect Files Between 1-5Mb; 'suspect_file_size_5_8m'= Suspect Files Between 5-8Mb; 'suspect_file_size_8_32m'= Suspect Files Between 8-32Mb; 'suspect_file_size_over_32m'= Suspect Files over 32Mb; 'good_file_size_less_1m'= Good Files Less than 1Mb; 'good_file_size_1_5m'= Good Files Between 1-5Mb; 'good_file_size_5_8m'= Good Files Between 5-8Mb; 'good_file_size_8_32m'= Good Files Between 8-32Mb; 'good_file_size_over_32m'= Good Files over 32Mb; 'bad_file_size_less_1m'= Bad Files Less than 1Mb; 'bad_file_size_1_5m'= Bad Files Between 1-5Mb; 'bad_file_size_5_8m'= Bad Files Between 5-8Mb; 'bad_file_size_8_32m'= Bad Files Between 8-32Mb; 'bad_file_size_over_32m'= Bad Files over 32Mb;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    upload_bad_blocked (optional, any, None)
      Upload malware blocked


    bad_file_size_less_1m (optional, any, None)
      Bad Files Less than 1Mb


    suspect_file_size_1_5m (optional, any, None)
      Suspect Files Between 1-5Mb


    upload_suspect_allowed (optional, any, None)
      Upload suspect allowed


    total_file_size_less_1m (optional, any, None)
      Total Files Less than 1Mb


    bad_file_size_1_5m (optional, any, None)
      Bad Files Between 1-5Mb


    total_file_size_1_5m (optional, any, None)
      Total Files Between 1-5Mb


    non_supported_file (optional, any, None)
      Non supported file type


    suspect_file_size_8_32m (optional, any, None)
      Suspect Files Between 8-32Mb


    icap_bytes_sent (optional, any, None)
      Icap bytes sent


    icap_other_status_code (optional, any, None)
      Receive icap other status code


    bypass_aflex (optional, any, None)
      Bypassed by aflex


    good_file_size_over_32m (optional, any, None)
      Good Files over 32Mb


    total_suspect_bandwidth (optional, any, None)
      Total Suspected Files Bytes


    upload_good_ext_inspect (optional, any, None)
      Upload safe external inspect


    good_file_size_8_32m (optional, any, None)
      Good Files Between 8-32Mb


    reset_service_down (optional, any, None)
      Reset - Internal service down


    icap_500 (optional, any, None)
      Receive icap status 500


    upload_suspect_ext_inspect (optional, any, None)
      Upload suspect extrnal inspect


    download_good_allowed (optional, any, None)
      Download safe external inspect


    bypass_max_concurrent_files_reached (optional, any, None)
      Bypassed - max concurrent files on server reached


    bypass_service_down (optional, any, None)
      Bypassed - Internal service down


    total_file_size_8_32m (optional, any, None)
      Total Files Between 8-32Mb


    bypass_non_inspection (optional, any, None)
      Bypassed non inspection data


    suspect_file_size_5_8m (optional, any, None)
      Suspect Files Between 5-8Mb


    total_bandwidth (optional, any, None)
      Total File Bytes


    download_bad_allowed (optional, any, None)
      Download malware allowed


    download_good_ext_inspect (optional, any, None)
      Download safe allowed


    bad_file_size_8_32m (optional, any, None)
      Bad Files Between 8-32Mb


    total_file_size_over_32m (optional, any, None)
      Total Files over 32Mb


    suspect_file_size_less_1m (optional, any, None)
      Suspect Files Less than 1Mb


    good_file_size_less_1m (optional, any, None)
      Good Files Less than 1Mb


    good_file_size_5_8m (optional, any, None)
      Good Files Between 5-8Mb


    transactions_free (optional, any, None)
      Total transactions freed


    transactions_failure (optional, any, None)
      Total transactions failure


    suspect_file_size_over_32m (optional, any, None)
      Suspect Files over 32Mb


    icap_200 (optional, any, None)
      Receive icap status 200


    icap_204 (optional, any, None)
      Receive icap status 204


    orig_conn_bytes_bypassed (optional, any, None)
      Original connection bytes bypassed


    download_good_blocked (optional, any, None)
      Download safe blocked


    upload_bad_ext_inspect (optional, any, None)
      Upload malware extrnal inspect


    orig_conn_bytes_sent (optional, any, None)
      Original connection bytes sent


    download_suspect_allowed (optional, any, None)
      Download suspect allowed


    bypass_service_disabled (optional, any, None)
      Bypassed - Internal service disabled


    total_file_size_5_8m (optional, any, None)
      Total Files Between 5-8Mb


    icap_connect_fail (optional, any, None)
      Icap connect fail


    upload_good_blocked (optional, any, None)
      Upload safe blocked


    orig_conn_bytes_received (optional, any, None)
      Original connection bytes received


    download_suspect_ext_inspect (optional, any, None)
      Download suspect extrnal inspect


    bad_file_size_5_8m (optional, any, None)
      Bad Files Between 5-8Mb


    icap_connection_closed (optional, any, None)
      Icap connection closed


    download_bad_blocked (optional, any, None)
      Download malware blocked


    bad_file_size_over_32m (optional, any, None)
      Bad Files over 32Mb


    download_bad_ext_inspect (optional, any, None)
      Download malware extrnal inspect


    transactions_aborted (optional, any, None)
      Total transactions aborted


    total_good_bandwidth (optional, any, None)
      Total Good Files Bytes


    transactions_alloc (optional, any, None)
      Total transactions allocated


    bypass_buffered_overlimit (optional, any, None)
      Total Bytes Buffered Overlimit


    total_bad_bandwidth (optional, any, None)
      Total Bad Files Bytes


    upload_suspect_blocked (optional, any, None)
      Upload suspect blocked


    icap_connection_rst (optional, any, None)
      Icap connection rst


    good_file_size_1_5m (optional, any, None)
      Good Files Between 1-5Mb


    icap_bytes_received (optional, any, None)
      Icap bytes received


    icap_connection_established (optional, any, None)
      Icap connection established


    download_suspect_blocked (optional, any, None)
      Download suspect blocked


    icap_connection_created (optional, any, None)
      Icap connection created


    bypass_large_file (optional, any, None)
      Bypassed - large file size


    upload_good_allowed (optional, any, None)
      Upload safe allowed


    upload_bad_allowed (optional, any, None)
      Upload malware allowed



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  file_content (False, any, None)
    Content of the uploaded file


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

