.. _a10_vpn_error_module:


a10_vpn_error -- Configures A10 vpn.error
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Error counters






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    bad_opcode (optional, any, None)
      Field bad_opcode


    bad_sg_write_len (optional, any, None)
      Field bad_sg_write_len


    ipv6_rh_length_error (optional, any, None)
      Field ipv6_rh_length_error


    ah_not_supported_with_gcm_gmac_sha2 (optional, any, None)
      Field ah_not_supported_with_gcm_gmac_sha2


    bad_auth_type (optional, any, None)
      Field bad_auth_type


    bad_gre_protocol (optional, any, None)
      Field bad_gre_protocol


    ipv6_outbound_rh_copy_addr_error (optional, any, None)
      Field ipv6_outbound_rh_copy_addr_error


    bad_ip_payload_type (optional, any, None)
      Field bad_ip_payload_type


    ipv6_extension_headers_too_big (optional, any, None)
      Field ipv6_extension_headers_too_big


    bad_encrypt_type (optional, any, None)
      Field bad_encrypt_type


    bad_checksum (optional, any, None)
      Field bad_checksum


    bad_gre_header (optional, any, None)
      Field bad_gre_header


    bad_ipsec_context (optional, any, None)
      Field bad_ipsec_context


    bad_min_frag_size_auth_sha384_512 (optional, any, None)
      Field bad_min_frag_size_auth_sha384_512


    bad_ipsec_padding (optional, any, None)
      Field bad_ipsec_padding


    bad_inline_data (optional, any, None)
      Field bad_inline_data


    dummy_payload (optional, any, None)
      Field dummy_payload


    bad_ip_version (optional, any, None)
      Field bad_ip_version


    bad_encrypt_type_ctr_gcm (optional, any, None)
      Field bad_encrypt_type_ctr_gcm


    bad_fragment_size (optional, any, None)
      Field bad_fragment_size


    bad_esp_next_header (optional, any, None)
      Field bad_esp_next_header


    ipv6_hop_by_hop_error (optional, any, None)
      Field ipv6_hop_by_hop_error


    error_ipv6_decrypt_rh_segs_left_error (optional, any, None)
      Field error_ipv6_decrypt_rh_segs_left_error


    bad_ipsec_spi (optional, any, None)
      Field bad_ipsec_spi


    bad_ipsec_context_flag_mismatch (optional, any, None)
      Field bad_ipsec_context_flag_mismatch


    error_IPv6_extension_header_bad (optional, any, None)
      Field error_IPv6_extension_header_bad


    bad_ipsec_protocol (optional, any, None)
      Field bad_ipsec_protocol


    bad_frag_size_configuration (optional, any, None)
      Field bad_frag_size_configuration


    bad_ipsec_auth (optional, any, None)
      Field bad_ipsec_auth


    bad_ipcomp_configuration (optional, any, None)
      Field bad_ipcomp_configuration


    bad_len (optional, any, None)
      Field bad_len


    bad_ipsec_context_direction (optional, any, None)
      Field bad_ipsec_context_direction


    bad_ipsec_unknown (optional, any, None)
      Field bad_ipsec_unknown


    ipcomp_payload (optional, any, None)
      Field ipcomp_payload


    bad_srtp_auth_tag (optional, any, None)
      Field bad_srtp_auth_tag


    tfc_padding_with_prefrag_not_supported (optional, any, None)
      Field tfc_padding_with_prefrag_not_supported


    dsiv_incorrect_param (optional, any, None)
      Field dsiv_incorrect_param


    bad_selector_match (optional, any, None)
      Field bad_selector_match



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

