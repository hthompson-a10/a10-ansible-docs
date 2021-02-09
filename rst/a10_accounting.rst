.. _a10_accounting_module:


a10_accounting -- Configures A10 accounting
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configuration for accounting






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  nexec (False, any, None)
    Field exec


    accounting_exec_type (optional, any, None)
      'start-stop'= Record start and stop without waiting; 'stop-only'= Record stop when service terminates;


    accounting_exec_method (optional, any, None)
      'tacplus'= Use TACACS+ servers for accounting; 'radius'= Use radius servers for accounting;


    uuid (optional, any, None)
      uuid of the object



  ansible_password (True, any, None)
    Password for AXAPI authentication


  commands (False, any, None)
    Enable level for commands accounting


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  tacplus (False, any, None)
    Use TACACS+ servers for accounting


  stop_only (False, any, None)
    Record stop when service terminates


  debug (False, any, None)
    Specify the debug level for accounting (Debug level for command accounting. bitwise OR of the following= 1(common), 2(packet),4(packet detail), 8(md5))


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

