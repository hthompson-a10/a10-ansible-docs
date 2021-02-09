.. _a10_sessions_module:


a10_sessions -- Configures A10 sessions
=======================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Field sessions






Parameters
----------

  oper (False, any, None)
    Field oper


    app (optional, any, None)
      Field app


    nat_ipv4_addr (optional, any, None)
      Field nat_ipv4_addr


    nat_port (optional, any, None)
      Field nat_port


    total_sessions (optional, any, None)
      Field total_sessions


    fw_dest_zone (optional, any, None)
      Field fw_dest_zone


    name_str (optional, any, None)
      Field name_str


    zone_name (optional, any, None)
      Field zone_name


    dest_port (optional, any, None)
      Field dest_port


    check_inside_user (optional, any, None)
      Field check_inside_user


    src_port (optional, any, None)
      Field src_port


    src_ipv6_addr (optional, any, None)
      Field src_ipv6_addr


    fw_dest_obj_grp (optional, any, None)
      Field fw_dest_obj_grp


    smp (optional, any, None)
      Field smp


    smp_table (optional, any, None)
      Field smp_table


    application (optional, any, None)
      Field application


    sport_rate_limit_curr (optional, any, None)
      Field sport_rate_limit_curr


    fw_dest_rserver (optional, any, None)
      Field fw_dest_rserver


    fw_src_rserver (optional, any, None)
      Field fw_src_rserver


    fw_dest_obj (optional, any, None)
      Field fw_dest_obj


    fw_src_obj_grp (optional, any, None)
      Field fw_src_obj_grp


    session_list (optional, any, None)
      Field session_list


    app_category (optional, any, None)
      Field app_category


    fw_ip_type (optional, any, None)
      Field fw_ip_type


    dst_ipv4_addr (optional, any, None)
      Field dst_ipv4_addr


    filter_type (optional, any, None)
      Field filter_type


    fw_src_zone (optional, any, None)
      Field fw_src_zone


    src_ipv6_prefix (optional, any, None)
      Field src_ipv6_prefix


    fw_dest_vserver (optional, any, None)
      Field fw_dest_vserver


    full_width (optional, any, None)
      Field full_width


    src_ipv4_addr (optional, any, None)
      Field src_ipv4_addr


    sport_rate_limit_exceed (optional, any, None)
      Field sport_rate_limit_exceed


    fw_helper_sessions (optional, any, None)
      Field fw_helper_sessions


    dst_ipv6_addr (optional, any, None)
      Field dst_ipv6_addr


    l4_protocol (optional, any, None)
      Field l4_protocol


    app_sessions (optional, any, None)
      Field app_sessions


    session_id (optional, any, None)
      Field session_id


    ext (optional, any, None)
      Field ext


    dst_ipv6_prefix (optional, any, None)
      Field dst_ipv6_prefix


    fw_src_obj (optional, any, None)
      Field fw_src_obj


    fw_rule (optional, any, None)
      Field fw_rule



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


  smp (False, any, None)
    Field smp


    uuid (optional, any, None)
      uuid of the object



  smp_table (False, any, None)
    Field smp_table


    uuid (optional, any, None)
      uuid of the object



  ext (False, any, None)
    Field ext


    uuid (optional, any, None)
      uuid of the object



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

