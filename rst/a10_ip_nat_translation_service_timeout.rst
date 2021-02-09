.. _a10_ip_nat_translation_service_timeout_module:


a10_ip_nat_translation_service_timeout -- Configures A10 ip.nat.translation.service-timeout
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify any custom service timeout






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  timeout_type (False, any, None)
    'age'= Expiration time; 'fast'= Use Fast aging;


  ansible_password (True, any, None)
    Password for AXAPI authentication


  timeout_val (False, any, None)
    Timeout in seconds (Interval of 60 seconds)


  ansible_host (True, any, None)
    Host for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  service_type (True, any, None)
    'tcp'= TCP Protocol; 'udp'= UDP Protocol;


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (True, any, None)
    Port Number









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

