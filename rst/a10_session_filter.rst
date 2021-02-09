.. _a10_session_filter_module:


a10_session_filter -- Configures A10 session-filter
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create a convenience Filter to display/clear sessions






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  set (False, any, None)
    Set filter criteria


  name (True, any, None)
    Session filter name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  filter_cfg (False, any, None)
    Field filter_cfg


    app_category (optional, any, None)
      'aaa'= Protocol/application used for AAA (Authentification, Authorization and Accounting) purposes.; 'adult-content'= Adult content.; 'advertising'= Advertising networks and applications.; 'analytics-and-statistics'= user- analytics and statistics.; 'anonymizers-and-proxies'= Traffic-anonymization protocol/application.; 'audio-chat'= Protocol/application used for Audio Chat.; 'basic'= Protocols required for basic classification, e.g., ARP, HTTP; 'blog'= Blogging platform.; 'cdn'= Protocol/application used for Content-Delivery Networks.; 'chat'= Protocol/application used for Text Chat.; 'classified-ads'= Protocol/application used for Classified ads.; 'cloud-based-services'= SaaS and/or PaaS cloud based services.; 'crowdfunding'= Service for funding a project or venture by raising small amounts of money from a large number of people.; 'cryptocurrency'= Cryptocurrency.; 'database'= Database-specific protocols.; 'disposable-email'= Disposable email accounts.; 'ebook-reader'= Services for e-book readers.; 'email'= Native email protocol.; 'enterprise'= Protocol/application used in an enterprise network.; 'file-management'= Protocol/application designed specifically for file management and exchange, e.g., Dropbox, SMB; 'file-transfer'= Protocol that offers file transferring as a functionality as a secondary feature. e.g., Skype, Whatsapp; 'forum'= Online forum.; 'gaming'= Protocol/application used by games.; 'instant-messaging-and- multimedia-conferencing'= Protocol/application used for Instant messaging or multiconferencing.; 'internet-of-things'= Internet Of Things protocol/application.; 'mobile'= Mobile-specific protocol/application.; 'map- service'= Digital Maps service.; 'multimedia-streaming'= Protocol/application used for multimedia streaming.; 'networking'= Protocol used for (inter) networking purpose.; 'news-portal'= Protocol/application used for News Portals.; 'peer-to-peer'= Protocol/application used for Peer-to-peer purposes.; 'remote-access'= Protocol/application used for remote access.; 'scada'= SCADA (Supervisory control and data acquisition) protocols, all generations.; 'social-networks'= Social networking application.; 'software-update'= Auto- update protocol.; 'standards-based'= Protocol issued from standardized bodies such as IETF, ITU, IEEE, ETSI, OIF.; 'transportation'= Transportation.; 'video- chat'= Protocol/application used for Video Chat.; 'voip'= Application used for Voice over IP.; 'vpn-tunnels'= Protocol/application used for VPN or tunneling purposes.; 'web'= Application based on HTTP/HTTPS.; 'web-e-commerce'= Protocol/application used for E-commerce websites.; 'web-search-engines'= Protocol/application used for Web search portals.; 'web-websites'= Protocol/application used for Company Websites.; 'webmails'= Web email application.; 'web-ext-adult'= Web Extension Adult; 'web-ext-auctions'= Web Extension Auctions; 'web-ext-blogs'= Web Extension Blogs; 'web-ext-business- and-economy'= Web Extension Business and Economy; 'web-ext-cdns'= Web Extension CDNs; 'web-ext-collaboration'= Web Extension Collaboration; 'web-ext-computer- and-internet-info'= Web Extension Computer and Internet Info; 'web-ext- computer-and-internet-security'= Web Extension Computer and Internet Security; 'web-ext-dating'= Web Extension Dating; 'web-ext-educational-institutions'= Web Extension Educational Institutions; 'web-ext-entertainment-and-arts'= Web Extension Entertainment and Arts; 'web-ext-fashion-and-beauty'= Web Extension Fashion and Beauty; 'web-ext-file-share'= Web Extension File Share; 'web-ext- financial-services'= Web Extension Financial Services; 'web-ext-gambling'= Web Extension Gambling; 'web-ext-games'= Web Extension Games; 'web-ext-government'= Web Extension Government; 'web-ext-health-and-medicine'= Web Extension Health and Medicine; 'web-ext-individual-stock-advice-and-tools'= Web Extension Individual Stock Advice and Tools; 'web-ext-internet-portals'= Web Extension Internet Portals; 'web-ext-job-search'= Web Extension Job Search; 'web-ext- local-information'= Web Extension Local Information; 'web-ext-malware'= Web Extension Malware; 'web-ext-motor-vehicles'= Web Extension Motor Vehicles; 'web-ext-music'= Web Extension Music; 'web-ext-news'= Web Extension News; 'web- ext-p2p'= Web Extension P2P; 'web-ext-parked-sites'= Web Extension Parked Sites; 'web-ext-proxy-avoid-and-anonymizers'= Web Extension Proxy Avoid and Anonymizers; 'web-ext-real-estate'= Web Extension Real Estate; 'web-ext- reference-and-research'= Web Extension Reference and Research; 'web-ext-search- engines'= Web Extension Search Engines; 'web-ext-shopping'= Web Extension Shopping; 'web-ext-social-network'= Web Extension Social Network; 'web-ext- society'= Web Extension Society; 'web-ext-software'= Web Extension Software; 'web-ext-sports'= Web Extension Sports; 'web-ext-streaming-media'= Web Extension Streaming Media; 'web-ext-training-and-tools'= Web Extension Training and Tools; 'web-ext-translation'= Web Extension Translation; 'web-ext-travel'= Web Extension Travel; 'web-ext-web-advertisements'= Web Extension Web Advertisements; 'web-ext-web-based-email'= Web Extension Web based Email; 'web- ext-web-hosting'= Web Extension Web Hosting; 'web-ext-web-service'= Web Extension Web Service;


    source_mask (optional, any, None)
      Forward Source IP Subnet (Source Netmask)


    dport2 (optional, any, None)
      Forward Destination Port (Dest Port)


    source_addr (optional, any, None)
      Forward Source IP (Source IP address)


    dest_mask (optional, any, None)
      Forward Destination IP Subnet (Destination Netmask)


    session_type (optional, any, None)
      'ipv6'= Display ipv6 sessions only; 'sip'= SIP sessions;


    app (optional, any, None)
      Specify application(s), separated by comma (For example= http,tcp)


    dest_addr (optional, any, None)
      Forward Destination IP (Destination IP address)


    source_port (optional, any, None)
      Forward Source Port



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

