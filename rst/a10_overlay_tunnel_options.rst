.. _a10_overlay_tunnel_options_module:


a10_overlay_tunnel_options -- Configures A10 overlay.tunnel.options
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Global overlay-tunnel configuration options






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  tcp_mss_adjust_disable (False, any, None)
    Disable TCP MSS adjustment in SYN packet for tunnels


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  vxlan_dest_port (False, any, None)
    VXLAN UDP Destination Port (UDP Port Number (default 4789))


  ansible_host (True, any, None)
    Host for AXAPI authentication


  nvgre_key_mode_lower24 (False, any, None)
    Use the lower 24-bits of the GRE key as the VSID


  state (True, any, None)
    State of the object to be created.


  ip_dscp_preserve (False, any, None)
    Copy DSCP bits from inner IP to outer IP header


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  gateway_mac (False, any, None)
    MAC to be used with Gateway segment Id (MAC Address for the Gateway segment)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  nvgre_disable_flow_id (False, any, None)
    Disable Flow-ID computation for NVGRE









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

