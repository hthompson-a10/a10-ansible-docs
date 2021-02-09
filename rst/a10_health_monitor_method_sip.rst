.. _a10_health_monitor_method_sip_module:


a10_health_monitor_method_sip -- Configures A10 health.monitor.method.sip
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

SIP type






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  sip (False, any, None)
    SIP type


  expect_response_code (False, any, None)
    Specify accepted response codes (e.g. 200, 400-430, any) (Format is xxx,xxx- xxx,any (xxx between [100,899]))


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  monitor_name (optional, any, None)
    Key to identify parent object


  register (False, any, None)
    Send SIP REGISTER message, default is to send OPTION message


  sip_port (False, any, None)
    Specify the SIP port, default is 5060 (Port Number)


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  sip_tcp (False, any, None)
    Use TCP for transmission, default is UDP


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

