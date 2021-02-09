.. _a10_slb_template_diameter_module:


a10_slb_template_diameter -- Configures A10 slb.template.diameter
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

diameter template






Parameters
----------

  forward_unknown_session_id (False, any, None)
    Forward server message even it has unknown session id


  origin_realm (False, any, None)
    origin-realm name avp


  service_group_name (False, any, None)
    service group name, this is the service group that the message needs to be copied to


  ansible_username (True, any, None)
    Username for AXAPI authentication


  load_balance_on_session_id (False, any, None)
    Load balance based on the session id


  forward_to_latest_server (False, any, None)
    Forward client message to the latest server that sends message with the same session id


  vendor_id (False, any, None)
    vendor-id avp (Vendor Id)


  terminate_on_cca_t (False, any, None)
    remove diameter session when receiving CCA-T message


  avp_list (False, any, None)
    Field avp_list


    int32 (optional, any, None)
      32 bits integer


    avp (optional, any, None)
      customize avps for cer to the server (avp number)


    mandatory (optional, any, None)
      mandatory avp


    int64 (optional, any, None)
      64 bits integer


    string (optional, any, None)
      String (string name, max length 127 bytes)



  idle_timeout (False, any, None)
    user sesison idle timeout (in minutes, default is 5)


  session_age (False, any, None)
    user session age allowed (default 10), this is not idle-time (in minutes)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  name (True, any, None)
    diameter template Name


  origin_host (False, any, None)
    Field origin_host


    origin_host_name (optional, any, None)
      origin-host name avp


    uuid (optional, any, None)
      uuid of the object



  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  avp_string (False, any, None)
    pattern to be matched in the avp string name, max length 127 bytes


  dwr_time (False, any, None)
    dwr health-check timer interval (in 100 milli second unit, default is 100, 0 means unset this option)


  dwr_up_retry (False, any, None)
    number of successful dwr health-check before declaring target up


  message_code_list (False, any, None)
    Field message_code_list


    message_code (optional, any, None)
      Field message_code



  customize_cea (False, any, None)
    customizing cea response


  avp_code (False, any, None)
    avp code


  state (True, any, None)
    State of the object to be created.


  multiple_origin_host (False, any, None)
    allowing multiple origin-host to a single server


  user_tag (False, any, None)
    Customized tag


  product_name (False, any, None)
    product name avp









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

