.. _a10_slb_ssl_cert_module:


a10_slb_ssl_cert -- Configures A10 slb.ssl-cert
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Field ssl_cert






Parameters
----------

  oper (False, any, None)
    Field oper


    sortby_name (optional, any, None)
      Field sortby_name


    ssl_certs (optional, any, None)
      Field ssl_certs


    exact_match (optional, any, None)
      Field exact_match


    sortby_exp (optional, any, None)
      Field sortby_exp


    partition (optional, any, None)
      Field partition



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    uuid (optional, any, None)
      uuid of the object



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

