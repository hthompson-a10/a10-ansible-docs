.. _a10_key_key_module:


a10_key_key -- Configures A10 key.key
=====================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure a key






Parameters
----------

  key_number (True, any, None)
    Key identifier number


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  key_string (False, any, None)
    Set key string (The key)


  key_chain_flag (optional, any, None)
    Key to identify parent object


  key_chain_name (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  user_tag (False, any, None)
    Customized tag









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

