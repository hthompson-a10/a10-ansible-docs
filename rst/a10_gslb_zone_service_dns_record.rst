.. _a10_gslb_zone_service_dns_record_module:


a10_gslb_zone_service_dns_record -- Configures A10 gslb.zone.service.dns-record
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify DNS Record






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  data (False, any, None)
    Specify DNS Data


  ntype (True, any, None)
    Specify DNS Type


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  service_name (optional, any, None)
    Key to identify parent object


  service_port (optional, any, None)
    Key to identify parent object


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  zone_name (optional, any, None)
    Key to identify parent object


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

