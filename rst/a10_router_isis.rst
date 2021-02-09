.. _a10_router_isis_module:


a10_router_isis -- Configures A10 router.isis
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Intermediate System - Intermediate System (IS-IS)






Parameters
----------

  set_overload_bit_cfg (False, any, None)
    Field set_overload_bit_cfg


    set_overload_bit (optional, any, None)
      Signal other touers not to use us in SPF


    suppress_cfg (optional, any, None)
      Field suppress_cfg


    on_startup (optional, any, None)
      Field on_startup



  ansible_username (True, any, None)
    Username for AXAPI authentication


  log_adjacency_changes_cfg (False, any, None)
    Field log_adjacency_changes_cfg


    state (optional, any, None)
      'detail'= Log changes in adjacency state; 'disable'= Disable logging;



  is_type (False, any, None)
    'level-1'= Act as a station router only; 'level-1-2'= Act as both a station router and an area router; 'level-2-only'= Act as an area router only;


  tag (True, any, None)
    ISO routing area tag


  area_password_cfg (False, any, None)
    Field area_password_cfg


    password (optional, any, None)
      Configure the authentication password for an area (Area password)


    authenticate (optional, any, None)
      Field authenticate



  lsp_gen_interval_list (False, any, None)
    Field lsp_gen_interval_list


    interval (optional, any, None)
      Minimum interval in seconds


    level (optional, any, None)
      'level-1'= Set interval for level 1 only; 'level-2'= Set interval for level 2 only;



  metric_style_list (False, any, None)
    Field metric_style_list


    ntype (optional, any, None)
      'narrow'= Use old style of TLVs with narrow metric; 'wide'= Use new style of TLVs to carry wider metric; 'transition'= Send and accept both styles of TLVs during transition; 'narrow-transition'= Send old style of TLVs with narrow metric with accepting both styles of TLVs; 'wide-transition'= Send new style of TLVs to carry wider metric with accepting both styles of TLVs;


    level (optional, any, None)
      'level-1'= Level-1 only; 'level-1-2'= Level-1-2; 'level-2'= Level-2 only;



  uuid (False, any, None)
    uuid of the object


  bfd (False, any, None)
    'all-interfaces'= Enable BFD on all interfaces;


  max_lsp_lifetime (False, any, None)
    Set maximum LSP lifetime (Maximum LSP lifetime in seconds)


  authentication (False, any, None)
    Field authentication


    send_only_list (optional, any, None)
      Field send_only_list


    key_chain_list (optional, any, None)
      Field key_chain_list


    mode_list (optional, any, None)
      Field mode_list



  adjacency_check (False, any, None)
    Check ISIS neighbor protocol support


  state (True, any, None)
    State of the object to be created.


  spf_interval_exp_list (False, any, None)
    Field spf_interval_exp_list


    max (optional, any, None)
      Maximum Delay between receiving a change to SPF calculation in milliseconds


    min (optional, any, None)
      Minimum Delay between receiving a change to SPF calculation in milliseconds


    level (optional, any, None)
      'level-1'= Set interval for level 1 only; 'level-2'= Set interval for level 2 only;



  domain_password_cfg (False, any, None)
    Field domain_password_cfg


    password (optional, any, None)
      Set the authentication password for a routing domain (Routing domain password)


    authenticate (optional, any, None)
      Field authenticate



  net_list (False, any, None)
    Field net_list


    net (optional, any, None)
      A Network Entity Title for this process (XX.XXXX. ... .XXXX.XX  Network entity title (NET))



  lsp_refresh_interval (False, any, None)
    Set LSP refresh interval (LSP refresh time in seconds)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  default_information (False, any, None)
    'originate'= Distribute a default route;


  protocol_list (False, any, None)
    Field protocol_list


    protocol_topology (optional, any, None)
      Protocol Topology



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  address_family (False, any, None)
    Field address_family


    ipv6 (optional, any, None)
      Field ipv6



  distance_list (False, any, None)
    Field distance_list


    distance (optional, any, None)
      ISIS Administrative Distance (Distance value)


    System_ID (optional, any, None)
      System-ID in XXXX.XXXX.XXXX


    acl (optional, any, None)
      Access list name



  redistribute (False, any, None)
    Field redistribute


    vip_list (optional, any, None)
      Field vip_list


    isis (optional, any, None)
      Field isis


    redist_list (optional, any, None)
      Field redist_list


    uuid (optional, any, None)
      uuid of the object



  ignore_lsp_errors (False, any, None)
    Ignore LSPs with bad checksums


  ansible_password (True, any, None)
    Password for AXAPI authentication


  summary_address_list (False, any, None)
    Field summary_address_list


    prefix (optional, any, None)
      IP network prefix


    level (optional, any, None)
      'level-1'= Summarize into level-1 area; 'level-1-2'= Summarize into both area and sub-domain; 'level-2'= Summarize into level-2 sub-domain;



  passive_interface_list (False, any, None)
    Field passive_interface_list


    lif (optional, any, None)
      Logical interface (Lif interface number)


    ve (optional, any, None)
      Virtual ethernet interface (Virtual ethernet interface number)


    loopback (optional, any, None)
      Loopback interface (Port number)


    tunnel (optional, any, None)
      Tunnel interface (Tunnel interface number)


    ethernet (optional, any, None)
      Ethernet interface (Port number)


    trunk (optional, any, None)
      Trunk interface (Trunk interface number)



  ha_standby_extra_cost (False, any, None)
    Field ha_standby_extra_cost


    extra_cost (optional, any, None)
      The extra cost value


    group (optional, any, None)
      Group (Group ID)



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

