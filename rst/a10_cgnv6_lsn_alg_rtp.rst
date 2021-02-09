.. _a10_cgnv6_lsn_alg_rtp_module:


a10_cgnv6_lsn_alg_rtp -- Configures A10 cgnv6.lsn.alg.rtp
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

RTP






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


  rtp_stun_timeout (False, any, None)
    RTP/RTCP STUN timeout (default= 5 minutes)}


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

