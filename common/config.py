ja3_configs = [
    {
      "ip": "141.164.52.100:23641",
      "http_version": "h2",
      "method": "GET",
      "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
      "tls": {
        "ciphers": [
          "TLS_GREASE (0xAAAA)",
          "TLS_AES_128_GCM_SHA256",
          "TLS_AES_256_GCM_SHA384",
          "TLS_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
          "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
          "TLS_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_RSA_WITH_AES_128_CBC_SHA",
          "TLS_RSA_WITH_AES_256_CBC_SHA"
        ],
        "extensions": [
          {
            "name": "TLS_GREASE (0x9a9a)"
          },
          {
            "name": "signed_certificate_timestamp (18)"
          },
          {
            "name": "extensionEncryptedClientHello (boringssl) (65037)",
            "data": "0000010001ce0020b32add585045418bb827b3035a2a138d98a041ca62b79ed382aa0f59fb75b24200b09fdf2a3aba7b09e6839fea7e7d6639bac6a03b525fc17b753b29d1a48b542fd3ee4ab9bc746b38855d97c9cc61da2e3a11c0a389c63706b22b31933cc2fc59a21707fb85dad0d7910c4d4a97ce4d98768555d5a0529d9b1184ae816f274810e79b1807ff2850f8b9181864ebf25380c25f446e4823282570416c77f972e313378018c6311e3df1070688b866cccf69fad5bfa327afc81a9623cfdd407f07fb8a7916806bfbdd799de2de9197b35ef923"
          },
          {
            "name": "compress_certificate (27)",
            "algorithms": [
              "brotli (2)"
            ]
          },
          {
            "name": "signature_algorithms (13)",
            "signature_algorithms": [
              "ecdsa_secp256r1_sha256",
              "rsa_pss_rsae_sha256",
              "rsa_pkcs1_sha256",
              "ecdsa_secp384r1_sha384",
              "rsa_pss_rsae_sha384",
              "rsa_pkcs1_sha384",
              "rsa_pss_rsae_sha512",
              "rsa_pkcs1_sha512"
            ]
          },
          {
            "name": "psk_key_exchange_modes (45)",
            "PSK_Key_Exchange_Mode": "PSK with (EC)DHE key establishment (psk_dhe_ke) (1)"
          },
          {
            "name": "supported_versions (43)",
            "versions": [
              "TLS_GREASE (0x3a3a)",
              "TLS 1.3",
              "TLS 1.2"
            ]
          },
          {
            "name": "server_name (0)",
            "server_name": "tls.peet.ws"
          },
          {
            "name": "supported_groups (10)",
            "supported_groups": [
              "TLS_GREASE (0xbaba)",
              "X25519 (29)",
              "P-256 (23)",
              "P-384 (24)"
            ]
          },
          {
            "name": "session_ticket (35)",
            "data": ""
          },
          {
            "name": "status_request (5)",
            "status_request": {
              "certificate_status_type": "OSCP (1)",
              "responder_id_list_length": 0,
              "request_extensions_length": 0
            }
          },
          {
            "name": "extended_master_secret (23)",
            "master_secret_data": "",
            "extended_master_secret_data": ""
          },
          {
            "name": "key_share (51)",
            "shared_keys": [
              {
                "TLS_GREASE (0xbaba)": "00"
              },
              {
                "X25519 (29)": "cbfea5295917098bb6a58e9f6ba62f1889681025518bc60d8ca38c203320a816"
              }
            ]
          },
          {
            "name": "extensionRenegotiationInfo (boringssl) (65281)",
            "data": "00"
          },
          {
            "name": "application_settings (17513)",
            "protocols": [
              "h2"
            ]
          },
          {
            "name": "ec_point_formats (11)",
            "elliptic_curves_point_formats": [
              "0x00"
            ]
          },
          {
            "name": "application_layer_protocol_negotiation (16)",
            "protocols": [
              "h2",
              "http/1.1"
            ]
          },
          {
            "name": "TLS_GREASE (0x0a0a)"
          }
        ],
        "tls_version_record": "771",
        "tls_version_negotiated": "772",
        "ja3": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,18-65037-27-13-45-43-0-10-35-5-23-51-65281-17513-11-16,29-23-24,0",
        "ja3_hash": "b4fb3730a7bdf8223b41c5e8dd021404",
        "ja4": "t13d1516h2_8daaf6152771_b1ff8ab2d16f",
        "peetprint": "GREASE-772-771|2-1.1|GREASE-29-23-24|1027-2052-1025-1283-2053-1281-2054-1537|1|2|GREASE-4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53|0-10-11-13-16-17513-18-23-27-35-43-45-5-51-65037-65281-GREASE-GREASE",
        "peetprint_hash": "8ad9325e12f531d2983b78860de7b0ec",
        "client_random": "4a7b30a49d7749a58b5fa241fad272f9ed3608db3570828286c64c78e0cedb16",
        "session_id": "1b8d77172e9f56e3998fa955fd1a0ad40ac0423e5e4be24d5ed635fa9fe4fe75"
      },
      "http2": {
        "akamai_fingerprint": "1:65536,2:0,4:6291456,6:262144|15663105|0|m,a,s,p",
        "akamai_fingerprint_hash": "90224459f8bf70b7d0a8797eb916dbc9",
        "sent_frames": [
          {
            "frame_type": "SETTINGS",
            "length": 24,
            "settings": [
              "HEADER_TABLE_SIZE = 65536",
              "ENABLE_PUSH = 0",
              "INITIAL_WINDOW_SIZE = 6291456",
              "MAX_HEADER_LIST_SIZE = 262144"
            ]
          },
          {
            "frame_type": "WINDOW_UPDATE",
            "length": 4,
            "increment": 15663105
          },
          {
            "frame_type": "HEADERS",
            "stream_id": 1,
            "length": 445,
            "headers": [
              ":method: GET",
              ":authority: tls.peet.ws",
              ":scheme: https",
              ":path: /api/all",
              "sec-ch-ua: \\\"Google Chrome\\\";v=\\\"123\\\", \\\"Not:A-Brand\\\";v=\\\"8\\\", \\\"Chromium\\\";v=\\\"123\\",
              "sec-ch-ua-mobile: ?0",
              "sec-ch-ua-platform: \\\"Windows\\",
              "upgrade-insecure-requests: 1",
              "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
              "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
              "sec-fetch-site: none",
              "sec-fetch-mode: navigate",
              "sec-fetch-user: ?1",
              "sec-fetch-dest: document",
              "accept-encoding: gzip, deflate, br, zstd",
              "accept-language: zh-CN,zh;q=0.9"
            ],
            "flags": [
              "EndStream (0x1)",
              "EndHeaders (0x4)",
              "Priority (0x20)"
            ],
            "priority": {
              "weight": 256,
              "depends_on": 0,
              "exclusive": 1
            }
          }
        ]
      },
      "tcpip": {
        "cap_length": 66,
        "dst_port": 443,
        "src_port": 23641,
        "ip": {
          "id": 52732,
          "ttl": 54,
          "ip_version": 4,
          "dst_ip": "205.185.123.167",
          "src_ip": "141.164.52.100"
        },
        "tcp": {
          "ack": 2046008190,
          "checksum": 58381,
          "seq": 3739640074,
          "window": 83
        }
      }
    },
    {
        "ip": "141.164.52.100:28825",
        "http_version": "h2",
        "method": "GET",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
        "tls": {
            "ciphers": [
                "TLS_GREASE (0x7A7A)",
                "TLS_AES_128_GCM_SHA256",
                "TLS_AES_256_GCM_SHA384",
                "TLS_CHACHA20_POLY1305_SHA256",
                "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
                "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
                "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
                "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
                "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256",
                "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256",
                "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
                "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
                "TLS_RSA_WITH_AES_128_GCM_SHA256",
                "TLS_RSA_WITH_AES_256_GCM_SHA384",
                "TLS_RSA_WITH_AES_128_CBC_SHA",
                "TLS_RSA_WITH_AES_256_CBC_SHA"
            ],
            "extensions": [
                {
                    "name": "TLS_GREASE (0x2a2a)"
                },
                {
                    "name": "status_request (5)",
                    "status_request": {
                        "certificate_status_type": "OSCP (1)",
                        "responder_id_list_length": 0,
                        "request_extensions_length": 0
                    }
                },
                {
                    "name": "session_ticket (35)",
                    "data": ""
                },
                {
                    "name": "psk_key_exchange_modes (45)",
                    "PSK_Key_Exchange_Mode": "PSK with (EC)DHE key establishment (psk_dhe_ke) (1)"
                },
                {
                    "name": "supported_versions (43)",
                    "versions": [
                        "TLS_GREASE (0x8a8a)",
                        "TLS 1.3",
                        "TLS 1.2"
                    ]
                },
                {
                    "name": "ec_point_formats (11)",
                    "elliptic_curves_point_formats": [
                        "0x00"
                    ]
                },
                {
                    "name": "extensionEncryptedClientHello (boringssl) (65037)",
                    "data": "0000010001d60020e07f6335b9cdb0d729792f66408c43565911d45b72c67b74579c6c04956fbb3500b07772024e3147f071c19df5e421ef0231ae24dc06320e35e12b2a6a221f3ee0b46a630a1f55e2dca907baf1662e377a6a564a8d00a39f308946cda74deda4f4eb6bf938dbbb34b4bcb6b24b9c5d4bdde8a6374bb7939b62cf8c34ad80a534691f44c91fe33b7742699a351959591e36ffa8b5aae5fac3a960ba8e66107d33d19a58ff3389b669cf9c068be019309da23ea0e839ad36622114e65a31b1e3fcc99e79ef428f3ad1851172dc224f5ce1f59d"
                },
                {
                    "name": "server_name (0)",
                    "server_name": "tls.peet.ws"
                },
                {
                    "name": "key_share (51)",
                    "shared_keys": [
                        {
                            "TLS_GREASE (0x7a7a)": "00"
                        },
                        {
                            "X25519 (29)": "d9c661d5cfdc34abb2b9ed29608f19b9f3125298ceb0e33e49662c9961b8ec26"
                        }
                    ]
                },
                {
                    "name": "signed_certificate_timestamp (18)"
                },
                {
                    "name": "extensionRenegotiationInfo (boringssl) (65281)",
                    "data": "00"
                },
                {
                    "name": "application_layer_protocol_negotiation (16)",
                    "protocols": [
                        "h2",
                        "http/1.1"
                    ]
                },
                {
                    "name": "supported_groups (10)",
                    "supported_groups": [
                        "TLS_GREASE (0x7a7a)",
                        "X25519 (29)",
                        "P-256 (23)",
                        "P-384 (24)"
                    ]
                },
                {
                    "name": "extended_master_secret (23)",
                    "master_secret_data": "",
                    "extended_master_secret_data": ""
                },
                {
                    "name": "application_settings (17513)",
                    "protocols": [
                        "h2"
                    ]
                },
                {
                    "name": "signature_algorithms (13)",
                    "signature_algorithms": [
                        "ecdsa_secp256r1_sha256",
                        "rsa_pss_rsae_sha256",
                        "rsa_pkcs1_sha256",
                        "ecdsa_secp384r1_sha384",
                        "rsa_pss_rsae_sha384",
                        "rsa_pkcs1_sha384",
                        "rsa_pss_rsae_sha512",
                        "rsa_pkcs1_sha512"
                    ]
                },
                {
                    "name": "compress_certificate (27)",
                    "algorithms": [
                        "brotli (2)"
                    ]
                },
                {
                    "name": "TLS_GREASE (0x3a3a)"
                }
            ],
            "tls_version_record": "771",
            "tls_version_negotiated": "772",
            "ja3": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,5-35-45-43-11-65037-0-51-18-65281-16-10-23-17513-13-27,29-23-24,0",
            "ja3_hash": "d8ed43771952efd737ace8b655141c2b",
            "ja4": "t13d1516h2_8daaf6152771_b1ff8ab2d16f",
            "peetprint": "GREASE-772-771|2-1.1|GREASE-29-23-24|1027-2052-1025-1283-2053-1281-2054-1537|1|2|GREASE-4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53|0-10-11-13-16-17513-18-23-27-35-43-45-5-51-65037-65281-GREASE-GREASE",
            "peetprint_hash": "8ad9325e12f531d2983b78860de7b0ec",
            "client_random": "2c6e2f7582b5744bcea77974ab9f064faa2978e53ea73b0323dcd2c6b923e133",
            "session_id": "ecd57acc8c24efc7e0bd97cc8f33af55c9f5127187f6c7be445baf35c062c49b"
        },
        "http2": {
            "akamai_fingerprint": "1:65536,2:0,4:6291456,6:262144|15663105|0|m,a,s,p",
            "akamai_fingerprint_hash": "90224459f8bf70b7d0a8797eb916dbc9",
            "sent_frames": [
                {
                    "frame_type": "SETTINGS",
                    "length": 24,
                    "settings": [
                        "HEADER_TABLE_SIZE = 65536",
                        "ENABLE_PUSH = 0",
                        "INITIAL_WINDOW_SIZE = 6291456",
                        "MAX_HEADER_LIST_SIZE = 262144"
                    ]
                },
                {
                    "frame_type": "WINDOW_UPDATE",
                    "length": 4,
                    "increment": 15663105
                },
                {
                    "frame_type": "HEADERS",
                    "stream_id": 1,
                    "length": 482,
                    "headers": [
                        ":method: GET",
                        ":authority: tls.peet.ws",
                        ":scheme: https",
                        ":path: /api/all",
                        "sec-ch-ua: \\\"Microsoft Edge\\\";v=\\\"123\\\", \\\"Not:A-Brand\\\";v=\\\"8\\\", \\\"Chromium\\\";v=\\\"123\\",
                        "sec-ch-ua-mobile: ?0",
                        "sec-ch-ua-platform: \\\"Windows\\",
                        "upgrade-insecure-requests: 1",
                        "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
                        "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "sec-fetch-site: none",
                        "sec-fetch-mode: navigate",
                        "sec-fetch-user: ?1",
                        "sec-fetch-dest: document",
                        "accept-encoding: gzip, deflate, br, zstd",
                        "accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
                    ],
                    "flags": [
                        "EndStream (0x1)",
                        "EndHeaders (0x4)",
                        "Priority (0x20)"
                    ],
                    "priority": {
                        "weight": 256,
                        "depends_on": 0,
                        "exclusive": 1
                    }
                }
            ]
        },
        "tcpip": {
            "cap_length": 66,
            "dst_port": 443,
            "src_port": 28825,
            "ip": {
                "id": 51068,
                "ttl": 54,
                "ip_version": 4,
                "dst_ip": "205.185.123.167",
                "src_ip": "141.164.52.100"
            },
            "tcp": {
                "ack": 728859184,
                "checksum": 42390,
                "seq": 94047335,
                "window": 83
            }
        }
    },
    {
      "ip": "141.164.52.100:16105",
      "http_version": "h2",
      "method": "GET",
      "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
      "tls": {
        "ciphers": [
          "TLS_GREASE (0xEAEA)",
          "TLS_AES_128_GCM_SHA256",
          "TLS_AES_256_GCM_SHA384",
          "TLS_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
          "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
          "TLS_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_RSA_WITH_AES_128_CBC_SHA",
          "TLS_RSA_WITH_AES_256_CBC_SHA"
        ],
        "extensions": [
          {
            "name": "TLS_GREASE (0xeaea)"
          },
          {
            "name": "application_layer_protocol_negotiation (16)",
            "protocols": [
              "h2",
              "http/1.1"
            ]
          },
          {
            "name": "extensionRenegotiationInfo (boringssl) (65281)",
            "data": "00"
          },
          {
            "name": "supported_groups (10)",
            "supported_groups": [
              "TLS_GREASE (0x3a3a)",
              "X25519 (29)",
              "P-256 (23)",
              "P-384 (24)"
            ]
          },
          {
            "name": "session_ticket (35)",
            "data": ""
          },
          {
            "name": "application_settings (17513)",
            "protocols": [
              "h2"
            ]
          },
          {
            "name": "key_share (51)",
            "shared_keys": [
              {
                "TLS_GREASE (0x3a3a)": "00"
              },
              {
                "X25519 (29)": "ec571e2229c3e594a521fa692a5d8877676650d8f06558d9e88eade13e6b837e"
              }
            ]
          },
          {
            "name": "status_request (5)",
            "status_request": {
              "certificate_status_type": "OSCP (1)",
              "responder_id_list_length": 0,
              "request_extensions_length": 0
            }
          },
          {
            "name": "signature_algorithms (13)",
            "signature_algorithms": [
              "ecdsa_secp256r1_sha256",
              "rsa_pss_rsae_sha256",
              "rsa_pkcs1_sha256",
              "ecdsa_secp384r1_sha384",
              "rsa_pss_rsae_sha384",
              "rsa_pkcs1_sha384",
              "rsa_pss_rsae_sha512",
              "rsa_pkcs1_sha512"
            ]
          },
          {
            "name": "ec_point_formats (11)",
            "elliptic_curves_point_formats": [
              "0x00"
            ]
          },
          {
            "name": "supported_versions (43)",
            "versions": [
              "TLS_GREASE (0xdada)",
              "TLS 1.3",
              "TLS 1.2"
            ]
          },
          {
            "name": "psk_key_exchange_modes (45)",
            "PSK_Key_Exchange_Mode": "PSK with (EC)DHE key establishment (psk_dhe_ke) (1)"
          },
          {
            "name": "compress_certificate (27)",
            "algorithms": [
              "brotli (2)"
            ]
          },
          {
            "name": "signed_certificate_timestamp (18)"
          },
          {
            "name": "extensionEncryptedClientHello (boringssl) (65037)",
            "data": "00000100019300209775db8603f53c5d97547b75f710fb586eaabf3e78fa9092e2207080bca650790090812d0ff8ba2944c052e3738e81689034bbed4057b4ea895403293ba9de048baec9edd7fe4fd4270a6c4c1dab858bab6538dbf114c31b9c83d81e07e349b3e3d63493c843fc341ce4d652483c0b244b1eacd222c1137b179efa4a87477c12140e2733513ca4f7bc9588ecd4059dc904aa231b53b5b6af2f14b305acb6b0dface7fecfe6495dfdc49351c1b20fb7263ec3"
          },
          {
            "name": "server_name (0)",
            "server_name": "tls.peet.ws"
          },
          {
            "name": "extended_master_secret (23)",
            "master_secret_data": "",
            "extended_master_secret_data": ""
          },
          {
            "name": "TLS_GREASE (0x2a2a)"
          },
          {
            "name": "padding (21)",
            "padding_data_length": 28
          }
        ],
        "tls_version_record": "771",
        "tls_version_negotiated": "772",
        "ja3": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,16-65281-10-35-17513-51-5-13-11-43-45-27-18-65037-0-23-21,29-23-24,0",
        "ja3_hash": "38866db8749fe7159cfc3667a2044ad6",
        "ja4": "t13d1517h2_8daaf6152771_39ff608a2b00",
        "peetprint": "GREASE-772-771|2-1.1|GREASE-29-23-24|1027-2052-1025-1283-2053-1281-2054-1537|1|2|GREASE-4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53|0-10-11-13-16-17513-18-21-23-27-35-43-45-5-51-65037-65281-GREASE-GREASE",
        "peetprint_hash": "96b72764e015fb524fd8d005deb7209d",
        "client_random": "60443a49b4ed0bacb12f5c1ab790d1520eaa65f2e907e47f55849782a99cd216",
        "session_id": "8ad0382d81d608cb5a2897d5752b35bc14891ae60c65e6530cfae8a4ef16c166"
      },
      "http2": {
        "akamai_fingerprint": "1:65536,2:0,4:6291456,6:262144|15663105|0|m,a,s,p",
        "akamai_fingerprint_hash": "90224459f8bf70b7d0a8797eb916dbc9",
        "sent_frames": [
          {
            "frame_type": "SETTINGS",
            "length": 24,
            "settings": [
              "HEADER_TABLE_SIZE = 65536",
              "ENABLE_PUSH = 0",
              "INITIAL_WINDOW_SIZE = 6291456",
              "MAX_HEADER_LIST_SIZE = 262144"
            ]
          },
          {
            "frame_type": "WINDOW_UPDATE",
            "length": 4,
            "increment": 15663105
          },
          {
            "frame_type": "HEADERS",
            "stream_id": 1,
            "length": 445,
            "headers": [
              ":method: GET",
              ":authority: tls.peet.ws",
              ":scheme: https",
              ":path: /api/all",
              "sec-ch-ua: \\\"Google Chrome\\\";v=\\\"123\\\", \\\"Not:A-Brand\\\";v=\\\"8\\\", \\\"Chromium\\\";v=\\\"123\\",
              "sec-ch-ua-mobile: ?0",
              "sec-ch-ua-platform: \\\"Windows\\",
              "upgrade-insecure-requests: 1",
              "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
              "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
              "sec-fetch-site: none",
              "sec-fetch-mode: navigate",
              "sec-fetch-user: ?1",
              "sec-fetch-dest: document",
              "accept-encoding: gzip, deflate, br, zstd",
              "accept-language: zh-CN,zh;q=0.9"
            ],
            "flags": [
              "EndStream (0x1)",
              "EndHeaders (0x4)",
              "Priority (0x20)"
            ],
            "priority": {
              "weight": 256,
              "depends_on": 0,
              "exclusive": 1
            }
          }
        ]
      },
      "tcpip": {
        "cap_length": 66,
        "dst_port": 443,
        "src_port": 16105,
        "ip": {
          "id": 64019,
          "ttl": 54,
          "ip_version": 4,
          "dst_ip": "205.185.123.167",
          "src_ip": "141.164.52.100"
        },
        "tcp": {
          "ack": 3277666179,
          "checksum": 42241,
          "seq": 105110497,
          "window": 83
        }
      }
    },
    {
      "ip": "103.85.172.132:51740",
      "http_version": "h2",
      "method": "GET",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
      "tls": {
        "ciphers": [
          "TLS_GREASE (0x9A9A)",
          "TLS_AES_128_GCM_SHA256",
          "TLS_AES_256_GCM_SHA384",
          "TLS_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
          "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
          "TLS_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_RSA_WITH_AES_128_CBC_SHA",
          "TLS_RSA_WITH_AES_256_CBC_SHA"
        ],
        "extensions": [
          {
            "name": "TLS_GREASE (0x4a4a)"
          },
          {
            "name": "extensionEncryptedClientHello (boringssl) (65037)",
            "data": "0000010001cc0020350e96118d7a7302d1a00f92ce35478659ac77322c1aec52c3f3782c5524c62c0090c99d96f382ff6f8e32dc41308c46de477b68550b56ba85e99b104b0ece3b752f406c8ed8a64b4cf3f921ba4cfabca778f37e53bacb73c526ba175c3810926defb05980d64a0e82e57018f7e286c5e3cf0639b7d4d3230142a863c0bf91c676bf64b9043fcb962706c60b2c25f8ea3737c6e7fdc65525498621a5e799a931a021da14a66bfa72498ec7666aafba737868"
          },
          {
            "name": "key_share (51)",
            "shared_keys": [
              {
                "TLS_GREASE (0x0a0a)": "00"
              },
              {
                "X25519 (29)": "5faf5145cd17e0d89a33d0d3dcc7480d19f55c4e6e805a5dbed4742f8eafc736"
              }
            ]
          },
          {
            "name": "supported_groups (10)",
            "supported_groups": [
              "TLS_GREASE (0x0a0a)",
              "X25519 (29)",
              "P-256 (23)",
              "P-384 (24)"
            ]
          },
          {
            "name": "extended_master_secret (23)",
            "master_secret_data": "",
            "extended_master_secret_data": ""
          },
          {
            "name": "ec_point_formats (11)",
            "elliptic_curves_point_formats": [
              "0x00"
            ]
          },
          {
            "name": "compress_certificate (27)",
            "algorithms": [
              "brotli (2)"
            ]
          },
          {
            "name": "supported_versions (43)",
            "versions": [
              "TLS_GREASE (0x1a1a)",
              "TLS 1.3",
              "TLS 1.2"
            ]
          },
          {
            "name": "application_settings (17513)",
            "protocols": [
              "h2"
            ]
          },
          {
            "name": "application_layer_protocol_negotiation (16)",
            "protocols": [
              "h2",
              "http/1.1"
            ]
          },
          {
            "name": "psk_key_exchange_modes (45)",
            "PSK_Key_Exchange_Mode": "PSK with (EC)DHE key establishment (psk_dhe_ke) (1)"
          },
          {
            "name": "session_ticket (35)",
            "data": ""
          },
          {
            "name": "server_name (0)",
            "server_name": "tls.peet.ws"
          },
          {
            "name": "extensionRenegotiationInfo (boringssl) (65281)",
            "data": "00"
          },
          {
            "name": "signature_algorithms (13)",
            "signature_algorithms": [
              "ecdsa_secp256r1_sha256",
              "rsa_pss_rsae_sha256",
              "rsa_pkcs1_sha256",
              "ecdsa_secp384r1_sha384",
              "rsa_pss_rsae_sha384",
              "rsa_pkcs1_sha384",
              "rsa_pss_rsae_sha512",
              "rsa_pkcs1_sha512"
            ]
          },
          {
            "name": "status_request (5)",
            "status_request": {
              "certificate_status_type": "OSCP (1)",
              "responder_id_list_length": 0,
              "request_extensions_length": 0
            }
          },
          {
            "name": "signed_certificate_timestamp (18)"
          },
          {
            "name": "TLS_GREASE (0x7a7a)"
          },
          {
            "name": "padding (21)",
            "padding_data_length": 28
          }
        ],
        "tls_version_record": "771",
        "tls_version_negotiated": "772",
        "ja3": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,65037-51-10-23-11-27-43-17513-16-45-35-0-65281-13-5-18-21,29-23-24,0",
        "ja3_hash": "b9ca227f51626186e863c34d45e39aa2",
        "ja4": "t13d1517h2_8daaf6152771_39ff608a2b00",
        "peetprint": "GREASE-772-771|2-1.1|GREASE-29-23-24|1027-2052-1025-1283-2053-1281-2054-1537|1|2|GREASE-4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53|0-10-11-13-16-17513-18-21-23-27-35-43-45-5-51-65037-65281-GREASE-GREASE",
        "peetprint_hash": "96b72764e015fb524fd8d005deb7209d",
        "client_random": "cdc7ec43b5812c3169dbdbde02f0fbe4b2b0dec231a1b2ed9c6ea1c7f2c70016",
        "session_id": "d6c2259973e508a7571d92b6b5d2ebe8820da7571c880cef3f93daf6553ae57a"
      },
      "http2": {
        "akamai_fingerprint": "1:65536,2:0,4:6291456,6:262144|15663105|0|m,a,s,p",
        "akamai_fingerprint_hash": "90224459f8bf70b7d0a8797eb916dbc9",
        "sent_frames": [
          {
            "frame_type": "SETTINGS",
            "length": 24,
            "settings": [
              "HEADER_TABLE_SIZE = 65536",
              "ENABLE_PUSH = 0",
              "INITIAL_WINDOW_SIZE = 6291456",
              "MAX_HEADER_LIST_SIZE = 262144"
            ]
          },
          {
            "frame_type": "WINDOW_UPDATE",
            "length": 4,
            "increment": 15663105
          },
          {
            "frame_type": "HEADERS",
            "stream_id": 1,
            "length": 455,
            "headers": [
              ":method: GET",
              ":authority: tls.peet.ws",
              ":scheme: https",
              ":path: /api/all",
              "sec-ch-ua: \\\"Google Chrome\\\";v=\\\"123\\\", \\\"Not:A-Brand\\\";v=\\\"8\\\", \\\"Chromium\\\";v=\\\"123\\",
              "sec-ch-ua-mobile: ?0",
              "sec-ch-ua-platform: \\\"macOS\\",
              "upgrade-insecure-requests: 1",
              "user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
              "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
              "sec-fetch-site: none",
              "sec-fetch-mode: navigate",
              "sec-fetch-user: ?1",
              "sec-fetch-dest: document",
              "accept-encoding: gzip, deflate, br, zstd",
              "accept-language: zh-CN,zh;q=0.9,en;q=0.8"
            ],
            "flags": [
              "EndStream (0x1)",
              "EndHeaders (0x4)",
              "Priority (0x20)"
            ],
            "priority": {
              "weight": 256,
              "depends_on": 0,
              "exclusive": 1
            }
          }
        ]
      },
      "tcpip": {
        "cap_length": 583,
        "dst_port": 443,
        "src_port": 51740,
        "ip": {
          "ttl": 47,
          "ip_version": 4,
          "dst_ip": "205.185.123.167",
          "src_ip": "103.85.172.132"
        },
        "tcp": {
          "ack": 138335670,
          "checksum": 61864,
          "seq": 3443107417,
          "window": 2060
        }
      }
    },
    {
      "ip": "103.85.172.132:52325",
      "http_version": "h2",
      "method": "GET",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
      "tls": {
        "ciphers": [
          "TLS_AES_128_GCM_SHA256",
          "TLS_AES_256_GCM_SHA384",
          "TLS_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
          "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
          "TLS_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_RSA_WITH_AES_128_CBC_SHA",
          "TLS_RSA_WITH_AES_256_CBC_SHA",
          "TLS_RSA_WITH_3DES_EDE_CBC_SHA"
        ],
        "extensions": [
          {
            "name": "server_name (0)",
            "server_name": "tls.peet.ws"
          },
          {
            "name": "extended_master_secret (23)",
            "master_secret_data": "",
            "extended_master_secret_data": ""
          },
          {
            "name": "extensionRenegotiationInfo (boringssl) (65281)",
            "data": "00"
          },
          {
            "name": "supported_groups (10)",
            "supported_groups": [
              "X25519 (29)",
              "P-256 (23)",
              "P-384 (24)",
              "ffdhe3072 (257)"
            ]
          },
          {
            "name": "ec_point_formats (11)",
            "elliptic_curves_point_formats": [
              "0x00"
            ]
          },
          {
            "name": "session_ticket (35)",
            "data": ""
          },
          {
            "name": "application_layer_protocol_negotiation (16)",
            "protocols": [
              "h2",
              "http/1.1"
            ]
          },
          {
            "name": "status_request (5)",
            "status_request": {
              "certificate_status_type": "OSCP (1)",
              "responder_id_list_length": 0,
              "request_extensions_length": 0
            }
          },
          {
            "name": "signature_algorithms (13)",
            "signature_algorithms": [
              "ecdsa_secp256r1_sha256",
              "rsa_pss_rsae_sha256",
              "rsa_pkcs1_sha256",
              "ecdsa_secp384r1_sha384",
              "rsa_pss_rsae_sha384",
              "rsa_pkcs1_sha384",
              "rsa_pss_rsae_sha512",
              "rsa_pkcs1_sha512",
              "rsa_pkcs1_sha1",
              "0x1010"
            ]
          },
          {
            "name": "signed_certificate_timestamp (18)"
          },
          {
            "name": "key_share (51)",
            "shared_keys": [
              {
                "X25519 (29)": "69588996c111f35109f3b7402043c4b6aab3ffd32a83f86299d053117d9bf26f"
              }
            ]
          },
          {
            "name": "psk_key_exchange_modes (45)",
            "PSK_Key_Exchange_Mode": "PSK with (EC)DHE key establishment (psk_dhe_ke) (1)"
          },
          {
            "name": "supported_versions (43)",
            "versions": [
              "TLS 1.3",
              "TLS 1.2",
              "TLS 1.1",
              "TLS 1.0"
            ]
          },
          {
            "name": "compress_certificate (27)",
            "algorithms": [
              "brotli (2)"
            ]
          },
          {
            "name": "padding (21)",
            "padding_data_length": 122
          },
          {
            "name": "pre_shared_key (41)",
            "data": "00770071c9c8bf05f0a62843dc750d4020783270f04dc8c0a9a35ab06827cfea4dda539c6a3b42e5151030ea09459b51cebc90a53aa093081f3667fefc9393ff81874e7a7ea06c624f1dac946957d503692154d66b8ade5eef40850fdca141fc54d2342d0e8d13e39c5671f02510a2f1248e2aca1ac67a1c4a002120c508b629e6aa0280e3bc9e36ccca4698861ffa261bebe12de4bbe0e471f55abb"
          }
        ],
        "tls_version_record": "771",
        "tls_version_negotiated": "772",
        "ja3": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53-10,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-21-41,29-23-24-257,0",
        "ja3_hash": "19c8cf31d7e69a1956e3bc4c96693bce",
        "ja4": "t13d1616h2_46e7e9700bed_b0b0b1c1b67b",
        "peetprint": "772-771-770-769|2-1.1|29-23-24-257|1027-2052-1025-1283-2053-1281-2054-1537-513-4112|1|2|4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53-10|0-10-11-13-16-18-21-23-27-35-41-43-45-5-51-65281",
        "peetprint_hash": "8e3499602cab6f7da6c6a5bf07789690",
        "client_random": "9696c68eaa96f5764e1a100d8309f6fccd8d34a6a097da110718427e6190749c",
        "session_id": "7458565e3e74fd0f9173674f51cfb1040fba703b77a1a58e9db9340da18a28ca"
      },
      "http2": {
        "akamai_fingerprint": "1:65536,3:1000,4:6291456|15663105|0|m,a,s,p",
        "akamai_fingerprint_hash": "0671021d33b7fb9f0728b3e8f0ee1089",
        "sent_frames": [
          {
            "frame_type": "SETTINGS",
            "length": 18,
            "settings": [
              "HEADER_TABLE_SIZE = 65536",
              "MAX_CONCURRENT_STREAMS = 1000",
              "INITIAL_WINDOW_SIZE = 6291456"
            ]
          },
          {
            "frame_type": "WINDOW_UPDATE",
            "length": 4,
            "increment": 15663105
          },
          {
            "frame_type": "HEADERS",
            "stream_id": 1,
            "length": 307,
            "headers": [
              ":method: GET",
              ":authority: tls.peet.ws",
              ":scheme: https",
              ":path: /api/all",
              "upgrade-insecure-requests: 1",
              "user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
              "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
              "sec-fetch-site: none",
              "sec-fetch-mode: navigate",
              "accept-encoding: gzip, deflate, br",
              "accept-language: zh-CN,zh;q=0.9,en;q=0.8"
            ],
            "flags": [
              "EndStream (0x1)",
              "EndHeaders (0x4)",
              "Priority (0x20)"
            ],
            "priority": {
              "weight": 256,
              "depends_on": 0,
              "exclusive": 1
            }
          }
        ]
      },
      "tcpip": {
        "cap_length": 66,
        "dst_port": 443,
        "src_port": 52325,
        "ip": {
          "ttl": 47,
          "ip_version": 4,
          "dst_ip": "205.185.123.167",
          "src_ip": "103.85.172.132"
        },
        "tcp": {
          "ack": 1350460121,
          "checksum": 64235,
          "seq": 2255574087,
          "window": 2054
        }
      }
    },
    {
      "ip": "49.157.47.219:25733",
      "http_version": "h2",
      "method": "GET",
      "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
      "tls": {
        "ciphers": [
          "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
          "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
          "TLS_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_RSA_WITH_AES_128_CBC_SHA",
          "TLS_RSA_WITH_AES_256_CBC_SHA"
        ],
        "extensions": [
          {
            "name": "server_name (0)",
            "server_name": "tls.peet.ws"
          },
          {
            "name": "status_request (5)",
            "status_request": {
              "certificate_status_type": "OSCP (1)",
              "responder_id_list_length": 0,
              "request_extensions_length": 0
            }
          },
          {
            "name": "supported_groups (10)",
            "supported_groups": [
              "P-256 (23)",
              "P-384 (24)",
              "P-521 (25)"
            ]
          },
          {
            "name": "ec_point_formats (11)",
            "elliptic_curves_point_formats": [
              "0x00"
            ]
          },
          {
            "name": "signature_algorithms (13)",
            "signature_algorithms": [
              "ecdsa_secp256r1_sha256",
              "ecdsa_secp384r1_sha384",
              "ecdsa_secp521r1_sha512",
              "rsa_pss_rsae_sha256",
              "rsa_pss_rsae_sha384",
              "rsa_pss_rsae_sha512",
              "rsa_pss_pss_sha256",
              "rsa_pss_pss_sha384",
              "rsa_pss_pss_sha512",
              "rsa_pkcs1_sha256",
              "rsa_pkcs1_sha384",
              "rsa_pkcs1_sha512",
              "0x402",
              "0x303",
              "0x301",
              "0x302",
              "ecdsa_sha1",
              "rsa_pkcs1_sha1",
              "0x202"
            ]
          },
          {
            "name": "signature_algorithms_cert (50)",
            "data": "00260403050306030804080508060809080a080b0401050106010402030303010302020302010202"
          },
          {
            "name": "application_layer_protocol_negotiation (16)",
            "protocols": [
              "h2",
              "http/1.1"
            ]
          },
          {
            "name": "status_request_v2 (17)",
            "data": "000702000400000000"
          },
          {
            "name": "extended_master_secret (23)",
            "master_secret_data": "",
            "extended_master_secret_data": ""
          },
          {
            "name": "supported_versions (43)",
            "versions": [
              "TLS 1.2"
            ]
          },
          {
            "name": "extensionRenegotiationInfo (boringssl) (65281)",
            "data": "00"
          }
        ],
        "tls_version_record": "771",
        "tls_version_negotiated": "771",
        "ja3": "771,49195-49199-49196-49200-49171-49172-156-157-47-53,0-5-10-11-13-50-16-17-23-43-65281,23-24-25,0",
        "ja3_hash": "25caec08e73f3efac7cfd90ccb3a3849",
        "ja4": "t12d1011h2_75366a718a82_f1763c68ef9b",
        "peetprint": "771|2-1.1|23-24-25|1027-1283-1539-2052-2053-2054-2057-2058-2059-1025-1281-1537-1026-771-769-770-515-513-514|0||49195-49199-49196-49200-49171-49172-156-157-47-53|0-10-11-13-16-17-23-43-5-50-65281",
        "peetprint_hash": "ec56fe83bccdadd977cab849582adad8",
        "client_random": "4f14a26d7ccebb39583aac4c62c03deb6f34ec96e0d1d18a00029eecf6321b97",
        "session_id": ""
      },
      "http2": {
        "akamai_fingerprint": "1:65536,3:1000,4:6291456,6:262144|15663105|0|m,a,s,p",
        "akamai_fingerprint_hash": "7ad845f20fc17cc8088a0d9312b17da1",
        "sent_frames": [
          {
            "frame_type": "SETTINGS",
            "length": 24,
            "settings": [
              "HEADER_TABLE_SIZE = 65536",
              "MAX_CONCURRENT_STREAMS = 1000",
              "INITIAL_WINDOW_SIZE = 6291456",
              "MAX_HEADER_LIST_SIZE = 262144"
            ]
          },
          {
            "frame_type": "WINDOW_UPDATE",
            "length": 4,
            "increment": 15663105
          },
          {
            "frame_type": "HEADERS",
            "stream_id": 1,
            "length": 436,
            "headers": [
              ":method: GET",
              ":authority: tls.peet.ws",
              ":scheme: https",
              ":path: /api/all",
              "sec-ch-ua: \\\"Google Chrome\\\";v=\\\"105\\\", \\\"Not)A;Brand\\\";v=\\\"8\\\", \\\"Chromium\\\";v=\\\"105\\",
              "sec-ch-ua-mobile: ?0",
              "sec-ch-ua-platform: \\\"Windows\\",
              "upgrade-insecure-requests: 1",
              "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
              "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
              "sec-fetch-site: none",
              "sec-fetch-mode: navigate",
              "sec-fetch-user: ?1",
              "sec-fetch-dest: document",
              "accept-encoding: gzip, deflate, br",
              "accept-language: zh-CN,zh;q=0.9"
            ],
            "flags": [
              "EndStream (0x1)",
              "EndHeaders (0x4)"
            ]
          }
        ]
      },
      "tcpip": {
        "cap_length": 66,
        "dst_port": 443,
        "src_port": 25733,
        "ip": {
          "id": 52408,
          "ttl": 55,
          "ip_version": 4,
          "dst_ip": "205.185.123.167",
          "src_ip": "49.157.47.219"
        },
        "tcp": {
          "ack": 1770676555,
          "checksum": 60742,
          "seq": 2717094645,
          "window": 83
        }
      }
    }
]


