.. _a10_interface_ve_isis_module:


a10_interface_ve_isis -- Configures A10 interface.ve.isis
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

ISIS






Parameters
----------

  mesh_group (False, any, None)
    Field mesh_group


    value (optional, any, None)
      Mesh group number


    blocked (optional, any, None)
      Block LSPs on this interface



  bfd_cfg (False, any, None)
    Field bfd_cfg


    disable (optional, any, None)
      Disable BFD


    bfd (optional, any, None)
      Bidirectional Forwarding Detection (BFD)



  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  lsp_interval (False, any, None)
    Set LSP transmission interval (LSP transmission interval (milliseconds))


  padding (False, any, None)
    Add padding to IS-IS hello packets


  csnp_interval_list (False, any, None)
    Field csnp_interval_list


    csnp_interval (optional, any, None)
      Set CSNP interval in seconds (CSNP interval value)


    level (optional, any, None)
      'level-1'= Speficy interval for level-1 CSNPs; 'level-2'= Specify interval for level-2 CSNPs;



  hello_multiplier_list (False, any, None)
    Field hello_multiplier_list


    hello_multiplier (optional, any, None)
      Set multiplier for Hello holding time (Hello multiplier value)


    level (optional, any, None)
      'level-1'= Specify hello multiplier for level-1 IIHs; 'level-2'= Specify hello multiplier for level-2 IIHs;



  priority_list (False, any, None)
    Field priority_list


    priority (optional, any, None)
      Set priority for Designated Router election (Priority value)


    level (optional, any, None)
      'level-1'= Specify priority for level-1 routing; 'level-2'= Specify priority for level-2 routing;



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  wide_metric_list (False, any, None)
    Field wide_metric_list


    wide_metric (optional, any, None)
      Configure the wide metric for interface


    level (optional, any, None)
      'level-1'= Apply metric to level-1 links; 'level-2'= Apply metric to level-2 links;



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  retransmit_interval (False, any, None)
    Set per-LSP retransmission interval (Interval between retransmissions of the same LSP (seconds))


  metric_list (False, any, None)
    Field metric_list


    metric (optional, any, None)
      Configure the metric for interface (Default metric)


    level (optional, any, None)
      'level-1'= Apply metric to level-1 links; 'level-2'= Apply metric to level-2 links;



  network (False, any, None)
    'broadcast'= Specify IS-IS broadcast multi-access network; 'point-to-point'= Specify IS-IS point-to-point network;


  circuit_type (False, any, None)
    'level-1'= Level-1 only adjacencies are formed; 'level-1-2'= Level-1-2 adjacencies are formed; 'level-2-only'= Level-2 only adjacencies are formed;


  password_list (False, any, None)
    Field password_list


    password (optional, any, None)
      Configure the authentication password for interface


    level (optional, any, None)
      'level-1'= Specify password for level-1 PDUs; 'level-2'= Specify password for level-2 PDUs;



  authentication (False, any, None)
    Field authentication


    send_only_list (optional, any, None)
      Field send_only_list


    key_chain_list (optional, any, None)
      Field key_chain_list


    mode_list (optional, any, None)
      Field mode_list



  hello_interval_list (False, any, None)
    Field hello_interval_list


    hello_interval (optional, any, None)
      Set Hello interval in seconds (Hello interval value)


    level (optional, any, None)
      'level-1'= Specify hello-interval for level-1 IIHs; 'level-2'= Specify hello- interval for level-2 IIHs;



  state (True, any, None)
    State of the object to be created.


  ve_ifnum (optional, any, None)
    Key to identify parent object


  hello_interval_minimal_list (False, any, None)
    Field hello_interval_minimal_list


    hello_interval_minimal (optional, any, None)
      Set Hello holdtime 1 second, interval depends on multiplier


    level (optional, any, None)
      'level-1'= Specify hello-interval for level-1 IIHs; 'level-2'= Specify hello- interval for level-2 IIHs;



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

