.. _a10_gslb_policy_geo_location_module:


a10_gslb_policy_geo_location -- Configures A10 gslb.policy.geo-location
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify geo-location






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Specify geo-location name, section range is (1-15)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  policy_name (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  ip_multiple_fields (False, any, None)
    Field ip_multiple_fields


    ip_mask_sub (optional, any, None)
      Specify IP/mask format (Specify IP address mask)


    ip_addr2_sub (optional, any, None)
      Specify IP address range


    ip_sub (optional, any, None)
      Specify IP information



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ipv6_multiple_fields (False, any, None)
    Field ipv6_multiple_fields


    ipv6_sub (optional, any, None)
      Specify IPv6 information


    ipv6_mask_sub (optional, any, None)
      Specify IPv6/mask format (Specify IP address mask)


    ipv6_addr2_sub (optional, any, None)
      Specify IPv6 address range



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


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

