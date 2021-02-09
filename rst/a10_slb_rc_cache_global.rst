.. _a10_slb_rc_cache_global_module:


a10_slb_rc_cache_global -- Configures A10 slb.rc-cache-global
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

global ram cache stats






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'hits'= Cache Hits; 'miss'= Cache Misses; 'bytes_served'= Bytes Served; 'total_req'= Total Requests; 'caching_req'= Cacheable Requests; 'nc_req_header'= No-cache Request; 'nc_res_header'= Not cacheable; 'rv_success'= Revalidation Successes; 'rv_failure'= Revalidation Failures; 'ims_request'= IMS Requests; 'nm_response'= Responses from cache 304 Not Modified; 'rsp_type_CL'= Responses from server 200 OK - Cont Len; 'rsp_type_CE'= Responses from server 200 OK - Chnk Enc; 'rsp_type_304'= Responses from server 304 Not Modified; 'rsp_type_other'= Responses from server 200 OK - Other; 'rsp_no_compress'= Responses from cache 200 OK - No Comp; 'rsp_gzip'= Responses from cache 200 OK - Gzip; 'rsp_deflate'= Responses from cache 200 OK - Deflate; 'rsp_other'= Responses from cache Other; 'nocache_match'= Policy URI nocache; 'match'= Policy URI cache; 'invalidate_match'= Policy URI invalidate; 'content_toobig'= Policy Content Too Big; 'content_toosmall'= Policy Content Too Small; 'entry_create_failures'= Entry Create failures; 'mem_size'= Memory Used; 'entry_num'= Entry Cached; 'replaced_entry'= Entry Replaced; 'aging_entry'= Entry Aged Out; 'cleaned_entry'= Entry Cleaned;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    nm_response (optional, any, None)
      Responses from cache 304 Not Modified


    rsp_type_304 (optional, any, None)
      Responses from server 304 Not Modified


    cleaned_entry (optional, any, None)
      Entry Cleaned


    rsp_other (optional, any, None)
      Responses from cache Other


    content_toosmall (optional, any, None)
      Policy Content Too Small


    entry_num (optional, any, None)
      Entry Cached


    entry_create_failures (optional, any, None)
      Entry Create failures


    bytes_served (optional, any, None)
      Bytes Served


    nocache_match (optional, any, None)
      Policy URI nocache


    total_req (optional, any, None)
      Total Requests


    content_toobig (optional, any, None)
      Policy Content Too Big


    rv_failure (optional, any, None)
      Revalidation Failures


    replaced_entry (optional, any, None)
      Entry Replaced


    miss (optional, any, None)
      Cache Misses


    rsp_gzip (optional, any, None)
      Responses from cache 200 OK - Gzip


    nc_req_header (optional, any, None)
      No-cache Request


    hits (optional, any, None)
      Cache Hits


    rsp_type_other (optional, any, None)
      Responses from server 200 OK - Other


    rsp_type_CE (optional, any, None)
      Responses from server 200 OK - Chnk Enc


    aging_entry (optional, any, None)
      Entry Aged Out


    rsp_no_compress (optional, any, None)
      Responses from cache 200 OK - No Comp


    mem_size (optional, any, None)
      Memory Used


    rsp_type_CL (optional, any, None)
      Responses from server 200 OK - Cont Len


    rv_success (optional, any, None)
      Revalidation Successes


    nc_res_header (optional, any, None)
      Not cacheable


    caching_req (optional, any, None)
      Cacheable Requests


    ims_request (optional, any, None)
      IMS Requests


    rsp_deflate (optional, any, None)
      Responses from cache 200 OK - Deflate


    invalidate_match (optional, any, None)
      Policy URI invalidate


    match (optional, any, None)
      Policy URI cache



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

