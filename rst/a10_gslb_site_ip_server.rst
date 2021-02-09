.. _a10_gslb_site_ip_server_module:


a10_gslb_site_ip_server -- Configures A10 gslb.site.ip-server
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify a real server for the GSLB site






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'hits'= Number of times the IP was selected;



  oper (False, any, None)
    Field oper


    ip_server_name (optional, any, None)
      Specify the real server name


    state (optional, any, None)
      Field state


    ip_address (optional, any, None)
      Field ip_address


    ip_server_port (optional, any, None)
      Field ip_server_port


    ip_server (optional, any, None)
      Field ip_server



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    ip_server_name (optional, any, None)
      Specify the real server name


    hits (optional, any, None)
      Number of times the IP was selected



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  ip_server_name (True, any, None)
    Specify the real server name


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  site_name (optional, any, None)
    Key to identify parent object


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

