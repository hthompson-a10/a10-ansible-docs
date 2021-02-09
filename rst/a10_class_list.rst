.. _a10_class_list_module:


a10_class_list -- Configures A10 class-list
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure classification list






Parameters
----------

  oper (False, any, None)
    Field oper


    string_entries (optional, any, None)
      Field string_entries


    ntype (optional, any, None)
      Field type


    string_total_entries (optional, any, None)
      Field string_total_entries


    ipv6_entries (optional, any, None)
      Field ipv6_entries


    dns_entries (optional, any, None)
      Field dns_entries


    name (optional, any, None)
      Specify name of the class list


    file_or_string (optional, any, None)
      Field file_or_string


    ac_entries (optional, any, None)
      Field ac_entries


    ipv6_total_subnet (optional, any, None)
      Field ipv6_total_subnet


    ipv4_total_subnet (optional, any, None)
      Field ipv4_total_subnet


    ipv4_entries (optional, any, None)
      Field ipv4_entries


    ipv4_total_single_ip (optional, any, None)
      Field ipv4_total_single_ip


    dns_total_entries (optional, any, None)
      Field dns_total_entries


    ipv6_total_single_ip (optional, any, None)
      Field ipv6_total_single_ip


    ac_total_entries (optional, any, None)
      Field ac_total_entries


    user_tag (optional, any, None)
      Field user_tag



  ansible_username (True, any, None)
    Username for AXAPI authentication


  ntype (False, any, None)
    'ac'= Make class-list type Aho-Corasick; 'dns'= Make class-list type DNS; 'ipv4'= Make class-list type IPv4; 'ipv6'= Make class-list type IPv6; 'string'= Make class-list type String; 'string-case-insensitive'= Make class-list type String-case-insensitive. Case insensitive is applied to key string;


  file (False, any, None)
    Create/Edit a class-list stored as a file


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ipv4_list (False, any, None)
    Field ipv4_list


    lid (optional, any, None)
      Use Limit ID defined in template (Specify LID index)


    shared_partition_glid (optional, any, None)
      Reference a glid from shared partition


    lsn_lid (optional, any, None)
      LSN Limit ID (LID index)


    glid (optional, any, None)
      Use global Limit ID (Specify global LID index)


    lsn_radius_profile (optional, any, None)
      LSN RADIUS Profile Index


    age (optional, any, None)
      Specify age in minutes


    ipv4addr (optional, any, None)
      Specify IP address


    glid_shared (optional, any, None)
      Use global Limit ID



  uuid (False, any, None)
    uuid of the object


  str_list (False, any, None)
    Field str_list


    str_lid (optional, any, None)
      LID index


    str (optional, any, None)
      Specify key string


    str_glid_shared (optional, any, None)
      Use global Limit ID


    str_glid (optional, any, None)
      Global LID index


    str_glid_dummy (optional, any, None)
      Use global Limit ID


    value_str (optional, any, None)
      Specify value string


    shared_partition_str_glid (optional, any, None)
      Reference a glid from shared partition


    str_lid_dummy (optional, any, None)
      Use Limit ID defined in template



  ansible_port (True, any, None)
    Port for AXAPI authentication


  ipv6_list (False, any, None)
    Field ipv6_list


    ipv6_addr (optional, any, None)
      Specify IPv6 host or subnet


    v6_lsn_radius_profile (optional, any, None)
      LSN RADIUS Profile Index


    v6_glid (optional, any, None)
      Use global Limit ID (Specify global LID index)


    v6_lid (optional, any, None)
      Use Limit ID defined in template (Specify LID index)


    v6_glid_shared (optional, any, None)
      Use global Limit ID


    v6_lsn_lid (optional, any, None)
      LSN Limit ID (LID index)


    shared_partition_v6_glid (optional, any, None)
      Reference a glid from shared partition


    v6_age (optional, any, None)
      Specify age in minutes



  ac_list (False, any, None)
    Field ac_list


    ac_key_string (optional, any, None)
      Specify key string


    ac_match_type (optional, any, None)
      'contains'= String contains another string; 'ends-with'= String ends with another string; 'equals'= String equals another string; 'starts-with'= String starts with another string;


    ac_value (optional, any, None)
      Specify value string



  name (True, any, None)
    Specify name of the class list


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  dns (False, any, None)
    Field dns


    dns_match_type (optional, any, None)
      'contains'= Domain contains another string; 'ends-with'= Domain ends with another string; 'starts-with'= Domain starts-with another string;


    dns_match_string (optional, any, None)
      Domain name


    dns_lid (optional, any, None)
      Use Limit ID defined in template (Specify LID index)


    shared_partition_dns_glid (optional, any, None)
      Reference a glid from shared partition


    dns_glid_shared (optional, any, None)
      Use global Limit ID


    dns_glid (optional, any, None)
      Use global Limit ID (Specify global LID index)



  user_tag (False, any, None)
    Customized tag









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

