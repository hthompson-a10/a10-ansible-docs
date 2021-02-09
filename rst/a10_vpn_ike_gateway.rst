.. _a10_vpn_ike_gateway_module:


a10_vpn_ike_gateway -- Configures A10 vpn.ike-gateway
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IKE-gateway settings






Parameters
----------

  oper (False, any, None)
    Field oper


    Status (optional, any, None)
      Field Status


    Hash (optional, any, None)
      Field Hash


    Initiator_SPI (optional, any, None)
      Field Initiator_SPI


    Local_IP (optional, any, None)
      Field Local_IP


    Encryption (optional, any, None)
      Field Encryption


    NAT_Traversal (optional, any, None)
      Field NAT_Traversal


    Responder_SPI (optional, any, None)
      Field Responder_SPI


    Lifetime (optional, any, None)
      Field Lifetime


    Remote_IP (optional, any, None)
      Field Remote_IP


    name (optional, any, None)
      IKE-gateway name



  remote_id (False, any, None)
    Remote Gateway Identity


  ansible_username (True, any, None)
    Username for AXAPI authentication


  local_cert (False, any, None)
    Field local_cert


    local_cert_name (optional, any, None)
      Certificate File Name



  remote_ca_cert (False, any, None)
    Field remote_ca_cert


    remote_cert_name (optional, any, None)
      Remote CA certificate DN (C=, ST=, L=, O=, CN=) without emailAddress



  lifetime (False, any, None)
    IKE SA age in seconds


  ike_version (False, any, None)
    'v1'= IKEv1 key exchange; 'v2'= IKEv2 key exchange;


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'v2-init-rekey'= Initiate Rekey; 'v2-rsp-rekey'= Respond Rekey; 'v2-child-sa-rekey'= Child SA Rekey; 'v2-in-invalid'= Incoming Invalid; 'v2-in- invalid-spi'= Incoming Invalid SPI; 'v2-in-init-req'= Incoming Init Request; 'v2-in-init-rsp'= Incoming Init Response; 'v2-out-init-req'= Outgoing Init Request; 'v2-out-init-rsp'= Outgoing Init Response; 'v2-in-auth-req'= Incoming Auth Request; 'v2-in-auth-rsp'= Incoming Auth Response; 'v2-out-auth-req'= Outgoing Auth Request; 'v2-out-auth-rsp'= Outgoing Auth Response; 'v2-in- create-child-req'= Incoming Create Child Request; 'v2-in-create-child-rsp'= Incoming Create Child Response; 'v2-out-create-child-req'= Outgoing Create Child Request; 'v2-out-create-child-rsp'= Outgoing Create Child Response; 'v2-in-info-req'= Incoming Info Request; 'v2-in-info-rsp'= Incoming Info Response; 'v2-out-info-req'= Outgoing Info Request; 'v2-out-info-rsp'= Outgoing Info Response; 'v1-in-id-prot-req'= Incoming ID Protection Request; 'v1-in-id- prot-rsp'= Incoming ID Protection Response; 'v1-out-id-prot-req'= Outgoing ID Protection Request; 'v1-out-id-prot-rsp'= Outgoing ID Protection Response; 'v1-in-auth-only-req'= Incoming Auth Only Request; 'v1-in-auth-only-rsp'= Incoming Auth Only Response; 'v1-out-auth-only-req'= Outgoing Auth Only Request; 'v1-out-auth-only-rsp'= Outgoing Auth Only Response; 'v1-in- aggressive-req'= Incoming Aggressive Request; 'v1-in-aggressive-rsp'= Incoming Aggressive Response; 'v1-out-aggressive-req'= Outgoing Aggressive Request; 'v1-out-aggressive-rsp'= Outgoing Aggressive Response; 'v1-in-info-v1-req'= Incoming Info Request; 'v1-in-info-v1-rsp'= Incoming Info Response; 'v1-out- info-v1-req'= Outgoing Info Request; 'v1-out-info-v1-rsp'= Outgoing Info Response; 'v1-in-transaction-req'= Incoming Transaction Request; 'v1-in- transaction-rsp'= Incoming Transaction Response; 'v1-out-transaction-req'= Outgoing Transaction Request; 'v1-out-transaction-rsp'= Outgoing Transaction Response; 'v1-in-quick-mode-req'= Incoming Quick Mode Request; 'v1-in-quick- mode-rsp'= Incoming Quick Mode Response; 'v1-out-quick-mode-req'= Outgoing Quick Mode Request; 'v1-out-quick-mode-rsp'= Outgoing Quick Mode Response; 'v1-in-new-group-mode-req'= Incoming New Group Mode Request; 'v1-in-new-group- mode-rsp'= Incoming New Group Mode Response; 'v1-out-new-group-mode-req'= Outgoing New Group Mode Request; 'v1-out-new-group-mode-rsp'= Outgoing New Group Mode Response; 'v1-child-sa-invalid-spi'= Invalid SPI for Child SAs; 'v2-child-sa-invalid-spi'= Invalid SPI for Child SAs; 'ike-current-version'= IKE version;



  stats (False, any, None)
    Field stats


    v1_in_aggressive_req (optional, any, None)
      Incoming Aggressive Request


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


    ike_current_version (optional, any, None)
      IKE version


    v2_init_rekey (optional, any, None)
      Initiate Rekey


    v2_out_init_req (optional, any, None)
      Outgoing Init Request


    v1_out_transaction_req (optional, any, None)
      Outgoing Transaction Request


    v2_in_auth_rsp (optional, any, None)
      Incoming Auth Response


    v2_child_sa_invalid_spi (optional, any, None)
      Invalid SPI for Child SAs


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


    name (optional, any, None)
      IKE-gateway name


    v1_out_quick_mode_rsp (optional, any, None)
      Outgoing Quick Mode Response


    v1_in_new_group_mode_rsp (optional, any, None)
      Incoming New Group Mode Response


    v1_in_info_v1_rsp (optional, any, None)
      Incoming Info Response


    v1_child_sa_invalid_spi (optional, any, None)
      Invalid SPI for Child SAs


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


  dh_group (False, any, None)
    '1'= Diffie-Hellman group 1 - 768-bit(Default); '2'= Diffie-Hellman group 2 - 1024-bit; '5'= Diffie-Hellman group 5 - 1536-bit; '14'= Diffie-Hellman group 14 - 2048-bit; '15'= Diffie-Hellman group 15 - 3072-bit; '16'= Diffie-Hellman group 16 - 4096-bit; '18'= Diffie-Hellman group 18 - 8192-bit; '19'= Diffie- Hellman group 19 - 256-bit Elliptic Curve; '20'= Diffie-Hellman group 20 - 384-bit Elliptic Curve;


  vrid (False, any, None)
    Field vrid


    vrid_num (optional, any, None)
      Specify ha VRRP-A vrid



  auth_method (False, any, None)
    'preshare-key'= Authenticate the remote gateway using a pre-shared key (Default); 'rsa-signature'= Authenticate the remote gateway using an RSA certificate; 'ecdsa-signature'= Authenticate the remote gateway using an ECDSA certificate;


  state (True, any, None)
    State of the object to be created.


  local_id (False, any, None)
    Local Gateway Identity


  local_address (False, any, None)
    Field local_address


    local_ipv6 (optional, any, None)
      Ipv6 address


    local_ip (optional, any, None)
      Ipv4 address



  nat_traversal (False, any, None)
    Field nat_traversal


  remote_address (False, any, None)
    Field remote_address


    remote_ipv6 (optional, any, None)
      Ipv6 address


    dns (optional, any, None)
      Remote IP based on Domain name


    remote_ip (optional, any, None)
      Ipv4 address



  enc_cfg (False, any, None)
    Field enc_cfg


    priority (optional, any, None)
      Prioritizes (1-10) security protocol, least value has highest priority


    encryption (optional, any, None)
      'des'= Data Encryption Standard algorithm; '3des'= Triple Data Encryption Standard algorithm; 'aes-128'= Advanced Encryption Standard algorithm CBC Mode(key size= 128 bits); 'aes-192'= Advanced Encryption Standard algorithm CBC Mode(key size= 192 bits); 'aes-256'= Advanced Encryption Standard algorithm CBC Mode(key size= 256 bits); 'aes-gcm-128'= Advanced Encryption Standard algorithm Galois/Counter Mode(key size= 128 bits, ICV size= 16 bytes), only for IKEv2; 'aes-gcm-192'= Advanced Encryption Standard algorithm Galois/Counter Mode(key size= 192 bits, ICV size= 16 bytes), only for IKEv2; 'aes-gcm-256'= Advanced Encryption Standard algorithm Galois/Counter Mode(key size= 256 bits, ICV size= 16 bytes), only for IKEv2; 'null'= No encryption algorithm, only for IKEv2;


    gcm_priority (optional, any, None)
      Prioritizes (1-10) security protocol, least value has highest priority


    prf (optional, any, None)
      'md5'= MD5 Dessage-Digest Algorithm; 'sha1'= Secure Hash Algorithm 1; 'sha256'= Secure Hash Algorithm 256; 'sha384'= Secure Hash Algorithm 384; 'sha512'= Secure Hash Algorithm 512;


    hash (optional, any, None)
      'md5'= MD5 Dessage-Digest Algorithm; 'sha1'= Secure Hash Algorithm 1; 'sha256'= Secure Hash Algorithm 256; 'sha384'= Secure Hash Algorithm 384; 'sha512'= Secure Hash Algorithm 512;



  key (False, any, None)
    Private Key


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  preshare_key_value (False, any, None)
    pre-shared key


  name (True, any, None)
    IKE-gateway name


  ansible_password (True, any, None)
    Password for AXAPI authentication


  key_passphrase (False, any, None)
    Private Key Pass Phrase


  dpd (False, any, None)
    Field dpd


    interval (optional, any, None)
      Interval time in seconds


    retry (optional, any, None)
      Retry times



  mode (False, any, None)
    'main'= Negotiate Main mode (Default); 'aggressive'= Negotiate Aggressive mode;


  user_tag (False, any, None)
    Customized tag


  key_passphrase_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED key string)


  preshare_key_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED pre-shared key string)









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

