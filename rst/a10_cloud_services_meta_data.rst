.. _a10_cloud_services_meta_data_module:


a10_cloud_services_meta_data -- Configures A10 cloud.services.meta-data
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

user-data Services configuration only works in shared partition






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  prevent_admin_ssh_key (False, any, None)
    Prevents admin ssh-key from being added if in YAML config


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  prevent_admin_passwd (False, any, None)
    Prevents admin password from being changed if in YAML config


  a10_partition (False, any, None)
    Destination/target partition for object/command


  prevent_user_ops (False, any, None)
    Prevents user from being added command is in user-data


  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  prevent_license (False, any, None)
    Prevents a10_license configuration in YAML config


  ansible_password (True, any, None)
    Password for AXAPI authentication


  prevent_webservice (False, any, None)
    Prevents a10_license configuration in YAML config


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  prevent_cloud_service (False, any, None)
    Prevents cloud-service configuration in YAML config


  provider (False, any, None)
    'aws'= AWS user-data services; 'openstack'= OpenStack user-data services;


  action (False, any, None)
    'enable'= enable; 'disable'= disable;


  prevent_blob (False, any, None)
    Prevents a10_blob from loading in YAML config


  prevent_autofill (False, any, None)
    prevents use of meta-data to complete user_data configuration









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

