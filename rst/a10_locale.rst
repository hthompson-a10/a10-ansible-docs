.. _a10_locale_module:


a10_locale -- Configures A10 locale
===================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set locale for the CLI startup






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


  value (False, any, None)
    'en_US.UTF-8'= English locale for the USA, encoding with UTF-8 (default); 'zh_CN.UTF-8'= Chinese locale for PRC, encoding with UTF-8; 'zh_CN.GB18030'= Chinese locale for PRC, encoding with GB18030; 'zh_CN.GBK'= Chinese locale for PRC, encoding with GBK; 'zh_CN.GB2312'= Chinese locale for PRC, encoding with GB2312; 'zh_TW.UTF-8'= Chinese locale for Taiwan, encoding with UTF-8; 'zh_TW.BIG5'= Chinese locale for Taiwan, encoding with BIG5; 'zh_TW.EUCTW'= Chinese locale for Taiwan, encoding with EUC-TW; 'ja_JP.UTF-8'= Japanese locale for Japan, encoding with UTF-8; 'ja_JP.EUC-JP'= Japanese locale for Japan, encoding with EUC-JP;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  test (False, any, None)
    Field test


    locale (optional, any, None)
      'zh_CN'= Chinese locale for PRC; 'zh_TW'= Chinese locale for Taiwan; 'ja_JP'= Japanese locale for Japan;



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

