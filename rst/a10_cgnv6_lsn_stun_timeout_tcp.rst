.. _a10_cgnv6_lsn_stun_timeout_tcp_module:


a10_cgnv6_lsn_stun_timeout_tcp -- Configures A10 cgnv6.lsn.stun.timeout.tcp
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set TCP STUN timeout






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  port_end (True, any, None)
    Port Range (Port Range End)


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  timeout (False, any, None)
    STUN timeout in minutes (default= 2 minutes)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  port_start (True, any, None)
    Port Range (Port Range Start)


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

