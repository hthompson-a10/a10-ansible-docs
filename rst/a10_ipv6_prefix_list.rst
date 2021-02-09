.. _a10_ipv6_prefix_list_module:


a10_ipv6_prefix_list -- Configures A10 ipv6.prefix-list
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Prefix-list






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Name of a prefix list


  ansible_username (True, any, None)
    Username for AXAPI authentication


  rules (False, any, None)
    Field rules


    ge (optional, any, None)
      Minimum prefix length to be matched


    le (optional, any, None)
      Maximum prefix length to be matched


    description (optional, any, None)
      Prefix-list specific description (Up to 80 characters describing this prefix- list)


    seq (optional, any, None)
      Sequence number of an entry


    action (optional, any, None)
      'deny'= Specify packets to reject; 'permit'= Specify packets to forward;


    ipaddr (optional, any, None)
      IPv6 prefix, e.g., 3ffe==/16


    any (optional, any, None)
      Any prefix match. Same as '==0/0 le 128'



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

