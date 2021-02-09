.. _a10_logging_local_log_app_fw_dot_plot_module:


a10_logging_local_log_app_fw_dot_plot -- Configures A10 logging.local.log.app.fw.dot-plot
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Application firewall dot plot






Parameters
----------

  oper (False, any, None)
    Field oper


    client_ip (optional, any, None)
      Field client_ip


    start_time (optional, any, None)
      Field start_time


    interval (optional, any, None)
      Field interval


    application_name (optional, any, None)
      Field application_name


    total (optional, any, None)
      Field total


    data (optional, any, None)
      Field data


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

