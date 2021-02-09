.. _a10_network_mac_age_time_module:


a10_network_mac_age_time -- Configures A10 network.mac-age-time
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set Aging period for all MAC Interfaces






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


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  aging_time (False, any, None)
    Set aging period in seconds for all MAC interfaces (default 300 seconds)


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

