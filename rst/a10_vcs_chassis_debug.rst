.. _a10_vcs_chassis_debug_module:


a10_vcs_chassis_debug -- Configures A10 vcs.chassis.debug
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

VCS debug






Parameters
----------

  vblade_msg (False, any, None)
    vBlade Message component


  info (False, any, None)
    Information component


  vblade (False, any, None)
    vBlade component


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  encoder (False, any, None)
    Encoder component


  util (False, any, None)
    Utility component


  ssl (False, any, None)
    SSL component


  election (False, any, None)
    Election component


  vmaster (False, any, None)
    vMaster component


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  daemon_msg (False, any, None)
    Daemon message component


  daemon (False, any, None)
    Daemon component


  lib (False, any, None)
    Lib component


  election_pdu (False, any, None)
    Election pdu component


  state (True, any, None)
    State of the object to be created.


  handler (False, any, None)
    Handler component


  net (False, any, None)
    Net component


  ansible_password (True, any, None)
    Password for AXAPI authentication


  vmaster_msg (False, any, None)
    vMaster Message component









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

