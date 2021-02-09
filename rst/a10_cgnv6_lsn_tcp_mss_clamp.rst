.. _a10_cgnv6_lsn_tcp_mss_clamp_module:


a10_cgnv6_lsn_tcp_mss_clamp -- Configures A10 cgnv6.lsn.tcp.mss-clamp
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

LSN TCP MSS Clamping






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  mss_value (False, any, None)
    The max value allowed for the TCP MSS (default= not configured)},


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  mss_clamp_type (False, any, None)
    'fixed'= Specify a fixed max value for the TCP MSS; 'subtract'= Specify the value to subtract from the TCP MSS; 'none'= No TCP MSS clamping (default);


  min (False, any, None)
    Specify the min value allowed for the TCP MSS (Specify the min value allowed for the TCP MSS (default= ((576 - 60 - 60))))


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  mss_subtract (False, any, None)
    Specify the value to subtract from the TCP MSS (default= not configured)


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

