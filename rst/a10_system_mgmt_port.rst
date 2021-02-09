.. _a10_system_mgmt_port_module:


a10_system_mgmt_port -- Configures A10 system.mgmt-port
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

set management port






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  port_index (False, any, None)
    port index to be configured (Specify port index)


  pci_address (False, any, None)
    pci-address to be configured as mgmt port


  state (True, any, None)
    State of the object to be created.


  mac_address (False, any, None)
    mac-address to be configured as mgmt port


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

