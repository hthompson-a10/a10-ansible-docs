.. _a10_slb_common_dns_response_rate_limiting_module:


a10_slb_common_dns_response_rate_limiting -- Configures A10 slb.common.dns-response-rate-limiting
=================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

DNS Response-Rate-Limiting Global Settings






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


  max_table_entries (False, any, None)
    Maximum number of entries allowed


  state (True, any, None)
    State of the object to be created.


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

