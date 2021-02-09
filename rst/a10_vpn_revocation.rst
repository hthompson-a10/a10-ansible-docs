.. _a10_vpn_revocation_module:


a10_vpn_revocation -- Configures A10 vpn.revocation
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IPsec VPN revocation settings






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Revocation name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ca (False, any, None)
    Certificate Authority file name


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ocsp (False, any, None)
    Field ocsp


    ocsp_sec (optional, any, None)
      Secondary OCSP Authentication Server


    ocsp_pri (optional, any, None)
      Primary OCSP Authentication Server



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  crl (False, any, None)
    Field crl


    crl_pri (optional, any, None)
      Primary CRL URL (http=//www.example.com/ocsp) (only .der filetypes)


    crl_sec (optional, any, None)
      Secondary CRL URL (http=//www.example.com/ocsp) (only .der filetypes)



  uuid (False, any, None)
    uuid of the object









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

