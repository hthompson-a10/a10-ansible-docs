.. _a10_import_periodic_class_list_convert_module:


a10_import_periodic_class_list_convert -- Configures A10 import-periodic.class-list-convert
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Convert Class List File to A10 format






Parameters
----------

  class_list_type (False, any, None)
    'ac'= ac; 'ipv4'= ipv4; 'ipv6'= ipv6; 'string'= string; 'string-case- insensitive'= string-case-insensitive;


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  period (False, any, None)
    Specify the period in second


  class_list_convert (True, any, None)
    Class List File


  state (True, any, None)
    State of the object to be created.


  use_mgmt_port (False, any, None)
    Use management port as source port


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  remote_file (False, any, None)
    profile name for remote url









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

