.. _a10_import_periodic_bw_list_module:


a10_import_periodic_bw_list -- Configures A10 import-periodic.bw-list
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Black white list files






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  remote_file (False, any, None)
    profile name for remote url


  period (False, any, None)
    Specify the period in second


  state (True, any, None)
    State of the object to be created.


  bw_list (True, any, None)
    Black white List File


  use_mgmt_port (False, any, None)
    Use management port as source port


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

