.. _a10_hsm_template_module:


a10_hsm_template -- Configures A10 hsm.template
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

HSM Template






Parameters
----------

  softhsm_enum (False, any, None)
    'softHSM'= software implementation of a cryptographic store; 'thalesHSM'= Thales HSM;


  enroll_timeout (False, any, None)
    Specify Enroll Timeout


  ansible_username (True, any, None)
    Username for AXAPI authentication


  encrypted (False, any, None)
    Do NOT use this option manually (This is an A10 reserved keyword) (The ENCRYPTED password string)


  rfs_port (False, any, None)
    Specify Port


  worker (False, any, None)
    Specify number of workers for each data CPU


  protection (False, any, None)
    Specify Protection Method


  password_string (False, any, None)
    Password (minimum 4 characters)


  rfs_ip (False, any, None)
    Specify Thales Remote File System


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  password (False, any, None)
    Specify HSM Passphrase


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  protection_softcard_hash (False, any, None)
    Hash


  ansible_port (True, any, None)
    Port for AXAPI authentication


  health_check_interval (False, any, None)
    Specify Thales HSM Health Check Interval


  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  sec_world (False, any, None)
    Security World Name


  state (True, any, None)
    State of the object to be created.


  protection_ocs (False, any, None)
    Operator Card Set


  template_name (True, any, None)
    Specify Template name


  softcard (False, any, None)
    Softcard


  user_tag (False, any, None)
    Customized tag


  protection_module (False, any, None)
    Module


  hsm_dev (False, any, None)
    Field hsm_dev


    hsm_priority (optional, any, None)
      Specify Priority


    hsm_ip (optional, any, None)
      Specify HSM Device IP Address


    hsm_port (optional, any, None)
      Specify Port










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

