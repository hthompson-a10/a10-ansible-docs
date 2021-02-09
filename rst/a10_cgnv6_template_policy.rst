.. _a10_cgnv6_template_policy_module:


a10_cgnv6_template_policy -- Configures A10 cgnv6.template.policy
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Policy config






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Policy template name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  class_list (False, any, None)
    Field class_list


    client_ip_l3_dest (optional, any, None)
      Use destination IP as client IP address


    lid_list (optional, any, None)
      Field lid_list


    client_ip_l7_header (optional, any, None)
      Use extract client IP address from L7 header


    uuid (optional, any, None)
      uuid of the object


    header_name (optional, any, None)
      Specify L7 header name


    name (optional, any, None)
      Class list name



  state (True, any, None)
    State of the object to be created.


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

