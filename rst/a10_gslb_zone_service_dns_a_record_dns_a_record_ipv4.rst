.. _a10_gslb_zone_service_dns_a_record_dns_a_record_ipv4_module:


a10_gslb_zone_service_dns_a_record_dns_a_record_ipv4 -- Configures A10 gslb.zone.service.dns.a.record.dns-a-record-ipv4
=======================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify DNS Address Record






Parameters
----------

  as_replace (False, any, None)
    Return this Service-IP when enable ip-replace


  weight (False, any, None)
    Specify weight for Service-IP (Weight value)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  service_name (optional, any, None)
    Key to identify parent object


  disable (False, any, None)
    Disable this Service-IP


  static (False, any, None)
    Return this Service-IP in DNS server mode


  ttl (False, any, None)
    Specify TTL for Service-IP


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  zone_name (optional, any, None)
    Key to identify parent object


  admin_ip (False, any, None)
    Specify admin priority of Service-IP (Specify the priority)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'hits'= Number of times the record has been used;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    hits (optional, any, None)
      Number of times the record has been used


    dns_a_record_ip (optional, any, None)
      Specify IP address



  uuid (False, any, None)
    uuid of the object


  dns_a_record_ip (True, any, None)
    Specify IP address


  service_port (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  as_backup (False, any, None)
    As backup when fail


  no_resp (False, any, None)
    Don't use this Service-IP as DNS response


  ansible_password (True, any, None)
    Password for AXAPI authentication









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

