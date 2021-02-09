.. _a10_slb_template_udp_module:


a10_slb_template_udp -- Configures A10 slb.template.udp
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

L4 UDP switch config






Parameters
----------

  qos (False, any, None)
    QOS level (number)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  radius_lb_method_hash_type (False, any, None)
    'ip'= IP-Hash;


  disable_clear_session (False, any, None)
    Disable immediate clearing of session


  avp (False, any, None)
    '4'= NAS-IP-address; '8'= Framed-IP-Address;


  re_select_if_server_down (False, any, None)
    re-select another server if service port is down


  immediate (False, any, None)
    Immediate Removal after Transaction


  idle_timeout (False, any, None)
    Idle Timeout value (Interval of 60 seconds), default 120 seconds (idle timeout in second, default 120)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  short (False, any, None)
    Short lived session


  name (True, any, None)
    Fast UDP Template Name


  user_tag (False, any, None)
    Customized tag


  age (False, any, None)
    short age (in sec), default is 31


  stateless_conn_timeout (False, any, None)
    Stateless Current Connection Timeout value (5 - 120 seconds) (idle timeout in second, default 120)


  state (True, any, None)
    State of the object to be created.


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

