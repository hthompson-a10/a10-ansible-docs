.. _a10_health_monitor_method_tcp_module:


a10_health_monitor_method_tcp -- Configures A10 health.monitor.method.tcp
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

TCP type






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  port_resp (False, any, None)
    Field port_resp


    port_contains (optional, any, None)
      Mark server up if response string contains another string (Specify the string)



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  monitor_name (optional, any, None)
    Key to identify parent object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  port_halfopen (False, any, None)
    Set TCP SYN check


  port_send (False, any, None)
    Send a string to server (Specify the string)


  method_tcp (False, any, None)
    TCP type


  state (True, any, None)
    State of the object to be created.


  tcp_port (False, any, None)
    Specify TCP port (Specify port number)


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

