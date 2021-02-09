.. _a10_cgnv6_template_logging_source_address_module:


a10_cgnv6_template_logging_source_address -- Configures A10 cgnv6.template.logging.source-address
=================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify source address of logging packet






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ip (False, any, None)
    Specify source IP address


  ansible_password (True, any, None)
    Password for AXAPI authentication


  logging_name (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  ipv6 (False, any, None)
    Specify source IPv6 address


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

