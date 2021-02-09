.. _a10_aam_authorization_policy_jwt_claim_map_module:


a10_aam_authorization_policy_jwt_claim_map -- Configures A10 aam.authorization.policy.jwt-claim-map
===================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Map attributes to JWT claims






Parameters
----------

  claim (False, any, None)
    Specify JWT claim name to map to.


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ntype (False, any, None)
    Specify claim type


  string_type (False, any, None)
    Claim type is string


  policy_name (optional, any, None)
    Key to identify parent object


  attr_num (True, any, None)
    Spcify attribute ID for claim mapping


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  str_val (False, any, None)
    Specify JWT claim value.


  num_val (False, any, None)
    Specify JWT claim value.


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  boolean_type (False, any, None)
    Claim type is boolean


  state (True, any, None)
    State of the object to be created.


  bool_val (False, any, None)
    'true'= True; 'false'= False;


  number_type (False, any, None)
    Claim type is number


  ansible_password (True, any, None)
    Password for AXAPI authentication









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

