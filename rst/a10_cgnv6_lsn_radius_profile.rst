.. _a10_cgnv6_lsn_radius_profile_module:


a10_cgnv6_lsn_radius_profile -- Configures A10 cgnv6.lsn-radius-profile
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure LSN RADIUS Profile






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  lid_profile_index (True, any, None)
    LSN RADIUS Profile Index


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  radius (False, any, None)
    Field radius


    default_lsn_lid (optional, any, None)
      LSN Limit ID (LID index)


    starts_with_lsn_lid (optional, any, None)
      LSN Limit ID (LID index)


    exact_value_lsn_lid (optional, any, None)
      LSN Limit ID (LID index)


    attribute (optional, any, None)
      'custom1'= Configure RADIUS Attribute Custom 1; 'custom2'= Configure RADIUS Attribute Custom 2; 'custom3'= Configure RADIUS Attribute Custom 3; 'imei'= Configure RADIUS Attribute IMEI; 'imsi'= Configure RADIUS Attribute IMSI; 'msisdn'= Configure RADIUS Attribute MSISDN; 'default'= Configure default;


    exact_value (optional, any, None)
      Value of the attribute


    starts_with (optional, any, None)
      Value of the attribute



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


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

