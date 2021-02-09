.. _a10_dnssec_template_module:


a10_dnssec_template -- Configures A10 dnssec.template
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

template Settings






Parameters
----------

  dnssec_template_ksk (False, any, None)
    Field dnssec_template_ksk


    ksk_lifetime_v (optional, any, None)
      Default value is 365 days


    ksk_keysize_k (optional, any, None)
      Specify the number of bits in the DNSSEC KSK keys


    ksk_keysize_v (optional, any, None)
      Default size is 2048 and must be an exact multiple of 64


    ksk_lifetime_k (optional, any, None)
      Set the lifetime for DNSSEC KSK keys in days


    zsk_rollover_time_v (optional, any, None)
      7 days less than the lifetime by default


    ksk_rollover_time_k (optional, any, None)
      Set the rollover time in days



  dnskey_ttl_v (False, any, None)
    in seconds, 14400 seconds by default


  ansible_username (True, any, None)
    Username for AXAPI authentication


  hsm (False, any, None)
    specify the HSM template


  dnssec_temp_name (True, any, None)
    DNSSEC Template Name


  enable_nsec3 (False, any, None)
    enable NSEC3 support. disabled by default


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  dnskey_ttl_k (False, any, None)
    The TTL value of DNSKEY RR


  a10_partition (False, any, None)
    Destination/target partition for object/command


  return_nsec_on_failure (False, any, None)
    return NSEC/NSEC3 or not on failure case. return by default


  signature_validity_period_k (False, any, None)
    The period that a signature is valid


  ansible_port (True, any, None)
    Port for AXAPI authentication


  dnssec_template_zsk (False, any, None)
    Field dnssec_template_zsk


    zsk_rollover_time_k (optional, any, None)
      Set the rollover time in days


    zsk_keysize_k (optional, any, None)
      Specify the number of bits in the DNSSEC ZSK keys


    zsk_lifetime_v (optional, any, None)
      Default value is 90 days


    zsk_keysize_v (optional, any, None)
      Default size is 2048 and must be an exact multiple of 64


    zsk_lifetime_k (optional, any, None)
      Set the lifetime for DNSSEC ZSK keys in days


    zsk_rollover_time_v (optional, any, None)
      7 days less than the lifetime by default



  uuid (False, any, None)
    uuid of the object


  algorithm (False, any, None)
    'RSASHA1'= RSASHA1 algorithm; 'RSASHA256'= RSASHA256 algorithm; 'RSASHA512'= RSASHA512 algorithm;


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  combinations_limit (False, any, None)
    the max number of combinations per RRset (Default value is 31)


  user_tag (False, any, None)
    Customized tag


  signature_validity_period_v (False, any, None)
    in days, 10 days by default









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

