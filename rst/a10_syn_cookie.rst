.. _a10_syn_cookie_module:


a10_syn_cookie -- Configures A10 syn-cookie
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Global Syn-Cookie Protection






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  enable (False, any, None)
    Global Syn-Cookie Protection


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  off_threshold (False, any, None)
    off-threshold for Syn-cookie (Decimal number)


  state (True, any, None)
    State of the object to be created.


  on_threshold (False, any, None)
    on-threshold for Syn-cookie (Decimal number)


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

