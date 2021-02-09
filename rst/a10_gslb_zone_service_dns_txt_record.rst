.. _a10_gslb_zone_service_dns_txt_record_module:


a10_gslb_zone_service_dns_txt_record -- Configures A10 gslb.zone.service.dns-txt-record
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify DNS TXT Record






Parameters
----------

  record_name (True, any, None)
    Specify the Object Name for TXT Data


  ansible_username (True, any, None)
    Username for AXAPI authentication


  service_name (optional, any, None)
    Key to identify parent object


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


    record_name (optional, any, None)
      Specify the Object Name for TXT Data



  uuid (False, any, None)
    uuid of the object


  service_port (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  ansible_password (True, any, None)
    Password for AXAPI authentication


  txt_data (False, any, None)
    Specify TXT Data









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

