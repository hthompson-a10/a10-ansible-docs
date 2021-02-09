.. _a10_fw_session_aging_tcp_module:


a10_fw_session_aging_tcp -- Configures A10 fw.session.aging.tcp
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

TCP Aging options






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  tcp_idle_timeout (False, any, None)
    Idle Timeout (sec), default is 600 (number)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  session_aging_name (optional, any, None)
    Key to identify parent object


  ansible_host (True, any, None)
    Host for AXAPI authentication


  half_close_idle_timeout (False, any, None)
    TCP Half Close Idle Timeout (sec), default is off (number)


  state (True, any, None)
    State of the object to be created.


  force_delete_timeout (False, any, None)
    The maximum time that a session can stay in the system before being deleted, default is off (number (second))


  force_delete_timeout_100ms (False, any, None)
    The maximum time that a session can stay in the system before being deleted, default is off (number in 100ms)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  half_open_idle_timeout (False, any, None)
    TCP Half Open Idle Timeout (sec), default is off (number)


  port_cfg (False, any, None)
    Field port_cfg


    half_close_idle_timeout (optional, any, None)
      TCP Half Close Idle Timeout (sec), default is off (number)


    force_delete_timeout (optional, any, None)
      The maximum time that a session can stay in the system before being deleted, default is off (number (second))


    tcp_idle_timeout (optional, any, None)
      Idle Timeout (sec), default is 600 (number)


    force_delete_timeout_100ms (optional, any, None)
      The maximum time that a session can stay in the system before being deleted, default is off (number in 100ms)


    tcp_port (optional, any, None)
      Field tcp_port


    half_open_idle_timeout (optional, any, None)
      TCP Half Open Idle Timeout (sec), default is off (number)










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

