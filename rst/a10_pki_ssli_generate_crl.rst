.. _a10_pki_ssli_generate_crl_module:


a10_pki_ssli_generate_crl -- Configures A10 pki.ssli.generate.crl
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Generate a CRL for for a vport






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  port (False, any, None)
    port number


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ansible_host (True, any, None)
    Host for AXAPI authentication


  a10_partition (False, any, None)
    Destination/target partition for object/command


  vip_name (False, any, None)
    VIP name









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

