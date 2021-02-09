.. _a10_cgnv6_port_list_module:


a10_cgnv6_port_list -- Configures A10 cgnv6.port-list
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure port list






Parameters
----------

  port_config (False, any, None)
    Field port_config


    translated_port (optional, any, None)
      Port after translation


    original_port (optional, any, None)
      Original port to be translated



  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Specify name of the port list


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  state (True, any, None)
    State of the object to be created.


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

