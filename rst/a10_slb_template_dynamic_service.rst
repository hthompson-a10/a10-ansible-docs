.. _a10_slb_template_dynamic_service_module:


a10_slb_template_dynamic_service -- Configures A10 slb.template.dynamic-service
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Dynamic service template






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  dns_server (False, any, None)
    Field dns_server


    ipv4_dns_server (optional, any, None)
      DNS Server IPv4 Address


    ipv6_dns_server (optional, any, None)
      DNS Server IPv6 Address



  name (True, any, None)
    Dynamic Service Template Name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


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

