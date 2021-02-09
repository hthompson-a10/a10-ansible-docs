.. _a10_network_lldp_management_address_ipv4_addr_module:


a10_network_lldp_management_address_ipv4_addr -- Configures A10 network.lldp.management.address.ipv4-addr
=========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure lldp management-address ipv4 address






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  interface_ipv4 (False, any, None)
    Field interface_ipv4


    ipv4_ve (optional, any, None)
      configure lldp management-address interface ve (lldp management-address interface port number)


    ipv4_eth (optional, any, None)
      configure lldp management-address interface ethernet (lldp management-address interface port number)


    ipv4_mgmt (optional, any, None)
      configure lldp management-address interface management



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  ipv4 (True, any, None)
    Configure lldp management-address, subtype is ipv4 (lldp management-address ipv4 address)


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

