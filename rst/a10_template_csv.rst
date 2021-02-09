.. _a10_template_csv_module:


a10_template_csv -- Configures A10 template.csv
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify csv template






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  csv_name (True, any, None)
    Specify name of csv template


  multiple_fields (False, any, None)
    Field multiple_fields


    field (optional, any, None)
      Field index number (Index of Field)


    csv_type (optional, any, None)
      'ip-from'= Beginning address of IP range or subnet; 'ip-to-mask'= Ending address of IP range or Mask; 'continent'= Continent; 'country'= Country; 'state'= State or province; 'city'= City;



  state (True, any, None)
    State of the object to be created.


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ipv6_enable (False, any, None)
    Support IPv6 IP ranges


  delim_char (False, any, None)
    enter a delimiter character, default ','


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  delim_num (False, any, None)
    enter a delimiter number, default 44 (',')


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

