.. _a10_gslb_site_slb_dev_vip_server_vip_server_v4_module:


a10_gslb_site_slb_dev_vip_server_vip_server_v4 -- Configures A10 gslb.site.slb.dev.vip.server.vip-server-v4
===========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify a VIP for the SLB device






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'dev_vip_hits'= Number of times the service-ip was selected;



  oper (False, any, None)
    Field oper


    dev_vip_addr (optional, any, None)
      Field dev_vip_addr


    ipv4 (optional, any, None)
      Specify IP address


    dev_vip_state (optional, any, None)
      Field dev_vip_state


    dev_vip_port_list (optional, any, None)
      Field dev_vip_port_list



  ansible_port (True, any, None)
    Port for AXAPI authentication


  site_name (optional, any, None)
    Key to identify parent object


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  slb_dev_device_name (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  ipv4 (True, any, None)
    Specify IP address


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  stats (False, any, None)
    Field stats


    ipv4 (optional, any, None)
      Specify IP address


    dev_vip_hits (optional, any, None)
      Number of times the service-ip was selected



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

