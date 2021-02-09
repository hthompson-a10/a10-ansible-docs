.. _a10_tacacs_server_module:


a10_tacacs_server -- Configures A10 tacacs-server
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure TACACS+ servers






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  monitor (False, any, None)
    Configure TACACS+ servers


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  interval (False, any, None)
    The moniter interval in seconds (default 60)


  state (True, any, None)
    State of the object to be created.


  host (False, any, None)
    Field host


    tacacs_hostname_list (optional, any, None)
      Field tacacs_hostname_list


    ipv6_list (optional, any, None)
      Field ipv6_list


    ipv4_list (optional, any, None)
      Field ipv4_list



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


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

