.. _a10_slb_virtual_server_port_stats_http_vport_module:


a10_slb_virtual_server_port_stats_http_vport -- Configures A10 slb.virtual-server.port.stats.http-vport
=======================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Statistics for the object port






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  protocol (optional, any, None)
    Key to identify parent object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  virtual_server_name (optional, any, None)
    Key to identify parent object


  port_number (optional, any, None)
    Key to identify parent object


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  stats (False, any, None)
    Field stats


    http_vport (optional, any, None)
      Field http_vport



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

