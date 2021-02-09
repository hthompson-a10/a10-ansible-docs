.. _a10_slb_template_cache_module:


a10_slb_template_cache -- Configures A10 slb.template.cache
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

RAM caching template






Parameters
----------

  uri_policy (False, any, None)
    Field uri_policy


    invalidate (optional, any, None)
      Specify if URI should invalidate cache entries matching pattern (pattern that would match entries to be invalidated (64 chars max))


    cache_action (optional, any, None)
      'cache'= Specify if certain URIs should be cached; 'nocache'= Specify if certain URIs should not be cached;


    uri (optional, any, None)
      Specify URI for cache policy (Specify URI pattern that the policy should be applied to, maximum 63 charaters)


    cache_value (optional, any, None)
      Specify seconds that content should be cached, default is age specified in cache template



  remove_cookies (False, any, None)
    Remove cookies in response and cache


  replacement_policy (False, any, None)
    'LFU'= LFU;


  ansible_username (True, any, None)
    Username for AXAPI authentication


  max_content_size (False, any, None)
    Maximum size (bytes) of response that can be cached - default 81920 (80KB)


  max_cache_size (False, any, None)
    Specify maximum cache size in megabytes, default is 80MB (RAM cache size in megabytes (default 80MB))


  min_content_size (False, any, None)
    Minimum size (bytes) of response that can be cached - default 512


  disable_insert_via (False, any, None)
    Disable insertion of via header in response served from RAM cache


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  logging (False, any, None)
    Specify logging template (Logging Config name)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  name (True, any, None)
    Specify cache template name


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'hits'= Cache hits; 'miss'= Cache misses; 'bytes_served'= Bytes served from cache; 'total_req'= Total requests received; 'caching_req'= Total requests to cache; 'nc_req_header'= nc_req_header; 'nc_res_header'= nc_res_header; 'rv_success'= rv_success; 'rv_failure'= rv_failure; 'ims_request'= ims_request; 'nm_response'= nm_response; 'rsp_type_CL'= rsp_type_CL; 'rsp_type_CE'= rsp_type_CE; 'rsp_type_304'= rsp_type_304; 'rsp_type_other'= rsp_type_other; 'rsp_no_compress'= rsp_no_compress; 'rsp_gzip'= rsp_gzip; 'rsp_deflate'= rsp_deflate; 'rsp_other'= rsp_other; 'nocache_match'= nocache_match; 'match'= match; 'invalidate_match'= invalidate_match; 'content_toobig'= content_toobig; 'content_toosmall'= content_toosmall; 'entry_create_failures'= entry_create_failures; 'mem_size'= mem_size; 'entry_num'= entry_num; 'replaced_entry'= replaced_entry; 'aging_entry'= aging_entry; 'cleaned_entry'= cleaned_entry;



  disable_insert_age (False, any, None)
    Disable insertion of age header in response served from RAM cache


  stats (False, any, None)
    Field stats


    nm_response (optional, any, None)
      Field nm_response


    rsp_type_304 (optional, any, None)
      Field rsp_type_304


    cleaned_entry (optional, any, None)
      Field cleaned_entry


    rsp_other (optional, any, None)
      Field rsp_other


    content_toosmall (optional, any, None)
      Field content_toosmall


    entry_num (optional, any, None)
      Field entry_num


    entry_create_failures (optional, any, None)
      Field entry_create_failures


    bytes_served (optional, any, None)
      Bytes served from cache


    nocache_match (optional, any, None)
      Field nocache_match


    total_req (optional, any, None)
      Total requests received


    content_toobig (optional, any, None)
      Field content_toobig


    rv_failure (optional, any, None)
      Field rv_failure


    replaced_entry (optional, any, None)
      Field replaced_entry


    miss (optional, any, None)
      Cache misses


    rsp_type_CE (optional, any, None)
      Field rsp_type_CE


    rsp_gzip (optional, any, None)
      Field rsp_gzip


    nc_req_header (optional, any, None)
      Field nc_req_header


    hits (optional, any, None)
      Cache hits


    rsp_type_other (optional, any, None)
      Field rsp_type_other


    name (optional, any, None)
      Specify cache template name


    aging_entry (optional, any, None)
      Field aging_entry


    rsp_no_compress (optional, any, None)
      Field rsp_no_compress


    mem_size (optional, any, None)
      Field mem_size


    rsp_type_CL (optional, any, None)
      Field rsp_type_CL


    rv_success (optional, any, None)
      Field rv_success


    nc_res_header (optional, any, None)
      Field nc_res_header


    caching_req (optional, any, None)
      Total requests to cache


    ims_request (optional, any, None)
      Field ims_request


    rsp_deflate (optional, any, None)
      Field rsp_deflate


    invalidate_match (optional, any, None)
      Field invalidate_match


    match (optional, any, None)
      Field match



  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  age (False, any, None)
    Specify duration in seconds cached content valid, default is 3600 seconds (seconds that the cached content is valid (default 3600 seconds))


  state (True, any, None)
    State of the object to be created.


  verify_host (False, any, None)
    Verify request using host before sending response from RAM cache


  accept_reload_req (False, any, None)
    Accept reload requests via cache-control directives in HTTP headers


  ansible_port (True, any, None)
    Port for AXAPI authentication


  default_policy_nocache (False, any, None)
    Specify default policy to be to not cache


  local_uri_policy (False, any, None)
    Field local_uri_policy


    local_uri (optional, any, None)
      Specify Local URI for caching (Specify URI pattern that the policy should be applied to, maximum 63 charaters)










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

