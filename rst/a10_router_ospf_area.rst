.. _a10_router_ospf_area_module:


a10_router_ospf_area -- Configures A10 router.ospf.area
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

OSPF area parameters






Parameters
----------

  range_list (False, any, None)
    Field range_list


    area_range_prefix (optional, any, None)
      Area range for IPv4 prefix


    option (optional, any, None)
      'advertise'= Advertise this range (default); 'not-advertise'= DoNotAdvertise this range;



  ansible_username (True, any, None)
    Username for AXAPI authentication


  nssa_cfg (False, any, None)
    Field nssa_cfg


    no_summary (optional, any, None)
      Do not send summary LSA into NSSA


    no_redistribution (optional, any, None)
      No redistribution into this NSSA area


    default_information_originate (optional, any, None)
      Originate Type 7 default into NSSA area


    metric_type (optional, any, None)
      OSPF metric type (OSPF metric type for default routes)


    metric (optional, any, None)
      OSPF default metric (OSPF metric)


    translator_role (optional, any, None)
      'always'= Translate always; 'candidate'= Candidate for translator (default); 'never'= Do not translate;


    nssa (optional, any, None)
      Specify a NSSA area



  filter_lists (False, any, None)
    Field filter_lists


    plist_name (optional, any, None)
      Filter networks by prefix-list (Name of an IP prefix-list)


    plist_direction (optional, any, None)
      'in'= Filter networks sent to this area; 'out'= Filter networks sent from this area;


    filter_list (optional, any, None)
      Filter networks between OSPF areas


    acl_name (optional, any, None)
      Filter networks by access-list (Name of an access-list)


    acl_direction (optional, any, None)
      'in'= Filter networks sent to this area; 'out'= Filter networks sent from this area;



  area_num (True, any, None)
    OSPF area ID as a decimal value


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ospf_process_id (optional, any, None)
    Key to identify parent object


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  virtual_link_list (False, any, None)
    Field virtual_link_list


    retransmit_interval (optional, any, None)
      LSA retransmit interval (Seconds)


    bfd (optional, any, None)
      Bidirectional Forwarding Detection (BFD)


    virtual_link_ip_addr (optional, any, None)
      ID (IP addr) associated with virtual link neighbor


    virtual_link_authentication (optional, any, None)
      Enable authentication


    message_digest_key (optional, any, None)
      Set message digest key (Key ID)


    virtual_link_auth_type (optional, any, None)
      'message-digest'= Use message-digest authentication; 'null'= Use null authentication;


    dead_interval (optional, any, None)
      Dead router detection time (Seconds)


    hello_interval (optional, any, None)
      Hello packet interval (Seconds)


    authentication_key (optional, any, None)
      Set authentication key (Authentication key (8 chars))


    transmit_delay (optional, any, None)
      LSA transmission delay (Seconds)


    md5 (optional, any, None)
      Use MD5 algorithm (Authentication key (16 chars))



  stub_cfg (False, any, None)
    Field stub_cfg


    stub (optional, any, None)
      Configure OSPF area as stub


    no_summary (optional, any, None)
      Do not inject inter-area routes into area



  state (True, any, None)
    State of the object to be created.


  shortcut (False, any, None)
    'default'= Set default shortcutting behavior; 'disable'= Disable shortcutting through the area; 'enable'= Enable shortcutting through the area;


  default_cost (False, any, None)
    Set the summary-default cost of a NSSA or stub area (Stub's advertised default summary cost)


  area_ipv4 (True, any, None)
    OSPF area ID in IP address format


  ansible_password (True, any, None)
    Password for AXAPI authentication


  auth_cfg (False, any, None)
    Field auth_cfg


    authentication (optional, any, None)
      Enable authentication


    message_digest (optional, any, None)
      Use message-digest authentication










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

