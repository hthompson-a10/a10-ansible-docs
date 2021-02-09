.. _a10_gslb_service_group_module:


a10_gslb_service_group -- Configures A10 gslb.service-group
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify GSLB Service Group






Parameters
----------

  oper (False, any, None)
    Field oper


    session_list (optional, any, None)
      Field session_list


    service_group_name (optional, any, None)
      Specify Service Group name


    total_sessions (optional, any, None)
      Field total_sessions


    matched (optional, any, None)
      Field matched



  disable_site_list (False, any, None)
    Field disable_site_list


    disable_site (optional, any, None)
      Site name



  ansible_username (True, any, None)
    Username for AXAPI authentication


  service_group_name (True, any, None)
    Specify Service Group name


  ansible_password (True, any, None)
    Password for AXAPI authentication


  disable (False, any, None)
    Disable all members


  persistent_ipv6_mask (False, any, None)
    Specify IPv6 mask length, default is 128


  persistent_mask (False, any, None)
    Specify IP mask, default is /32


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  member (False, any, None)
    Field member


    member_name (optional, any, None)
      Service name



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  user_tag (False, any, None)
    Customized tag


  persistent_site (False, any, None)
    Persistent based on site


  state (True, any, None)
    State of the object to be created.


  persistent_aging_time (False, any, None)
    Specify aging-time, unit= min, default is 5 (Aging time)


  dependency_site (False, any, None)
    Dependency on site









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

