.. _a10_slb_template_http_policy_module:


a10_slb_template_http_policy -- Configures A10 slb.template.http-policy
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

http-policy template






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    http-policy template name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  cookie_name (False, any, None)
    name of cookie to match (Cookie Name)


  geo_location_match (False, any, None)
    Field geo_location_match


    geo_location_template_name (optional, any, None)
      WAF template to be used (Template Name)


    geo_location_service_group (optional, any, None)
      Service Group to be used (Service Group Name)


    geo_location (optional, any, None)
      Geolocation name


    geo_location_template (optional, any, None)
      'waf'= waf;  (WAF template to be used)



  state (True, any, None)
    State of the object to be created.


  http_policy_match (False, any, None)
    Field http_policy_match


    service_group (optional, any, None)
      Service Group to be used (Service Group Name)


    match_type (optional, any, None)
      'contains'= Select service group if URL string contains another string; 'ends- with'= Select service group if URL string ends with another string; 'equals'= Select service group if URL string equals another string; 'starts-with'= Select service group if URL string starts with another string;


    template (optional, any, None)
      'waf'= waf;  (WAF template to be used)


    template_name (optional, any, None)
      WAF template to be used (Template Name)


    ntype (optional, any, None)
      'cookie'= cookie value match; 'host'= hostname match; 'url'= URL match;


    match_string (optional, any, None)
      URL String



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  uuid (False, any, None)
    uuid of the object









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

