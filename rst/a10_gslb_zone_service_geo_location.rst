.. _a10_gslb_zone_service_geo_location_module:


a10_gslb_zone_service_geo_location -- Configures A10 gslb.zone.service.geo-location
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Geo location settings






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  service_name (optional, any, None)
    Key to identify parent object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  action (False, any, None)
    Action for this geo-location


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  zone_name (optional, any, None)
    Key to identify parent object


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  geo_name (True, any, None)
    Specify the geo-location


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  service_port (optional, any, None)
    Key to identify parent object


  alias (False, any, None)
    Field alias


    alias (optional, any, None)
      Send CNAME response for this geo-location (Specify a CNAME record)



  state (True, any, None)
    State of the object to be created.


  action_type (False, any, None)
    'allow'= Allow query from this geo-location; 'drop'= Drop query from this geo- location; 'forward'= Forward packet for this geo-location; 'ignore'= Send empty response to this geo-location; 'reject'= Send refuse response to this geo- location;


  policy (False, any, None)
    Policy for this geo-location (Specify the policy name)


  user_tag (False, any, None)
    Customized tag


  forward_type (False, any, None)
    'both'= Forward both query and response; 'query'= Forward query from this geo- location; 'response'= Forward response to this geo-location;









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

