.. _a10_acos_events_logdb_module:


a10_acos_events_logdb -- Configures A10 acos.events.logdb
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure global logging template






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  enable_ssli (False, any, None)
    Enable SSLi logging


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  enable_http_forward_proxy (False, any, None)
    Enable HTTP forward proxy logging


  state (True, any, None)
    State of the object to be created.


  enable_smtp (False, any, None)
    Enable SMTP logging


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  enable_file_inspection (False, any, None)
    Enable file-inspection logging


  enable_all (False, any, None)
    Enable logging for all widgets


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  enable_cgn (False, any, None)
    Enable CGN logging


  enable_fw (False, any, None)
    Enable Firewall logging









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

