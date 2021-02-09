.. _a10_aam_authorization_jwt_cache_module:


a10_aam_authorization_jwt_cache -- Configures A10 aam.authorization.jwt.cache
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

AAM authorization JWT cache related operations






Parameters
----------

  oper (False, any, None)
    Field oper


    max_token_cache (optional, any, None)
      Field max_token_cache


    audience (optional, any, None)
      Field audience


    token_cached (optional, any, None)
      Field token_cached


    token_cache_hit (optional, any, None)
      Field token_cache_hit


    cache_list (optional, any, None)
      Field cache_list



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

