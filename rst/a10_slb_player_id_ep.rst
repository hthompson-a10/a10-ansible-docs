.. _a10_slb_player_id_ep_module:


a10_slb_player_id_ep -- Configures A10 slb.player-id-ep
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Player-id endpoint






Parameters
----------

  oper (False, any, None)
    Field oper


    total_players (optional, any, None)
      Field total_players


    player_id (optional, any, None)
      Field player_id


    player_id_ep_list (optional, any, None)
      Field player_id_ep_list


    filter_type (optional, any, None)
      Field filter_type



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


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

