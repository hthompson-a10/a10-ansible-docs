.. _a10_slb_template_dns_class_list_module:


a10_slb_template_dns_class_list -- Configures A10 slb.template.dns.class-list
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Classification list






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  name (True, any, None)
    Specify a class list name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  dns_name (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  lid_list (False, any, None)
    Field lid_list


    action_value (optional, any, None)
      'dns-cache-disable'= Disable DNS cache when it exceeds limit; 'dns-cache- enable'= Enable DNS cache when it exceeds limit; 'forward'= Forward the traffic even it exceeds limit;


    conn_rate_limit (optional, any, None)
      Connection rate limit


    log (optional, any, None)
      Log a message


    over_limit_action (optional, any, None)
      Action when exceeds limit


    lidnum (optional, any, None)
      Specify a limit ID


    per (optional, any, None)
      Per (Number of 100ms)


    lockout (optional, any, None)
      Don't accept any new connection for certain time (Lockout duration in minutes)


    log_interval (optional, any, None)
      Log interval (minute, by default system will log every over limit instance)


    dns (optional, any, None)
      Field dns


    user_tag (optional, any, None)
      Customized tag


    uuid (optional, any, None)
      uuid of the object



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object









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

