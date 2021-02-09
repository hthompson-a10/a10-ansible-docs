.. _a10_vpn_module:


a10_vpn -- Configures A10 vpn
=============================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

VPN Commands






Parameters
----------

  oper (False, any, None)
    Field oper


    Crypto_mem (optional, any, None)
      Field Crypto_mem


    ike_gateway_list (optional, any, None)
      Field ike_gateway_list


    Crypto_cores_assigned_to_IPsec (optional, any, None)
      Field Crypto_cores_assigned_to_IPsec


    IKE_Gateway_total (optional, any, None)
      Field IKE_Gateway_total


    all_partition_list (optional, any, None)
      Field all_partition_list


    Num_hardware_devices (optional, any, None)
      Field Num_hardware_devices


    IPsec_mode (optional, any, None)
      Field IPsec_mode


    ocsp (optional, any, None)
      Field ocsp


    specific_partition (optional, any, None)
      Field specific_partition


    IKE_SA_total (optional, any, None)
      Field IKE_SA_total


    log (optional, any, None)
      Field log


    default (optional, any, None)
      Field default


    IPsec_total (optional, any, None)
      Field IPsec_total


    Crypto_cores_total (optional, any, None)
      Field Crypto_cores_total


    ipsec_list (optional, any, None)
      Field ipsec_list


    crl (optional, any, None)
      Field crl


    shared (optional, any, None)
      Field shared


    all_partitions (optional, any, None)
      Field all_partitions


    IPsec_SA_total (optional, any, None)
      Field IPsec_SA_total


    ipsec_sa_by_gw (optional, any, None)
      Field ipsec_sa_by_gw


    errordump (optional, any, None)
      Field errordump



  revocation_list (False, any, None)
    Field revocation_list


    uuid (optional, any, None)
      uuid of the object


    name (optional, any, None)
      Revocation name


    ca (optional, any, None)
      Certificate Authority file name


    user_tag (optional, any, None)
      Customized tag


    crl (optional, any, None)
      Field crl


    ocsp (optional, any, None)
      Field ocsp



  asymmetric_flow_support (False, any, None)
    Support asymmetric flows pass through IPsec tunnel


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ike_gateway_list (False, any, None)
    Field ike_gateway_list


    remote_id (optional, any, None)
      Remote Gateway Identity


    nat_traversal (optional, any, None)
      Field nat_traversal


    remote_address (optional, any, None)
      Field remote_address


    local_cert (optional, any, None)
      Field local_cert


    remote_ca_cert (optional, any, None)
      Field remote_ca_cert


    key (optional, any, None)
      Private Key


    lifetime (optional, any, None)
      IKE SA age in seconds


    auth_method (optional, any, None)
      'preshare-key'= Authenticate the remote gateway using a pre-shared key (Default); 'rsa-signature'= Authenticate the remote gateway using an RSA certificate; 'ecdsa-signature'= Authenticate the remote gateway using an ECDSA certificate;


    ike_version (optional, any, None)
      'v1'= IKEv1 key exchange; 'v2'= IKEv2 key exchange;


    sampling_enable (optional, any, None)
      Field sampling_enable


    dpd (optional, any, None)
      Field dpd


    preshare_key_value (optional, any, None)
      pre-shared key


    uuid (optional, any, None)
      uuid of the object


    dh_group (optional, any, None)
      '1'= Diffie-Hellman group 1 - 768-bit(Default); '2'= Diffie-Hellman group 2 - 1024-bit; '5'= Diffie-Hellman group 5 - 1536-bit; '14'= Diffie-Hellman group 14 - 2048-bit; '15'= Diffie-Hellman group 15 - 3072-bit; '16'= Diffie-Hellman group 16 - 4096-bit; '18'= Diffie-Hellman group 18 - 8192-bit; '19'= Diffie- Hellman group 19 - 256-bit Elliptic Curve; '20'= Diffie-Hellman group 20 - 384-bit Elliptic Curve;


    vrid (optional, any, None)
      Field vrid


    enc_cfg (optional, any, None)
      Field enc_cfg


    name (optional, any, None)
      IKE-gateway name


    key_passphrase (optional, any, None)
      Private Key Pass Phrase


    local_id (optional, any, None)
      Local Gateway Identity


    mode (optional, any, None)
      'main'= Negotiate Main mode (Default); 'aggressive'= Negotiate Aggressive mode;


    local_address (optional, any, None)
      Field local_address


    user_tag (optional, any, None)
      Customized tag


    key_passphrase_encrypted (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED key string)


    preshare_key_encrypted (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED pre-shared key string)



  stateful_mode (False, any, None)
    VPN module will work in stateful mode and create sessions


  tcp_mss_adjust_disable (False, any, None)
    Disable TCP MSS adjustment in SYN packet


  ike_sa_timeout (False, any, None)
    Timeout IKE-SA in connecting state in seconds (default 600s)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ike_stats_global (False, any, None)
    Field ike_stats_global


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ipsec_error_dump (False, any, None)
    Support record the error ipsec cavium information in dump file


  ocsp (False, any, None)
    Field ocsp


    uuid (optional, any, None)
      uuid of the object



  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'passthrough'= passthrough; 'ha-standby-drop'= ha-standby-drop;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  nat_traversal_flow_affinity (False, any, None)
    Choose IPsec UDP source port based on port of inner flow (only for A10 to A10)


  stats (False, any, None)
    Field stats


    ha_standby_drop (optional, any, None)
      Field ha_standby_drop


    ipsec_list (optional, any, None)
      Field ipsec_list


    ike_stats_global (optional, any, None)
      Field ike_stats_global


    ike_gateway_list (optional, any, None)
      Field ike_gateway_list


    error (optional, any, None)
      Field error


    passthrough (optional, any, None)
      Field passthrough



  log (False, any, None)
    Field log


    uuid (optional, any, None)
      uuid of the object



  jumbo_fragment (False, any, None)
    Support IKE jumbo fragment packet


  crl (False, any, None)
    Field crl


    uuid (optional, any, None)
      uuid of the object



  default (False, any, None)
    Field default


    uuid (optional, any, None)
      uuid of the object



  uuid (False, any, None)
    uuid of the object


  state (True, any, None)
    State of the object to be created.


  ipsec_list (False, any, None)
    Field ipsec_list


    anti_replay_window (optional, any, None)
      '0'= Disable Anti-Replay Window Check; '32'= Window size of 32; '64'= Window size of 64; '128'= Window size of 128; '256'= Window size of 256; '512'= Window size of 512; '1024'= Window size of 1024;


    traffic_selector (optional, any, None)
      Field traffic_selector


    enc_cfg (optional, any, None)
      Field enc_cfg


    sequence_number_disable (optional, any, None)
      Do not use incremental sequence number in the ESP header


    lifetime (optional, any, None)
      IPsec SA age in seconds


    uuid (optional, any, None)
      uuid of the object


    sampling_enable (optional, any, None)
      Field sampling_enable


    lifebytes (optional, any, None)
      IPsec SA age in megabytes (0 indicates unlimited bytes)


    name (optional, any, None)
      IPsec name


    proto (optional, any, None)
      'esp'= Encapsulating security protocol (Default);


    dh_group (optional, any, None)
      '0'= Diffie-Hellman group 0 (Default); '1'= Diffie-Hellman group 1 - 768-bits; '2'= Diffie-Hellman group 2 - 1024-bits; '5'= Diffie-Hellman group 5 - 1536-bits; '14'= Diffie-Hellman group 14 - 2048-bits; '15'= Diffie-Hellman group 15 - 3072-bits; '16'= Diffie-Hellman group 16 - 4096-bits; '18'= Diffie- Hellman group 18 - 8192-bits; '19'= Diffie-Hellman group 19 - 256-bit Elliptic Curve; '20'= Diffie-Hellman group 20 - 384-bit Elliptic Curve;


    up (optional, any, None)
      Initiates SA negotiation to bring the IPsec connection up


    ike_gateway (optional, any, None)
      Gateway to use for IPsec SA


    mode (optional, any, None)
      'tunnel'= Encapsulating the packet in IPsec tunnel mode (Default);


    user_tag (optional, any, None)
      Customized tag


    bind_tunnel (optional, any, None)
      Field bind_tunnel



  errordump (False, any, None)
    Field errordump


    uuid (optional, any, None)
      uuid of the object



  error (False, any, None)
    Field error


    uuid (optional, any, None)
      uuid of the object



  fragment_after_encap (False, any, None)
    Fragment after adding IPsec headers


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ipsec_sa_by_gw (False, any, None)
    Field ipsec_sa_by_gw


    uuid (optional, any, None)
      uuid of the object










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

