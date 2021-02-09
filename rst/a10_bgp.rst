.. _a10_bgp_module:


a10_bgp -- Configures A10 bgp
=============================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Border Gateway Protocol (BGP)






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


  extended_asn_cap (False, any, None)
    Enable the router to send 4-octet ASN capabilities


  nexthop_trigger (False, any, None)
    Field nexthop_trigger


    delay (optional, any, None)
      Configure nexthop trigger delay time interval (Nexthop Trigger Delay time interval between 1 and 100)


    enable (optional, any, None)
      Enable the nexthop tracking functionality



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

