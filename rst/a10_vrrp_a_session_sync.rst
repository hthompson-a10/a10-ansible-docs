.. _a10_vrrp_a_session_sync_module:


a10_vrrp_a_session_sync -- Configures A10 vrrp.a.session-sync
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enable/Disable vrrp-a session sync






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


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  action (False, any, None)
    'enable'= enable vrrp-a session sync (default); 'disable'= disable vrrp-a session sync;


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

