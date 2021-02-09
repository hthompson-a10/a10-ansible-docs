.. _a10_admin_session_module:


a10_admin_session -- Configures A10 admin-session
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Admin session management






Parameters
----------

  oper (False, any, None)
    Field oper


    session_list (optional, any, None)
      Field session_list



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  clear (False, any, None)
    clear admin session


  all (False, any, None)
    Clear all admin sessions


  state (True, any, None)
    State of the object to be created.


  sid (False, any, None)
    Session ID


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

