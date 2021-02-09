.. _a10_vpn_ipsec_module:


a10_vpn_ipsec -- Configures A10 vpn.ipsec
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IPsec settings






Parameters
----------

  oper (False, any, None)
    Field oper


    Lifebytes (optional, any, None)
      Field Lifebytes


    Remote_SPI (optional, any, None)
      Field Remote_SPI


    Local_IP (optional, any, None)
      Field Local_IP


    DH_Group (optional, any, None)
      Field DH_Group


    NAT_Traversal (optional, any, None)
      Field NAT_Traversal


    Peer_IP (optional, any, None)
      Field Peer_IP


    Encryption_Algorithm (optional, any, None)
      Field Encryption_Algorithm


    Mode (optional, any, None)
      Field Mode


    Local_SPI (optional, any, None)
      Field Local_SPI


    Status (optional, any, None)
      Field Status


    Protocol (optional, any, None)
      Field Protocol


    name (optional, any, None)
      IPsec name


    SA_Index (optional, any, None)
      Field SA_Index


    Anti_Replay (optional, any, None)
      Field Anti_Replay


    Hash_Algorithm (optional, any, None)
      Field Hash_Algorithm


    Lifetime (optional, any, None)
      Field Lifetime



  ansible_username (True, any, None)
    Username for AXAPI authentication


  sequence_number_disable (False, any, None)
    Do not use incremental sequence number in the ESP header


  traffic_selector (False, any, None)
    Field traffic_selector


    ipv4 (optional, any, None)
      Field ipv4


    ipv6 (optional, any, None)
      Field ipv6



  enc_cfg (False, any, None)
    Field enc_cfg


    priority (optional, any, None)
      Prioritizes (1-10) security protocol, least value has highest priority


    encryption (optional, any, None)
      'des'= Data Encryption Standard algorithm; '3des'= Triple Data Encryption Standard algorithm; 'aes-128'= Advanced Encryption Standard algorithm CBC Mode(key size= 128 bits); 'aes-192'= Advanced Encryption Standard algorithm CBC Mode(key size= 192 bits); 'aes-256'= Advanced Encryption Standard algorithm CBC Mode(key size= 256 bits); 'aes-gcm-128'= Advanced Encryption Standard algorithm Galois/Counter Mode(key size= 128 bits, ICV size= 16 bytes); 'aes-gcm-192'= Advanced Encryption Standard algorithm Galois/Counter Mode(key size= 192 bits, ICV size= 16 bytes); 'aes-gcm-256'= Advanced Encryption Standard algorithm Galois/Counter Mode(key size= 256 bits, ICV size= 16 bytes); 'null'= No encryption algorithm;


    gcm_priority (optional, any, None)
      Prioritizes (1-10) security protocol, least value has highest priority


    hash (optional, any, None)
      'md5'= MD5 Dessage-Digest Algorithm; 'sha1'= Secure Hash Algorithm 1; 'sha256'= Secure Hash Algorithm 256; 'sha384'= Secure Hash Algorithm 384; 'sha512'= Secure Hash Algorithm 512; 'null'= No hash algorithm;



  anti_replay_window (False, any, None)
    '0'= Disable Anti-Replay Window Check; '32'= Window size of 32; '64'= Window size of 64; '128'= Window size of 128; '256'= Window size of 256; '512'= Window size of 512; '1024'= Window size of 1024;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  lifetime (False, any, None)
    IPsec SA age in seconds


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  name (True, any, None)
    IPsec name


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'packets-encrypted'= Encrypted Packets; 'packets-decrypted'= Decrypted Packets; 'anti-replay-num'= Anti-Replay Failure; 'rekey-num'= Rekey Times; 'packets-err-inactive'= Inactive Error; 'packets-err-encryption'= Encryption Error; 'packets-err-pad-check'= Pad Check Error; 'packets-err-pkt- sanity'= Packets Sanity Error; 'packets-err-icv-check'= ICV Check Error; 'packets-err-lifetime-lifebytes'= Lifetime Lifebytes Error; 'bytes-encrypted'= Encrypted Bytes; 'bytes-decrypted'= Decrypted Bytes; 'prefrag-success'= Pre- frag Success; 'prefrag-error'= Pre-frag Error; 'cavium-bytes-encrypted'= CAVIUM Encrypted Bytes; 'cavium-bytes-decrypted'= CAVIUM Decrypted Bytes; 'cavium- packets-encrypted'= CAVIUM Encrypted Packets; 'cavium-packets-decrypted'= CAVIUM Decrypted Packets; 'tunnel-intf-down'= Packet dropped= Tunnel Interface Down; 'pkt-fail-prep-to-send'= Packet dropped= Failed in prepare to send; 'no- next-hop'= Packet dropped= No next hop; 'invalid-tunnel-id'= Packet dropped= Invalid tunnel ID; 'no-tunnel-found'= Packet dropped= No tunnel found; 'pkt- fail-to-send'= Packet dropped= Failed to send; 'frag-after-encap-frag-packets'= Frag-after-encap Fragment Generated; 'frag-received'= Fragment Received; 'sequence-num'= Sequence Number; 'sequence-num-rollover'= Sequence Number Rollover; 'packets-err-nh-check'= Next Header Check Error;



  lifebytes (False, any, None)
    IPsec SA age in megabytes (0 indicates unlimited bytes)


  stats (False, any, None)
    Field stats


    anti_replay_num (optional, any, None)
      Anti-Replay Failure


    rekey_num (optional, any, None)
      Rekey Times


    no_next_hop (optional, any, None)
      Packet dropped= No next hop


    sequence_num (optional, any, None)
      Sequence Number


    packets_err_nh_check (optional, any, None)
      Next Header Check Error


    prefrag_error (optional, any, None)
      Pre-frag Error


    pkt_fail_prep_to_send (optional, any, None)
      Packet dropped= Failed in prepare to send


    packets_err_lifetime_lifebytes (optional, any, None)
      Lifetime Lifebytes Error


    cavium_bytes_decrypted (optional, any, None)
      CAVIUM Decrypted Bytes


    frag_after_encap_frag_packets (optional, any, None)
      Frag-after-encap Fragment Generated


    bytes_decrypted (optional, any, None)
      Decrypted Bytes


    packets_err_icv_check (optional, any, None)
      ICV Check Error


    packets_err_pad_check (optional, any, None)
      Pad Check Error


    cavium_packets_decrypted (optional, any, None)
      CAVIUM Decrypted Packets


    packets_encrypted (optional, any, None)
      Encrypted Packets


    bytes_encrypted (optional, any, None)
      Encrypted Bytes


    pkt_fail_to_send (optional, any, None)
      Packet dropped= Failed to send


    packets_err_pkt_sanity (optional, any, None)
      Packets Sanity Error


    sequence_num_rollover (optional, any, None)
      Sequence Number Rollover


    tunnel_intf_down (optional, any, None)
      Packet dropped= Tunnel Interface Down


    invalid_tunnel_id (optional, any, None)
      Packet dropped= Invalid tunnel ID


    name (optional, any, None)
      IPsec name


    cavium_bytes_encrypted (optional, any, None)
      CAVIUM Encrypted Bytes


    prefrag_success (optional, any, None)
      Pre-frag Success


    cavium_packets_encrypted (optional, any, None)
      CAVIUM Encrypted Packets


    packets_decrypted (optional, any, None)
      Decrypted Packets


    no_tunnel_found (optional, any, None)
      Packet dropped= No tunnel found


    frag_received (optional, any, None)
      Fragment Received


    packets_err_encryption (optional, any, None)
      Encryption Error


    packets_err_inactive (optional, any, None)
      Inactive Error



  uuid (False, any, None)
    uuid of the object


  proto (False, any, None)
    'esp'= Encapsulating security protocol (Default);


  dh_group (False, any, None)
    '0'= Diffie-Hellman group 0 (Default); '1'= Diffie-Hellman group 1 - 768-bits; '2'= Diffie-Hellman group 2 - 1024-bits; '5'= Diffie-Hellman group 5 - 1536-bits; '14'= Diffie-Hellman group 14 - 2048-bits; '15'= Diffie-Hellman group 15 - 3072-bits; '16'= Diffie-Hellman group 16 - 4096-bits; '18'= Diffie- Hellman group 18 - 8192-bits; '19'= Diffie-Hellman group 19 - 256-bit Elliptic Curve; '20'= Diffie-Hellman group 20 - 384-bit Elliptic Curve;


  ansible_password (True, any, None)
    Password for AXAPI authentication


  up (False, any, None)
    Initiates SA negotiation to bring the IPsec connection up


  bind_tunnel (False, any, None)
    Field bind_tunnel


    tunnel (optional, any, None)
      Tunnel interface index


    next_hop_v6 (optional, any, None)
      IPsec Next Hop IPv6 Address


    next_hop (optional, any, None)
      IPsec Next Hop IP Address


    uuid (optional, any, None)
      uuid of the object



  ike_gateway (False, any, None)
    Gateway to use for IPsec SA


  state (True, any, None)
    State of the object to be created.


  mode (False, any, None)
    'tunnel'= Encapsulating the packet in IPsec tunnel mode (Default);


  user_tag (False, any, None)
    Customized tag


  ansible_port (True, any, None)
    Port for AXAPI authentication









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

