.. _a10_system_resource_accounting_template_system_resources_module:


a10_system_resource_accounting_template_system_resources -- Configures A10 system.resource.accounting.template.system-resources
===============================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enter the system resource limits






Parameters
----------

  l7cps_limit_cfg (False, any, None)
    Field l7cps_limit_cfg


    l7cps_limit_max (optional, any, None)
      L7cps-limit (L7 cps limit (no limits applied by default))



  ansible_username (True, any, None)
    Username for AXAPI authentication


  template_name (optional, any, None)
    Key to identify parent object


  fwcps_limit_cfg (False, any, None)
    Field fwcps_limit_cfg


    fwcps_limit_max (optional, any, None)
      Enter the Firewall cps limit (Firewall cps limit (no limits applied by default))



  threshold (False, any, None)
    Enter the threshold as a percentage (Threshold in percentage(default is 100%))


  l4cps_limit_cfg (False, any, None)
    Field l4cps_limit_cfg


    l4cps_limit_max (optional, any, None)
      Enter the L4 cps limit (L4 cps limit (no limits applied by default))



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  bw_limit_cfg (False, any, None)
    Field bw_limit_cfg


    bw_limit_watermark_disable (optional, any, None)
      Disable watermark (90% drop, keep existing sessions, drop  new sessions)


    bw_limit_max (optional, any, None)
      Enter the bandwidth limit in mbps (Bandwidth limit in Mbit/s (no limits applied by default))



  ansible_port (True, any, None)
    Port for AXAPI authentication


  natcps_limit_cfg (False, any, None)
    Field natcps_limit_cfg


    natcps_limit_max (optional, any, None)
      Enter the Nat cps limit (NAT cps limit (no limits applied by default))



  uuid (False, any, None)
    uuid of the object


  ssl_throughput_limit_cfg (False, any, None)
    Field ssl_throughput_limit_cfg


    ssl_throughput_limit_max (optional, any, None)
      Enter the ssl throughput limit in mbps (SSL Througput limit in Mbit/s (no limits applied by default))


    ssl_throughput_limit_watermark_disable (optional, any, None)
      Disable watermark (90% drop, keep existing sessions, drop  new sessions)



  concurrent_session_limit_cfg (False, any, None)
    Field concurrent_session_limit_cfg


    concurrent_session_limit_max (optional, any, None)
      Enter the Concurrent Session limit (cps) (Concurrent-Session cps limit (no limits applied by default))



  l4_session_limit_cfg (False, any, None)
    Field l4_session_limit_cfg


    l4_session_limit_max (optional, any, None)
      Enter the l4 session limit in % (0.01% to 99.99%) (Enter a number from 0.01 to 99.99 (up to 2 digits precision))


    l4_session_limit_min_guarantee (optional, any, None)
      minimum guaranteed value in % (up to 2 digits precision) (Enter a number from 0 to 99.99)



  sslcps_limit_cfg (False, any, None)
    Field sslcps_limit_cfg


    sslcps_limit_max (optional, any, None)
      Enter the SSL cps limit (SSL cps limit (no limits applied by default))



  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ansible_password (True, any, None)
    Password for AXAPI authentication









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

