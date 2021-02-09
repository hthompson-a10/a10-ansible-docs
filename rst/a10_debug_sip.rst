.. _a10_debug_sip_module:


a10_debug_sip -- Configures A10 debug.sip
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Debug SIP






Parameters
----------

  INVITE (False, any, None)
    Method INVITE


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ACK (False, any, None)
    Method ACK


  UPDATE (False, any, None)
    SIP Method UPDATE


  PUBLISH (False, any, None)
    SIP Method PUBLISH


  CANCEL (False, any, None)
    SIP Method CANCEL


  NOTIFY (False, any, None)
    SIP Method NOTIFY


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  BYE (False, any, None)
    SIP Method BYE


  a10_partition (False, any, None)
    Destination/target partition for object/command


  OPTIONS (False, any, None)
    SIP Method OPTIONS


  REFER (False, any, None)
    SIP Method REFER


  INFO (False, any, None)
    SIP Method INFO


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  REGISTER (False, any, None)
    SIP Method REGISTER


  PRACK (False, any, None)
    SIP Method PRACK


  ansible_host (True, any, None)
    Host for AXAPI authentication


  SUBSCRIBE (False, any, None)
    SIP Method SUBSCRIBE


  state (True, any, None)
    State of the object to be created.


  MESSAGE (False, any, None)
    SIP Method MESSAGE


  ansible_password (True, any, None)
    Password for AXAPI authentication


  method (False, any, None)
    Set filter with SIP method types









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

