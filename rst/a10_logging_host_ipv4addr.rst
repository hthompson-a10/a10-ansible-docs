.. _a10_logging_host_ipv4addr_module:


a10_logging_host_ipv4addr -- Configures A10 logging.host.ipv4addr
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

host DNS name or ipv4 address of remote syslog server






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  host_ipv4 (True, any, None)
    Set syslog host ip address


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  tcp (False, any, None)
    Use TCP as transport protocol


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  use_mgmt_port (False, any, None)
    Use management port for connections


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (False, any, None)
    Set remote syslog port number


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

