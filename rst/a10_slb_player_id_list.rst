.. _a10_slb_player_id_list_module:


a10_slb_player_id_list -- Configures A10 slb.player-id-list
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Player id records config






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  player_record (False, any, None)
    Field player_record


    player_id (optional, any, None)
      64/32 bit player id based on config


    game_server_ipv6 (optional, any, None)
      Specify IPv6 address


    game_server_port_v4 (optional, any, None)
      Port


    game_server_ipv4 (optional, any, None)
      Specify IP address


    game_server_port_v6 (optional, any, None)
      Port



  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


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

