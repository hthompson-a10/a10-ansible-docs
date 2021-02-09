.. _a10_vpn_ike_stats_global_module:


a10_vpn_ike_stats_global -- Configures A10 vpn.ike-stats-global
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IKE-stats-global statistic






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'v2-init-rekey'= Initiate Rekey; 'v2-rsp-rekey'= Respond Rekey; 'v2-child-sa-rekey'= Child SA Rekey; 'v2-in-invalid'= Incoming Invalid; 'v2-in- invalid-spi'= Incoming Invalid SPI; 'v2-in-init-req'= Incoming Init Request; 'v2-in-init-rsp'= Incoming Init Response; 'v2-out-init-req'= Outgoing Init Request; 'v2-out-init-rsp'= Outgoing Init Response; 'v2-in-auth-req'= Incoming Auth Request; 'v2-in-auth-rsp'= Incoming Auth Response; 'v2-out-auth-req'= Outgoing Auth Request; 'v2-out-auth-rsp'= Outgoing Auth Response; 'v2-in- create-child-req'= Incoming Create Child Request; 'v2-in-create-child-rsp'= Incoming Create Child Response; 'v2-out-create-child-req'= Outgoing Create Child Request; 'v2-out-create-child-rsp'= Outgoing Create Child Response; 'v2-in-info-req'= Incoming Info Request; 'v2-in-info-rsp'= Incoming Info Response; 'v2-out-info-req'= Outgoing Info Request; 'v2-out-info-rsp'= Outgoing Info Response; 'v1-in-id-prot-req'= Incoming ID Protection Request; 'v1-in-id- prot-rsp'= Incoming ID Protection Response; 'v1-out-id-prot-req'= Outgoing ID Protection Request; 'v1-out-id-prot-rsp'= Outgoing ID Protection Response; 'v1-in-auth-only-req'= Incoming Auth Only Request; 'v1-in-auth-only-rsp'= Incoming Auth Only Response; 'v1-out-auth-only-req'= Outgoing Auth Only Request; 'v1-out-auth-only-rsp'= Outgoing Auth Only Response; 'v1-in- aggressive-req'= Incoming Aggressive Request; 'v1-in-aggressive-rsp'= Incoming Aggressive Response; 'v1-out-aggressive-req'= Outgoing Aggressive Request; 'v1-out-aggressive-rsp'= Outgoing Aggressive Response; 'v1-in-info-v1-req'= Incoming Info Request; 'v1-in-info-v1-rsp'= Incoming Info Response; 'v1-out- info-v1-req'= Outgoing Info Request; 'v1-out-info-v1-rsp'= Outgoing Info Response; 'v1-in-transaction-req'= Incoming Transaction Request; 'v1-in- transaction-rsp'= Incoming Transaction Response; 'v1-out-transaction-req'= Outgoing Transaction Request; 'v1-out-transaction-rsp'= Outgoing Transaction Response; 'v1-in-quick-mode-req'= Incoming Quick Mode Request; 'v1-in-quick- mode-rsp'= Incoming Quick Mode Response; 'v1-out-quick-mode-req'= Outgoing Quick Mode Request; 'v1-out-quick-mode-rsp'= Outgoing Quick Mode Response; 'v1-in-new-group-mode-req'= Incoming New Group Mode Request; 'v1-in-new-group- mode-rsp'= Incoming New Group Mode Response; 'v1-out-new-group-mode-req'= Outgoing New Group Mode Request; 'v1-out-new-group-mode-rsp'= Outgoing New Group Mode Response;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    v2_in_invalid_spi (optional, any, None)
      Incoming Invalid SPI


    v1_in_quick_mode_req (optional, any, None)
      Incoming Quick Mode Request


    v1_in_new_group_mode_req (optional, any, None)
      Incoming New Group Mode Request


    v2_in_auth_req (optional, any, None)
      Incoming Auth Request


    v2_out_info_rsp (optional, any, None)
      Outgoing Info Response


    v2_in_invalid (optional, any, None)
      Incoming Invalid


    v2_out_auth_req (optional, any, None)
      Outgoing Auth Request


    v1_in_aggressive_rsp (optional, any, None)
      Incoming Aggressive Response


    v1_out_id_prot_req (optional, any, None)
      Outgoing ID Protection Request


    v2_init_rekey (optional, any, None)
      Initiate Rekey


    v2_out_init_req (optional, any, None)
      Outgoing Init Request


    v1_out_transaction_req (optional, any, None)
      Outgoing Transaction Request


    v2_in_auth_rsp (optional, any, None)
      Incoming Auth Response


    v1_in_auth_only_rsp (optional, any, None)
      Incoming Auth Only Response


    v2_in_create_child_req (optional, any, None)
      Incoming Create Child Request


    v2_out_info_req (optional, any, None)
      Outgoing Info Request


    v2_in_init_rsp (optional, any, None)
      Incoming Init Response


    v1_out_info_v1_req (optional, any, None)
      Outgoing Info Request


    v1_out_new_group_mode_rsp (optional, any, None)
      Outgoing New Group Mode Response


    v1_in_id_prot_req (optional, any, None)
      Incoming ID Protection Request


    v2_child_sa_rekey (optional, any, None)
      Child SA Rekey


    v2_in_info_req (optional, any, None)
      Incoming Info Request


    v2_out_auth_rsp (optional, any, None)
      Outgoing Auth Response


    v1_in_id_prot_rsp (optional, any, None)
      Incoming ID Protection Response


    v1_out_aggressive_req (optional, any, None)
      Outgoing Aggressive Request


    v2_in_create_child_rsp (optional, any, None)
      Incoming Create Child Response


    v1_out_info_v1_rsp (optional, any, None)
      Outgoing Info Response


    v1_out_new_group_mode_req (optional, any, None)
      Outgoing New Group Mode Request


    v1_in_info_v1_req (optional, any, None)
      Incoming Info Request


    v1_out_aggressive_rsp (optional, any, None)
      Outgoing Aggressive Response


    v2_out_init_rsp (optional, any, None)
      Outgoing Init Response


    v1_out_auth_only_req (optional, any, None)
      Outgoing Auth Only Request


    v1_out_id_prot_rsp (optional, any, None)
      Outgoing ID Protection Response


    v1_in_auth_only_req (optional, any, None)
      Incoming Auth Only Request


    v1_out_quick_mode_req (optional, any, None)
      Outgoing Quick Mode Request


    v1_out_transaction_rsp (optional, any, None)
      Outgoing Transaction Response


    v2_out_create_child_rsp (optional, any, None)
      Outgoing Create Child Response


    v1_in_aggressive_req (optional, any, None)
      Incoming Aggressive Request


    v1_out_quick_mode_rsp (optional, any, None)
      Outgoing Quick Mode Response


    v1_in_new_group_mode_rsp (optional, any, None)
      Incoming New Group Mode Response


    v1_in_info_v1_rsp (optional, any, None)
      Incoming Info Response


    v2_out_create_child_req (optional, any, None)
      Outgoing Create Child Request


    v1_in_transaction_rsp (optional, any, None)
      Incoming Transaction Response


    v2_in_info_rsp (optional, any, None)
      Incoming Info Response


    v1_out_auth_only_rsp (optional, any, None)
      Outgoing Auth Only Response


    v1_in_transaction_req (optional, any, None)
      Incoming Transaction Request


    v2_in_init_req (optional, any, None)
      Incoming Init Request


    v1_in_quick_mode_rsp (optional, any, None)
      Incoming Quick Mode Response


    v2_rsp_rekey (optional, any, None)
      Respond Rekey



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

