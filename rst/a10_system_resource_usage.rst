.. _a10_system_resource_usage_module:


a10_system_resource_usage -- Configures A10 system.resource-usage
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure System Resource Usage






Parameters
----------

  oper (False, any, None)
    Field oper


    nat_pool_addr_min (optional, any, None)
      Field nat_pool_addr_min


    aflex_file_size_min (optional, any, None)
      Field aflex_file_size_min


    aflex_authz_collection_number_default (optional, any, None)
      Field aflex_authz_collection_number_default


    aflex_table_entry_count_min (optional, any, None)
      Field aflex_table_entry_count_min


    class_list_ac_min (optional, any, None)
      Field class_list_ac_min


    aflex_file_size_default (optional, any, None)
      Field aflex_file_size_default


    aflex_authz_collection_number_min (optional, any, None)
      Field aflex_authz_collection_number_min


    aflex_authz_collection_number_max (optional, any, None)
      Field aflex_authz_collection_number_max


    visibility_mon_entity_default (optional, any, None)
      Field visibility_mon_entity_default


    radius_table_size_min (optional, any, None)
      Field radius_table_size_min


    class_list_ipv6_addr_max (optional, any, None)
      Field class_list_ipv6_addr_max


    radius_table_size_max (optional, any, None)
      Field radius_table_size_max


    class_list_ac_max (optional, any, None)
      Field class_list_ac_max


    aflex_table_entry_count_default (optional, any, None)
      Field aflex_table_entry_count_default


    nat_pool_addr_default (optional, any, None)
      Field nat_pool_addr_default


    authz_policy_number_max (optional, any, None)
      Field authz_policy_number_max


    class_list_ipv6_addr_min (optional, any, None)
      Field class_list_ipv6_addr_min


    auth_portal_html_file_size_max (optional, any, None)
      Field auth_portal_html_file_size_max


    radius_table_size_default (optional, any, None)
      Field radius_table_size_default


    visibility_mon_entity_min (optional, any, None)
      Field visibility_mon_entity_min


    l4_session_count_min (optional, any, None)
      Field l4_session_count_min


    class_list_ac_default (optional, any, None)
      Field class_list_ac_default


    auth_portal_html_file_size_default (optional, any, None)
      Field auth_portal_html_file_size_default


    auth_portal_html_file_size_min (optional, any, None)
      Field auth_portal_html_file_size_min


    l4_session_count_default (optional, any, None)
      Field l4_session_count_default


    authz_policy_number_default (optional, any, None)
      Field authz_policy_number_default


    auth_portal_image_file_size_default (optional, any, None)
      Field auth_portal_image_file_size_default


    auth_portal_image_file_size_max (optional, any, None)
      Field auth_portal_image_file_size_max


    l4_session_count_max (optional, any, None)
      Field l4_session_count_max


    visibility_mon_entity_max (optional, any, None)
      Field visibility_mon_entity_max


    aflex_table_entry_count_max (optional, any, None)
      Field aflex_table_entry_count_max


    authz_policy_number_min (optional, any, None)
      Field authz_policy_number_min


    class_list_ipv6_addr_default (optional, any, None)
      Field class_list_ipv6_addr_default


    auth_portal_image_file_size_min (optional, any, None)
      Field auth_portal_image_file_size_min


    nat_pool_addr_max (optional, any, None)
      Field nat_pool_addr_max


    aflex_file_size_max (optional, any, None)
      Field aflex_file_size_max



  ansible_username (True, any, None)
    Username for AXAPI authentication


  auth_portal_html_file_size (False, any, None)
    Specify maximum html file size for each html page in auth portal (in KB)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  visibility (False, any, None)
    Field visibility


    uuid (optional, any, None)
      uuid of the object


    monitored_entity_count (optional, any, None)
      Total number of monitored entities for visibility



  aflex_table_entry_count (False, any, None)
    Total aFleX table entry in the system (Total aFlex entry in the system)


  authz_policy_number (False, any, None)
    Specify the maximum number of authorization policies


  class_list_ac_entry_count (False, any, None)
    Total entries for AC class-list


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  max_aflex_authz_collection_number (False, any, None)
    Specify the maximum number of collections supported by aFleX authorization


  uuid (False, any, None)
    uuid of the object


  ssl_context_memory (False, any, None)
    Total SSL context memory needed in units of MB. Will be rounded to closest multiple of 2MB


  nat_pool_addr_count (False, any, None)
    Total configurable NAT Pool addresses in the System


  auth_portal_image_file_size (False, any, None)
    Specify maximum image file size for default portal (in KB)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  max_aflex_file_size (False, any, None)
    Set maximum aFleX file size (Maximum file size in KBytes, default is 32K)


  state (True, any, None)
    State of the object to be created.


  ssl_dma_memory (False, any, None)
    Total SSL DMA memory needed in units of MB. Will be rounded to closest multiple of 2MB


  l4_session_count (False, any, None)
    Total Sessions in the System


  class_list_ipv6_addr_count (False, any, None)
    Total IPv6 addresses for class-list


  radius_table_size (False, any, None)
    Total configurable CGNV6 RADIUS Table entries









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

