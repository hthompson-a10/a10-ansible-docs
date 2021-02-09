.. _a10_export_module:


a10_export -- Configures A10 export
===================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Put files to remote site






Parameters
----------

  lw_4o6_binding_table_validation_log (False, any, None)
    LW-4over6 Binding Table Validation Log File


  ssl_key (False, any, None)
    SSL Key File


  ssl_crl (False, any, None)
    SSL Crl File


  ansible_username (True, any, None)
    Username for AXAPI authentication


  tgz (False, any, None)
    Export the merged pcap in .tgz format


  local_uri_file (False, any, None)
    Local URI files for http response


  ssl_cert_key (False, any, None)
    Local SSL Key/Certificate file name


  mon_entity_debug_file (False, any, None)
    Enter Mon entity debug file name


  status_check (False, any, None)
    check export task status


  dnssec_ds (False, any, None)
    DNSSEC DS file for child zone


  running_config (False, any, None)
    Running Config


  use_mgmt_port (False, any, None)
    Use management port as source port


  auth_jwks (False, any, None)
    Json web key


  aflex (False, any, None)
    aFleX Script Source File


  file_inspection_bw_list (False, any, None)
    Black white List File


  per_cpu (False, any, None)
    Export the per-cpu files along with the merged pcap file in .tgz format


  externalfilename (False, any, None)
    Export the External Program from the System


  lw_4o6 (False, any, None)
    LW-4over6 Binding Table File


  a10_partition (False, any, None)
    Destination/target partition for object/command


  debug_monitor (False, any, None)
    Debug Monitor Output


  store_name (False, any, None)
    Export store name


  state (True, any, None)
    State of the object to be created.


  geo_location (False, any, None)
    Geo-location CSV File


  ip_map_list (False, any, None)
    IP Map List File


  policy (False, any, None)
    WAF policy File


  saml_idp_name (False, any, None)
    SAML metadata of identity provider


  store (False, any, None)
    Field store


    create (optional, any, None)
      Create an export store profile


    remote_file (optional, any, None)
      Field remote_file


    name (optional, any, None)
      profile name to store remote url


    delete (optional, any, None)
      Delete an export store profile



  csr (False, any, None)
    Certificate Signing Request


  fixed_nat_archive (False, any, None)
    Fixed NAT Port Mapping Archive File


  auth_portal_image (False, any, None)
    Image file for default portal


  ca_cert (False, any, None)
    CA Cert File


  visibility (False, any, None)
    Export Visibility module related files


  class_list (False, any, None)
    Class List File


  axdebug (False, any, None)
    AX Debug Packet File


  profile (False, any, None)
    Startup-config Profile


  xml_schema (False, any, None)
    XML-Schema File


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  wsdl (False, any, None)
    Web Services Definition Language File


  fixed_nat (False, any, None)
    Fixed NAT Port Mapping File


  dnssec_dnskey (False, any, None)
    DNSSEC DNSKEY(KSK) file for child zone


  ansible_host (True, any, None)
    Host for AXAPI authentication


  auth_portal (False, any, None)
    Portal file for http authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ssl_cert (False, any, None)
    SSL Cert File


  merged_pcap (False, any, None)
    Export the merged pcap file when there are multiple Export sessions


  syslog (False, any, None)
    Enter 'messages' as the default syslog file name


  ansible_password (True, any, None)
    Password for AXAPI authentication


  startup_config (False, any, None)
    Startup Config


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

