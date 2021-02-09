.. _a10_cgnv6_lsn_endpoint_independent_filtering_udp_module:


a10_cgnv6_lsn_endpoint_independent_filtering_udp -- Configures A10 cgnv6.lsn.endpoint.independent.filtering.udp
===============================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set behavior for UDP






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  session_limit (False, any, None)
    Limit number of EIF sessions that can be created per port


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  port_list (False, any, None)
    Field port_list


    port_end (optional, any, None)
      Port Range End


    port (optional, any, None)
      Single Destination Port or Port Range Start



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

