.. _a10_admin_module:


a10_admin -- Configures A10 admin
=================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

System admin user configuration






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  aws_accesskey (False, any, None)
    Field aws_accesskey


    nimport (optional, any, None)
      Import an aws-accesskey


    delete (optional, any, None)
      Delete an authorized aws accesskey


    file_url (optional, any, None)
      File URL


    use_mgmt_port (optional, any, None)
      Use management port as source port


    show (optional, any, None)
      Show authorized aws accesskey



  unlock (False, any, None)
    Unlock admin user


  user (True, any, None)
    System admin user name


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  privilege_list (False, any, None)
    Field privilege_list


    privilege_partition (optional, any, None)
      'partition-enable-disable'= Set per-partition enable/disable privilege; 'partition-read'= Set per-partition read privilege; 'partition-write'= Set per- partition write privilege;


    partition_name (optional, any, None)
      Partition Name



  password (False, any, None)
    Field password


    password_in_module (optional, any, None)
      Config admin user password


    uuid (optional, any, None)
      uuid of the object


    encrypted_in_module (optional, any, None)
      Specify an ENCRYPTED password string (System admin user password)



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  passwd_string (False, any, None)
    Config admin user password


  uuid (False, any, None)
    uuid of the object


  trusted_host (False, any, None)
    Set trusted network administrator can login in


  privilege_global (False, any, None)
    'read'= Set read privilege; 'write'= Set write privilege; 'hm'= Set external health monitor script content operations privilege;


  user_tag (False, any, None)
    Customized tag


  access_list (False, any, None)
    Specify an ACL to classify a trusted host


  access (False, any, None)
    Field access


    uuid (optional, any, None)
      uuid of the object


    access_type (optional, any, None)
      Field access_type



  state (True, any, None)
    State of the object to be created.


  ssh_pubkey (False, any, None)
    Field ssh_pubkey


    file_url (optional, any, None)
      File URL


    nimport (optional, any, None)
      Import an authorized public key


    list (optional, any, None)
      List all authorized public keys


    use_mgmt_port (optional, any, None)
      Use management port as source port


    delete (optional, any, None)
      Delete an authorized public key (SSH key index)



  trusted_host_acl_id (False, any, None)
    ACL ID


  action (False, any, None)
    'enable'= Enable user; 'disable'= Disable user;


  ansible_password (True, any, None)
    Password for AXAPI authentication


  trusted_host_cidr (False, any, None)
    Trusted IP Address with network mask


  password_key (False, any, None)
    Config admin user password









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

