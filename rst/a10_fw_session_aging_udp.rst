.. _a10_fw_session_aging_udp_module:


a10_fw_session_aging_udp -- Configures A10 fw.session.aging.udp
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

UDP Aging options






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


  udp_idle_timeout (False, any, None)
    Idle Timeout (sec), default is 120 (number)


  session_aging_name (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  port_cfg (False, any, None)
    Field port_cfg


    udp_idle_timeout (optional, any, None)
      Idle Timeout (sec), default is 120 (number)


    udp_port (optional, any, None)
      Field udp_port










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

