.. _a10_gslb_zone_dns_mx_record_module:


a10_gslb_zone_dns_mx_record -- Configures A10 gslb.zone.dns-mx-record
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify DNS MX Record






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'hits'= Number of times the record has been used;



  mx_name (True, any, None)
    Specify Domain Name


  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    mx_name (optional, any, None)
      Specify Domain Name


    hits (optional, any, None)
      Number of times the record has been used



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  priority (False, any, None)
    Specify Priority


  state (True, any, None)
    State of the object to be created.


  ttl (False, any, None)
    Specify TTL


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  zone_name (optional, any, None)
    Key to identify parent object


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  oper (False, any, None)
    Field oper


    mx_name (optional, any, None)
      Specify Domain Name


    last_server (optional, any, None)
      Field last_server










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

