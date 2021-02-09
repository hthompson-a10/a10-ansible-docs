.. _a10_sys_ut_template_tcp_options_module:


a10_sys_ut_template_tcp_options -- Configures A10 sys.ut.template.tcp.options
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Tcp Flags






Parameters
----------

  sack_type (False, any, None)
    'permitted'= permitted; 'block'= block;


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  nop (False, any, None)
    No Op


  time_stamp_enable (False, any, None)
    adds Time Stamp to options


  mss (False, any, None)
    TCP MSS


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  template_name (optional, any, None)
    Key to identify parent object


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  wscale (False, any, None)
    Field wscale









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

