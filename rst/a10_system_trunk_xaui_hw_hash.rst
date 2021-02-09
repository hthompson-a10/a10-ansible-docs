.. _a10_system_trunk_xaui_hw_hash_module:


a10_system_trunk_xaui_hw_hash -- Configures A10 system.trunk-xaui-hw-hash
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set Trunk XAUI HW Hash Mode






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


  state (True, any, None)
    State of the object to be created.


  mode (False, any, None)
    Set HW hash mode, default is 6 (1=dst-mac 2=src-mac 3=src-dst-mac 4=src-ip 5=dst-ip 6=rtag6 7=rtag7)


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

