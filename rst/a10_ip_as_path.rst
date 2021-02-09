.. _a10_ip_as_path_module:


a10_ip_as_path -- Configures A10 ip.as-path
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure an AS-path list for BGP






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  access_list (True, any, None)
    Specify an access list name (Regular expression access-list name)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  value (True, any, None)
    A regular-expression to match the BGP AS paths


  action (True, any, None)
    'deny'= Specify packets to reject; 'permit'= Specify packets to forward;


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