server_config = {
    "captcha_port": 18999,
    "server_port": 30200
}


host = {
    "3": "al",
    "5": "ad",
    "10": "am",
    "12": "au",
    "13": "at",
    "14": "az",
    "16": "bh",
    "20": "be",
    "26": "ba",
    "29": "br",
    "32": "bg",
    "37": "ca",
    "42": "cl",
    "45": "co",
    "49": "cr",
    "50": "hr",
    "52": "cy",
    "53": "cz",
    "54": "dk",
    "57": "do",
    "64": "ee",
    "68": "fi",
    "69": "fr",
    "75": "ge",
    "76": "de",
    "79": "gr",
    "83": "gu",
    "90": "hu",
    "91": "is",
    "96": "ie",
    "97": "il",
    "98": "it",
    "100": "jp",
    "101": "jo",
    "102": "kz",
    "105": "kw",
    "108": "lv",
    "109": "lb",
    "113": "lt",
    "114": "lu",
    "116": "mk",
    "119": "my",
    "122": "mt",
    "126": "mu",
    "128": "mx",
    "130": "md",
    "134": "me",
    "135": "ma",
    "141": "nl",
    "144": "nz",
    "151": "no",
    "152": "om",
    "159": "pe",
    "160": "ph",
    "162": "pl",
    "163": "pt",
    "164": "pr",
    "165": "qa",
    "167": "ro",
    "174": "sa",
    "175": "rs",
    "179": "sg",
    "180": "sk",
    "181": "si",
    "184": "za",
    "185": "kr",
    "186": "es",
    "191": "se",
    "192": "ch",
    "194": "tw",
    "197": "th",
    "203": "tr",
    "208": "ua",
    "209": "ae",
    "210": "uk",
    "211": "us",
    "212": "uy",
    "219": "vi",
    "235": "xk",
    "236": "mp"
}
gV = {
    "us": {
        "id": 211,
        "dr": "us",
        "ldp": "us"
    },
    "ca": {
        "id": 37,
        "dr": "us",
        "ldp": "ca"
    },
    "au": {
        "id": 12,
        "dr": "us",
        "ldp": "au"
    },
    "nz": {
        "id": 144,
        "dr": "us",
        "ldp": "nz"
    },
    "uk": {
        "id": 210,
        "dr": "eu"
    },
    "de": {
        "id": 76,
        "dr": "eu"
    },
    "fr": {
        "id": 69,
        "dr": "eu"
    },
    "it": {
        "id": 98,
        "dr": "eu"
    },
    "nl": {
        "id": 141,
        "dr": "eu"
    },
    "es": {
        "id": 186,
        "dr": "eu"
    },
    "mx": {
        "id": 128,
        "dr": "us"
    },
    "at": {
        "id": 13,
        "dr": "eu"
    },
    "be": {
        "id": 20,
        "dr": "eu"
    },
    "pt": {
        "id": 163,
        "dr": "eu"
    },
    "pl": {
        "id": 162,
        "dr": "eu"
    },
    "se": {
        "id": 191,
        "dr": "eu"
    },
    "ch": {
        "id": 192,
        "dr": "eu"
    },
    "ro": {
        "id": 167,
        "dr": "eu"
    },
    "gr": {
        "id": 79,
        "dr": "eu"
    },
    "cz": {
        "id": 53,
        "dr": "eu"
    },
    "hu": {
        "id": 90,
        "dr": "eu"
    },
    "ie": {
        "id": 96,
        "dr": "eu"
    },
    "dk": {
        "id": 54,
        "dr": "eu"
    },
    "fi": {
        "id": 68,
        "dr": "eu"
    },
    "sk": {
        "id": 180,
        "dr": "eu"
    },
    "si": {
        "id": 181,
        "dr": "eu"
    },
    "ee": {
        "id": 64,
        "dr": "eu"
    },
    "lv": {
        "id": 108,
        "dr": "eu"
    },
    "mt": {
        "id": 122,
        "dr": "eu"
    },
    "cy": {
        "id": 52,
        "dr": "eu"
    },
    "bg": {
        "id": 32,
        "dr": "eu"
    },
    "hr": {
        "id": 50,
        "dr": "eu"
    },
    "lt": {
        "id": 113,
        "dr": "eu"
    },
    "lu": {
        "id": 114,
        "dr": "eu"
    },
    "jp": {
        "id": 100,
        "dr": "us",
        "ldp": "jp"
    },
    "kr": {
        "id": 185,
        "dr": "us",
        "ldp": "kr"
    },
    "sa": {
        "id": 174,
        "dr": "eu",
        "ldp": "qa"
    },
    "ae": {
        "id": 209,
        "dr": "eu",
        "ldp": "qa"
    },
    "kw": {
        "id": 105,
        "dr": "eu",
        "ldp": "qa"
    },
    "no": {
        "id": 151,
        "dr": "eu"
    },
    "sg": {
        "id": 179,
        "dr": "us",
        "ldp": "sg"
    },
    "cl": {
        "id": 42,
        "dr": "us",
        "ldp": "br"
    },
    "br": {
        "id": 29,
        "dr": "us",
        "ldp": "br"
    },
    "ph": {
        "id": 160,
        "dr": "us",
        "ldp": "jp"
    },
    "il": {
        "id": 97,
        "dr": "eu"
    },
    "my": {
        "id": 119,
        "dr": "us",
        "ldp": "sg"
    },
    "qa": {
        "id": 165,
        "dr": "eu",
        "ldp": "qa"
    },
    "bh": {
        "id": 16,
        "dr": "eu",
        "ldp": "qa"
    },
    "om": {
        "id": 152,
        "dr": "eu",
        "ldp": "qa"
    },
    "tw": {
        "id": 194,
        "dr": "us",
        "ldp": "jp"
    },
    "th": {
        "id": 197,
        "dr": "us",
        "ldp": "sg"
    },
    "lb": {
        "id": 109,
        "dr": "eu",
        "ldp": "qa"
    },
    "jo": {
        "id": 101,
        "dr": "eu",
        "ldp": "qa"
    },
    "za": {
        "id": 184,
        "dr": "eu",
        "ldp": "za"
    },
    "rs": {
        "id": 175,
        "dr": "eu"
    },
    "md": {
        "id": 130,
        "dr": "eu"
    },
    "me": {
        "id": 134,
        "dr": "eu"
    },
    "is": {
        "id": 91,
        "dr": "eu"
    },
    "ad": {
        "id": 5,
        "dr": "eu"
    },
    "ba": {
        "id": 26,
        "dr": "eu"
    },
    "al": {
        "id": 3,
        "dr": "eu"
    },
    "mk": {
        "id": 116,
        "dr": "eu"
    },
    "xk": {
        "id": 235,
        "dr": "eu"
    },
    "kz": {
        "id": 102,
        "dr": "eu"
    },
    "co": {
        "id": 45,
        "dr": "us"
    },
    "az": {
        "id": 14,
        "dr": "eu"
    },
    "ua": {
        "id": 208,
        "dr": "eu"
    },
    "uy": {
        "id": 212,
        "dr": "us",
        "ldp": "br"
    },
    "mu": {
        "id": 126,
        "dr": "eu",
        "ldp": "za"
    },
    "pe": {
        "id": 159,
        "dr": "us",
        "ldp": "br"
    },
    "ge": {
        "id": 75,
        "dr": "eu"
    },
    "am": {
        "id": 10,
        "dr": "eu"
    },
    "ma": {
        "id": 135,
        "dr": "eu"
    },
    "do": {
        "id": 57,
        "dr": "us"
    },
    "tr": {
        "id": 203,
        "dr": "eu"
    },
    "cr": {
        "id": 49,
        "dr": "us"
    },
    "gu": {
        "id": 83,
        "dr": "us",
        "ldp": "jp"
    },
    "mp": {
        "id": 236,
        "dr": "us",
        "ldp": "jp"
    },
    "pr": {
        "id": 164,
        "dr": "us"
    },
    "vi": {
        "id": 219,
        "dr": "us"
    }
}

def get_gif_url(r):
    h = host[str(r)]
    h = gV.get(h,{}).get("ldp") or gV.get(h,{}).get("dr") or "us"
    return "https://"+h+".thtk.temu.com/c/th.gif"

def get_dr(r):
    h = host[str(r)]

    return gV.get(h,{}).get("dr")


redis_config = {
    "REDIS_HOST": "172.24.16.162",
    "REDIS_PORT": 6379,
    "REDIS_DB": 24,
    "REDIS_PASSWORD": "KNzC8A*md%#7HQTq",
}
cookie_key = "temu_login_cookie"
cookie_len = 30

if __name__ == '__main__':

    print(get_dr(210))
    print(get_gif_url(210))