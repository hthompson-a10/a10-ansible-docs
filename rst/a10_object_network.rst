.. _a10_object_network_module:


a10_object_network -- Configures A10 object.network
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Network Object






Parameters
----------

  description (False, any, None)
    Description of the object instance


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ip_range_start (False, any, None)
    IPv4 Host Address start


  ipv6_subnet (False, any, None)
    IPv6 Network Address


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ipv6_range_end (False, any, None)
    IPV6 Host address end


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  subnet (False, any, None)
    IPv4 Network Address


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ip_range_end (False, any, None)
    IPV4 Host address end


  uuid (False, any, None)
    uuid of the object


  user_tag (False, any, None)
    Customized tag


  state (True, any, None)
    State of the object to be created.


  ipv6_range_start (False, any, None)
    IPv6 Host Address start


  net_name (True, any, None)
    Network Object Name


  ansible_password (True, any, None)
    Password for AXAPI authentication









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

