.. _a10_interface_ve_bfd_module:


a10_interface_ve_bfd -- Configures A10 interface.ve.bfd
=======================================================

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


  interval_cfg (False, any, None)
    Field interval_cfg


    interval (optional, any, None)
      Transmit interval between BFD packets (Milliseconds)


    min_rx (optional, any, None)
      Minimum receive interval capability (Milliseconds)


    multiplier (optional, any, None)
      Multiplier value used to compute holddown (value used to multiply the interval)



  ve_ifnum (optional, any, None)
    Key to identify parent object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  echo (False, any, None)
    Enable BFD Echo


  authentication (False, any, None)
    Field authentication


    key_id (optional, any, None)
      Key ID


    password (optional, any, None)
      Key String


    method (optional, any, None)
      'md5'= Keyed MD5; 'meticulous-md5'= Meticulous Keyed MD5; 'meticulous-sha1'= Meticulous Keyed SHA1; 'sha1'= Keyed SHA1; 'simple'= Simple Password;


    encrypted (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)



  demand (False, any, None)
    Demand mode


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object









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

