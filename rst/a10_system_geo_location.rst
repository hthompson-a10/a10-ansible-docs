.. _a10_system_geo_location_module:


a10_system_geo_location -- Configures A10 system.geo-location
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure system global geo-location






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  geoloc_load_file_list (False, any, None)
    Field geoloc_load_file_list


    geo_location_load_filename (optional, any, None)
      Specify file to be loaded


    template_name (optional, any, None)
      CSV template to load this file



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  geolite2_city_include_ipv6 (False, any, None)
    Include IPv6 address


  ansible_password (True, any, None)
    Password for AXAPI authentication


  geo_location_iana (False, any, None)
    Load built-in IANA Database


  geo_location_geolite2_country (False, any, None)
    Load built-in Maxmind GeoLite2-Country database. Database available from http=//www.maxmind.com


  state (True, any, None)
    State of the object to be created.


  geo_location_geolite2_city (False, any, None)
    Load built-in Maxmind GeoLite2-City database. Database available from http=//www.maxmind.com


  entry_list (False, any, None)
    Field entry_list


    geo_locn_multiple_addresses (optional, any, None)
      Field geo_locn_multiple_addresses


    user_tag (optional, any, None)
      Customized tag


    uuid (optional, any, None)
      uuid of the object


    geo_locn_obj_name (optional, any, None)
      Specify geo-location name, section range is (1-15)



  geolite2_country_include_ipv6 (False, any, None)
    Include IPv6 address


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


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

