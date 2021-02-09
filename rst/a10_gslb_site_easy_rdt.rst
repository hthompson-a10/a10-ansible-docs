.. _a10_gslb_site_easy_rdt_module:


a10_gslb_site_easy_rdt -- Configures A10 gslb.site.easy-rdt
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Active RDT options






Parameters
----------

  site_name (optional, any, None)
    Key to identify parent object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  bind_geoloc (False, any, None)
    Bind RDT to geo-location


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  aging_time (False, any, None)
    Aging Time, Unit= min, default is 10


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ignore_count (False, any, None)
    Ignore count if RDT is out of range, default is 5


  mask (False, any, None)
    Client IP subnet mask, default is 32


  overlap (False, any, None)
    Enable overlap for geo-location to do longest match


  state (True, any, None)
    State of the object to be created.


  limit (False, any, None)
    Limit of valid RDT, default is 16383 (Limit, unit= millisecond)


  smooth_factor (False, any, None)
    Factor of Smooth RDT, default is 10


  ansible_password (True, any, None)
    Password for AXAPI authentication


  range_factor (False, any, None)
    Factor of RDT Range, default is 25 (Range Factor of Smooth RDT)









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

