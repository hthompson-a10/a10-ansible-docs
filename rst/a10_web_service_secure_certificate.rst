.. _a10_web_service_secure_certificate_module:


a10_web_service_secure_certificate -- Configures A10 web.service.secure.certificate
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Web-service secure certificate operation






Parameters
----------

  load (False, any, None)
    Load WEB certificate


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  file_url (False, any, None)
    File URL


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

