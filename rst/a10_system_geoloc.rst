.. _a10_system_geoloc_module:


a10_system_geoloc -- Configures A10 system.geoloc
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Field geoloc






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'place-holder'= place-holder;



  oper (False, any, None)
    Field oper


    total_geolocs (optional, any, None)
      Field total_geolocs


    ipv6rangestrt (optional, any, None)
      Field ipv6rangestrt


    iprangeend (optional, any, None)
      Field iprangeend


    geoloc_list (optional, any, None)
      Field geoloc_list


    iprangestrt (optional, any, None)
      Field iprangestrt


    filter4 (optional, any, None)
      Field filter4


    depth (optional, any, None)
      Field depth


    filter1 (optional, any, None)
      Field filter1


    filter3 (optional, any, None)
      Field filter3


    filter2 (optional, any, None)
      Field filter2


    pol_name (optional, any, None)
      Field pol_name


    geo_name (optional, any, None)
      Field geo_name



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


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

