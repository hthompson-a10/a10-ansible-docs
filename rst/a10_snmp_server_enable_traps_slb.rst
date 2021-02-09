.. _a10_snmp_server_enable_traps_slb_module:


a10_snmp_server_enable_traps_slb -- Configures A10 snmp.server.enable.traps.slb
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enable SLB group traps






Parameters
----------

  service_group_member_up (False, any, None)
    Enable SLB service-group-member-up trap


  all (False, any, None)
    Enable all SLB traps


  ansible_username (True, any, None)
    Username for AXAPI authentication


  server_selection_failure (False, any, None)
    Enable SLB server selection failure trap


  vip_connlimit (False, any, None)
    Enable the virtual server reach conn-limit trap


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  server_down (False, any, None)
    Enable SLB server-down trap


  service_group_up (False, any, None)
    Enable SLB service-group-up trap


  vip_port_down (False, any, None)
    Enable SLB virtual port down trap


  service_down (False, any, None)
    Enable SLB service-down trap


  vip_port_connlimit (False, any, None)
    Enable the virtual port reach conn-limit trap


  service_group_down (False, any, None)
    Enable SLB service-group-down trap


  uuid (False, any, None)
    uuid of the object


  service_group_member_down (False, any, None)
    Enable SLB service-group-member-down trap


  state (True, any, None)
    State of the object to be created.


  server_conn_limit (False, any, None)
    Enable SLB server connection limit trap


  service_up (False, any, None)
    Enable SLB service-up trap


  service_conn_resume (False, any, None)
    Enable SLB service connection resume trap


  vip_port_connratelimit (False, any, None)
    Enable the virtual port reach conn-rate-limit trap


  server_conn_resume (False, any, None)
    Enable SLB server connection resume trap


  application_buffer_limit (False, any, None)
    Enable application buffer reach limit trap


  vip_connratelimit (False, any, None)
    Enable the virtual server reach conn-rate-limit trap


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  vip_port_up (False, any, None)
    Enable SLB virtual port up trap


  vip_up (False, any, None)
    Enable SLB virtual server up trap


  bw_rate_limit_exceed (False, any, None)
    Enable SLB server/port bandwidth rate limit exceed trap


  gateway_up (False, any, None)
    Enable SLB server gateway up trap


  service_conn_limit (False, any, None)
    Enable SLB service connection limit trap


  vip_down (False, any, None)
    Enable SLB virtual server down trap


  server_up (False, any, None)
    Enable slb server up trap


  server_disabled (False, any, None)
    Enable SLB server-disabled trap


  bw_rate_limit_resume (False, any, None)
    Enable SLB server/port bandwidth rate limit resume trap


  gateway_down (False, any, None)
    Enable SLB server gateway down trap


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

