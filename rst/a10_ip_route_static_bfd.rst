.. _a10_ip_route_static_bfd_module:


a10_ip_route_static_bfd -- Configures A10 ip.route.static.bfd
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Bidirectional Forwarding Detection






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


  local_ip (True, any, None)
    Local IP address


  state (True, any, None)
    State of the object to be created.


  action (False, any, None)
    'down'= BFD down;  (BFD state)


  nexthop_ip (True, any, None)
    Nexthop IP address


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  template (False, any, None)
    Configure tracking template (bind tracking template name)


  threshold (False, any, None)
    action triggering threshold


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

