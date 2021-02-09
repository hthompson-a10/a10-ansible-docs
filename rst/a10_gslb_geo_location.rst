.. _a10_gslb_geo_location_module:


a10_gslb_geo_location -- Configures A10 gslb.geo-location
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure a GSLB global geo-location object






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  geo_locn_multiple_addresses (False, any, None)
    Field geo_locn_multiple_addresses


    first_ipv6_address (optional, any, None)
      Specify IPv6 address


    ip_addr2 (optional, any, None)
      Specify IP address range


    ipv6_addr2 (optional, any, None)
      Specify IPv6 address range


    geol_ipv6_mask (optional, any, None)
      Specify IPv6 mask


    geol_ipv4_mask (optional, any, None)
      Specify IPv4 mask


    first_ip_address (optional, any, None)
      Specify IP information (Specify IP address)



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  geo_locn_obj_name (True, any, None)
    Specify geo-location name, section range is (1-15)









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

