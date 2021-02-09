.. _a10_aam_authentication_password_retry_module:


a10_aam_authentication_password_retry -- Configures A10 aam.authentication.password-retry
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Field password_retry






Parameters
----------

  oper (False, any, None)
    Field oper


    logon_name (optional, any, None)
      Field logon_name


    entry_list (optional, any, None)
      Field entry_list


    name (optional, any, None)
      Field name



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

