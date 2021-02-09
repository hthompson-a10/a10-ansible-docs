.. _a10_license_manager_host_module:


a10_license_manager_host -- Configures A10 license-manager.host
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure license manager host






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  host_ipv4 (True, any, None)
    license server ip address (length=1-31)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  host_ipv6 (True, any, None)
    Configure license manager server ipv6-address


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (False, any, None)
    Configure the license manager port, default is 443


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

