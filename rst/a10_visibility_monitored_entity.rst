.. _a10_visibility_monitored_entity_module:


a10_visibility_monitored_entity -- Configures A10 visibility.monitored-entity
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Display Monitoring entities






Parameters
----------

  oper (False, any, None)
    Field oper


    topk (optional, any, None)
      Field topk


    primary_keys (optional, any, None)
      Field primary_keys


    sessions (optional, any, None)
      Field sessions


    all_keys (optional, any, None)
      Field all_keys


    mon_entity_list (optional, any, None)
      Field mon_entity_list


    detail (optional, any, None)
      Field detail


    secondary (optional, any, None)
      Field secondary



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  sessions (False, any, None)
    Field sessions


    uuid (optional, any, None)
      uuid of the object



  detail (False, any, None)
    Field detail


    debug (optional, any, None)
      Field debug


    uuid (optional, any, None)
      uuid of the object



  state (True, any, None)
    State of the object to be created.


  topk (False, any, None)
    Field topk


    sources (optional, any, None)
      Field sources


    uuid (optional, any, None)
      uuid of the object



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  secondary (False, any, None)
    Field secondary


    topk (optional, any, None)
      Field topk










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

