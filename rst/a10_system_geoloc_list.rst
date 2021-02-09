.. _a10_system_geoloc_list_module:


a10_system_geoloc_list -- Configures A10 system.geoloc-list
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure geolocation list






Parameters
----------

  oper (False, any, None)
    Field oper


    geoloc_list (optional, any, None)
      Field geoloc_list


    name (optional, any, None)
      Specify name of Geolocation list



  exclude_geoloc_name_list (False, any, None)
    Field exclude_geoloc_name_list


    exclude_geoloc_name_val (optional, any, None)
      Geolocation name to exclude



  ansible_username (True, any, None)
    Username for AXAPI authentication


  include_geoloc_name_list (False, any, None)
    Field include_geoloc_name_list


    include_geoloc_name_val (optional, any, None)
      Geolocation name to add



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'hit-count'= hit-count; 'total-geoloc'= total-geoloc; 'total- active'= total-active;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    hit_count (optional, any, None)
      Field hit_count


    name (optional, any, None)
      Specify name of Geolocation list


    total_geoloc (optional, any, None)
      Field total_geoloc


    total_active (optional, any, None)
      Field total_active



  name (True, any, None)
    Specify name of Geolocation list


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  shared (False, any, None)
    Enable sharing with other partitions


  user_tag (False, any, None)
    Customized tag









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

