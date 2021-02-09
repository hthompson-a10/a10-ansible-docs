.. _a10_gslb_system_module:


a10_gslb_system -- Configures A10 gslb.system
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

GSLB system options






Parameters
----------

  age_interval (False, any, None)
    Interval to age runtime statistics. 0= never age, default is 10 (Time, unit= sec, default is 10)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  gslb_service_ip (False, any, None)
    GSLB Service-IP


  gslb_load_file_list (False, any, None)
    Field gslb_load_file_list


    geo_location_load_filename (optional, any, None)
      Specify file to be loaded


    template_name (optional, any, None)
      CSV template to load this file



  module (False, any, None)
    Specify Auto Map Module


  gslb_site (False, any, None)
    GSLB Site


  ttl (False, any, None)
    Specify Auto Map TTL (TTL, default is 300)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  gslb_group (False, any, None)
    GSLB Group


  wait (False, any, None)
    Disable GSLB until timeout if system is not ready (Time, unit= sec, default is 0)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  slb_device (False, any, None)
    SLB Device


  hostname (False, any, None)
    System's Network Name


  geo_location_iana (False, any, None)
    Load built-in IANA table


  ip_ttl (False, any, None)
    TTL of IP packets, default is 0 (IP TTL value, default is 0)


  state (True, any, None)
    State of the object to be created.


  slb_server (False, any, None)
    SLB Server


  ansible_password (True, any, None)
    Password for AXAPI authentication


  slb_virtual_server (False, any, None)
    SLB Virtual Server









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

