.. _a10_aam_authentication_server_module:


a10_aam_authentication_server -- Configures A10 aam.authentication.server
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Authentication server configuration






Parameters
----------

  oper (False, any, None)
    Field oper


    rport_count (optional, any, None)
      Field rport_count


    part_id (optional, any, None)
      Field part_id


    rserver_count (optional, any, None)
      Field rserver_count


    ldap (optional, any, None)
      Field ldap


    get_count (optional, any, None)
      Field get_count


    rserver_list (optional, any, None)
      Field rserver_list


    name (optional, any, None)
      Field name



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  windows (False, any, None)
    Field windows


    sampling_enable (optional, any, None)
      Field sampling_enable


    instance_list (optional, any, None)
      Field instance_list


    uuid (optional, any, None)
      uuid of the object



  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  radius (False, any, None)
    Field radius


    sampling_enable (optional, any, None)
      Field sampling_enable


    instance_list (optional, any, None)
      Field instance_list


    uuid (optional, any, None)
      uuid of the object



  ldap (False, any, None)
    Field ldap


    sampling_enable (optional, any, None)
      Field sampling_enable


    instance_list (optional, any, None)
      Field instance_list


    uuid (optional, any, None)
      uuid of the object



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ocsp (False, any, None)
    Field ocsp


    sampling_enable (optional, any, None)
      Field sampling_enable


    instance_list (optional, any, None)
      Field instance_list


    uuid (optional, any, None)
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

