.. _a10_template_lid_module:


a10_template_lid -- Configures A10 template.lid
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create an Lid






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


  respond_to_user_mac (False, any, None)
    Use the user's source MAC for the next hop rather than the routing table (default=off)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  src_ip (False, any, None)
    Field src_ip


    concurrent_sessions (optional, any, None)
      Concurrent Session Limit per Source IP Address (Number of Concurrent Sessions)


    prefix_length (optional, any, None)
      Source prefix length


    enable_high_perf (optional, any, None)
      Enable High Perf


    log (optional, any, None)
      Log when Session Limit is exceeded



  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  lid_number (True, any, None)
    Lid Number









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

