.. _a10_smtp_module:


a10_smtp -- Configures A10 smtp
===============================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure SMTP Server






Parameters
----------

  mailfrom (False, any, None)
    Configure email source address


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  smtp_server_v6 (False, any, None)
    Configure SMTP Server IPV6 address


  smtp_server (False, any, None)
    Configure SMTP Server (length=1-254)


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  username_cfg (False, any, None)
    Field username_cfg


    username (optional, any, None)
      Configure SMTP login username


    password (optional, any, None)
      Field password



  use_mgmt_port (False, any, None)
    Use management port as source port


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  needauthentication (False, any, None)
    Configure SMTP server need authtication


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (False, any, None)
    Configure SMTP Port (Configure SMTP port, default is 25)









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

