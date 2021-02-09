.. _a10_threat_intel_webroot_global_module:


a10_threat_intel_webroot_global -- Configures A10 threat.intel.webroot-global
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Global counters for webroot module






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'spam-sources'= Hits for spam sources; 'windows-exploits'= Hits for windows exploits; 'web-attacks'= Hits for web attacks; 'botnets'= Hits for botnets; 'scanners'= Hits for scanners; 'dos-attacks'= Hits for dos attacks; 'reputation'= Hits for reputation; 'phishing'= Hits for phishing; 'proxy'= Hits for proxy; 'mobile-threats'= Hits for mobile threats; 'tor-proxy'= Hits for tor-proxy; 'rtu-lookup'= Number of lookups in RTU cache; 'database-lookup'= Number of lookups in database; 'non-malicious-ips'= IP's not found in database or RTU cache;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    spam_sources (optional, any, None)
      Hits for spam sources


    botnets (optional, any, None)
      Hits for botnets


    phishing (optional, any, None)
      Hits for phishing


    web_attacks (optional, any, None)
      Hits for web attacks


    mobile_threats (optional, any, None)
      Hits for mobile threats


    dos_attacks (optional, any, None)
      Hits for dos attacks


    proxy (optional, any, None)
      Hits for proxy


    rtu_lookup (optional, any, None)
      Number of lookups in RTU cache


    database_lookup (optional, any, None)
      Number of lookups in database


    tor_proxy (optional, any, None)
      Hits for tor-proxy


    non_malicious_ips (optional, any, None)
      IP's not found in database or RTU cache


    scanners (optional, any, None)
      Hits for scanners


    windows_exploits (optional, any, None)
      Hits for windows exploits


    reputation (optional, any, None)
      Hits for reputation



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

