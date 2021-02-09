.. _a10_ipsec_sa_by_gw_module:


a10_ipsec_sa_by_gw -- Configures A10 ipsec_sa_by_gw
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Get IPsec SAs by IKE Gateway






Parameters
----------

  oper (False, any, None)
    Field oper


    ike_gateway_name (optional, any, None)
      Field ike_gateway_name


    ipsec_sa_list (optional, any, None)
      Field ipsec_sa_list


    local_ip (optional, any, None)
      Field local_ip


    peer_ip (optional, any, None)
      Field peer_ip



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

