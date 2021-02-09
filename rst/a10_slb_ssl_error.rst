.. _a10_slb_ssl_error_module:


a10_slb_ssl_error -- Configures A10 slb.ssl-error
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Error






Parameters
----------

  oper (False, any, None)
    Field oper


    dh_public_value_length_is_wrong (optional, any, None)
      dh public value length is wrong


    missing_rsa_signing_cert (optional, any, None)
      missing rsa signing cert


    ssl_ctx_has_no_default_ssl_version (optional, any, None)
      ssl ctx has no default ssl version


    problems_mapping_cipher_functions (optional, any, None)
      problems mapping cipher functions


    required_cipher_missing (optional, any, None)
      required cipher missing


    public_key_encrypt_error (optional, any, None)
      public key encrypt error


    bad_data_returned_by_callback (optional, any, None)
      bad data returned by callback


    missing_rsa_certificate (optional, any, None)
      missing rsa certificate


    connection_type_not_set (optional, any, None)
      connection type not set


    krb5_server_tkt_not_yet_valid (optional, any, None)
      krb5 server tkt not yet valid


    key_arg_too_long (optional, any, None)
      key arg too long


    no_cipher_match (optional, any, None)
      no cipher match


    krb5_client_init (optional, any, None)
      krb5 client init


    peer_error (optional, any, None)
      peer error


    error_generating_tmp_rsa_key (optional, any, None)
      error generating tmp rsa key


    tls_rsa_encrypted_value_length_is_wrong (optional, any, None)
      tls rsa encrypted value length is wrong


    invalid_command (optional, any, None)
      invalid command


    unknown_protocol (optional, any, None)
      unknown protocol


    missing_export_tmp_dh_key (optional, any, None)
      missing export tmp dh key


    tlsv1_alert_internal_error (optional, any, None)
      tlsv1 alert internal error


    ssl_session_id_conflict (optional, any, None)
      ssl session id conflict


    attempt_to_reuse_sess_in_diff_context (optional, any, None)
      attempt to reuse sess in diff context


    bad_length (optional, any, None)
      bad length


    cipher_or_hash_unavailable (optional, any, None)
      cipher or hash unavailable


    reuse_cert_type_not_zero (optional, any, None)
      reuse cert type not zero


    data_between_ccs_and_finished (optional, any, None)
      data between ccs and finished


    public_key_is_not_rsa (optional, any, None)
      public key is not rsa


    tls_invalid_ecpointformat_list (optional, any, None)
      tls invalid ecpointformat list


    uninitialized (optional, any, None)
      uninitialized


    unable_to_find_ssl_method (optional, any, None)
      unable to find ssl method


    ca_dn_length_mismatch (optional, any, None)
      ca dn length mismatch


    krb5_server_tkt_expired (optional, any, None)
      krb5 server tkt expired


    cipher_table_src_error (optional, any, None)
      cipher table src error


    compressed_length_too_long (optional, any, None)
      compressed length too long


    ssl2_connection_id_too_long (optional, any, None)
      ssl2 connection id too long


    ca_dn_too_long (optional, any, None)
      ca dn too long


    length_mismatch (optional, any, None)
      length mismatch


    cert_length_mismatch (optional, any, None)
      cert length mismatch


    unknown_pkey_type (optional, any, None)
      unknown pkey type


    bad_ssl_filetype (optional, any, None)
      bad ssl filetype


    mast_key_too_long (optional, any, None)
      mast key too long


    sslv3_alert_unexpected_msg (optional, any, None)
      sslv3 alert unexpected msg


    missing_verify_message (optional, any, None)
      missing verify message


    no_method_specified (optional, any, None)
      no method specified


    unable_to_find_dh_parameters (optional, any, None)
      unable to find dh parameters


    unknown_key_exchange_type (optional, any, None)
      unknown key exchange type


    bad_ssl_session_id_length (optional, any, None)
      bad ssl session id length


    invalid_trust (optional, any, None)
      invalid trust


    unknown_certificate_type (optional, any, None)
      unknown certificate type


    packet_length_too_long (optional, any, None)
      packet length too long


    bad_message_type (optional, any, None)
      bad message type


    tlsv1_alert_decrypt_error (optional, any, None)
      tlsv1 alert decrypt error


    missing_tmp_rsa_key (optional, any, None)
      missing tmp rsa key


    library_has_no_ciphers (optional, any, None)
      library has no ciphers


    bad_change_cipher_spec (optional, any, None)
      bad change cipher spec


    ssl23_doing_session_id_reuse (optional, any, None)
      ssl23 doing session id reuse


    bad_decompression (optional, any, None)
      bad decompression


    length_too_short (optional, any, None)
      length too short


    krb5_server_tkt_skew (optional, any, None)
      krb5 server tkt skew


    non_sslv2_initial_packet (optional, any, None)
      non sslv2 initial packet


    invalid_challenge_length (optional, any, None)
      invalid challenge length


    library_bug (optional, any, None)
      library bug


    no_protocols_available (optional, any, None)
      no protocols available


    ssl3_ext_invalid_servername (optional, any, None)
      ssl3 ext invalid servername


    read_bio_not_set (optional, any, None)
      read bio not set


    unknown_alert_type (optional, any, None)
      unknown alert type


    krb5_server_bad_ticket (optional, any, None)
      krb5 server bad ticket


    peer_did_not_return_a_certificate (optional, any, None)
      peer did not return a certificate


    ssl_session_id_callback_failed (optional, any, None)
      ssl session id callback failed


    bad_packet_length (optional, any, None)
      bad packet length


    bad_rsa_decrypt (optional, any, None)
      bad rsa decrypt


    decryption_failed_or_bad_record_mac (optional, any, None)
      decryption failed or bad record mac


    sslv3_alert_peer_error_no_cert (optional, any, None)
      sslv3 alert peer error no cert


    decryption_failed (optional, any, None)
      decryption failed


    unable_to_decode_dh_certs (optional, any, None)
      unable to decode dh certs


    bad_response_argument (optional, any, None)
      bad response argument


    peer_error_no_cipher (optional, any, None)
      peer error no cipher


    session_id_context_uninitialized (optional, any, None)
      session id context uninitialized


    bad_dh_g_length (optional, any, None)
      bad dh g length


    block_cipher_pad_is_wrong (optional, any, None)
      block cipher pad is wrong


    missing_export_tmp_rsa_key (optional, any, None)
      missing export tmp rsa key


    sslv3_alert_bad_certificate (optional, any, None)
      sslv3 alert bad certificate


    compression_library_error (optional, any, None)
      compression library error


    sslv3_alert_peer_error_cert (optional, any, None)
      sslv3 alert peer error cert


    bad_checksum (optional, any, None)
      bad checksum


    bad_digest_length (optional, any, None)
      bad digest length


    connection_id_is_different (optional, any, None)
      connection id is different


    unable_to_load_ssl3_sha1_routines (optional, any, None)
      unable to load ssl3 sha1 routines


    no_certificate_specified (optional, any, None)
      no certificate specified


    record_too_large (optional, any, None)
      record too large


    no_cipher_list (optional, any, None)
      no cipher list


    bad_dsa_signature (optional, any, None)
      bad dsa signature


    bad_protocol_version_number (optional, any, None)
      bad protocol version number


    unsupported_option (optional, any, None)
      unsupported option


    http_request (optional, any, None)
      http request


    bad_rsa_e_length (optional, any, None)
      bad rsa e length


    no_certificate_set (optional, any, None)
      no certificate set


    extra_data_in_message (optional, any, None)
      extra data in message


    old_session_cipher_not_returned (optional, any, None)
      old session cipher not returned


    ssl_library_has_no_ciphers (optional, any, None)
      ssl library has no ciphers


    sslv3_alert_peer_error_no_cipher (optional, any, None)
      sslv3 alert peer error no cipher


    reuse_cipher_list_not_zero (optional, any, None)
      reuse cipher list not zero


    null_ssl_ctx (optional, any, None)
      null ssl ctx


    no_compression_specified (optional, any, None)
      no compression specified


    read_wrong_packet_type (optional, any, None)
      read wrong packet type


    ccs_received_early (optional, any, None)
      ccs received early


    unsupported_ssl_version (optional, any, None)
      unsupported ssl version


    bad_rsa_modulus_length (optional, any, None)
      bad rsa modulus length


    bio_not_set (optional, any, None)
      bio not set


    tls_client_cert_req_with_anon_cipher (optional, any, None)
      tls client cert req with anon cipher


    encrypted_length_too_long (optional, any, None)
      encrypted length too long


    sslv3_alert_certificate_expired (optional, any, None)
      sslv3 alert certificate expired


    pre_mac_length_too_long (optional, any, None)
      pre mac length too long


    unsupported_protocol (optional, any, None)
      unsupported protocol


    bad_rsa_signature (optional, any, None)
      bad rsa signature


    x509_verification_setup_problems (optional, any, None)
      x509 verification setup problems


    reuse_cert_length_not_zero (optional, any, None)
      reuse cert length not zero


    krb5_client_get_cred (optional, any, None)
      krb5 client get cred


    no_shared_cipher (optional, any, None)
      no shared cipher


    peer_error_no_certificate (optional, any, None)
      peer error no certificate


    short_read (optional, any, None)
      short read


    no_required_digest (optional, any, None)
      no required digest


    unsupported_compression_algorithm (optional, any, None)
      unsupported compression algorithm


    tried_to_use_unsupported_cipher (optional, any, None)
      tried to use unsupported cipher


    krb5_client_mk_req (optional, any, None)
      krb5 client mk_req


    illegal_padding (optional, any, None)
      illegal padding


    parse_tlsext (optional, any, None)
      parse tlsext


    excessive_message_size (optional, any, None)
      excessive message size


    ssl_session_id_has_bad_length (optional, any, None)
      ssl session id has bad length


    unable_to_extract_public_key (optional, any, None)
      unable to extract public key


    no_verify_callback (optional, any, None)
      no verify callback


    sslv3_alert_illegal_parameter (optional, any, None)
      sslv3 alert illegal parameter


    missing_rsa_encrypting_cert (optional, any, None)
      missing rsa encrypting cert


    wrong_ssl_version (optional, any, None)
      wrong ssl version


    ssl3_session_id_too_long (optional, any, None)
      ssl3 session id too long


    record_too_small (optional, any, None)
      record too small


    null_ssl_method_passed (optional, any, None)
      null ssl method passed


    invalid_status_response (optional, any, None)
      invalid status response


    unable_to_find_public_key_parameters (optional, any, None)
      unable to find public key parameters


    error_in_received_cipher_list (optional, any, None)
      error in received cipher list


    public_key_not_rsa (optional, any, None)
      public key not rsa


    wrong_signature_length (optional, any, None)
      wrong signature length


    no_certificates_returned (optional, any, None)
      no certificates returned


    missing_dh_dsa_cert (optional, any, None)
      missing dh dsa cert


    invalid_purpose (optional, any, None)
      invalid purpose


    no_certificate_returned (optional, any, None)
      no certificate returned


    peer_error_unsupported_certificate_type (optional, any, None)
      peer error unsupported certificate type


    tlsv1_alert_decode_error (optional, any, None)
      tlsv1 alert decode error


    tlsv1_alert_no_renegotiation (optional, any, None)
      tlsv1 alert no renegotiation


    krb5_client_cc_principal (optional, any, None)
      krb5 client cc principal


    tlsv1_alert_protocol_version (optional, any, None)
      tlsv1 alert protocol version


    sslv3_alert_handshake_failure (optional, any, None)
      sslv3 alert handshake failure


    bad_state (optional, any, None)
      bad state


    unknown_remote_error_type (optional, any, None)
      unknown remote error type


    cipher_code_wrong_length (optional, any, None)
      cipher code wrong length


    bad_hello_request (optional, any, None)
      bad hello request


    unknown_cipher_type (optional, any, None)
      unknown cipher type


    missing_dsa_signing_cert (optional, any, None)
      missing dsa signing cert


    unsupported_cipher (optional, any, None)
      unsupported cipher


    https_proxy_request (optional, any, None)
      https proxy request


    unsupported_status_type (optional, any, None)
      unsupported status type


    wrong_version_number (optional, any, None)
      wrong version number


    wrong_message_type (optional, any, None)
      wrong message type


    sslv3_alert_peer_error_unsupp_cert_type (optional, any, None)
      sslv3 alert peer error unsupp cert type


    no_private_key_assigned (optional, any, None)
      no private key assigned


    digest_check_failed (optional, any, None)
      digest check failed


    no_privatekey (optional, any, None)
      no privatekey


    clienthello_tlsext (optional, any, None)
      clienthello tlsext


    no_ciphers_passed (optional, any, None)
      no ciphers passed


    unable_to_load_ssl3_md5_routines (optional, any, None)
      unable to load ssl3 md5 routines


    bad_dh_p_length (optional, any, None)
      bad dh p length


    tlsv1_alert_decryption_failed (optional, any, None)
      tlsv1 alert decryption failed


    missing_dh_rsa_cert (optional, any, None)
      missing dh rsa cert


    tls_peer_did_not_respond_with_cert_list (optional, any, None)
      tls peer did not respond with cert list


    no_client_cert_received (optional, any, None)
      no client cert received


    sslv3_alert_unknown_remote_err_type (optional, any, None)
      sslv3 alert unknown remote err type


    sslv3_alert_no_certificate (optional, any, None)
      sslv3 alert no certificate


    no_ciphers_specified (optional, any, None)
      no ciphers specified


    bad_write_retry (optional, any, None)
      bad write retry


    bad_alert_record (optional, any, None)
      bad alert record


    unknown_state (optional, any, None)
      unknown state


    compression_failure (optional, any, None)
      compression failure


    wrong_number_of_key_bits (optional, any, None)
      wrong number of key bits


    krb5 (optional, any, None)
      krb5


    protocol_is_shutdown (optional, any, None)
      protocol is shutdown


    unexpected_message (optional, any, None)
      unexpected message


    multiple_sgc_restarts (optional, any, None)
      multiple sgc restarts


    challenge_is_different (optional, any, None)
      challenge is different


    unexpected_record (optional, any, None)
      unexpected record


    unknown_ssl_version (optional, any, None)
      unknown ssl version


    inappropriate_fallback (optional, any, None)
      inappropriate fallback


    bad_signature (optional, any, None)
      bad signature


    bad_ecc_cert (optional, any, None)
      bad ecc cert


    ssl_session_id_is_different (optional, any, None)
      ssl session id is different


    unsupported_elliptic_curve (optional, any, None)
      unsupported elliptic curve


    krb5_server_init (optional, any, None)
      krb5 server init


    sslv3_alert_certificate_revoked (optional, any, None)
      sslv3 alert certificate revoked


    tlsv1_alert_unknown_ca (optional, any, None)
      tlsv1 alert unknown ca


    no_publickey (optional, any, None)
      no publickey


    sslv3_alert_bad_record_mac (optional, any, None)
      sslv3 alert bad record mac


    sslv3_alert_unspported_cert (optional, any, None)
      sslv3 alert unspported cert


    got_a_fin_before_a_ccs (optional, any, None)
      got a fin before a ccs


    sslv3_alert_certificate_unknown (optional, any, None)
      sslv3 alert certificate unknown


    cookie_mismatch (optional, any, None)
      cookie mismatch


    ssl_session_id_context_too_long (optional, any, None)
      ssl session id context too long


    path_too_long (optional, any, None)
      path too long


    ssl3_ext_invalid_servername_type (optional, any, None)
      ssl3 ext invalid servername type


    wrong_cipher_returned (optional, any, None)
      wrong cipher returned


    signature_for_non_signing_certificate (optional, any, None)
      signature for non signing certificate


    unable_to_load_ssl2_md5_routines (optional, any, None)
      unable to load ssl2 md5 routines


    bad_handshake_length (optional, any, None)
      bad handshake length


    certificate_verify_failed (optional, any, None)
      certificate verify failed


    scsv_received_when_renegotiating (optional, any, None)
      scsv received when renegotiating


    bad_rsa_encrypt (optional, any, None)
      bad rsa encrypt


    krb5_server_rd_req (optional, any, None)
      krb5 server rd_req


    unknown_cipher_returned (optional, any, None)
      unknown cipher returned


    record_length_mismatch (optional, any, None)
      record length mismatch


    write_bio_not_set (optional, any, None)
      write bio not set


    peer_error_certificate (optional, any, None)
      peer error certificate


    bad_ecdsa_sig (optional, any, None)
      bad ecdsa sig


    data_length_too_long (optional, any, None)
      data length too long


    serverhello_tlsext (optional, any, None)
      serverhello tlsext


    bad_dh_pub_key_length (optional, any, None)
      bad dh pub key length


    missing_tmp_rsa_pkey (optional, any, None)
      missing tmp rsa pkey


    x509_lib (optional, any, None)
      x509 lib


    no_certificate_assigned (optional, any, None)
      no certificate assigned


    wrong_signature_size (optional, any, None)
      wrong signature size


    tlsv1_alert_access_denied (optional, any, None)
      tlsv1 alert access denied


    app_data_in_handshake (optional, any, None)
      app data in handshake


    no_ciphers_available (optional, any, None)
      no ciphers available


    bn_lib (optional, any, None)
      bn lib


    unsupported_digest_type (optional, any, None)
      unsupported digest type


    tlsv1_alert_insufficient_security (optional, any, None)
      tlsv1 alert insufficient security


    missing_tmp_dh_key (optional, any, None)
      missing tmp dh key


    bad_mac_decode (optional, any, None)
      bad mac decode


    ssl3_session_id_too_short (optional, any, None)
      ssl3 session id too short


    message_too_long (optional, any, None)
      message too long


    missing_dh_key (optional, any, None)
      missing dh key


    sslv3_alert_decompression_failure (optional, any, None)
      sslv3 alert decompression failure


    bad_ecpoint (optional, any, None)
      bad ecpoint


    bad_authentication_type (optional, any, None)
      bad authentication type


    ssl_handshake_failure (optional, any, None)
      ssl handshake failure


    tlsv1_alert_user_cancelled (optional, any, None)
      tlsv1 alert user cancelled


    tlsv1_alert_export_restriction (optional, any, None)
      tlsv1 alert export restriction


    tlsv1_alert_record_overflow (optional, any, None)
      tlsv1 alert record overflow



  ansible_port (True, any, None)
    Port for AXAPI authentication


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

