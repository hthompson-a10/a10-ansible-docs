.. _a10_cgnv6_nat64_fragmentation_df_bit_transparency_module:


a10_cgnv6_nat64_fragmentation_df_bit_transparency -- Configures A10 cgnv6.nat64.fragmentation.df-bit-transparency
=================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Add an empty IPv6 fragmentation header if IPv4 DF bit is zero (default=disabled)






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


  df_bit_value (False, any, None)
    'enable'= Add an empty IPv6 fragmentation header if IPv4 DF bit is zero;


  state (True, any, None)
    State of the object to be created.


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

