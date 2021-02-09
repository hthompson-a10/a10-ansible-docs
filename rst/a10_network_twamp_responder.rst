.. _a10_network_twamp_responder_module:


a10_network_twamp_responder -- Configures A10 network.twamp.responder
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure TWAMP responder






Parameters
----------

  both (False, any, None)
    Enable both IP and IPv6 TWAMP packets


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ip (False, any, None)
    Field ip


    acl_id (optional, any, None)
      ACL id


    uuid (optional, any, None)
      uuid of the object


    acl_name (optional, any, None)
      Apply a named access list (Access List name)



  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  ipv6 (False, any, None)
    Field ipv6


    v6_acl_name (optional, any, None)
      Apply an access list (Named Access List)


    uuid (optional, any, None)
      uuid of the object



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (False, any, None)
    Port number









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

