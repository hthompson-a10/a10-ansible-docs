.. _a10_debug_lb_module:


a10_debug_lb -- Configures A10 debug.lb
=======================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Load Balancing debug switch parameter






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  cfg (False, any, None)
    Load Balancing configuration debug switch


  flow (False, any, None)
    Packet flow debug switch


  all (False, any, None)
    Load Balancing debug all switch


  clb (False, any, None)
    Cache Load Balancing debug switch


  fwlb (False, any, None)
    Firewall Load Balancing debug switch


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  llb (False, any, None)
    Link Load Balancing debug switch


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  slb (False, any, None)
    Server Load Balancing debug switch









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

