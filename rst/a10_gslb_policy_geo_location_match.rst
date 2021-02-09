.. _a10_gslb_policy_geo_location_match_module:


a10_gslb_policy_geo_location_match -- Configures A10 gslb.policy.geo-location-match
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify match order of geographic






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  geo_type_overlap (False, any, None)
    'global'= Global Geo-location; 'policy'= Policy Geo-location;


  overlap (False, any, None)
    Enable overlap mode to do longest match


  policy_name (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  match_first (False, any, None)
    'global'= Global Geo-location; 'policy'= Policy Geo-location;


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

