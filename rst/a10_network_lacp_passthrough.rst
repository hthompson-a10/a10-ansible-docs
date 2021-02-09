.. _a10_network_lacp_passthrough_module:


a10_network_lacp_passthrough -- Configures A10 network.lacp-passthrough
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Peer ports to forward received lacp packets






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


  peer_from (True, any, None)
    Peer member to forward received LACP packets


  state (True, any, None)
    State of the object to be created.


  peer_to (True, any, None)
    Peer member to forward received LACP packets


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

