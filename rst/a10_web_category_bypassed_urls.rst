.. _a10_web_category_bypassed_urls_module:


a10_web_category_bypassed_urls -- Configures A10 web.category.bypassed-urls
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Bypassed URLS






Parameters
----------

  oper (False, any, None)
    Field oper


    number_of_urls (optional, any, None)
      Field number_of_urls


    url_list (optional, any, None)
      Field url_list


    url_name (optional, any, None)
      Field url_name


    all_urls (optional, any, None)
      Field all_urls



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication









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

