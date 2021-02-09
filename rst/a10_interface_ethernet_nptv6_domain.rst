.. _a10_interface_ethernet_nptv6_domain_module:


a10_interface_ethernet_nptv6_domain -- Configures A10 interface.ethernet.nptv6.domain
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Apply NPTv6 translation domain on interface






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  bind_type (True, any, None)
    'inside'= This interface is connected to NPTv6 inside networks; 'outside'= This interface is connected to NPTv6 outside networks;


  domain_name (True, any, None)
    NPTv6 domain name


  state (True, any, None)
    State of the object to be created.


  ethernet_ifnum (optional, any, None)
    Key to identify parent object


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

