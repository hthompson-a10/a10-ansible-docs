.. _a10_slb_template_persist_source_ip_module:


a10_slb_template_persist_source_ip -- Configures A10 slb.template.persist.source-ip
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Source IP persistence






Parameters
----------

  enforce_higher_priority (False, any, None)
    Enforce to use high priority node if available


  netmask6 (False, any, None)
    IPV6 subnet mask


  match_type (False, any, None)
    Persistence type


  hash_persist (False, any, None)
    Use hash value of source IP address


  ansible_username (True, any, None)
    Username for AXAPI authentication


  primary_port (False, any, None)
    Primary port to create the persist session


  netmask (False, any, None)
    IP subnet mask


  dont_honor_conn_rules (False, any, None)
    Do not observe connection rate rules


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  server (False, any, None)
    Persist to the same server, default is port


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  name (True, any, None)
    Source IP persistence template name


  service_group (False, any, None)
    Persist within the same service group


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  incl_dst_ip (False, any, None)
    Include destination IP on the persist


  scan_all_members (False, any, None)
    Persist with SCAN of all members


  state (True, any, None)
    State of the object to be created.


  incl_sport (False, any, None)
    Include source port on the persist


  timeout (False, any, None)
    Persistence timeout (in minutes)


  user_tag (False, any, None)
    Customized tag









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

