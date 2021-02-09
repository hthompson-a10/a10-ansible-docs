.. _a10_slb_template_fix_module:


a10_slb_template_fix -- Configures A10 slb.template.fix
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

FIX template






Parameters
----------

  tag_switching (False, any, None)
    Field tag_switching


    service_group (optional, any, None)
      Create a Service Group comprising Servers (Service Group Name)


    switching_type (optional, any, None)
      'sender-comp-id'= Select service group based on SenderCompID; 'target-comp-id'= Select service group based on TargetCompID;


    equals (optional, any, None)
      Equals (Tag String)



  ansible_port (True, any, None)
    Port for AXAPI authentication


  logging (False, any, None)
    'init'= init only log; 'term'= termination only log; 'both'= both initial and termination log;


  name (True, any, None)
    FIX Template Name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  insert_client_ip (False, any, None)
    Insert client ip to tag 11447


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

