.. _a10_logging_local_log_global_module:


a10_logging_local_log_global -- Configures A10 logging.local.log.global
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Field global






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'enqueue'= Total local-log enqueue; 'enqueue-full'= Total local-log queue full; 'enqueue-error'= Total local-log enqueue error; 'dequeue'= Total local-log dequeue; 'dequeue-error'= Total local-log dequeue processing error; 'raw-log'= Total local-log raw logs; 'raw-log-error'= Total raw log logging error; 'log-summarized'= Total raw log summarized; 'l1-log-summarized'= Total layer 1 log summarized; 'l2-log-summarized'= Total layer 2 log summarized; 'log-summarized-error'= Total local-log summarization error; 'aam-db'= Total local-log AAM raw database; 'ep-db'= Total local-log EP raw database; 'fi-db'= Total local-log File-Inspection raw database; 'fw-db'= Total local-log Firewall raw database; 'aam-top-user-db'= Total local-log AAM top user summary database; 'ep-top-user-db'= Total local-log EP top user summary database; 'ep-top-src- db'= Total local-log EP top client summary database; 'ep-top-dst-db'= Total local-log EP top destination summary database; 'ep-top-domain-db'= Total local- log EP top domain summary database; 'ep-top-web-category-db'= Total local-log EP top web-category summary database; 'ep-top-host-db'= Total local-log EP top host summary database; 'fi-top-src-db'= Total local-log File-Inspection top source summary database; 'fi-top-dst-db'= Total local-log File-Inspection top destination summary database; 'fi-top-filename-db'= Total local-log File- Inspection top file name summary database; 'fi-top-file-ext-db'= Total local- log File-Inspection top file extension summary database; 'fi-top-url-db'= Total local-log File-Inspection top URL summary database; 'fw-top-app-db'= Total local-log Friewall top application summary database; 'fw-top-src-db'= Total local-log Friewall top source summary database; 'fw-top-app-src-db'= Total local-log Friewall top application and source summary database; 'fw-top- category-db'= Total local-log Friewall top category summary database; 'db- erro'= Total local-log database create error; 'query'= Total local-log axapi query; 'response'= Total local-log axapi response; 'query-error'= Total local- log axapi query error;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    ep_db (optional, any, None)
      Total local-log EP raw database


    fi_top_src_db (optional, any, None)
      Total local-log File-Inspection top source summary database


    dequeue (optional, any, None)
      Total local-log dequeue


    ep_top_web_category_db (optional, any, None)
      Total local-log EP top web-category summary database


    fi_db (optional, any, None)
      Total local-log File-Inspection raw database


    fw_top_app_db (optional, any, None)
      Total local-log Friewall top application summary database


    l2_log_summarized (optional, any, None)
      Total layer 2 log summarized


    query (optional, any, None)
      Total local-log axapi query


    aam_db (optional, any, None)
      Total local-log AAM raw database


    fw_top_category_db (optional, any, None)
      Total local-log Friewall top category summary database


    fw_db (optional, any, None)
      Total local-log Firewall raw database


    ep_top_dst_db (optional, any, None)
      Total local-log EP top destination summary database


    ep_top_user_db (optional, any, None)
      Total local-log EP top user summary database


    fw_top_app_src_db (optional, any, None)
      Total local-log Friewall top application and source summary database


    fi_top_filename_db (optional, any, None)
      Total local-log File-Inspection top file name summary database


    ep_top_host_db (optional, any, None)
      Total local-log EP top host summary database


    log_summarized (optional, any, None)
      Total raw log summarized


    ep_top_domain_db (optional, any, None)
      Total local-log EP top domain summary database


    enqueue_full (optional, any, None)
      Total local-log queue full


    fi_top_file_ext_db (optional, any, None)
      Total local-log File-Inspection top file extension summary database


    fw_top_src_db (optional, any, None)
      Total local-log Friewall top source summary database


    enqueue (optional, any, None)
      Total local-log enqueue


    raw_log_error (optional, any, None)
      Total raw log logging error


    db_erro (optional, any, None)
      Total local-log database create error


    fi_top_url_db (optional, any, None)
      Total local-log File-Inspection top URL summary database


    query_error (optional, any, None)
      Total local-log axapi query error


    response (optional, any, None)
      Total local-log axapi response


    raw_log (optional, any, None)
      Total local-log raw logs


    enqueue_error (optional, any, None)
      Total local-log enqueue error


    fi_top_dst_db (optional, any, None)
      Total local-log File-Inspection top destination summary database


    dequeue_error (optional, any, None)
      Total local-log dequeue processing error


    l1_log_summarized (optional, any, None)
      Total layer 1 log summarized


    log_summarized_error (optional, any, None)
      Total local-log summarization error


    ep_top_src_db (optional, any, None)
      Total local-log EP top client summary database


    aam_top_user_db (optional, any, None)
      Total local-log AAM top user summary database



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

