.. _a10_web_service_secure_module:


a10_web_service_secure -- Configures A10 web.service.secure
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Web-service secure operation






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  certificate (False, any, None)
    Field certificate


    load (optional, any, None)
      Load WEB certificate


    file_url (optional, any, None)
      File URL


    use_mgmt_port (optional, any, None)
      Use management port as source port



  ansible_username (True, any, None)
    Username for AXAPI authentication


  regenerate (False, any, None)
    Field regenerate


    country (optional, any, None)
      The country name


    state (optional, any, None)
      The location


    domain_name (optional, any, None)
      The domain name



  ansible_password (True, any, None)
    Password for AXAPI authentication


  private_key (False, any, None)
    Field private_key


    load (optional, any, None)
      Load WEB private-key


    file_url (optional, any, None)
      File URL


    use_mgmt_port (optional, any, None)
      Use management port as source port



  generate (False, any, None)
    Field generate


    country (optional, any, None)
      The country name


    state (optional, any, None)
      The location


    domain_name (optional, any, None)
      The domain name



  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ansible_host (True, any, None)
    Host for AXAPI authentication


  a10_partition (False, any, None)
    Destination/target partition for object/command


  wipe (False, any, None)
    Wipe WEB private-key and certificate


  restart (False, any, None)
    Restart WEB service









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

