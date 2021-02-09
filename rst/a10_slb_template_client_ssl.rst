.. _a10_slb_template_client_ssl_module:


a10_slb_template_client_ssl -- Configures A10 slb.template.client-ssl
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Client SSL Template






Parameters
----------

  forward_proxy_cert_not_ready_action (False, any, None)
    'bypass'= bypass the connection; 'reset'= reset the connection; 'intercept'= wait for cert and then inspect the connection;


  session_cache_timeout (False, any, None)
    Session Cache Timeout (Timeout value, in seconds. Default value 0 (Session cache timeout disabled))


  forward_proxy_decrypted_dscp_bypass (False, any, None)
    DSCP to apply to bypassed traffic


  ends_with_list (False, any, None)
    Field ends_with_list


    ends_with (optional, any, None)
      Forward proxy bypass if SNI string ends with another string



  forward_proxy_alt_sign (False, any, None)
    Forward proxy alternate signing cert and key


  bypass_cert_san_multi_class_list (False, any, None)
    Field bypass_cert_san_multi_class_list


    bypass_cert_san_multi_class_list_name (optional, any, None)
      Class List Name



  key_alternate (False, any, None)
    Specify the second private key (Key Name)


  fp_ca_key_shared (False, any, None)
    CA Private Key Partition Shared


  certificate_issuer_contains_list (False, any, None)
    Field certificate_issuer_contains_list


    certificate_issuer_contains (optional, any, None)
      Forward proxy bypass if Certificate  issuer contains another string (Certificate issuer)



  forward_proxy_enable (False, any, None)
    Enable SSL forward proxy


  template_cipher (False, any, None)
    Cipher Template Name


  forward_passphrase (False, any, None)
    Password Phrase


  enable_tls_alert_logging (False, any, None)
    Enable TLS alert logging


  key_shared_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  fp_cert_fetch_natpool_name (False, any, None)
    Specify NAT pool or pool group


  certificate_san_ends_with_list (False, any, None)
    Field certificate_san_ends_with_list


    certificate_san_ends_with (optional, any, None)
      Forward proxy bypass if Certificate SAN ends with another string



  uuid (False, any, None)
    uuid of the object


  forward_proxy_ocsp_disable (False, any, None)
    Disable ocsp-stapling for forward proxy


  cert_alternate (False, any, None)
    Specify the second certificate (Certificate Name)


  dgversion (False, any, None)
    Lower TLS/SSL version can be downgraded


  handshake_logging_enable (False, any, None)
    Enable SSL handshake logging


  ocspst_sg (False, any, None)
    Specify authentication service group


  notafteryear (False, any, None)
    Year


  expire_hours (False, any, None)
    Certificate lifetime in hours


  fp_alt_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  fp_alt_key (False, any, None)
    CA Private Key for forward proxy alternate signing (Key name)


  client_auth_equals_list (False, any, None)
    Field client_auth_equals_list


    client_auth_equals (optional, any, None)
      Forward proxy bypass if SNI string equals another string



  crl_certs (False, any, None)
    Field crl_certs


    crl_shared (optional, any, None)
      Certificate Revocation Lists Partition Shared


    crl (optional, any, None)
      Certificate Revocation Lists (Certificate Revocation Lists file name)



  bypass_cert_issuer_class_list_name (False, any, None)
    Class List Name


  ocspst_srvr_minutes (False, any, None)
    Specify update period, in minutes


  notbefore (False, any, None)
    notBefore date


  certificate_issuer_equals_list (False, any, None)
    Field certificate_issuer_equals_list


    certificate_issuer_equals (optional, any, None)
      Forward proxy bypass if Certificate issuer equals another string



  exception_certificate_san_cl_name (False, any, None)
    Exceptions to forward-proxy-bypass


  certificate_issuer_ends_with_list (False, any, None)
    Field certificate_issuer_ends_with_list


    certificate_issuer_ends_with (optional, any, None)
      Forward proxy bypass if Certificate issuer ends with another string



  notafter (False, any, None)
    notAfter date


  enable_ssli_ftp_alg (False, any, None)
    Enable SSLi FTP over TLS support at which port


  notbeforeday (False, any, None)
    Day


  ocsp_stapling (False, any, None)
    Config OCSP stapling support


  server_name_auto_map (False, any, None)
    Enable automatic mapping of server name indication in Client hello extension


  ocspst_srvr_timeout (False, any, None)
    Specify retry timeout (Default is 30 mins)


  session_cache_size (False, any, None)
    Session Cache Size (Maximum cache size. Default value 0 (Session ID reuse disabled))


  non_ssl_bypass_service_group (False, any, None)
    Service Group for Bypass non-ssl traffic (Service Group Name)


  ad_group_list (False, any, None)
    Forward proxy bypass if ad-group matches class-list


  certificate_subject_starts_with_list (False, any, None)
    Field certificate_subject_starts_with_list


    certificate_subject_starts (optional, any, None)
      Forward proxy bypass if Certificate Subject starts with another string



  name (True, any, None)
    Client SSL Template Name


  certificate_subject_equals_list (False, any, None)
    Field certificate_subject_equals_list


    certificate_subject_equals (optional, any, None)
      Forward proxy bypass if Certificate Subject equals another string



  equals_list (False, any, None)
    Field equals_list


    equals (optional, any, None)
      Forward proxy bypass if SNI string equals another string



  shared_partition_pool (False, any, None)
    Reference a NAT pool or pool group from shared partition


  client_auth_starts_with_list (False, any, None)
    Field client_auth_starts_with_list


    client_auth_starts_with (optional, any, None)
      Forward proxy bypass if SNI string starts with another string



  fp_cert_ext_crldp (False, any, None)
    CRL Distribution Point (CRL Distribution Point URI)


  client_auth_ends_with_list (False, any, None)
    Field client_auth_ends_with_list


    client_auth_ends_with (optional, any, None)
      Forward proxy bypass if SNI string ends with another string



  forward_proxy_block_message (False, any, None)
    Message to be included on the block page (Message, enclose in quotes if spaces are present)


  forward_proxy_cert_unknown_action (False, any, None)
    Action taken if a certificate revocation status is unknown, bypass SSLi processing by default


  key_alt_partition_shared (False, any, None)
    Key Partition Shared


  forward_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  ocspst_sg_minutes (False, any, None)
    Specify update period, in minutes


  cert_revoke_action (False, any, None)
    'bypass'= bypass SSLi processing; 'continue'= continue the connection; 'drop'= close the connection; 'block'= block the connection with a warning page;


  ansible_username (True, any, None)
    Username for AXAPI authentication


  forward_proxy_crl_disable (False, any, None)
    Disable Certificate Revocation List checking for forward proxy


  disable_sslv3 (False, any, None)
    Reject Client requests for SSL version 3


  forward_proxy_decrypted_dscp (False, any, None)
    Apply a DSCP to decrypted and bypassed traffic (DSCP to apply to decrypted traffic)


  template_hsm (False, any, None)
    HSM Template (HSM Template Name)


  certificate_subject_ends_with_list (False, any, None)
    Field certificate_subject_ends_with_list


    certificate_subject_ends_with (optional, any, None)
      Forward proxy bypass if Certificate Subject ends with another string



  forward_proxy_cert_expiry (False, any, None)
    Adjust certificate expiry relative to the time when it is created on the device


  forward_proxy_failsafe_disable (False, any, None)
    Disable Failsafe for SSL forward proxy


  inspect_certificate_san_cl_name (False, any, None)
    Forward proxy Inspect if Certificate Subject Alternative Name matches class- list


  forward_proxy_ca_key (False, any, None)
    CA Private Key for forward proxy (SSL forward proxy CA Key Name)


  ssl_false_start_disable (False, any, None)
    disable SSL False Start


  forward_proxy_cert_revoke_action (False, any, None)
    Action taken if a certificate is irreversibly revoked, bypass SSLi processing by default


  forward_proxy_no_shared_cipher_action (False, any, None)
    Action taken if handshake fails due to no shared ciper, close the connection by default


  hsm_type (False, any, None)
    'thales-embed'= Thales embed key; 'thales-hwcrhk'= Thales hwcrhk Key;


  notafterday (False, any, None)
    Day


  ocspst_sg_hours (False, any, None)
    Specify update period, in hours


  cache_persistence_list_name (False, any, None)
    Class List Name


  sni_enable_log (False, any, None)
    Enable logging of sni-auto-map failures. Disable by default


  key_passphrase (False, any, None)
    Password Phrase


  non_ssl_bypass_l4session (False, any, None)
    Handle the non-ssl session as L4 for performance optimization


  state (True, any, None)
    State of the object to be created.


  version (False, any, None)
    TLS/SSL version, default is the highest number supported (TLS/SSL version= 30-SSLv3.0, 31-TLSv1.0, 32-TLSv1.1 and 33-TLSv1.2)


  class_list_name (False, any, None)
    Class List Name


  fp_cert_fetch_autonat_precedence (False, any, None)
    Set this NAT pool as higher precedence than other source NAT like configued under template policy


  key_shared_str (False, any, None)
    Key Name


  forward_proxy_ssl_version (False, any, None)
    TLS/SSL version, default is TLS1.2 (TLS/SSL version= 31-TLSv1.0, 32-TLSv1.1 and 33-TLSv1.2)


  bypass_cert_issuer_multi_class_list (False, any, None)
    Field bypass_cert_issuer_multi_class_list


    bypass_cert_issuer_multi_class_list_name (optional, any, None)
      Class List Name



  forward_proxy_ca_cert (False, any, None)
    CA Certificate for forward proxy (SSL forward proxy CA Certificate Name)


  ocspst_ca_cert (False, any, None)
    CA certificate


  forward_proxy_cert_cache_limit (False, any, None)
    Certificate cache size limit, default is 524288 (set to 0 for unlimited size)


  certificate_san_starts_with_list (False, any, None)
    Field certificate_san_starts_with_list


    certificate_san_starts (optional, any, None)
      Forward proxy bypass if Certificate SAN starts with another string



  fp_ca_shared (False, any, None)
    CA Certificate Partition Shared


  certificate_subject_contains_list (False, any, None)
    Field certificate_subject_contains_list


    certificate_subject_contains (optional, any, None)
      Forward proxy bypass if Certificate Subject contains another string



  client_auth_case_insensitive (False, any, None)
    Case insensitive forward proxy client auth bypass


  chain_cert_shared_str (False, any, None)
    Chain Certificate Name


  fp_alt_passphrase (False, any, None)
    Password Phrase


  ocspst_sg_days (False, any, None)
    Specify update period, in days


  fp_cert_ext_aia_ocsp (False, any, None)
    OCSP (Authority Information Access URI)


  forward_proxy_trusted_ca_lists (False, any, None)
    Field forward_proxy_trusted_ca_lists


    forward_proxy_trusted_ca (optional, any, None)
      Forward proxy trusted CA file (CA file name)


    fp_trusted_ca_shared (optional, any, None)
      Trusted CA Certificate Partition Shared



  user_name_list (False, any, None)
    Forward proxy bypass if user-name matches class-list


  key_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  cert (False, any, None)
    Certificate Name


  starts_with_list (False, any, None)
    Field starts_with_list


    starts_with (optional, any, None)
      Forward proxy bypass if SNI string starts with another string



  notbeforemonth (False, any, None)
    Month


  forward_proxy_verify_cert_fail_action (False, any, None)
    Action taken if certificate verification fails, close the connection by default


  client_certificate (False, any, None)
    'Ignore'= Don't request client certificate; 'Require'= Require client certificate; 'Request'= Request client certificate;


  oper (False, any, None)
    Field oper


    cert_status_list (optional, any, None)
      Field cert_status_list


    name (optional, any, None)
      Client SSL Template Name



  key (False, any, None)
    Key Name


  auth_sg_filter (False, any, None)
    Specify LDAP search filter


  client_auth_class_list (False, any, None)
    Forward proxy client auth bypass if SNI string matches class-list (Class List Name)


  multi_class_list (False, any, None)
    Field multi_class_list


    multi_clist_name (optional, any, None)
      Class List Name



  verify_cert_fail_action (False, any, None)
    'bypass'= bypass SSLi processing; 'continue'= continue the connection; 'drop'= close the connection; 'block'= block the connection with a warning page;


  ocspst_srvr_days (False, any, None)
    Specify update period, in days


  contains_list (False, any, None)
    Field contains_list


    contains (optional, any, None)
      Forward proxy bypass if SNI string contains another string



  dh_type (False, any, None)
    '1024'= 1024; '1024-dsa'= 1024-dsa; '2048'= 2048;


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'real-estate'= real estate category; 'computer-and-internet- security'= computer and internet security category; 'financial-services'= financial services category; 'business-and-economy'= business and economy category; 'computer-and-internet-info'= computer and internet info category; 'auctions'= auctions category; 'shopping'= shopping category; 'cult-and- occult'= cult and occult category; 'travel'= travel category; 'drugs'= drugs category; 'adult-and-pornography'= adult and pornography category; 'home-and- garden'= home and garden category; 'military'= military category; 'social- network'= social network category; 'dead-sites'= dead sites category; 'stock- advice-and-tools'= stock advice and tools category; 'training-and-tools'= training and tools category; 'dating'= dating category; 'sex-education'= sex education category; 'religion'= religion category; 'entertainment-and-arts'= entertainment and arts category; 'personal-sites-and-blogs'= personal sites and blogs category; 'legal'= legal category; 'local-information'= local information category; 'streaming-media'= streaming media category; 'job-search'= job search category; 'gambling'= gambling category; 'translation'= translation category; 'reference-and-research'= reference and research category; 'shareware-and- freeware'= shareware and freeware category; 'peer-to-peer'= peer to peer category; 'marijuana'= marijuana category; 'hacking'= hacking category; 'games'= games category; 'philosophy-and-politics'= philosophy and politics category; 'weapons'= weapons category; 'pay-to-surf'= pay to surf category; 'hunting-and-fishing'= hunting and fishing category; 'society'= society category; 'educational-institutions'= educational institutions category; 'online-greeting-cards'= online greeting cards category; 'sports'= sports category; 'swimsuits-and-intimate-apparel'= swimsuits and intimate apparel category; 'questionable'= questionable category; 'kids'= kids category; 'hate- and-racism'= hate and racism category; 'personal-storage'= personal storage category; 'violence'= violence category; 'keyloggers-and-monitoring'= keyloggers and monitoring category; 'search-engines'= search engines category; 'internet-portals'= internet portals category; 'web-advertisements'= web advertisements category; 'cheating'= cheating category; 'gross'= gross category; 'web-based-email'= web based email category; 'malware-sites'= malware sites category; 'phishing-and-other-fraud'= phishing and other fraud category; 'proxy-avoid-and-anonymizers'= proxy avoid and anonymizers category; 'spyware- and-adware'= spyware and adware category; 'music'= music category; 'government'= government category; 'nudity'= nudity category; 'news-and-media'= news and media category; 'illegal'= illegal category; 'CDNs'= content delivery networks category; 'internet-communications'= internet communications category; 'bot-nets'= bot nets category; 'abortion'= abortion category; 'health-and- medicine'= health and medicine category; 'confirmed-SPAM-sources'= confirmed SPAM sources category; 'SPAM-URLs'= SPAM URLs category; 'unconfirmed-SPAM- sources'= unconfirmed SPAM sources category; 'open-HTTP-proxies'= open HTTP proxies category; 'dynamic-comment'= dynamic comment category; 'parked- domains'= parked domains category; 'alcohol-and-tobacco'= alcohol and tobacco category; 'private-IP-addresses'= private IP addresses category; 'image-and- video-search'= image and video search category; 'fashion-and-beauty'= fashion and beauty category; 'recreation-and-hobbies'= recreation and hobbies category; 'motor-vehicles'= motor vehicles category; 'web-hosting-sites'= web hosting sites category; 'food-and-dining'= food and dining category; 'uncategorised'= uncategorised; 'other-category'= other category;



  forward_proxy_selfsign_redir (False, any, None)
    Redirect connections to pages with self signed certs to a warning page


  local_logging (False, any, None)
    Enable local logging


  fp_cert_ext_aia_ca_issuers (False, any, None)
    CA Issuers (Authority Information Access URI)


  forward_proxy_cert_cache_timeout (False, any, None)
    Certificate cache timeout, default is 1 hour (seconds, set to 0 for never timeout)


  cert_shared_str (False, any, None)
    Certificate Name


  auth_username (False, any, None)
    Specify the Username Field in the Client Certificate(If multi-fields are specificed, prior one has higher priority)


  notaftermonth (False, any, None)
    Month


  ansible_host (True, any, None)
    Host for AXAPI authentication


  certificate_issuer_starts_with_list (False, any, None)
    Field certificate_issuer_starts_with_list


    certificate_issuer_starts (optional, any, None)
      Forward proxy bypass if Certificate issuer starts with another string



  require_web_category (False, any, None)
    Wait for web category to be resolved before taking bypass decision


  bypass_cert_subject_class_list_name (False, any, None)
    Class List Name


  authorization (False, any, None)
    Specify LDAP server for client SSL authorizaiton


  fp_cert_fetch_natpool_name_shared (False, any, None)
    Specify NAT pool or pool group


  inspect_list_name (False, any, None)
    Class List Name


  ocspst_sg_timeout (False, any, None)
    Specify retry timeout (Default is 30 mins)


  certificate_san_contains_list (False, any, None)
    Field certificate_san_contains_list


    certificate_san_contains (optional, any, None)
      Forward proxy bypass if Certificate SAN contains another string



  exception_certificate_subject_cl_name (False, any, None)
    Exceptions to forward-proxy-bypass


  server_name_list (False, any, None)
    Field server_name_list


    server_cert (optional, any, None)
      Server Certificate associated to SNI (Server Certificate Name)


    server_encrypted (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


    server_name_regex_alternate (optional, any, None)
      Specific the second certifcate


    server_passphrase (optional, any, None)
      help Password Phrase


    server_chain (optional, any, None)
      Server Certificate Chain associated to SNI (Server Certificate Chain Name)


    server_name_regex (optional, any, None)
      Server name indication in Client hello extension with regular expression (Server name String with regex)


    server_chain_regex (optional, any, None)
      Server Certificate Chain associated to SNI regex (Server Certificate Chain Name)


    server_encrypted_regex (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


    server_cert_regex (optional, any, None)
      Server Certificate associated to SNI regex (Server Certificate Name)


    server_shared_regex (optional, any, None)
      Server Name Partition Shared


    server_shared (optional, any, None)
      Server Name Partition Shared


    server_passphrase_regex (optional, any, None)
      help Password Phrase


    server_key (optional, any, None)
      Server Private Key associated to SNI (Server Private Key Name)


    server_name (optional, any, None)
      Server name indication in Client hello extension (Server name String)


    server_key_regex (optional, any, None)
      Server Private Key associated to SNI regex (Server Private Key Name)


    server_name_alternate (optional, any, None)
      Specific the second certifcate



  cert_alt_partition_shared (False, any, None)
    Certificate Partition Shared


  authen_name (False, any, None)
    Specify authorization LDAP server name


  ansible_port (True, any, None)
    Port for AXAPI authentication


  key_shared_passphrase (False, any, None)
    Password Phrase


  exception_user_name_list (False, any, None)
    Exceptions to forward proxy bypass if user-name matches class-list


  ansible_password (True, any, None)
    Password for AXAPI authentication


  fp_alt_shared (False, any, None)
    Alternate CA Certificate and Private Key Partition Shared


  cert_unknown_action (False, any, None)
    'bypass'= bypass SSLi processing; 'continue'= continue the connection; 'drop'= close the connection; 'block'= block the connection with a warning page;


  forward_proxy_require_sni_cert_matched (False, any, None)
    'no-match-action-inspect'= Inspected if not matched; 'no-match-action-drop'= Dropped if not matched;


  cipher_without_prio_list (False, any, None)
    Field cipher_without_prio_list


    cipher_wo_prio (optional, any, None)
      'SSL3_RSA_DES_192_CBC3_SHA'= SSL3_RSA_DES_192_CBC3_SHA; 'SSL3_RSA_RC4_128_MD5'= SSL3_RSA_RC4_128_MD5; 'SSL3_RSA_RC4_128_SHA'= SSL3_RSA_RC4_128_SHA; 'TLS1_RSA_AES_128_SHA'= TLS1_RSA_AES_128_SHA; 'TLS1_RSA_AES_256_SHA'= TLS1_RSA_AES_256_SHA; 'TLS1_RSA_AES_128_SHA256'= TLS1_RSA_AES_128_SHA256; 'TLS1_RSA_AES_256_SHA256'= TLS1_RSA_AES_256_SHA256; 'TLS1_DHE_RSA_AES_128_GCM_SHA256'= TLS1_DHE_RSA_AES_128_GCM_SHA256; 'TLS1_DHE_RSA_AES_128_SHA'= TLS1_DHE_RSA_AES_128_SHA; 'TLS1_DHE_RSA_AES_128_SHA256'= TLS1_DHE_RSA_AES_128_SHA256; 'TLS1_DHE_RSA_AES_256_GCM_SHA384'= TLS1_DHE_RSA_AES_256_GCM_SHA384; 'TLS1_DHE_RSA_AES_256_SHA'= TLS1_DHE_RSA_AES_256_SHA; 'TLS1_DHE_RSA_AES_256_SHA256'= TLS1_DHE_RSA_AES_256_SHA256; 'TLS1_ECDHE_ECDSA_AES_128_GCM_SHA256'= TLS1_ECDHE_ECDSA_AES_128_GCM_SHA256; 'TLS1_ECDHE_ECDSA_AES_128_SHA'= TLS1_ECDHE_ECDSA_AES_128_SHA; 'TLS1_ECDHE_ECDSA_AES_128_SHA256'= TLS1_ECDHE_ECDSA_AES_128_SHA256; 'TLS1_ECDHE_ECDSA_AES_256_GCM_SHA384'= TLS1_ECDHE_ECDSA_AES_256_GCM_SHA384; 'TLS1_ECDHE_ECDSA_AES_256_SHA'= TLS1_ECDHE_ECDSA_AES_256_SHA; 'TLS1_ECDHE_RSA_AES_128_GCM_SHA256'= TLS1_ECDHE_RSA_AES_128_GCM_SHA256; 'TLS1_ECDHE_RSA_AES_128_SHA'= TLS1_ECDHE_RSA_AES_128_SHA; 'TLS1_ECDHE_RSA_AES_128_SHA256'= TLS1_ECDHE_RSA_AES_128_SHA256; 'TLS1_ECDHE_RSA_AES_256_GCM_SHA384'= TLS1_ECDHE_RSA_AES_256_GCM_SHA384; 'TLS1_ECDHE_RSA_AES_256_SHA'= TLS1_ECDHE_RSA_AES_256_SHA; 'TLS1_RSA_AES_128_GCM_SHA256'= TLS1_RSA_AES_128_GCM_SHA256; 'TLS1_RSA_AES_256_GCM_SHA384'= TLS1_RSA_AES_256_GCM_SHA384; 'TLS1_ECDHE_RSA_AES_256_SHA384'= TLS1_ECDHE_RSA_AES_256_SHA384; 'TLS1_ECDHE_ECDSA_AES_256_SHA384'= TLS1_ECDHE_ECDSA_AES_256_SHA384; 'TLS1_ECDHE_RSA_CHACHA20_POLY1305_SHA256'= TLS1_ECDHE_RSA_CHACHA20_POLY1305_SHA256; 'TLS1_ECDHE_ECDSA_CHACHA20_POLY1305_SHA256'= TLS1_ECDHE_ECDSA_CHACHA20_POLY1305_SHA256; 'TLS1_DHE_RSA_CHACHA20_POLY1305_SHA256'= TLS1_DHE_RSA_CHACHA20_POLY1305_SHA256;



  fp_cert_fetch_autonat (False, any, None)
    'auto'= Configure auto NAT for server certificate fetching;


  key_alt_passphrase (False, any, None)
    Password Phrase


  auth_username_attribute (False, any, None)
    Specify attribute name of username for client SSL authorization


  certificate_san_equals_list (False, any, None)
    Field certificate_san_equals_list


    certificate_san_equals (optional, any, None)
      Forward proxy bypass if Certificate SAN equals another string



  notbeforeyear (False, any, None)
    Year


  alert_type (False, any, None)
    'fatal'= Log fatal alerts;


  fp_cert_fetch_natpool_precedence (False, any, None)
    Set this NAT pool as higher precedence than other source NAT like configued under template policy


  sslilogging (False, any, None)
    'disable'= Disable all logging; 'all'= enable all logging(error, info);


  fp_alt_cert (False, any, None)
    CA Certificate for forward proxy alternate signing (Certificate name)


  ldap_search_filter (False, any, None)
    Specify LDAP search filter


  shared_partition_cipher_template (False, any, None)
    Reference a cipher template from shared partition


  chain_cert (False, any, None)
    Chain Certificate Name


  key_alt_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  no_shared_cipher_action (False, any, None)
    'bypass'= bypass SSLi processing; 'drop'= close the connection;


  direct_client_server_auth (False, any, None)
    Let backend server does SSL client authentication directly


  session_ticket_lifetime (False, any, None)
    Session ticket lifetime in seconds from stateless session resumption (Lifetime value in seconds. Default value 0 (Session ticket lifetime limit disabled))


  ocspst_srvr_hours (False, any, None)
    Specify update period, in hours


  inspect_certificate_issuer_cl_name (False, any, None)
    Forward proxy Inspect if Certificate issuer matches class-list


  ocspst_ocsp (False, any, None)
    Specify OCSP Authentication


  exception_ad_group_list (False, any, None)
    Exceptions to forward proxy bypass if ad-group matches class-list


  ssli_logging (False, any, None)
    SSLi logging level, default is error logging only


  forward_proxy_no_sni_action (False, any, None)
    'intercept'= intercept in no SNI case; 'bypass'= bypass in no SNI case; 'reset'= reset in no SNI case;


  bypass_cert_san_class_list_name (False, any, None)
    Class List Name


  bypass_cert_subject_multi_class_list (False, any, None)
    Field bypass_cert_subject_multi_class_list


    bypass_cert_subject_multi_class_list_name (optional, any, None)
      Class List Name



  ca_certs (False, any, None)
    Field ca_certs


    client_ocsp (optional, any, None)
      Specify ocsp authentication server(s) for client certificate verification


    client_ocsp_sg (optional, any, None)
      Specify service-group (Service group name)


    ca_shared (optional, any, None)
      CA Certificate Partition Shared


    ca_cert (optional, any, None)
      CA Certificate (CA Certificate Name)


    client_ocsp_srvr (optional, any, None)
      Specify authentication server



  client_auth_contains_list (False, any, None)
    Field client_auth_contains_list


    client_auth_contains (optional, any, None)
      Forward proxy bypass if SNI string contains another string



  forward_proxy_log_disable (False, any, None)
    Disable SSL forward proxy logging


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  stats (False, any, None)
    Field stats


    entertainment_and_arts (optional, any, None)
      entertainment and arts category


    swimsuits_and_intimate_apparel (optional, any, None)
      swimsuits and intimate apparel category


    web_based_email (optional, any, None)
      web based email category


    CDNs (optional, any, None)
      content delivery networks category


    dynamic_comment (optional, any, None)
      dynamic comment category


    confirmed_SPAM_sources (optional, any, None)
      confirmed SPAM sources category


    pay_to_surf (optional, any, None)
      pay to surf category


    phishing_and_other_fraud (optional, any, None)
      phishing and other fraud category


    fashion_and_beauty (optional, any, None)
      fashion and beauty category


    news_and_media (optional, any, None)
      news and media category


    adult_and_pornography (optional, any, None)
      adult and pornography category


    bot_nets (optional, any, None)
      bot nets category


    cheating (optional, any, None)
      cheating category


    stock_advice_and_tools (optional, any, None)
      stock advice and tools category


    spyware_and_adware (optional, any, None)
      spyware and adware category


    illegal (optional, any, None)
      illegal category


    keyloggers_and_monitoring (optional, any, None)
      keyloggers and monitoring category


    cult_and_occult (optional, any, None)
      cult and occult category


    sex_education (optional, any, None)
      sex education category


    sports (optional, any, None)
      sports category


    health_and_medicine (optional, any, None)
      health and medicine category


    music (optional, any, None)
      music category


    other_category (optional, any, None)
      other category


    search_engines (optional, any, None)
      search engines category


    image_and_video_search (optional, any, None)
      image and video search category


    questionable (optional, any, None)
      questionable category


    reference_and_research (optional, any, None)
      reference and research category


    shopping (optional, any, None)
      shopping category


    food_and_dining (optional, any, None)
      food and dining category


    government (optional, any, None)
      government category


    drugs (optional, any, None)
      drugs category


    personal_sites_and_blogs (optional, any, None)
      personal sites and blogs category


    financial_services (optional, any, None)
      financial services category


    translation (optional, any, None)
      translation category


    open_HTTP_proxies (optional, any, None)
      open HTTP proxies category


    web_advertisements (optional, any, None)
      web advertisements category


    internet_communications (optional, any, None)
      internet communications category


    hunting_and_fishing (optional, any, None)
      hunting and fishing category


    computer_and_internet_info (optional, any, None)
      computer and internet info category


    name (optional, any, None)
      Client SSL Template Name


    dead_sites (optional, any, None)
      dead sites category


    abortion (optional, any, None)
      abortion category


    training_and_tools (optional, any, None)
      training and tools category


    educational_institutions (optional, any, None)
      educational institutions category


    hate_and_racism (optional, any, None)
      hate and racism category


    hacking (optional, any, None)
      hacking category


    streaming_media (optional, any, None)
      streaming media category


    SPAM_URLs (optional, any, None)
      SPAM URLs category


    parked_domains (optional, any, None)
      parked domains category


    nudity (optional, any, None)
      nudity category


    home_and_garden (optional, any, None)
      home and garden category


    online_greeting_cards (optional, any, None)
      online greeting cards category


    marijuana (optional, any, None)
      marijuana category


    society (optional, any, None)
      society category


    real_estate (optional, any, None)
      real estate category


    philosophy_and_politics (optional, any, None)
      philosophy and politics category


    gross (optional, any, None)
      gross category


    uncategorised (optional, any, None)
      uncategorised


    business_and_economy (optional, any, None)
      business and economy category


    travel (optional, any, None)
      travel category


    peer_to_peer (optional, any, None)
      peer to peer category


    legal (optional, any, None)
      legal category


    weapons (optional, any, None)
      weapons category


    religion (optional, any, None)
      religion category


    alcohol_and_tobacco (optional, any, None)
      alcohol and tobacco category


    gambling (optional, any, None)
      gambling category


    dating (optional, any, None)
      dating category


    shareware_and_freeware (optional, any, None)
      shareware and freeware category


    private_IP_addresses (optional, any, None)
      private IP addresses category


    internet_portals (optional, any, None)
      internet portals category


    personal_storage (optional, any, None)
      personal storage category


    social_network (optional, any, None)
      social network category


    job_search (optional, any, None)
      job search category


    malware_sites (optional, any, None)
      malware sites category


    military (optional, any, None)
      military category


    recreation_and_hobbies (optional, any, None)
      recreation and hobbies category


    kids (optional, any, None)
      kids category


    web_hosting_sites (optional, any, None)
      web hosting sites category


    violence (optional, any, None)
      violence category


    local_information (optional, any, None)
      local information category


    motor_vehicles (optional, any, None)
      motor vehicles category


    games (optional, any, None)
      games category


    auctions (optional, any, None)
      auctions category


    unconfirmed_SPAM_sources (optional, any, None)
      unconfirmed SPAM sources category


    proxy_avoid_and_anonymizers (optional, any, None)
      proxy avoid and anonymizers category


    computer_and_internet_security (optional, any, None)
      computer and internet security category



  exception_sni_cl_name (False, any, None)
    Exceptions to forward-proxy-bypass


  a10_partition (False, any, None)
    Destination/target partition for object/command


  auth_sg_dn (False, any, None)
    Use Subject DN as LDAP search base DN


  inspect_certificate_subject_cl_name (False, any, None)
    Forward proxy Inspect if Certificate Subject matches class-list


  ocspst_srvr (False, any, None)
    Specify OCSP authentication server


  renegotiation_disable (False, any, None)
    Disable SSL renegotiation


  close_notify (False, any, None)
    Send close notification when terminate connection


  ec_list (False, any, None)
    Field ec_list


    ec (optional, any, None)
      'secp256r1'= X9_62_prime256v1; 'secp384r1'= secp384r1;



  web_category (False, any, None)
    Field web_category


    entertainment_and_arts (optional, any, None)
      Category Entertainment and Arts


    swimsuits_and_intimate_apparel (optional, any, None)
      Category Swimsuits and Intimate Apparel


    web_based_email (optional, any, None)
      Category Web based email


    dynamic_comment (optional, any, None)
      Category Dynamic Comment


    confirmed_spam_sources (optional, any, None)
      Category Confirmed SPAM Sources


    pay_to_surf (optional, any, None)
      Category Pay to Surf


    phishing_and_other_fraud (optional, any, None)
      Category Phishing and Other Frauds


    fashion_and_beauty (optional, any, None)
      Category Fashion and Beauty


    news_and_media (optional, any, None)
      Category News and Media


    adult_and_pornography (optional, any, None)
      Category Adult and Pornography


    bot_nets (optional, any, None)
      Category Bot Nets


    cheating (optional, any, None)
      Category Cheating


    religion (optional, any, None)
      Category Religion


    spyware_and_adware (optional, any, None)
      Category Spyware and Adware


    illegal (optional, any, None)
      Category Illegal


    computer_and_internet_security (optional, any, None)
      Category Computer and Internet Security


    cdns (optional, any, None)
      Category CDNs


    sex_education (optional, any, None)
      Category Sex Education


    sports (optional, any, None)
      Category Sports


    health_and_medicine (optional, any, None)
      Category Health and Medicine


    music (optional, any, None)
      Category Music


    search_engines (optional, any, None)
      Category Search Engines


    military (optional, any, None)
      Category Military


    image_and_video_search (optional, any, None)
      Category Image and Video Search


    questionable (optional, any, None)
      Category Questionable


    reference_and_research (optional, any, None)
      Category Reference and Research


    shopping (optional, any, None)
      Category Shopping


    food_and_dining (optional, any, None)
      Category Food and Dining


    peer_to_peer (optional, any, None)
      Category Peer to Peer


    drugs (optional, any, None)
      Category Abused Drugs


    personal_sites_and_blogs (optional, any, None)
      Category Personal sites and Blogs


    financial_services (optional, any, None)
      Category Financial Services


    translation (optional, any, None)
      Category Translation


    open_http_proxies (optional, any, None)
      Category Open HTTP Proxies


    web_advertisements (optional, any, None)
      Category Web Advertisements


    internet_communications (optional, any, None)
      Category Internet Communications


    hunting_and_fishing (optional, any, None)
      Category Hunting and Fishing


    computer_and_internet_info (optional, any, None)
      Category Computer and Internet Info


    society (optional, any, None)
      Category Society


    abortion (optional, any, None)
      Category Abortion


    training_and_tools (optional, any, None)
      Category Training and Tools


    educational_institutions (optional, any, None)
      Category Educational Institutions


    unconfirmed_spam_sources (optional, any, None)
      Category Unconfirmed SPAM Sources


    hate_and_racism (optional, any, None)
      Category Hate and Racism


    hacking (optional, any, None)
      Category Hacking


    streaming_media (optional, any, None)
      Category Streaming Media


    violence (optional, any, None)
      Category Violence


    nudity (optional, any, None)
      Category Nudity


    home_and_garden (optional, any, None)
      Category Home and Garden


    online_greeting_cards (optional, any, None)
      Category Online Greeting cards


    marijuana (optional, any, None)
      Category Marijuana


    dead_sites (optional, any, None)
      Category Dead Sites (db Ops only)


    real_estate (optional, any, None)
      Category Real Estate


    philosophy_and_politics (optional, any, None)
      Category Philosophy and Political Advocacy


    gross (optional, any, None)
      Category Gross


    travel (optional, any, None)
      Category Travel


    government (optional, any, None)
      Category Government


    legal (optional, any, None)
      Category Legal


    weapons (optional, any, None)
      Category Weapons


    stock_advice_and_tools (optional, any, None)
      Category Stock Advice and Tools


    private_ip_addresses (optional, any, None)
      Category Private IP Addresses


    alcohol_and_tobacco (optional, any, None)
      Category Alcohol and Tobacco


    gambling (optional, any, None)
      Category Gambling


    dating (optional, any, None)
      Category Dating


    uncategorized (optional, any, None)
      Uncategorized URLs


    shareware_and_freeware (optional, any, None)
      Category Shareware and Freeware


    internet_portals (optional, any, None)
      Category Internet Portals


    personal_storage (optional, any, None)
      Category Personal Storage


    social_network (optional, any, None)
      Category Social Network


    job_search (optional, any, None)
      Category Job Search


    malware_sites (optional, any, None)
      Category Malware Sites


    business_and_economy (optional, any, None)
      Category Business and Economy


    recreation_and_hobbies (optional, any, None)
      Category Recreation and Hobbies


    spam_urls (optional, any, None)
      Category SPAM URLs


    kids (optional, any, None)
      Category Kids


    web_hosting_sites (optional, any, None)
      Category Web Hosting Sites


    parked_domains (optional, any, None)
      Category Parked Domains


    local_information (optional, any, None)
      Category Local Information


    motor_vehicles (optional, any, None)
      Category Motor Vehicles


    games (optional, any, None)
      Category Games


    auctions (optional, any, None)
      Category Auctions


    proxy_avoid_and_anonymizers (optional, any, None)
      Category Proxy Avoid and Anonymizers


    keyloggers_and_monitoring (optional, any, None)
      Category Keyloggers and Monitoring


    cult_and_occult (optional, any, None)
      Category Cult and Occult



  case_insensitive (False, any, None)
    Case insensitive forward proxy bypass


  auth_sg (False, any, None)
    Specify authorization LDAP service group


  req_ca_lists (False, any, None)
    Field req_ca_lists


    client_cert_req_ca_shared (optional, any, None)
      CA Certificate Partition Shared


    client_certificate_Request_CA (optional, any, None)
      Send CA lists in certificate request (CA Certificate Name)



  ldap_base_dn_from_cert (False, any, None)
    Use Subject DN as LDAP search base DN


  exception_certificate_issuer_cl_name (False, any, None)
    Exceptions to forward-proxy-bypass


  user_tag (False, any, None)
    Customized tag


  template_cipher_shared (False, any, None)
    Cipher Template Name


  sslv2_bypass_service_group (False, any, None)
    Service Group for Bypass SSLV2 (Service Group Name)









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

