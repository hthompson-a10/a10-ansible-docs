.. _a10_cgnv6_lsn_lid_module:


a10_cgnv6_lsn_lid -- Configures A10 cgnv6.lsn-lid
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create an LSN Lid






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  lsn_rule_list (False, any, None)
    Field lsn_rule_list


    destination (optional, any, None)
      Apply LSN Rule-List on Destination (LSN Rule-List Name)



  source_nat_pool (False, any, None)
    Field source_nat_pool


    pool_name (optional, any, None)
      Source NAT Pool or Pool-Group


    shared (optional, any, None)
      Use a shared source NAT pool or pool-group



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  extended_user_quota (False, any, None)
    Field extended_user_quota


    udp (optional, any, None)
      Field udp


    tcp (optional, any, None)
      Field tcp



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  conn_rate_limit (False, any, None)
    Field conn_rate_limit


    conn_rate_limit_val (optional, any, None)
      Maximum connections per second (Default= No limit)



  name (False, any, None)
    LSN Lid Name


  ansible_password (True, any, None)
    Password for AXAPI authentication


  respond_to_user_mac (False, any, None)
    Use the user's source MAC for the next hop rather than the routing table (default= off)


  ds_lite (False, any, None)
    Field ds_lite


    inside_src_permit_list (optional, any, None)
      Class-List of IPv4 addresses permitted (Class-list to match for DS-Lite)



  state (True, any, None)
    State of the object to be created.


  user_quota_prefix_length (False, any, None)
    NAT64/DS-Lite user quota prefix length (Prefix Length (Default= Uses the global NAT64/DS-Lite configured value))


  override (False, any, None)
    'none'= Apply source NAT if configured (default); 'drop'= Drop packets that match this LSN lid; 'pass-through'= Layer-3 route packets that match this LSN lid and do not apply source NAT;


  lid_number (True, any, None)
    LSN Lid


  user_tag (False, any, None)
    Customized tag


  user_quota (False, any, None)
    Field user_quota


    quota_tcp (optional, any, None)
      Field quota_tcp


    icmp (optional, any, None)
      User Quota for ICMP identifiers (NAT port quota per user (default= not configured))


    session (optional, any, None)
      User Quota for number of data sessions


    quota_udp (optional, any, None)
      Field quota_udp










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

