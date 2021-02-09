.. _a10_system_bfd_module:


a10_system_bfd -- Configures A10 system.bfd
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

BFD Statistics






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'ip_checksum_error'= IP packet checksum errors; 'udp_checksum_error'= UDP packet checksum errors; 'session_not_found'= Session not found; 'multihop_mismatch'= Multihop session or packet mismatch; 'version_mismatch'= BFD version mismatch; 'length_too_small'= Packets too small; 'data_is_short'= Packet data length too short; 'invalid_detect_mult'= Invalid detect multiplier; 'invalid_multipoint'= Invalid multipoint setting; 'invalid_my_disc'= Invalid my descriptor; 'invalid_ttl'= Invalid TTL; 'auth_length_invalid'= Invalid authentication length; 'auth_mismatch'= Authentication mismatch; 'auth_type_mismatch'= Authentication type mismatch; 'auth_key_id_mismatch'= Authentication key-id mismatch; 'auth_key_mismatch'= Authentication key mismatch; 'auth_seqnum_invalid'= Invalid authentication sequence number; 'auth_failed'= Authentication failures; 'local_state_admin_down'= Local admin down session state; 'dest_unreachable'= Destination unreachable; 'no_ipv6_enable'= No IPv6 enable; 'other_error'= Other errors;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    invalid_detect_mult (optional, any, None)
      Invalid detect multiplier


    no_ipv6_enable (optional, any, None)
      No IPv6 enable


    auth_length_invalid (optional, any, None)
      Invalid authentication length


    auth_key_mismatch (optional, any, None)
      Authentication key mismatch


    length_too_small (optional, any, None)
      Packets too small


    auth_mismatch (optional, any, None)
      Authentication mismatch


    invalid_ttl (optional, any, None)
      Invalid TTL


    invalid_multipoint (optional, any, None)
      Invalid multipoint setting


    session_not_found (optional, any, None)
      Session not found


    local_state_admin_down (optional, any, None)
      Local admin down session state


    ip_checksum_error (optional, any, None)
      IP packet checksum errors


    version_mismatch (optional, any, None)
      BFD version mismatch


    auth_key_id_mismatch (optional, any, None)
      Authentication key-id mismatch


    udp_checksum_error (optional, any, None)
      UDP packet checksum errors


    other_error (optional, any, None)
      Other errors


    invalid_my_disc (optional, any, None)
      Invalid my descriptor


    multihop_mismatch (optional, any, None)
      Multihop session or packet mismatch


    auth_failed (optional, any, None)
      Authentication failures


    auth_type_mismatch (optional, any, None)
      Authentication type mismatch


    data_is_short (optional, any, None)
      Packet data length too short


    auth_seqnum_invalid (optional, any, None)
      Invalid authentication sequence number


    dest_unreachable (optional, any, None)
      Destination unreachable



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

