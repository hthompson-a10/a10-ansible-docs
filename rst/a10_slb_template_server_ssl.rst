.. _a10_slb_template_server_ssl_module:


a10_slb_template_server_ssl -- Configures A10 slb.template.server-ssl
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Server Side SSL Template






Parameters
----------

  session_cache_timeout (False, any, None)
    Session Cache Timeout (Timeout value, in seconds. Default no timeout.)


  alert_type (False, any, None)
    'fatal'= Log fatal alerts;


  forward_proxy_enable (False, any, None)
    Enable SSL forward proxy


  ansible_username (True, any, None)
    Username for AXAPI authentication


  sslilogging (False, any, None)
    'disable'= Disable all logging; 'all'= enable all logging(error, info);


  cipher_template (False, any, None)
    Cipher Template Name


  shared_partition_cipher_template (False, any, None)
    Reference a cipher template from shared partition


  passphrase (False, any, None)
    Password Phrase


  dh_type (False, any, None)
    '1024'= 1024; '1024-dsa'= 1024-dsa; '2048'= 2048;


  key_shared_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  uuid (False, any, None)
    uuid of the object


  use_client_sni (False, any, None)
    use client SNI


  handshake_logging_enable (False, any, None)
    Enable SSL handshake logging


  dgversion (False, any, None)
    Lower TLS/SSL version can be downgraded


  cert_shared_str (False, any, None)
    Certificate Name


  state (True, any, None)
    State of the object to be created.


  version (False, any, None)
    TLS/SSL version, default is the highest number supported (TLS/SSL version= 30-SSLv3.0, 31-TLSv1.0, 32-TLSv1.1 and 33-TLSv1.2)


  session_ticket_enable (False, any, None)
    Enable server side session ticket support


  encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  ssli_logging (False, any, None)
    SSLi logging level, default is error logging only


  key_shared_passphrase (False, any, None)
    Password Phrase


  key_shared_str (False, any, None)
    Key Name


  server_certificate_error (False, any, None)
    Field server_certificate_error


    error_type (optional, any, None)
      'email'= Notify the error via email; 'ignore'= Ignore the error, which mean the connection can continue; 'logging'= Log the error; 'trap'= Notify the error by SNMP trap;



  crl_certs (False, any, None)
    Field crl_certs


    crl_partition_shared (optional, any, None)
      Certificate Revocation Lists Partition Shared


    crl (optional, any, None)
      Certificate Revocation Lists (Certificate Revocation Lists file name)



  ansible_port (True, any, None)
    Port for AXAPI authentication


  enable_ssli_ftp_alg (False, any, None)
    Enable SSLi FTP over TLS support at which port


  ocsp_stapling (False, any, None)
    Enable ocsp-stapling support


  key (False, any, None)
    Key Name


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  enable_tls_alert_logging (False, any, None)
    Enable TLS alert logging


  session_cache_size (False, any, None)
    Session Cache Size (Maximum cache size. Default value 0 (Session ID reuse disabled))


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  renegotiation_disable (False, any, None)
    Disable SSL renegotiation


  close_notify (False, any, None)
    Send close notification when terminate connection


  name (True, any, None)
    Server SSL Template Name


  ec_list (False, any, None)
    Field ec_list


    ec (optional, any, None)
      'secp256r1'= X9_62_prime256v1; 'secp384r1'= secp384r1;



  ansible_password (True, any, None)
    Password for AXAPI authentication


  dh_short_key_action (False, any, None)
    'none'= no change; 'prepend'= prepend dh key; 'regenerate'= regenerate dh key;


  cert (False, any, None)
    Certificate Name


  cipher_without_prio_list (False, any, None)
    Field cipher_without_prio_list


    cipher_wo_prio (optional, any, None)
      'SSL3_RSA_DES_192_CBC3_SHA'= SSL3_RSA_DES_192_CBC3_SHA; 'SSL3_RSA_RC4_128_MD5'= SSL3_RSA_RC4_128_MD5; 'SSL3_RSA_RC4_128_SHA'= SSL3_RSA_RC4_128_SHA; 'TLS1_RSA_AES_128_SHA'= TLS1_RSA_AES_128_SHA; 'TLS1_RSA_AES_256_SHA'= TLS1_RSA_AES_256_SHA; 'TLS1_RSA_AES_128_SHA256'= TLS1_RSA_AES_128_SHA256; 'TLS1_RSA_AES_256_SHA256'= TLS1_RSA_AES_256_SHA256; 'TLS1_DHE_RSA_AES_128_GCM_SHA256'= TLS1_DHE_RSA_AES_128_GCM_SHA256; 'TLS1_DHE_RSA_AES_128_SHA'= TLS1_DHE_RSA_AES_128_SHA; 'TLS1_DHE_RSA_AES_128_SHA256'= TLS1_DHE_RSA_AES_128_SHA256; 'TLS1_DHE_RSA_AES_256_GCM_SHA384'= TLS1_DHE_RSA_AES_256_GCM_SHA384; 'TLS1_DHE_RSA_AES_256_SHA'= TLS1_DHE_RSA_AES_256_SHA; 'TLS1_DHE_RSA_AES_256_SHA256'= TLS1_DHE_RSA_AES_256_SHA256; 'TLS1_ECDHE_ECDSA_AES_128_GCM_SHA256'= TLS1_ECDHE_ECDSA_AES_128_GCM_SHA256; 'TLS1_ECDHE_ECDSA_AES_128_SHA'= TLS1_ECDHE_ECDSA_AES_128_SHA; 'TLS1_ECDHE_ECDSA_AES_128_SHA256'= TLS1_ECDHE_ECDSA_AES_128_SHA256; 'TLS1_ECDHE_ECDSA_AES_256_GCM_SHA384'= TLS1_ECDHE_ECDSA_AES_256_GCM_SHA384; 'TLS1_ECDHE_ECDSA_AES_256_SHA'= TLS1_ECDHE_ECDSA_AES_256_SHA; 'TLS1_ECDHE_RSA_AES_128_GCM_SHA256'= TLS1_ECDHE_RSA_AES_128_GCM_SHA256; 'TLS1_ECDHE_RSA_AES_128_SHA'= TLS1_ECDHE_RSA_AES_128_SHA; 'TLS1_ECDHE_RSA_AES_128_SHA256'= TLS1_ECDHE_RSA_AES_128_SHA256; 'TLS1_ECDHE_RSA_AES_256_GCM_SHA384'= TLS1_ECDHE_RSA_AES_256_GCM_SHA384; 'TLS1_ECDHE_RSA_AES_256_SHA'= TLS1_ECDHE_RSA_AES_256_SHA; 'TLS1_RSA_AES_128_GCM_SHA256'= TLS1_RSA_AES_128_GCM_SHA256; 'TLS1_RSA_AES_256_GCM_SHA384'= TLS1_RSA_AES_256_GCM_SHA384; 'TLS1_ECDHE_RSA_AES_256_SHA384'= TLS1_ECDHE_RSA_AES_256_SHA384; 'TLS1_ECDHE_ECDSA_AES_256_SHA384'= TLS1_ECDHE_ECDSA_AES_256_SHA384; 'TLS1_ECDHE_RSA_CHACHA20_POLY1305_SHA256'= TLS1_ECDHE_RSA_CHACHA20_POLY1305_SHA256; 'TLS1_ECDHE_ECDSA_CHACHA20_POLY1305_SHA256'= TLS1_ECDHE_ECDSA_CHACHA20_POLY1305_SHA256; 'TLS1_DHE_RSA_CHACHA20_POLY1305_SHA256'= TLS1_DHE_RSA_CHACHA20_POLY1305_SHA256;



  ca_certs (False, any, None)
    Field ca_certs


    server_ocsp_srvr (optional, any, None)
      Specify authentication server


    ca_cert_partition_shared (optional, any, None)
      CA Certificate Partition Shared


    ca_cert (optional, any, None)
      Specify CA certificate


    server_ocsp_sg (optional, any, None)
      Specify service-group (Service group name)



  user_tag (False, any, None)
    Customized tag


  template_cipher_shared (False, any, None)
    Cipher Template Name









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

