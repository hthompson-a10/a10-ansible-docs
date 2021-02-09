.. _a10_slb_ssl_counters_module:


a10_slb_ssl_counters -- Configures A10 slb.ssl-counters
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Client side SSL Vport Statistics






Parameters
----------

  oper (False, any, None)
    Field oper


    tls1_ecdhe_ecdsa_aes_128_sha_failures (optional, any, None)
      TLS1_ECDHE_ECDSA_AES_128_SHA Failures


    kex_rsa_2048_failures (optional, any, None)
      Failed 2048-bit RSA key exchanges


    kex_rsa_4096_failures (optional, any, None)
      Failed 4096-bit RSA key exchanges


    tls1_ecdhe_ecdsa_aes_256_sha384_id (optional, any, None)
      TLS1_ECDHE_ECDSA_AES_256_SHA384 Cipher ID


    tls1_dhe_rsa_chacha20_poly1305_sha256_failures (optional, any, None)
      TLS1_DHE_RSA_CHACHA20_POLY1305_SHA256 Cipher failures


    tls1_ecdhe_ecdsa_aes_256_sha_id (optional, any, None)
      TLS1_ECDHE_ECDSA_AES_256_SHA Cipher ID


    tls1_ecdhe_rsa_aes_128_gcm_sha256_successes (optional, any, None)
      TLS1_ECDHE_RSA_AES_128_GCM_SHA256 Successes


    tls1_dhe_rsa_aes_256_gcm_sha384_id (optional, any, None)
      TLS1_DHE_RSA_AES_256_GCM_SHA384 Cipher ID


    sni_automap_successes (optional, any, None)
      Successful SNI auto mappings


    tls1_rsa_aes_128_sha_id (optional, any, None)
      TLS1_RSA_AES_128_SHA Cipher ID


    sni_automap_missing_cert (optional, any, None)
      Failed SNI auto map due to missing cert/key


    tls1_dhe_rsa_aes_128_gcm_sha256_id (optional, any, None)
      TLS1_DHE_RSA_AES_128_GCM_SHA256 Cipher ID


    vserver (optional, any, None)
      virtual server name


    tls1_dhe_rsa_aes_128_sha256_id (optional, any, None)
      TLS1_DHE_RSA_AES_128_SHA256 Cipher ID


    tls1_ecdhe_ecdsa_aes_128_sha256_id (optional, any, None)
      TLS1_ECDHE_ECDSA_AES_128_SHA256 Cipher ID


    tls1_dhe_rsa_aes_128_sha_successes (optional, any, None)
      TLS1_DHE_RSA_AES_128_SHA Successes


    ssl3_rsa_des_64_cbc_sha_successes (optional, any, None)
      SSL3_RSA_DES_64_CBC_SHA Successes


    tls1_ecdhe_rsa_aes_128_sha_successes (optional, any, None)
      TLS1_ECDHE_RSA_AES_128_SHA Successes


    ssl3_rsa_rc4_128_md5_failures (optional, any, None)
      SSL3_RSA_RC4_128_MD5 Failures


    ssl3_rsa_rc4_40_md5_successes (optional, any, None)
      SSL3_RSA_RC4_40_MD5 Successes


    tls1_dhe_rsa_aes_256_sha_id (optional, any, None)
      TLS1_DHE_RSA_AES_256_SHA Cipher ID


    renego_tls12_failures (optional, any, None)
      Failed TLS1.2 renegotiations


    ssl3_rsa_rc4_128_sha_failures (optional, any, None)
      SSL3_RSA_RC4_128_SHA Failures


    tls1_ecdhe_ecdsa_aes_128_gcm_sha256_successes (optional, any, None)
      TLS1_ECDHE_ECDSA_AES_128_GCM_SHA256 Successes


    tls1_rsa_aes_256_sha_id (optional, any, None)
      TLS1_RSA_AES_256_SHA Cipher ID


    tls1_ecdhe_ecdsa_aes_256_sha_successes (optional, any, None)
      TLS1_ECDHE_ECDSA_AES_256_SHA Successes


    tls10_failures (optional, any, None)
      Failed TLS1.0 connections


    tls1_dhe_rsa_aes_256_sha_failures (optional, any, None)
      TLS1_DHE_RSA_AES_256_SHA Failures


    tls1_rsa_aes_128_gcm_sha256_successes (optional, any, None)
      TLS1_RSA_AES_128_GCM_SHA256 Successes


    tls1_rsa_aes_128_gcm_sha256_failures (optional, any, None)
      TLS1_RSA_AES_128_GCM_SHA256 Failures


    kex_rsa_1024_failures (optional, any, None)
      Failed 1024-bit RSA key exchanges


    tls1_ecdhe_ecdsa_aes_256_sha_failures (optional, any, None)
      TLS1_ECDHE_ECDSA_AES_256_SHA Failures


    tls1_rsa_aes_256_sha256_successes (optional, any, None)
      TLS1_RSA_AES_256_SHA256 Successes


    tls1_rsa_aes_256_sha256_failures (optional, any, None)
      TLS1_RSA_AES_256_SHA256 Failures


    tls1_ecdhe_rsa_aes_128_sha_failures (optional, any, None)
      TLS1_ECDHE_RSA_AES_128_SHA Failures


    tls12_failures (optional, any, None)
      Failed TLS1.2 connections


    renego_tls11_failures (optional, any, None)
      Failed TLS1.1 renegotiations


    tls1_rsa_aes_256_gcm_sha384_id (optional, any, None)
      TLS1_RSA_AES_256_GCM_SHA384 Cipher ID


    kex_ecdhe_secp384r1_failures (optional, any, None)
      Failed secp384r1 ECDHE key exchanges


    tls1_dhe_rsa_aes_128_sha_id (optional, any, None)
      TLS1_DHE_RSA_AES_128_SHA Cipher ID


    kex_rsa_4096_successes (optional, any, None)
      Successful 4096-bit RSA key exchanges


    kex_rsa_512_failures (optional, any, None)
      Failed 512-bit RSA key exchanges


    tls1_ecdhe_rsa_aes_128_sha256_successes (optional, any, None)
      TLS1_ECDHE_RSA_AES_128_SHA256 Successes


    kex_rsa_512_successes (optional, any, None)
      Successful 512-bit RSA key exchanges


    tls1_rsa_export1024_rc4_56_sha_id (optional, any, None)
      TLS1_RSA_EXPORT1024_RC4_56_SHA Cipher ID


    kex_ecdhe_secp384r1_successes (optional, any, None)
      Successful secp384r1 ECDHE key exchanges


    ssl3_rsa_des_64_cbc_sha_id (optional, any, None)
      SSL3_RSA_DES_64_CBC_SHA Cipher ID


    tls1_ecdhe_rsa_aes_256_sha_failures (optional, any, None)
      TLS1_ECDHE_RSA_AES_256_SHA Failures


    renego_ssl2_failures (optional, any, None)
      Failed SSL2 renegotiations


    tls1_ecdhe_rsa_aes_256_sha384_failures (optional, any, None)
      TLS1_ECDHE_RSA_AES_256_SHA384 Failures


    tls1_ecdhe_ecdsa_aes_128_gcm_sha256_id (optional, any, None)
      TLS1_ECDHE_ECDSA_AES_128_GCM_SHA256 Cipher ID


    ssl3_rsa_des_40_cbc_sha_failures (optional, any, None)
      SSL3_RSA_DES_40_CBC_SHA Failures


    ssl3_rsa_des_40_cbc_sha_successes (optional, any, None)
      SSL3_RSA_DES_40_CBC_SHA Successes


    ssl3_failures (optional, any, None)
      Failed SSL3 connections


    tls1_rsa_export1024_rc4_56_md5_failures (optional, any, None)
      TLS1_RSA_EXPORT1024_RC4_56_MD5 Failures


    tls1_rsa_aes_256_gcm_sha384_successes (optional, any, None)
      TLS1_RSA_AES_256_GCM_SHA384 Successes


    tls1_dhe_rsa_aes_256_gcm_sha384_failures (optional, any, None)
      TLS1_DHE_RSA_AES_256_GCM_SHA384 Failures


    renego_tls11_successes (optional, any, None)
      Successful TLS1.1 renegotiations


    tls1_rsa_export1024_rc4_56_sha_failures (optional, any, None)
      TLS1_RSA_EXPORT1024_RC4_56_SHA Failures


    ssl3_rsa_des_64_cbc_sha_failures (optional, any, None)
      SSL3_RSA_DES_64_CBC_SHA Failures


    renego_ssl2_successes (optional, any, None)
      Successful SSL2 renegotiations


    port (optional, any, None)
      Virtual Port


    sess_cache_timeout (optional, any, None)
      Session cache timeouts


    tls1_dhe_rsa_aes_128_sha256_successes (optional, any, None)
      TLS1_DHE_RSA_AES_128_SHA256 Successes


    sess_cache_curr_conn (optional, any, None)
      Session cache current connections


    kex_ecdhe_secp256r1_failures (optional, any, None)
      Failed secp256r1 ECDHE key exchanges


    kex_rsa_1024_successes (optional, any, None)
      Successful 1024-bit RSA key exchanges


    sess_cache_new (optional, any, None)
      Session cache new entries


    tls1_ecdhe_rsa_aes_128_gcm_sha256_failures (optional, any, None)
      TLS1_ECDHE_RSA_AES_128_GCM_SHA256 Failures


    sess_cache_hit (optional, any, None)
      Session cache hits


    sess_cache_miss (optional, any, None)
      Session cache misses


    ssl3_rsa_des_192_cbc3_sha_successes (optional, any, None)
      SSL3_RSA_DES_192_CBC3_SHA Successes


    cumulative_sessions (optional, any, None)
      Cumulative SSL sessions


    kex_dhe_2048_successes (optional, any, None)
      Successful 2048-bit DHE key exchanges


    tls1_ecdhe_ecdsa_chacha20_poly1305_sha256_successes (optional, any, None)
      TLS1_ECDHE_ECDSA_CHACHA20_POLY1305_SHA256 Cipher successes


    kex_dhe_512_successes (optional, any, None)
      Successful 512-bit DHE key exchanges


    tls1_ecdhe_ecdsa_chacha20_poly1305_sha256_id (optional, any, None)
      TLS1_ECDHE_ECDSA_CHACHA20_POLY1305_SHA256 Cipher ID


    tls1_rsa_export1024_rc4_56_md5_id (optional, any, None)
      TLS1_RSA_EXPORT1024_RC4_56_MD5 Cipher ID


    tls1_ecdhe_ecdsa_aes_128_sha_id (optional, any, None)
      TLS1_ECDHE_ECDSA_AES_128_SHA Cipher ID


    tls1_dhe_rsa_aes_256_gcm_sha384_successes (optional, any, None)
      TLS1_DHE_RSA_AES_256_GCM_SHA384 Successes


    kex_ecdhe_secp256r1_successes (optional, any, None)
      Successful secp256r1 ECDHE key exchanges


    ssl3_rsa_rc4_128_sha_id (optional, any, None)
      SSL3_RSA_RC4_128_SHA Cipher ID


    tls1_ecdhe_ecdsa_aes_128_gcm_sha256_failures (optional, any, None)
      TLS1_ECDHE_ECDSA_AES_128_GCM_SHA256 Failures


    tls1_ecdhe_rsa_aes_128_gcm_sha256_id (optional, any, None)
      TLS1_ECDHE_RSA_AES_128_GCM_SHA256 Cipher ID


    tls1_ecdhe_rsa_aes_128_sha256_id (optional, any, None)
      TLS1_ECDHE_RSA_AES_128_SHA256 Cipher ID


    ssl3_rsa_des_40_cbc_sha_id (optional, any, None)
      SSL3_RSA_DES_40_CBC_SHA Cipher ID


    renego_tls12_successes (optional, any, None)
      Successful TLS1.2 renegotiations


    tls1_ecdhe_ecdsa_chacha20_poly1305_sha256_failures (optional, any, None)
      TLS1_ECDHE_ECDSA_CHACHA20_POLY1305_SHA256 Cipher failures


    tls1_ecdhe_rsa_aes_256_sha384_successes (optional, any, None)
      TLS1_ECDHE_RSA_AES_256_SHA384 Successes


    tls1_rsa_aes_256_sha256_id (optional, any, None)
      TLS1_RSA_AES_256_SHA256 Cipher ID


    renego_ssl3_failures (optional, any, None)
      Failed SSL3 renegotiations


    tls1_rsa_aes_128_sha256_id (optional, any, None)
      TLS1_RSA_AES_128_SHA256 Cipher ID


    tls1_ecdhe_rsa_aes_128_sha256_failures (optional, any, None)
      TLS1_ECDHE_RSA_AES_128_SHA256 Failures


    tls1_dhe_rsa_aes_256_sha256_successes (optional, any, None)
      TLS1_DHE_RSA_AES_256_SHA256 Successes


    tls1_rsa_aes_128_sha_successes (optional, any, None)
      TLS1_RSA_AES_128_SHA Successes


    tls1_ecdhe_ecdsa_aes_128_sha256_successes (optional, any, None)
      TLS1_ECDHE_ECDSA_AES_128_SHA256 Successes


    tls1_ecdhe_rsa_aes_256_sha_id (optional, any, None)
      TLS1_ECDHE_RSA_AES_256_SHA Cipher ID


    tls1_rsa_aes_128_gcm_sha256_id (optional, any, None)
      TLS1_RSA_AES_128_GCM_SHA256 Cipher ID


    tls1_ecdhe_ecdsa_aes_256_sha384_failures (optional, any, None)
      TLS1_ECDHE_ECDSA_AES_256_SHA384 Failures


    tls1_ecdhe_ecdsa_aes_128_sha256_failures (optional, any, None)
      TLS1_ECDHE_ECDSA_AES_128_SHA256 Failures


    tls1_dhe_rsa_aes_256_sha256_id (optional, any, None)
      TLS1_DHE_RSA_AES_256_SHA256 Cipher ID


    tls1_rsa_aes_128_sha256_successes (optional, any, None)
      TLS1_RSA_AES_128_SHA256 Successes


    tls1_ecdhe_rsa_chacha20_poly1305_sha256_id (optional, any, None)
      TLS1_ECDHE_RSA_CHACHA20_POLY1305_SHA256 Cipher ID


    tls1_ecdhe_rsa_aes_128_sha_id (optional, any, None)
      TLS1_ECDHE_RSA_AES_128_SHA Cipher ID


    kex_rsa_2048_successes (optional, any, None)
      Successful 2048-bit RSA key exchanges


    tls11_successes (optional, any, None)
      Successful TLS1.1 connections


    hs_avg_time (optional, any, None)
      Average handshake time in milliseconds


    ssl3_rsa_rc4_40_md5_failures (optional, any, None)
      SSL3_RSA_RC4_40_MD5 Failures


    renegotiation_total (optional, any, None)
      Total renegotiations


    tls1_dhe_rsa_aes_128_gcm_sha256_failures (optional, any, None)
      TLS1_DHE_RSA_AES_128_GCM_SHA256 Failures


    kex_dhe_1024_failures (optional, any, None)
      Failed 1024-bit DHE key exchanges


    tls1_dhe_rsa_aes_256_sha_successes (optional, any, None)
      TLS1_DHE_RSA_AES_256_SHA Successes


    tls1_ecdhe_ecdsa_aes_256_gcm_sha384_failures (optional, any, None)
      TLS1_ECDHE_ECDSA_AES_256_GCM_SHA384 Failures


    cert_vfy (optional, any, None)
      Sent certificate verify for authentication


    renego_ssl3_successes (optional, any, None)
      Successful SSL3 renegotiations


    ssl3_rsa_rc4_40_md5_id (optional, any, None)
      SSL3_RSA_RC4_40_MD5 Cipher ID


    tls11_failures (optional, any, None)
      Failed TLS1.1 connections


    ssl3_rsa_des_192_cbc3_sha_id (optional, any, None)
      SSL3_RSA_DES_192_CBC3_SHA Cipher ID


    tls1_ecdhe_ecdsa_aes_256_sha384_successes (optional, any, None)
      TLS1_ECDHE_ECDSA_AES_256_SHA384 Successes


    ssl3_rsa_rc4_128_md5_successes (optional, any, None)
      SSL3_RSA_RC4_128_MD5 Successes


    renego_tls10_failures (optional, any, None)
      Failed TLS1.0 renegotiations


    tls1_ecdhe_rsa_aes_256_gcm_sha384_failures (optional, any, None)
      TLS1_ECDHE_RSA_AES_256_GCM_SHA384 Failures


    tls1_ecdhe_rsa_aes_256_sha384_id (optional, any, None)
      TLS1_ECDHE_RSA_AES_256_SHA384 Cipher ID


    tls1_rsa_aes_256_sha_successes (optional, any, None)
      TLS1_RSA_AES_256_SHA Successes


    tls1_dhe_rsa_aes_128_gcm_sha256_successes (optional, any, None)
      TLS1_DHE_RSA_AES_128_GCM_SHA256 Successes


    tls1_ecdhe_rsa_chacha20_poly1305_sha256_successes (optional, any, None)
      TLS1_ECDHE_RSA_CHACHA20_POLY1305_SHA256 Cipher successes


    tls1_rsa_export1024_rc4_56_sha_successes (optional, any, None)
      TLS1_RSA_EXPORT1024_RC4_56_SHA Successes


    tls1_rsa_export1024_rc4_56_md5_successes (optional, any, None)
      TLS1_RSA_EXPORT1024_RC4_56_MD5 Successes


    renego_tls10_successes (optional, any, None)
      Successful TLS1.0 renegotiations


    tls1_rsa_aes_256_gcm_sha384_failures (optional, any, None)
      TLS1_RSA_AES_256_GCM_SHA384 Failures


    tls1_dhe_rsa_chacha20_poly1305_sha256_id (optional, any, None)
      TLS1_DHE_RSA_CHACHA20_POLY1305_SHA256 Cipher ID


    ssl3_rsa_des_192_cbc3_sha_failures (optional, any, None)
      SSL3_RSA_DES_192_CBC3_SHA Failures


    tls1_dhe_rsa_aes_256_sha256_failures (optional, any, None)
      TLS1_DHE_RSA_AES_256_SHA256 Failures


    ssl2_failures (optional, any, None)
      Failed SSL2 connections


    ssl3_rsa_rc4_128_md5_id (optional, any, None)
      SSL3_RSA_RC4_128_MD5 Cipher ID


    tls1_ecdhe_rsa_aes_256_gcm_sha384_id (optional, any, None)
      TLS1_ECDHE_RSA_AES_256_GCM_SHA384 Cipher ID


    sni_automap_max_active_conn (optional, any, None)
      Failed SNI auto map due to max active limit


    kex_dhe_2048_failures (optional, any, None)
      Failed 2048-bit DHE key exchanges


    tls1_rsa_aes_128_sha256_failures (optional, any, None)
      TLS1_RSA_AES_128_SHA256 Failures


    tls1_dhe_rsa_chacha20_poly1305_sha256_successes (optional, any, None)
      TLS1_DHE_RSA_CHACHA20_POLY1305_SHA256 Cipher successes


    ssl3_successes (optional, any, None)
      Successful SSL3 connections


    hs_failures (optional, any, None)
      Total handshake failures


    tls1_ecdhe_ecdsa_aes_128_sha_successes (optional, any, None)
      TLS1_ECDHE_ECDSA_AES_128_SHA Successes


    kex_dhe_1024_successes (optional, any, None)
      Successful 1024-bit DHE key exchanges


    kex_dhe_512_failures (optional, any, None)
      Failed 512-bit DHE key exchanges


    tls1_ecdhe_ecdsa_aes_256_gcm_sha384_successes (optional, any, None)
      TLS1_ECDHE_ECDSA_AES_256_GCM_SHA384 Successes


    tls1_ecdhe_rsa_aes_256_gcm_sha384_successes (optional, any, None)
      TLS1_ECDHE_RSA_AES_256_GCM_SHA384 Successes


    sni_automap_failures (optional, any, None)
      Failed SNI auto mappings


    tls10_successes (optional, any, None)
      Successful TLS1.0 connections


    tls1_rsa_aes_256_sha_failures (optional, any, None)
      TLS1_RSA_AES_256_SHA Failures


    tls1_ecdhe_ecdsa_aes_256_gcm_sha384_id (optional, any, None)
      TLS1_ECDHE_ECDSA_AES_256_GCM_SHA384 Cipher ID


    ssl3_rsa_rc4_128_sha_successes (optional, any, None)
      SSL3_RSA_RC4_128_SHA Successes


    tls1_dhe_rsa_aes_128_sha256_failures (optional, any, None)
      TLS1_DHE_RSA_AES_128_SHA256 Failures


    tls12_successes (optional, any, None)
      Successful TLS1.2 connections


    tls1_ecdhe_rsa_chacha20_poly1305_sha256_failures (optional, any, None)
      TLS1_ECDHE_RSA_CHACHA20_POLY1305_SHA256 Cipher failures


    tls1_rsa_aes_128_sha_failures (optional, any, None)
      TLS1_RSA_AES_128_SHA Failures


    ssl2_successes (optional, any, None)
      Successful SSL2 connections


    sni_automap_conn_closed (optional, any, None)
      Conn closed before SNI auto mappings


    tls1_dhe_rsa_aes_128_sha_failures (optional, any, None)
      TLS1_DHE_RSA_AES_128_SHA Failures


    tls1_ecdhe_rsa_aes_256_sha_successes (optional, any, None)
      TLS1_ECDHE_RSA_AES_256_SHA Successes



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

