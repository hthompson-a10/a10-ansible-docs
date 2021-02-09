.. _a10_threat_intel_threat_list_module:


a10_threat_intel_threat_list -- Configures A10 threat-intel.threat-list
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Threat Categories for malicious IPs






Parameters
----------

  spam_sources (False, any, None)
    IP's tunneling spam messages through a proxy, anomalous SMTP activities, and forum spam activities


  botnets (False, any, None)
    Botnet C&C channels, and infected zombie machines controlled by Bot master


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ntype (False, any, None)
    'webroot'= Configure Webroot threat categories;


  proxy (False, any, None)
    IP addresses providing proxy services


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  name (True, any, None)
    Threat category List name


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'spam-sources'= Hits for spam sources; 'windows-exploits'= Hits for windows exploits; 'web-attacks'= Hits for web attacks; 'botnets'= Hits for botnets; 'scanners'= Hits for scanners; 'dos-attacks'= Hits for dos attacks; 'reputation'= Hits for reputation; 'phishing'= Hits for phishing; 'proxy'= Hits for proxy; 'mobile-threats'= Hits for mobile threats; 'tor-proxy'= Hits for tor-proxy; 'total-hits'= Total hits for threat-list;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    spam_sources (optional, any, None)
      Hits for spam sources


    botnets (optional, any, None)
      Hits for botnets


    name (optional, any, None)
      Threat category List name


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


    total_hits (optional, any, None)
      Total hits for threat-list


    tor_proxy (optional, any, None)
      Hits for tor-proxy


    scanners (optional, any, None)
      Hits for scanners


    windows_exploits (optional, any, None)
      Hits for windows exploits


    reputation (optional, any, None)
      Hits for reputation



  uuid (False, any, None)
    uuid of the object


  phishing (False, any, None)
    IP addresses hosting phishing sites, ad click fraud or gaming fraud


  ansible_password (True, any, None)
    Password for AXAPI authentication


  web_attacks (False, any, None)
    IP's associated with cross site scripting, iFrame injection, SQL injection, cross domain injection, or domain password brute fo


  mobile_threats (False, any, None)
    IP's associated with mobile threats


  state (True, any, None)
    State of the object to be created.


  dos_attacks (False, any, None)
    IP's participating in DOS, DDOS, anomalous sync flood, and anomalous traffic detection


  reputation (False, any, None)
    IP addresses currently known to be infected with malware


  all_categories (False, any, None)
    Enable all categories


  tor_proxy (False, any, None)
    IP's providing tor proxy services


  user_tag (False, any, None)
    Customized tag


  scanners (False, any, None)
    IP's associated with probes, host scan, domain scan, and password brute force attack


  windows_exploits (False, any, None)
    IP's associated with malware, shell code, rootkits, worms or viruses









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

