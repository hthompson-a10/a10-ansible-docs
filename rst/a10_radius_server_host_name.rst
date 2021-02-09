.. _a10_radius_server_host_name_module:


a10_radius_server_host_name -- Configures A10 radius-server.host.name
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify the hostname of RADIUS server






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


  hostname (True, any, None)
    Hostname of RADIUS server


  state (True, any, None)
    State of the object to be created.


  secret (False, any, None)
    Field secret


    encrypted (optional, any, None)
       Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


    secret_value (optional, any, None)
      The RADIUS server's secret


    port_cfg (optional, any, None)
      Field port_cfg



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

