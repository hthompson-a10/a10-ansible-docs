.. _a10_interface_ethernet_map_module:


a10_interface_ethernet_map -- Configures A10 interface.ethernet.map
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure MAP on this interface






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


  inside (False, any, None)
    Configure MAP inside interface (connected to MAP domains)


  state (True, any, None)
    State of the object to be created.


  outside (False, any, None)
    Configure MAP outside interface


  ethernet_ifnum (optional, any, None)
    Key to identify parent object


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  map_t_inside (False, any, None)
    Configure MAP inside interface (connected to MAP domains)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  map_t_outside (False, any, None)
    Configure MAP outside interface









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

