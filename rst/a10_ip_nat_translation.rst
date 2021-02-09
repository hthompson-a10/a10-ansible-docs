.. _a10_ip_nat_translation_module:


a10_ip_nat_translation -- Configures A10 ip.nat.translation
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Change or Disable NAT translation values






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  service_timeout_list (False, any, None)
    Field service_timeout_list


    service_type (optional, any, None)
      'tcp'= TCP Protocol; 'udp'= UDP Protocol;


    timeout_type (optional, any, None)
      'age'= Expiration time; 'fast'= Use Fast aging;


    timeout_val (optional, any, None)
      Timeout in seconds (Interval of 60 seconds)


    port (optional, any, None)
      Port Number


    uuid (optional, any, None)
      uuid of the object



  tcp_timeout (False, any, None)
    TCP protocol extended translations (Timeout in seconds (Interval of 60 seconds), default is 300 seconds (5 minutes))


  udp_timeout (False, any, None)
    UDP protocol extended translations (Timeout in seconds (Interval of 60 seconds), default is 300 seconds (5 minutes))


  ignore_tcp_msl (False, any, None)
    reclaim TCP resource immediately without MSL


  state (True, any, None)
    State of the object to be created.


  icmp_timeout (False, any, None)
    Field icmp_timeout


    icmp_timeout_val (optional, any, None)
      Timeout in seconds (Interval of 60 seconds)


    icmp_timeout (optional, any, None)
      'age'= Expiration time; 'fast'= Use Fast aging;



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

