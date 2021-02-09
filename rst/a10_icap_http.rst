.. _a10_icap_http_module:


a10_icap_http -- Configures A10 icap_http
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure ICAP






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'status_200'= Status code 200; 'status_201'= Status code 201; 'status_202'= Status code 202; 'status_203'= Status code 203; 'status_204'= Status code 204; 'status_205'= Status code 205; 'status_206'= Status code 206; 'status_207'= Status code 207; 'status_100'= Status code 100; 'status_101'= Status code 101; 'status_102'= Status code 102; 'status_300'= Status code 300; 'status_301'= Status code 301; 'status_302'= Status code 302; 'status_303'= Status code 303; 'status_304'= Status code 304; 'status_305'= Status code 305; 'status_306'= Status code 306; 'status_307'= Status code 307; 'status_400'= Status code 400; 'status_401'= Status code 401; 'status_402'= Status code 402; 'status_403'= Status code 403; 'status_404'= Status code 404; 'status_405'= Status code 405; 'status_406'= Status code 406; 'status_407'= Status code 407; 'status_408'= Status code 408; 'status_409'= Status code 409; 'status_410'= Status code 410; 'status_411'= Status code 411; 'status_412'= Status code 412; 'status_413'= Status code 413; 'status_414'= Status code 414; 'status_415'= Status code 415; 'status_416'= Status code 416; 'status_417'= Status code 417; 'status_418'= Status code 418; 'status_422'= Status code 422; 'status_423'= Status code 423; 'status_424'= Status code 424; 'status_425'= Status code 425; 'status_426'= Status code 426; 'status_449'= Status code 449; 'status_450'= Status code 450; 'status_500'= Status code 500; 'status_501'= Status code 501; 'status_502'= Status code 502; 'status_503'= Status code 503; 'status_504'= Status code 504; 'status_505'= Status code 505; 'status_506'= Status code 506; 'status_507'= Status code 507; 'status_508'= Status code 508; 'status_509'= Status code 509; 'status_510'= Status code 510; 'status_1xx'= status code 1XX; 'status_2xx'= status code 2XX; 'status_3xx'= status code 3XX; 'status_4xx'= status code 4XX; 'status_5xx'= status code 5XX; 'status_6xx'= status code 6XX; 'status_unknown'= Status code unknown;



  oper (False, any, None)
    Field oper


    l4_cpu_list (optional, any, None)
      Field l4_cpu_list


    cpu_count (optional, any, None)
      Field cpu_count



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    status_503 (optional, any, None)
      Status code 503


    status_306 (optional, any, None)
      Status code 306


    status_500 (optional, any, None)
      Status code 500


    status_307 (optional, any, None)
      Status code 307


    status_1xx (optional, any, None)
      status code 1XX


    status_450 (optional, any, None)
      Status code 450


    status_412 (optional, any, None)
      Status code 412


    status_413 (optional, any, None)
      Status code 413


    status_410 (optional, any, None)
      Status code 410


    status_411 (optional, any, None)
      Status code 411


    status_416 (optional, any, None)
      Status code 416


    status_417 (optional, any, None)
      Status code 417


    status_414 (optional, any, None)
      Status code 414


    status_415 (optional, any, None)
      Status code 415


    status_418 (optional, any, None)
      Status code 418


    status_unknown (optional, any, None)
      Status code unknown


    status_100 (optional, any, None)
      Status code 100


    status_101 (optional, any, None)
      Status code 101


    status_102 (optional, any, None)
      Status code 102


    status_510 (optional, any, None)
      Status code 510


    status_303 (optional, any, None)
      Status code 303


    status_300 (optional, any, None)
      Status code 300


    status_301 (optional, any, None)
      Status code 301


    status_401 (optional, any, None)
      Status code 401


    status_400 (optional, any, None)
      Status code 400


    status_207 (optional, any, None)
      Status code 207


    status_206 (optional, any, None)
      Status code 206


    status_205 (optional, any, None)
      Status code 205


    status_204 (optional, any, None)
      Status code 204


    status_203 (optional, any, None)
      Status code 203


    status_202 (optional, any, None)
      Status code 202


    status_201 (optional, any, None)
      Status code 201


    status_200 (optional, any, None)
      Status code 200


    status_423 (optional, any, None)
      Status code 423


    status_422 (optional, any, None)
      Status code 422


    status_304 (optional, any, None)
      Status code 304


    status_305 (optional, any, None)
      Status code 305


    status_302 (optional, any, None)
      Status code 302


    status_426 (optional, any, None)
      Status code 426


    status_425 (optional, any, None)
      Status code 425


    status_424 (optional, any, None)
      Status code 424


    status_508 (optional, any, None)
      Status code 508


    status_509 (optional, any, None)
      Status code 509


    status_403 (optional, any, None)
      Status code 403


    status_402 (optional, any, None)
      Status code 402


    status_405 (optional, any, None)
      Status code 405


    status_404 (optional, any, None)
      Status code 404


    status_407 (optional, any, None)
      Status code 407


    status_2xx (optional, any, None)
      status code 2XX


    status_409 (optional, any, None)
      Status code 409


    status_408 (optional, any, None)
      Status code 408


    status_502 (optional, any, None)
      Status code 502


    status_406 (optional, any, None)
      Status code 406


    status_504 (optional, any, None)
      Status code 504


    status_505 (optional, any, None)
      Status code 505


    status_506 (optional, any, None)
      Status code 506


    status_507 (optional, any, None)
      Status code 507


    status_4xx (optional, any, None)
      status code 4XX


    status_6xx (optional, any, None)
      status code 6XX


    status_501 (optional, any, None)
      Status code 501


    status_449 (optional, any, None)
      Status code 449


    status_5xx (optional, any, None)
      status code 5XX


    status_3xx (optional, any, None)
      status code 3XX



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

