.. _a10_vrrp_a_vrid_module:


a10_vrrp_a_vrid -- Configures A10 vrrp-a.vrid
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify VRRP-A vrid






Parameters
----------

  oper (False, any, None)
    Field oper


    force_standby (optional, any, None)
      Field force_standby


    weight (optional, any, None)
      Field weight


    vrid_val (optional, any, None)
      Specify ha VRRP-A vrid


    priority (optional, any, None)
      Field priority


    state (optional, any, None)
      Field state


    became_active (optional, any, None)
      Field became_active


    peer_list (optional, any, None)
      Field peer_list


    unit (optional, any, None)
      Field unit



  ansible_username (True, any, None)
    Username for AXAPI authentication


  floating_ip (False, any, None)
    Field floating_ip


    ipv6_address_cfg (optional, any, None)
      Field ipv6_address_cfg


    ip_address_part_cfg (optional, any, None)
      Field ip_address_part_cfg


    ipv6_address_part_cfg (optional, any, None)
      Field ipv6_address_part_cfg


    ip_address_cfg (optional, any, None)
      Field ip_address_cfg



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  follow (False, any, None)
    Field follow


    vrid_lead (optional, any, None)
      Define a VRRP-A VRID leader



  a10_partition (False, any, None)
    Destination/target partition for object/command


  blade_parameters (False, any, None)
    Field blade_parameters


    priority (optional, any, None)
      VRRP-A priorty (Priority, default is 150)


    fail_over_policy_template (optional, any, None)
      Apply a fail over policy template (VRRP-A fail over policy template name)


    tracking_options (optional, any, None)
      Field tracking_options


    uuid (optional, any, None)
      uuid of the object



  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'associated_vip_count'= Number of vips associated to vrid; 'associated_vport_count'= Number of vports associated to vrid; 'associated_natpool_count'= Number of nat pools associated to vrid;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    associated_natpool_count (optional, any, None)
      Number of nat pools associated to vrid


    associated_vip_count (optional, any, None)
      Number of vips associated to vrid


    associated_vport_count (optional, any, None)
      Number of vports associated to vrid


    vrid_val (optional, any, None)
      Specify ha VRRP-A vrid



  uuid (False, any, None)
    uuid of the object


  user_tag (False, any, None)
    Customized tag


  vrid_val (True, any, None)
    Specify ha VRRP-A vrid


  preempt_mode (False, any, None)
    Field preempt_mode


    threshold (optional, any, None)
      preemption threshold (preemption threshhold (0-255), default 0)


    disable (optional, any, None)
      disable preemption



  state (True, any, None)
    State of the object to be created.


  ansible_host (True, any, None)
    Host for AXAPI authentication


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

