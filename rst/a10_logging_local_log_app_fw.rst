.. _a10_logging_local_log_app_fw_module:


a10_logging_local_log_app_fw -- Configures A10 logging.local.log.app-fw
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Application firewall






Parameters
----------

  oper (False, any, None)
    Field oper


    dot_plot (optional, any, None)
      Field dot_plot


    top_n (optional, any, None)
      Field top_n


    start_time (optional, any, None)
      Field start_time


    interval (optional, any, None)
      Field interval


    max_entries (optional, any, None)
      Field max_entries


    total (optional, any, None)
      Field total


    log_list (optional, any, None)
      Field log_list


    interval_position (optional, any, None)
      Field interval_position



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  top_n (False, any, None)
    Field top_n


    uuid (optional, any, None)
      uuid of the object



  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  dot_plot (False, any, None)
    Field dot_plot


    uuid (optional, any, None)
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

