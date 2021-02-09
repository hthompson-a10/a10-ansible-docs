.. _a10_network_bfd_module:


a10_network_bfd -- Configures A10 network.bfd
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure BFD (Bidirectional Forwarding Detection)






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  enable (False, any, None)
    Enable BFD


  interval_cfg (False, any, None)
    Field interval_cfg


    interval (optional, any, None)
      Transmit interval between BFD packets (Milliseconds (default= 800))


    min_rx (optional, any, None)
      Minimum receive interval capability (Milliseconds (default= 800))


    multiplier (optional, any, None)
      Multiplier value used to compute holddown (value used to multiply the interval (default= 4))



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  echo (False, any, None)
    Enable BFD Echo


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

