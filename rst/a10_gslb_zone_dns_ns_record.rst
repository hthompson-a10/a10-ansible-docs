.. _a10_gslb_zone_dns_ns_record_module:


a10_gslb_zone_dns_ns_record -- Configures A10 gslb.zone.dns-ns-record
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify DNS NS Record






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'hits'= Number of times the record has been used;



  oper (False, any, None)
    Field oper


    ns_name (optional, any, None)
      Specify Domain Name


    last_server (optional, any, None)
      Field last_server



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    hits (optional, any, None)
      Number of times the record has been used


    ns_name (optional, any, None)
      Specify Domain Name



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  ttl (False, any, None)
    Specify TTL


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  zone_name (optional, any, None)
    Key to identify parent object


  ns_name (True, any, None)
    Specify Domain Name


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

