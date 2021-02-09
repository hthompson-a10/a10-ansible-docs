.. _a10_cgnv6_translation_service_timeout_module:


a10_cgnv6_translation_service_timeout -- Configures A10 cgnv6.translation.service-timeout
=========================================================================================

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


  port_end (False, any, None)
    End Port Number


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  timeout_val (False, any, None)
    Timeout in seconds (Interval of 60 seconds)


  fast (False, any, None)
    Use Fast Aging


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

