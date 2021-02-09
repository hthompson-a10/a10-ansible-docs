.. _a10_logging_lsn_quota_exceeded_module:


a10_logging_lsn_quota_exceeded -- Configures A10 logging.lsn.quota-exceeded
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set LSN quota exceeded log parameters






Parameters
----------

  disable_pool_based (False, any, None)
    Disable log LSN user quota exceeded based on LSN pool(Default= enabled)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  msisdn (False, any, None)
    Mobile Subscriber Integrated Services Digital Netwrok-Number (MSISDN)


  custom1 (False, any, None)
    Customized attribute No.1


  custom2 (False, any, None)
    Customized attribute No.2


  custom3 (False, any, None)
    Customized attribute No.3


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  imei (False, any, None)
     International Mobile Equipment Identity (IMEI)


  ip_based (False, any, None)
    Log LSN user quota exceeded based on private IP(Default= disabled)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  with_radius_attribute (False, any, None)
    Log with radius attribute


  state (True, any, None)
    State of the object to be created.


  ansible_password (True, any, None)
    Password for AXAPI authentication


  imsi (False, any, None)
    International Mobile Subscriber Identity (IMSI)









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

