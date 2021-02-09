.. _a10_accounting_exec_module:


a10_accounting_exec -- Configures A10 accounting.exec
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configuration for EXEC <shell> accounting






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  accounting_exec_type (False, any, None)
    'start-stop'= Record start and stop without waiting; 'stop-only'= Record stop when service terminates;


  accounting_exec_method (False, any, None)
    'tacplus'= Use TACACS+ servers for accounting; 'radius'= Use radius servers for accounting;


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

