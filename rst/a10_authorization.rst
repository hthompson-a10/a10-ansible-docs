.. _a10_authorization_module:


a10_authorization -- Configures A10 authorization
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configuration for command authorization






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


  commands (False, any, None)
    Commands level for authorization


  ansible_host (True, any, None)
    Host for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  debug (False, any, None)
    Specify the debug level for authorization (Debug level for command authorization. bitwise OR of the following= 1(common), 2(packet),4(packet detail), 8(md5))


  a10_partition (False, any, None)
    Destination/target partition for object/command


  method (False, any, None)
    Field method


    none (optional, any, None)
      No command authorization


    tacplus (optional, any, None)
      Using TACACS+ protocol










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

