.. _a10_system_geoloc_name_helper_module:


a10_system_geoloc_name_helper -- Configures A10 system.geoloc-name-helper
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Geolocation name helper






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'place-holder'= place-holder;



  oper (False, any, None)
    Field oper


    geoloc (optional, any, None)
      Field geoloc


    geoloc_candidate_list (optional, any, None)
      Field geoloc_candidate_list



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

