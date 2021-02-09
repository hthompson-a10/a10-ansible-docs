.. _a10_network_lldp_management_address_dns_module:


a10_network_lldp_management_address_dns -- Configures A10 network.lldp.management.address.dns
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure lldp management-address dns address






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


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  dns (True, any, None)
    Configure lldp management-address, subtype is dns (lldp management-address dns address)


  interface (False, any, None)
    Field interface


    ethernet (optional, any, None)
      configure lldp management-address interface ethernet (lldp management-address interface port number)


    management (optional, any, None)
      configure lldp management-address interface management


    ve (optional, any, None)
      configure lldp management-address interface management (lldp management-address interface port number)



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

