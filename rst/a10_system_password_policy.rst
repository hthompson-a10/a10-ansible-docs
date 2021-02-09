.. _a10_system_password_policy_module:


a10_system_password_policy -- Configures A10 system.password-policy
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Password Complexity, Passsword Aging, Password history under password policy






Parameters
----------

  aging (False, any, None)
    'Strict'= Strict= Max Age-60 Days; 'Medium'= Medium= Max Age- 90 Days; 'Simple'= Simple= Max Age-120 Days;


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  min_pswd_len (False, any, None)
    Configure custom password length


  complexity (False, any, None)
    'Strict'= Strict= Min length=8, Min Lower Case=2, Min Upper Case=2, Min Numbers=2, Min Special Character=1; 'Medium'= Medium= Min length=6, Min Lower Case=2, Min Upper Case=2, Min Numbers=1, Min Special Character=1; 'Simple'= Simple= Min length=4, Min Lower Case=1, Min Upper Case=1, Min Numbers=1, Min Special Character=0;


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  history (False, any, None)
    'Strict'= Strict= Does not allow upto 5 old passwords; 'Medium'= Medium= Does not allow upto 4 old passwords; 'Simple'= Simple= Does not allow upto 3 old passwords;









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

