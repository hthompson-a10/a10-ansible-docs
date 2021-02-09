.. _a10_rrd_slb_service_group_module:


a10_rrd_slb_service_group -- Configures A10 rrd.slb-service-group
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

slb service group statistics in RRD






Parameters
----------

  oper (False, any, None)
    Field oper


    slb_server_statistics (optional, any, None)
      Field slb_server_statistics


    start_time (optional, any, None)
      Field start_time


    end_time (optional, any, None)
      Field end_time


    slb_service_group_name (optional, any, None)
      Field slb_service_group_name



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

