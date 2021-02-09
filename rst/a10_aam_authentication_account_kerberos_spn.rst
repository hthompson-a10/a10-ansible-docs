.. _a10_aam_authentication_account_kerberos_spn_module:


a10_aam_authentication_account_kerberos_spn -- Configures A10 aam.authentication.account.kerberos-spn
=====================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

AD domain account associated with a SPN






Parameters
----------

  secret_string (False, any, None)
    Password of AD account


  ansible_username (True, any, None)
    Username for AXAPI authentication


  encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.)


  account (False, any, None)
    Specify domain account for SPN


  service_principal_name (False, any, None)
    Specify service principal name


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  password (False, any, None)
    Specify password of domain account


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  realm (False, any, None)
    Specify Kerberos realm


  name (True, any, None)
    Specify AD account name


  user_tag (False, any, None)
    Customized tag


  state (True, any, None)
    State of the object to be created.


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

