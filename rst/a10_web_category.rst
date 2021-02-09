.. _a10_web_category_module:


a10_web_category -- Configures A10 web-category
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Web-Category Commands






Parameters
----------

  oper (False, any, None)
    Field oper


    statistics (optional, any, None)
      Field statistics


    web_cat_database_status (optional, any, None)
      Field web_cat_database_status


    license (optional, any, None)
      Field license


    web_cat_version (optional, any, None)
      Field web_cat_version


    web_cat_database_name (optional, any, None)
      Field web_cat_database_name


    web_cat_last_successful_connection (optional, any, None)
      Field web_cat_last_successful_connection


    web_cat_next_update_time (optional, any, None)
      Field web_cat_next_update_time


    web_cat_failure_reason (optional, any, None)
      Field web_cat_failure_reason


    web_cat_database_size (optional, any, None)
      Field web_cat_database_size


    web_cat_connection_status (optional, any, None)
      Field web_cat_connection_status


    url (optional, any, None)
      Field url


    web_cat_database_version (optional, any, None)
      Field web_cat_database_version


    web_cat_last_update_time (optional, any, None)
      Field web_cat_last_update_time


    intercepted_urls (optional, any, None)
      Field intercepted_urls


    bypassed_urls (optional, any, None)
      Field bypassed_urls



  proxy_server (False, any, None)
    Field proxy_server


    auth_type (optional, any, None)
      'ntlm'= NTLM authentication(default); 'basic'= Basic authentication;


    username (optional, any, None)
      Username for proxy authentication


    domain (optional, any, None)
      Realm for NTLM authentication


    http_port (optional, any, None)
      Proxy server HTTP port


    https_port (optional, any, None)
      Proxy server HTTPS port(HTTP port will be used if not configured)


    secret_string (optional, any, None)
      password value


    encrypted (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


    proxy_host (optional, any, None)
      Proxy server hostname or IP address


    password (optional, any, None)
      Password for proxy authentication


    uuid (optional, any, None)
      uuid of the object



  enable (False, any, None)
    Enable BrightCloud SDK


  database_server (False, any, None)
    BrightCloud Database Server


  rtu_cache_size (False, any, None)
    Maximum cache size for storing RTU updates


  ansible_username (True, any, None)
    Username for AXAPI authentication


  rtu_update_disable (False, any, None)
    Disables real time updates(default enable)


  intercepted_urls (False, any, None)
    Field intercepted_urls


    uuid (optional, any, None)
      uuid of the object



  server_timeout (False, any, None)
    BrightCloud Servers Timeout in seconds (default= 15s)


  use_mgmt_port (False, any, None)
    Use management interface for all communication with BrightCloud


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  server (False, any, None)
    BrightCloud Query Server


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (False, any, None)
    BrightCloud Query Server Listening Port(default 80)


  db_update_time (False, any, None)
    Time of day to update database (default= 00=00)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  statistics (False, any, None)
    Field statistics


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  uuid (False, any, None)
    uuid of the object


  license (False, any, None)
    Field license


    uuid (optional, any, None)
      uuid of the object



  url (False, any, None)
    Field url


    uuid (optional, any, None)
      uuid of the object



  cloud_query_disable (False, any, None)
    Disables cloud queries for URL's not present in local database(default enable)


  rtu_update_interval (False, any, None)
    Interval to check for real time updates if enabled in mins(default 60)


  cloud_query_cache_size (False, any, None)
    Maximum cache size for storing cloud query results


  ansible_host (True, any, None)
    Host for AXAPI authentication


  category_list_list (False, any, None)
    Field category_list_list


    entertainment_and_arts (optional, any, None)
      Category Entertainment and Arts


    swimsuits_and_intimate_apparel (optional, any, None)
      Category Swimsuits and Intimate Apparel


    cult_and_occult (optional, any, None)
      Category Cult and Occult


    dynamic_comment (optional, any, None)
      Category Dynamic Comment


    confirmed_spam_sources (optional, any, None)
      Category Confirmed SPAM Sources


    pay_to_surf (optional, any, None)
      Category Pay to Surf


    phishing_and_other_fraud (optional, any, None)
      Category Phishing and Other Frauds


    fashion_and_beauty (optional, any, None)
      Category Fashion and Beauty


    sampling_enable (optional, any, None)
      Field sampling_enable


    adult_and_pornography (optional, any, None)
      Category Adult and Pornography


    bot_nets (optional, any, None)
      Category Bot Nets


    cheating (optional, any, None)
      Category Cheating


    uuid (optional, any, None)
      uuid of the object


    stock_advice_and_tools (optional, any, None)
      Category Stock Advice and Tools


    spyware_and_adware (optional, any, None)
      Category Spyware and Adware


    illegal (optional, any, None)
      Category Illegal


    keyloggers_and_monitoring (optional, any, None)
      Category Keyloggers and Monitoring


    cdns (optional, any, None)
      Category CDNs


    sex_education (optional, any, None)
      Category Sex Education


    sports (optional, any, None)
      Category Sports


    health_and_medicine (optional, any, None)
      Category Health and Medicine


    music (optional, any, None)
      Category Music


    search_engines (optional, any, None)
      Category Search Engines


    image_and_video_search (optional, any, None)
      Category Image and Video Search


    questionable (optional, any, None)
      Category Questionable


    reference_and_research (optional, any, None)
      Category Reference and Research


    shopping (optional, any, None)
      Category Shopping


    food_and_dining (optional, any, None)
      Category Food and Dining


    government (optional, any, None)
      Category Government


    drugs (optional, any, None)
      Category Abused Drugs


    personal_sites_and_blogs (optional, any, None)
      Category Personal sites and Blogs


    financial_services (optional, any, None)
      Category Financial Services


    translation (optional, any, None)
      Category Translation


    open_http_proxies (optional, any, None)
      Category Open HTTP Proxies


    web_advertisements (optional, any, None)
      Category Web Advertisements


    internet_communications (optional, any, None)
      Category Internet Communications


    hunting_and_fishing (optional, any, None)
      Category Hunting and Fishing


    computer_and_internet_info (optional, any, None)
      Category Computer and Internet Info


    name (optional, any, None)
      Web Category List name


    dead_sites (optional, any, None)
      Category Dead Sites (db Ops only)


    abortion (optional, any, None)
      Category Abortion


    training_and_tools (optional, any, None)
      Category Training and Tools


    educational_institutions (optional, any, None)
      Category Educational Institutions


    unconfirmed_spam_sources (optional, any, None)
      Category Unconfirmed SPAM Sources


    hate_and_racism (optional, any, None)
      Category Hate and Racism


    hacking (optional, any, None)
      Category Hacking


    streaming_media (optional, any, None)
      Category Streaming Media


    parked_domains (optional, any, None)
      Category Parked Domains


    nudity (optional, any, None)
      Category Nudity


    home_and_garden (optional, any, None)
      Category Home and Garden


    online_greeting_cards (optional, any, None)
      Category Online Greeting cards


    marijuana (optional, any, None)
      Category Marijuana


    society (optional, any, None)
      Category Society


    web_based_email (optional, any, None)
      Category Web based email


    real_estate (optional, any, None)
      Category Real Estate


    philosophy_and_politics (optional, any, None)
      Category Philosophy and Political Advocacy


    gross (optional, any, None)
      Category Gross


    business_and_economy (optional, any, None)
      Category Business and Economy


    travel (optional, any, None)
      Category Travel


    peer_to_peer (optional, any, None)
      Category Peer to Peer


    legal (optional, any, None)
      Category Legal


    weapons (optional, any, None)
      Category Weapons


    religion (optional, any, None)
      Category Religion


    private_ip_addresses (optional, any, None)
      Category Private IP Addresses


    alcohol_and_tobacco (optional, any, None)
      Category Alcohol and Tobacco


    gambling (optional, any, None)
      Category Gambling


    dating (optional, any, None)
      Category Dating


    uncategorized (optional, any, None)
      Uncategorized URLs


    shareware_and_freeware (optional, any, None)
      Category Shareware and Freeware


    news_and_media (optional, any, None)
      Category News and Media


    internet_portals (optional, any, None)
      Category Internet Portals


    personal_storage (optional, any, None)
      Category Personal Storage


    social_network (optional, any, None)
      Category Social Network


    job_search (optional, any, None)
      Category Job Search


    malware_sites (optional, any, None)
      Category Malware Sites


    military (optional, any, None)
      Category Military


    recreation_and_hobbies (optional, any, None)
      Category Recreation and Hobbies


    spam_urls (optional, any, None)
      Category SPAM URLs


    kids (optional, any, None)
      Category Kids


    web_hosting_sites (optional, any, None)
      Category Web Hosting Sites


    violence (optional, any, None)
      Category Violence


    local_information (optional, any, None)
      Category Local Information


    motor_vehicles (optional, any, None)
      Category Motor Vehicles


    games (optional, any, None)
      Category Games


    auctions (optional, any, None)
      Category Auctions


    proxy_avoid_and_anonymizers (optional, any, None)
      Category Proxy Avoid and Anonymizers


    user_tag (optional, any, None)
      Customized tag


    computer_and_internet_security (optional, any, None)
      Category Computer and Internet Security



  state (True, any, None)
    State of the object to be created.


  ssl_port (False, any, None)
    BrightCloud Servers SSL Port(default 443)


  remote_syslog_enable (False, any, None)
    Enable data plane logging to a remote syslog server


  ansible_password (True, any, None)
    Password for AXAPI authentication


  bypassed_urls (False, any, None)
    Field bypassed_urls


    uuid (optional, any, None)
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

