.. _a10_cgnv6_nat64_prefix_module:


a10_cgnv6_nat64_prefix -- Configures A10 cgnv6.nat64.prefix
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure NAT64 Prefix






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


  vrid (False, any, None)
    VRRP-A vrid (Specify ha VRRP-A vrid)


  state (True, any, None)
    State of the object to be created.


  class_list (False, any, None)
    Class-list to match for NAT64


  prefix_val (True, any, None)
    NAT64 Prefix


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

