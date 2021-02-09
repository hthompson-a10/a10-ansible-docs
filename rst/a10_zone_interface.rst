.. _a10_zone_interface_module:


a10_zone_interface -- Configures A10 zone.interface
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Interface






Parameters
----------

  zone_name (optional, any, None)
    Key to identify parent object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  lif_list (False, any, None)
    Field lif_list


    interface_lif_end (optional, any, None)
      Field interface_lif_end


    interface_lif_start (optional, any, None)
      Field interface_lif_start



  state (True, any, None)
    State of the object to be created.


  tunnel_list (False, any, None)
    Field tunnel_list


    interface_tunnel_end (optional, any, None)
      Field interface_tunnel_end


    interface_tunnel_start (optional, any, None)
      Field interface_tunnel_start



  ethernet_list (False, any, None)
    Field ethernet_list


    interface_ethernet_end (optional, any, None)
      Field interface_ethernet_end


    interface_ethernet_start (optional, any, None)
      Field interface_ethernet_start



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ve_list (False, any, None)
    Field ve_list


    interface_ve_start (optional, any, None)
      Field interface_ve_start


    interface_ve_end (optional, any, None)
      Field interface_ve_end



  trunk_list (False, any, None)
    Field trunk_list


    interface_trunk_start (optional, any, None)
      Field interface_trunk_start


    interface_trunk_end (optional, any, None)
      Field interface_trunk_end



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

