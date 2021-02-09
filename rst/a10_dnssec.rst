.. _a10_dnssec_module:


a10_dnssec -- Configures A10 dnssec
===================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Domain Name System Security Extensions commands






Parameters
----------

  template_list (False, any, None)
    Field template_list


    signature_validity_period_k (optional, any, None)
      The period that a signature is valid


    dnssec_template_ksk (optional, any, None)
      Field dnssec_template_ksk


    dnssec_template_zsk (optional, any, None)
      Field dnssec_template_zsk


    dnskey_ttl_v (optional, any, None)
      in seconds, 14400 seconds by default


    uuid (optional, any, None)
      uuid of the object


    algorithm (optional, any, None)
      'RSASHA1'= RSASHA1 algorithm; 'RSASHA256'= RSASHA256 algorithm; 'RSASHA512'= RSASHA512 algorithm;


    return_nsec_on_failure (optional, any, None)
      return NSEC/NSEC3 or not on failure case. return by default


    hsm (optional, any, None)
      specify the HSM template


    dnssec_temp_name (optional, any, None)
      DNSSEC Template Name


    enable_nsec3 (optional, any, None)
      enable NSEC3 support. disabled by default


    dnskey_ttl_k (optional, any, None)
      The TTL value of DNSKEY RR


    combinations_limit (optional, any, None)
      the max number of combinations per RRset (Default value is 31)


    user_tag (optional, any, None)
      Customized tag


    signature_validity_period_v (optional, any, None)
      in days, 10 days by default



  oper (False, any, None)
    Field oper


    ptr_memory (optional, any, None)
      Field ptr_memory


    total_memory (optional, any, None)
      Field total_memory


    reference_objects (optional, any, None)
      Field reference_objects


    cname_memory (optional, any, None)
      Field cname_memory


    ds_objects (optional, any, None)
      Field ds_objects


    nsec_objects (optional, any, None)
      Field nsec_objects


    array_memory (optional, any, None)
      Field array_memory


    nsec3param_objects (optional, any, None)
      Field nsec3param_objects


    srv_memory (optional, any, None)
      Field srv_memory


    reference_memory (optional, any, None)
      Field reference_memory


    a_memory (optional, any, None)
      Field a_memory


    table_memory (optional, any, None)
      Field table_memory


    a_objects (optional, any, None)
      Field a_objects


    ns_memory (optional, any, None)
      Field ns_memory


    aaaa_memory (optional, any, None)
      Field aaaa_memory


    zone_objects (optional, any, None)
      Field zone_objects


    table_objects (optional, any, None)
      Field table_objects


    mx_memory (optional, any, None)
      Field mx_memory


    soa_memory (optional, any, None)
      Field soa_memory


    domain_objects (optional, any, None)
      Field domain_objects


    nsec_memory (optional, any, None)
      Field nsec_memory


    nsec3_objects (optional, any, None)
      Field nsec3_objects


    srv_objects (optional, any, None)
      Field srv_objects


    array_objects (optional, any, None)
      Field array_objects


    ns_objects (optional, any, None)
      Field ns_objects


    soa_objects (optional, any, None)
      Field soa_objects


    ds_memory (optional, any, None)
      Field ds_memory


    cname_objects (optional, any, None)
      Field cname_objects


    domain_memory (optional, any, None)
      Field domain_memory


    nsec3param_memory (optional, any, None)
      Field nsec3param_memory


    txt_memory (optional, any, None)
      Field txt_memory


    dnskey_memory (optional, any, None)
      Field dnskey_memory


    total_objects (optional, any, None)
      Field total_objects


    ptr_objects (optional, any, None)
      Field ptr_objects


    aaaa_objects (optional, any, None)
      Field aaaa_objects


    mx_objects (optional, any, None)
      Field mx_objects


    txt_objects (optional, any, None)
      Field txt_objects


    rrsig_objects (optional, any, None)
      Field rrsig_objects


    rrsig2_memory (optional, any, None)
      Field rrsig2_memory


    nsec3_memory (optional, any, None)
      Field nsec3_memory


    zone_memory (optional, any, None)
      Field zone_memory


    rrsig2_objects (optional, any, None)
      Field rrsig2_objects


    rrsig_memory (optional, any, None)
      Field rrsig_memory


    dnskey_objects (optional, any, None)
      Field dnskey_objects



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  standalone (False, any, None)
    Run DNSSEC in standalone mode, in GSLB group mode by default


  sign_zone_now (False, any, None)
    Field sign_zone_now


    zone_name (optional, any, None)
      Specify the name for the DNS zone, empty means sign all zones



  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  dnskey (False, any, None)
    Field dnskey


    zone_name (optional, any, None)
      DNS zone name of the child zone


    key_delete (optional, any, None)
      Delete the DNSKEY file



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ds (False, any, None)
    Field ds


    zone_name (optional, any, None)
      DNS zone name of the child zone


    ds_delete (optional, any, None)
      Delete the DS file



  key_rollover (False, any, None)
    Field key_rollover


    zsk_start (optional, any, None)
      start ZSK rollover in emergency mode


    zone_name (optional, any, None)
      Specify the name for the DNS zone


    ds_ready_in_parent_zone (optional, any, None)
      DS RR is already ready in the parent zone


    dnssec_key_type (optional, any, None)
      'ZSK'= Zone Signing Key; 'KSK'= Key Signing Key;


    ksk_start (optional, any, None)
      start KSK rollover in emergency mode










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

