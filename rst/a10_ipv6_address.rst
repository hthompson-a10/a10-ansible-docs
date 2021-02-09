.. _a10_ipv6_address_module:


a10_ipv6_address -- Configures A10 ipv6.address
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Transparent mode IPv6 Address






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


  ipv6_address (False, any, None)
    IPV6 address


  state (True, any, None)
    State of the object to be created.


  anycast (False, any, None)
    Configure an IPv6 anycast address


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  link_local (False, any, None)
    Configure an IPv6 link local address


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

