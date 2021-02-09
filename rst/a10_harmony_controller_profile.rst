.. _a10_harmony_controller_profile_module:


a10_harmony_controller_profile -- Configures A10 harmony.controller.profile
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Harmony controller profile






Parameters
----------

  oper (False, any, None)
    Field oper


    deregistration_status (optional, any, None)
      Field deregistration_status


    broker_info (optional, any, None)
      Field broker_info


    overall_status (optional, any, None)
      Field overall_status


    deregistration_status_code (optional, any, None)
      Field deregistration_status_code


    Number_of_tenant_unmapped_partitions (optional, any, None)
      Field Number_of_tenant_unmapped_partitions


    tunnel_error_message (optional, any, None)
      Field tunnel_error_message


    heartbeat_status (optional, any, None)
      Field heartbeat_status


    tunnel_status (optional, any, None)
      Field tunnel_status


    registration_status (optional, any, None)
      Field registration_status


    service_registry (optional, any, None)
      Field service_registry


    heartbeat_error_message (optional, any, None)
      Field heartbeat_error_message


    registration_error_message (optional, any, None)
      Field registration_error_message


    deregistration_error_message (optional, any, None)
      Field deregistration_error_message


    registration_status_code (optional, any, None)
      Field registration_status_code


    schema_registry_status (optional, any, None)
      Field schema_registry_status


    kafka_broker_state (optional, any, None)
      Field kafka_broker_state


    Number_of_tenant_mapped_partitions (optional, any, None)
      Field Number_of_tenant_mapped_partitions


    service_registry_error_message (optional, any, None)
      Field service_registry_error_message



  auto_restart_action (False, any, None)
    'enable'= enable auto analytics bus restart, default behavior is enable; 'disable'= disable auto analytics bus restart;


  interval (False, any, None)
    auto analytics bus restart time interval in mins, default is 3 mins


  re_sync (False, any, None)
    Field re_sync


    schema_registry (optional, any, None)
      re-sync the schema registry


    analytics_bus (optional, any, None)
      re-sync analtyics bus connections



  ansible_username (True, any, None)
    Username for AXAPI authentication


  password_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


  host (False, any, None)
    Set harmony controller host adddress


  cluster_id (False, any, None)
    cluster id for the device


  use_mgmt_port (False, any, None)
    Use management port for connections


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (False, any, None)
    Set port for remote Harmony Controller, default is 8443


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  tunnel (False, any, None)
    Field tunnel


    action (optional, any, None)
      'enable'= Tunnel Enable; 'disable'= Tunnel Disable;


    uuid (optional, any, None)
      uuid of the object



  ansible_password (True, any, None)
    Password for AXAPI authentication


  region (False, any, None)
    region of the thunder-device


  availability_zone (False, any, None)
    availablity zone of the thunder-device


  ansible_host (True, any, None)
    Host for AXAPI authentication


  cluster_name (False, any, None)
    cluster name for the device


  state (True, any, None)
    State of the object to be created.


  provider (False, any, None)
    provider for the harmony-controller


  action (False, any, None)
    'register'= Register the device to the controller; 'deregister'= Deregister the device from controller;


  user_name (False, any, None)
    user-name for the tenant


  thunder_mgmt_ip (False, any, None)
    Field thunder_mgmt_ip


    ip_address (optional, any, None)
      IP address (IPv4 address)


    uuid (optional, any, None)
      uuid of the object



  secret_value (False, any, None)
    Specify the password for the user









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

