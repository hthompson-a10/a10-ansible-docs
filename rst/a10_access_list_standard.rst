.. _a10_access_list_standard_module:


a10_access_list_standard -- Configures A10 access-list.standard
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Standard Access List






Parameters
----------

  std (True, any, None)
    IP standard access list


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


  stdrules (False, any, None)
    Field stdrules


    subnet (optional, any, None)
      Source Address


    std_remark (optional, any, None)
      Access list entry comment (Notes for this ACL)


    log (optional, any, None)
      Log matches against this entry


    seq_num (optional, any, None)
      Sequence number


    host (optional, any, None)
      A single source host (Host address)


    rev_subnet_mask (optional, any, None)
      Network Mask 0=apply 255=ignore


    action (optional, any, None)
      'deny'= Deny; 'permit'= Permit; 'l3-vlan-fwd-disable'= Disable L3 forwarding between VLANs;


    transparent_session_only (optional, any, None)
      Only log transparent sessions


    any (optional, any, None)
      Any source host



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

