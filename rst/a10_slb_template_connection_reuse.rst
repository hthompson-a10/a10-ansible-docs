.. _a10_slb_template_connection_reuse_module:


a10_slb_template_connection_reuse -- Configures A10 slb.template.connection-reuse
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Connection Reuse






Parameters
----------

  preopen (False, any, None)
    Preopen server connection


  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Connection Reuse Template Name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  num_conn_per_port (False, any, None)
    Connections per Server Port (default 100)


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  keep_alive_conn (False, any, None)
    Keep a number of server connections open


  state (True, any, None)
    State of the object to be created.


  limit_per_server (False, any, None)
    Max Server Connections allowed (Connections per Server Port (default 1000))


  timeout (False, any, None)
    Timeout in seconds. Multiple of 60 (default 2400)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


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

