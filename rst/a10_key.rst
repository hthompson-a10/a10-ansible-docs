.. _a10_key_module:


a10_key -- Configures A10 key
=============================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Authentication key management






Parameters
----------

  key_list (False, any, None)
    Field key_list


    key_number (optional, any, None)
      Key identifier number


    user_tag (optional, any, None)
      Customized tag


    uuid (optional, any, None)
      uuid of the object


    key_string (optional, any, None)
      Set key string (The key)



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  key_chain_flag (True, any, None)
    Key-chain management


  key_chain_name (True, any, None)
    Key-chain name


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

