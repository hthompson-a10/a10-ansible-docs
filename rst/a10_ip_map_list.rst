.. _a10_ip_map_list_module:


a10_ip_map_list -- Configures A10 ip.map-list
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure IP Map List name






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  mapping_list (False, any, None)
    Field mapping_list


    count (optional, any, None)
      Number of addresses to be translated in this range


    local_start_ip (optional, any, None)
      Local Start IPv4 Address of this list


    global_start_ip (optional, any, None)
      Global Start IPv4 Address of this list



  name (True, any, None)
    Specify name of the IP Map List


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  state (True, any, None)
    State of the object to be created.


  file (False, any, None)
    Create/Edit a IP Map List stored as a file


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

