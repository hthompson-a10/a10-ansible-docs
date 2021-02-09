.. _a10_import_module:


a10_import -- Configures A10 import
===================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Get files from remote site






Parameters
----------

  ssl_key (False, any, None)
    SSL Key File(enter bulk when import an archive file)


  cloud_creds (False, any, None)
    Cloud Credentials File


  ssl_crl (False, any, None)
    SSL Crl File


  ansible_username (True, any, None)
    Username for AXAPI authentication


  local_uri_file (False, any, None)
    Local URI files for http response


  pfx_password (False, any, None)
    The password for certificate file (pfx type only)


  ssl_cert_key (False, any, None)
    'bulk'= import an archive file;


  dnssec_ds (False, any, None)
    DNSSEC DS file for child zone


  class_list_type (False, any, None)
    'ac'= ac; 'ipv4'= ipv4; 'ipv6'= ipv6; 'string'= string; 'string-case- insensitive'= string-case-insensitive;


  use_mgmt_port (False, any, None)
    Use management port as source port


  auth_jwks (False, any, None)
    JSON web key


  aflex (False, any, None)
    aFleX Script Source File


  overwrite (False, any, None)
    Overwrite existing file


  file_inspection_bw_list (False, any, None)
    Black white List File


  certificate_type (False, any, None)
    'pem'= pem; 'der'= der; 'pfx'= pfx; 'p7b'= p7b;


  ca_cert (False, any, None)
    CA Cert File(enter bulk when import an archive file)


  lw_4o6 (False, any, None)
    LW-4over6 Binding Table File


  a10_partition (False, any, None)
    Destination/target partition for object/command


  secured (False, any, None)
    Mark as non-exportable


  glm_cert (False, any, None)
    GLM certificate


  terminal (False, any, None)
    terminal vi


  store_name (False, any, None)
    Import store name


  state (True, any, None)
    State of the object to be created.


  geo_location (False, any, None)
    Geo-location CSV File


  ip_map_list (False, any, None)
    IP Map List File


  policy (False, any, None)
    WAF policy File


  store (False, any, None)
    Field store


    create (optional, any, None)
      Create an import store profile


    remote_file (optional, any, None)
      Field remote_file


    name (optional, any, None)
      profile name to store remote url


    delete (optional, any, None)
      Delete an import store profile



  cloud_config (False, any, None)
    Cloud Configuration File


  glm_license (False, any, None)
    License File


  auth_portal_image (False, any, None)
    Image file for default portal


  web_category_license (False, any, None)
    License file to enable web-category feature


  health_postfile (False, any, None)
    Field health_postfile


    postfilename (optional, any, None)
      Specify the File Name


    password (optional, any, None)
      password for the remote site


    remote_file (optional, any, None)
      Profile name for remote url


    overwrite (optional, any, None)
      Overwrite existing file


    use_mgmt_port (optional, any, None)
      Use management port as source port



  ansible_password (True, any, None)
    Password for AXAPI authentication


  class_list (False, any, None)
    Class List File


  xml_schema (False, any, None)
    XML-Schema File


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  wsdl (False, any, None)
    Web Service Definition Language File


  password (False, any, None)
    password for the remote site


  dnssec_dnskey (False, any, None)
    DNSSEC DNSKEY(KSK) file for child zone


  ansible_host (True, any, None)
    Host for AXAPI authentication


  to_device (False, any, None)
    Field to_device


    glm_license (optional, any, None)
      License File


    web_category_license (optional, any, None)
      License file to enable web-category feature


    use_mgmt_port (optional, any, None)
      Use management port as source port


    glm_cert (optional, any, None)
      GLM certificate


    device (optional, any, None)
      Device (Device ID)


    remote_file (optional, any, None)
      profile name for remote url


    overwrite (optional, any, None)
      Overwrite existing file



  auth_portal (False, any, None)
    Portal file for http authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ssl_cert (False, any, None)
    SSL Cert File(enter bulk when import an archive file)


  usb_license (False, any, None)
    USB License File


  health_external (False, any, None)
    Field health_external


    description (optional, any, None)
      Describe the Program Function briefly


    externalfilename (optional, any, None)
      Specify the Program Name


    overwrite (optional, any, None)
      Overwrite existing file


    password (optional, any, None)
      password for the remote site


    remote_file (optional, any, None)
      Field remote_file


    use_mgmt_port (optional, any, None)
      Use management port as source port



  user_tag (False, any, None)
    Customized tag


  auth_saml_idp (False, any, None)
    Field auth_saml_idp


    use_mgmt_port (optional, any, None)
      Use management port as source port


    verify_xml_signature (optional, any, None)
      Verify metadata's XML signature


    saml_idp_name (optional, any, None)
      Metadata name


    password (optional, any, None)
      password for the remote site


    remote_file (optional, any, None)
      Profile name for remote url


    overwrite (optional, any, None)
      Overwrite existing file



  class_list_convert (False, any, None)
    Convert Class List File to A10 format


  bw_list (False, any, None)
    Black white List File


  thales_kmdata (False, any, None)
    Thales Kmdata files


  thales_secworld (False, any, None)
    Thales security world files


  remote_file (False, any, None)
    profile name for remote url









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

