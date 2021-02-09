.. _a10_vpn_default_module:


a10_vpn_default -- Configures A10 vpn.default
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Default






Parameters
----------

  oper (False, any, None)
    Field oper


    ike_remote_address (optional, any, None)
      Field ike_remote_address


    IPsec_protocol (optional, any, None)
      Field IPsec_protocol


    ike_local_address (optional, any, None)
      Field ike_local_address


    IPsec_hash (optional, any, None)
      Field IPsec_hash


    ike_dh_group (optional, any, None)
      Field ike_dh_group


    ike_encryption (optional, any, None)
      Field ike_encryption


    IPsec_local_port (optional, any, None)
      Field IPsec_local_port


    IPsec_priority (optional, any, None)
      Field IPsec_priority


    ike_priority (optional, any, None)
      Field ike_priority


    ike_mode (optional, any, None)
      Field ike_mode


    IPsec_remote_subnet (optional, any, None)
      Field IPsec_remote_subnet


    IPsec_mode (optional, any, None)
      Field IPsec_mode


    ike_version (optional, any, None)
      Field ike_version


    IPsec_lifetime (optional, any, None)
      Field IPsec_lifetime


    IPsec_lifebytes (optional, any, None)
      Field IPsec_lifebytes


    ike_hash (optional, any, None)
      Field ike_hash


    IPsec_encryption (optional, any, None)
      Field IPsec_encryption


    IPsec_remote_port (optional, any, None)
      Field IPsec_remote_port


    ike_dpd_interval (optional, any, None)
      Field ike_dpd_interval


    IPsec_local_subnet (optional, any, None)
      Field IPsec_local_subnet


    IPsec_remote_protocol (optional, any, None)
      Field IPsec_remote_protocol


    IPsec_anti_replay_window (optional, any, None)
      Field IPsec_anti_replay_window


    IPsec_local_protocol (optional, any, None)
      Field IPsec_local_protocol


    IPsec_dh_group (optional, any, None)
      Field IPsec_dh_group


    ike_auth_method (optional, any, None)
      Field ike_auth_method


    IPsec_traffic_selector (optional, any, None)
      Field IPsec_traffic_selector


    ike_lifetime (optional, any, None)
      Field ike_lifetime


    ike_nat_traversal (optional, any, None)
      Field ike_nat_traversal



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

