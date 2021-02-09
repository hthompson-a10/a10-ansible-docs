.. _a10_gslb_zone_service_dns_naptr_record_module:


a10_gslb_zone_service_dns_naptr_record -- Configures A10 gslb.zone.service.dns-naptr-record
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify DNS NAPTR Record






Parameters
----------

  service_proto (True, any, None)
    Specify Service and Protocol


  ansible_username (True, any, None)
    Username for AXAPI authentication


  service_name (optional, any, None)
    Key to identify parent object


  zone_name (optional, any, None)
    Key to identify parent object


  flag (True, any, None)
    Specify the flag (e.g., a, s). Default is empty flag


  preference (False, any, None)
    Specify Preference


  ttl (False, any, None)
    Specify TTL


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  regexp (False, any, None)
    Return the regular expression


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'naptr-hits'= Number of times the NAPTR has been used;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    naptr_target (optional, any, None)
      Specify the replacement or regular expression


    flag (optional, any, None)
      Specify the flag (e.g., a, s). Default is empty flag


    service_proto (optional, any, None)
      Specify Service and Protocol


    naptr_hits (optional, any, None)
      Number of times the NAPTR has been used



  uuid (False, any, None)
    uuid of the object


  naptr_target (True, any, None)
    Specify the replacement or regular expression


  state (True, any, None)
    State of the object to be created.


  service_port (optional, any, None)
    Key to identify parent object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  order (False, any, None)
    Specify Order









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

