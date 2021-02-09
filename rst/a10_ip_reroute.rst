.. _a10_ip_reroute_module:


a10_ip_reroute -- Configures A10 ip.reroute
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

reroute sessions






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


  suppress_protocols (False, any, None)
    Field suppress_protocols


    isis (optional, any, None)
      ISIS


    uuid (optional, any, None)
      uuid of the object


    ospf (optional, any, None)
      OSPF


    rip (optional, any, None)
      RIP


    ibgp (optional, any, None)
      IBGP


    ebgp (optional, any, None)
      EBGP


    static (optional, any, None)
      Field static


    connected (optional, any, None)
      Field connected



  state (True, any, None)
    State of the object to be created.


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

