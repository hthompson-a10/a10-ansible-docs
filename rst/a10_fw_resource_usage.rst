.. _a10_fw_resource_usage_module:


a10_fw_resource_usage -- Configures A10 fw.resource-usage
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Firewall resource usage






Parameters
----------

  oper (False, any, None)
    Field oper


    clause_per_obj_grp_current_count (optional, any, None)
      Field clause_per_obj_grp_current_count


    fw_rule_current_count (optional, any, None)
      Field fw_rule_current_count


    object (optional, any, None)
      Field object


    fw_zone_current_count (optional, any, None)
      Field fw_zone_current_count


    rule_set (optional, any, None)
      Field rule_set


    ip_range (optional, any, None)
      Field ip_range


    clause_per_obj_grp_total_count (optional, any, None)
      Field clause_per_obj_grp_total_count


    fw_object_total_count (optional, any, None)
      Field fw_object_total_count


    fw_object_group_current_count (optional, any, None)
      Field fw_object_group_current_count


    radius_table_current_count (optional, any, None)
      Field radius_table_current_count


    fw_zone_total_count (optional, any, None)
      Field fw_zone_total_count


    fw_helper_sessions_current_count (optional, any, None)
      Field fw_helper_sessions_current_count


    zone (optional, any, None)
      Field zone


    rule (optional, any, None)
      Field rule


    fw_rule_total_count (optional, any, None)
      Field fw_rule_total_count


    fw_ip_range_total_count (optional, any, None)
      Field fw_ip_range_total_count


    fw_ip_range_current_count (optional, any, None)
      Field fw_ip_range_current_count


    fw_object_current_count (optional, any, None)
      Field fw_object_current_count


    helper_sessions (optional, any, None)
      Field helper_sessions


    radius_table_total_count (optional, any, None)
      Field radius_table_total_count


    fw_helper_sessions_total_count (optional, any, None)
      Field fw_helper_sessions_total_count


    fw_rule_set_current_count (optional, any, None)
      Field fw_rule_set_current_count


    clause_per_obj_grp (optional, any, None)
      Field clause_per_obj_grp


    radius_table_size (optional, any, None)
      Field radius_table_size


    fw_object_group_total_count (optional, any, None)
      Field fw_object_group_total_count


    fw_rule_set_total_count (optional, any, None)
      Field fw_rule_set_total_count


    object_group (optional, any, None)
      Field object_group



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

