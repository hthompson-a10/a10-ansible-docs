.. _a10_gslb_zone_service_dns_cname_record_module:


a10_gslb_zone_service_dns_cname_record -- Configures A10 gslb.zone.service.dns-cname-record
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify DNS CNAME Record






Parameters
----------

  weight (False, any, None)
    Specify Weight, default is 1


  ansible_username (True, any, None)
    Username for AXAPI authentication


  service_name (optional, any, None)
    Key to identify parent object


  admin_preference (False, any, None)
    Specify Administrative Preference, default is 100


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
      'all'= all; 'cname-hits'= Number of times the CNAME has been used;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    cname_hits (optional, any, None)
      Number of times the CNAME has been used


    alias_name (optional, any, None)
      Specify the alias name



  uuid (False, any, None)
    uuid of the object


  alias_name (True, any, None)
    Specify the alias name


  state (True, any, None)
    State of the object to be created.


  as_backup (False, any, None)
    As backup when fail


  service_port (optional, any, None)
    Key to identify parent object


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

