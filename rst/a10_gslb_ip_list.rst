.. _a10_gslb_ip_list_module:


a10_gslb_ip_list -- Configures A10 gslb.ip-list
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify a IP List






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  gslb_ip_list_filename (False, any, None)
    Load IP List file (IP List filename)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  gslb_ip_list_addr_list (False, any, None)
    Field gslb_ip_list_addr_list


    ip (optional, any, None)
      Specify IP address


    id (optional, any, None)
      ID Number


    ip_mask (optional, any, None)
      IP mask



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  gslb_ip_list_obj_name (True, any, None)
    Specify IP List name


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

