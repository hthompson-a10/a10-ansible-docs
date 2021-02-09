.. _a10_cgnv6_lsn_port_overloading_global_module:


a10_cgnv6_lsn_port_overloading_global -- Configures A10 cgnv6.lsn.port.overloading.global
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Port-Overloading Behavior






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  allow_different_user (False, any, None)
    Allow different users to overload the same port (default= disabled)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  unique (False, any, None)
    'destination-address'= Allow overloading when the destination addresses is unique; 'destination-address-and-port'= Allow overloading when the destination address and port 2-tuple is unique (default);


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

