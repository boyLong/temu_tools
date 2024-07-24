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
    },
{
  "ip": "50.7.158.106:21744",
  "http_version": "h2",
  "method": "GET",
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
  "tls": {
    "ciphers": [
      "TLS_GREASE (0x5A5A)",
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
        "name": "extensionEncryptedClientHello (boringssl) (65037)",
        "data": "0000010001740020961cf581ffad38c42583284a56a1b408840b435998a96d4f4ec0dc97fad7ef0900f0c9ddf63ee95ecc7ff96fb326893bbd2f52ffbde4afad5d48fe0ec231c91962a1bc543f9a1468bc6f0e2aeadd2ed481a034b8a1b7fb67fdfb71803d7824bd4f0a9e079567c954536592961e561f5c878ddf6d07b7811480fd03fe4c57a6c999401e64ac61b561bf17049fe22aad499b9d3652681957cae86f02cc1792b33c0c29d4aac3470d2bd968446c141d589fd334d5cf7b18fdf6f093d089768a15c8499ce6239b22ba64345f5cd3c5ceb8f422da048f755abca8c7931cfb2cad1a88d181bb24aa1a9d8dd802c406b23c2f642198b713d0d5b3ccf64efa3048fc85aa69a4c8e2c5bf0a14a99d77aeebafd41067c5"
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
        "name": "server_name (0)",
        "server_name": "tls.peet.ws"
      },
      {
        "name": "application_layer_protocol_negotiation (16)",
        "protocols": [
          "h2",
          "http/1.1"
        ]
      },
      {
        "name": "session_ticket (35)",
        "data": ""
      },
      {
        "name": "signed_certificate_timestamp (18)"
      },
      {
        "name": "ec_point_formats (11)",
        "elliptic_curves_point_formats": [
          "0x00"
        ]
      },
      {
        "name": "extensionRenegotiationInfo (boringssl) (65281)",
        "data": "00"
      },
      {
        "name": "supported_versions (43)",
        "versions": [
          "TLS_GREASE (0x0a0a)",
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
        "name": "key_share (51)",
        "shared_keys": [
          {
            "TLS_GREASE (0x3a3a)": "00"
          },
          {
            "X25519Kyber768 (25497)": "8e5a0355f34e0c5388a42c17c0c3bea8352b239e38f0202f2ad2f0470ff81438b3d360731400ef048631e4a4417290130229fa0069917c440459862948a177560e34e6c139785d09909d397699494840bab24635f44ab5bc8dea38acaf41044e663dd6097b0f553197cb4b9566051aba2760b8674e369679c41c7289995746a2ac87b3f2539cf6f98b66655b6fe86feae6a486813e4b2c7fbda769270327c5e8be1148855f35983c7c32ab551837657827a103f1120e0a5c51b8e70f5bf2242c4b385134752f37a65ec49d76eb2c77b742de4720bbc9cdd0861885aa2cbcd832b8d82b682ab32eb188dc2c4eef82293d578178d657145831a49a1b88191ad631a3af2ab8e40734dfa86e590587c9000448d2aca4889a281258fbd4712c9368dc968c97b4a362575daec0c18a4a81da005c0bbc8a9313087e202a78364466324675054602d45e71058ab3d35e192270e82016c8eb1babc37dca399f011b4ecb9c044ea33f2ac153eda482bff96e8469cbfb48c7270683425063548a8987939f472c7994c0c2b9954da6e30928f8049b3a474fa092c443a932b6048207373ef21ea3085851a686290abddbb67ec0500f7958698cc5131a645fb4e92178486f35151cf3735ee4aa34b530375bf98cf131694f1884b7fc08c4e3a163686221fb994d86112758a0188b97030cb597d205ea5c25e43408b0f86076614661b08ad5d8c4237220c4e458fedb64dbf3c8f4eb233fdc051358319f769397b46834ba2bf829ac065c40ffa9a9f919b822364d5d67837d1149eeb3c8bf226502576355d372afcc7598c07d3d1742285490a39728a60a9aaf28bb9c2831f9d37f3a121665bb023767b9d7fb5dc947477b7773ffd99bbf01a5e07368ad397976385a6fa64519e88c887365ac4c76c9310b7f86b0b67c62d57c13c186105205a7aa93b9e256cd31731aa1656065874409051a603201554731b45814373bb32a327d95b2c97ae9606321251c3717c34bc19ef8356cac7fc88409f82162abeac280c76b677236220c5d5ee0000a8726d8557e2ce0525470bed7699ea193ab8e9c846f285563ca141f27c2c1643bb174b5ce118f5d2c5e2d860ea2086b9be717790a1e801b7290b4b32986bb2e754f1eca142b5692c419860c233bcd64b8e464b1e4464480d228ac0285bc334d0fb46967407d10ab0c05c6687e4b5a715088ab411406a2054ea441752c320568c354e79976939c438c89db5acec6811b4750474c5a76df8a4fef1bab06cb027d2371cf6b2e8519b01128410687af96b80b1b17afcf7139d2b4215f993c09440ae275bb290533303b0cc1ac18bacc3b0c78083cc938fa52c72ccb4feaa76eba4c4642351f8708ae80c295b1894880f1bddd43226aa985c9002d251002ac34b0a19c595ae89623585a7dd0cb29ab2b0b01a120eaca817199c9886460ac419a2a25abfbba3f28be241a0f0fb5a2907060a07a1f6cc062df4b890445c6c8631fae73c6409bc0174b03131a5050e6c786546ef27b368c21067fa5c49a038c2af5cd173a53c8d0a305d5ce9f2b2527d4a08110119963a87d80059d011b74019d91827916dabc67484a7b19a2bb13a12d133cca03bc5a911c7c348123ecb574280a51045418267b13619983d8863c532ccaf1bad02c6a169765865bb18cd409aeb1fe8810fb8ed05345e32c6c7ac5f47320b692835a65b49744a18b6ac56dac"
          },
          {
            "X25519 (29)": "ee6e86b9c0e9e2c53c27154ac1e4a4427469c6948793fc34a05cbc97f3e87935"
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
        "name": "supported_groups (10)",
        "supported_groups": [
          "TLS_GREASE (0x3a3a)",
          "X25519Kyber768 (25497)",
          "X25519 (29)",
          "P-256 (23)",
          "P-384 (24)"
        ]
      },
      {
        "name": "TLS_GREASE (0x8a8a)"
      },
      {
        "name": "pre_shared_key (41)",
        "data": "007700718fe86d6c4cff6db29d81b04940ff62a7fffa7f27bb867bcbc734399dcdd866ee9f93d9673714b825cde556dbf6d608ecbc55489de5c875289bb4232a4fcff9e765636510b52fdcd2b551b7988344fd3f1821f2284c00b88059e21757b129e4db191fe43e967b228ccff46edbf0b60f481a7bf7a07e0021202adeadaa5a397d0ce5877b1a8c34ca0d3e9e0d343fc46e89a23c096efe80df74"
      }
    ],
    "tls_version_record": "771",
    "tls_version_negotiated": "772",
    "ja3": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,65037-13-0-16-35-18-11-65281-43-45-27-23-17513-51-5-10-41,25497-29-23-24,0",
    "ja3_hash": "14f8f99f41473b73267dfc9a6c3e250c",
    "ja4": "t13d1517h2_8daaf6152771_abb8c90afe16",
    "peetprint": "GREASE-772-771|2-1.1|GREASE-25497-29-23-24|1027-2052-1025-1283-2053-1281-2054-1537|1|2|GREASE-4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53|0-10-11-13-16-17513-18-23-27-35-41-43-45-5-51-65037-65281-GREASE-GREASE",
    "peetprint_hash": "9cb72b909981b498e833d0f5e5929c70",
    "client_random": "1c6f20fca6f490445c6ca9ae9fe38c5c104d786ceaa6f546ff7248714d19fc9e",
    "session_id": "3801fa38034875ffc53af51b7b35692a3c02fd8cec5a9b680343fdd6a32f4c1e"
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
        "length": 459,
        "headers": [
          ":method: GET",
          ":authority: tls.peet.ws",
          ":scheme: https",
          ":path: /api/all",
          "sec-ch-ua: \\\"Not/A)Brand\\\";v=\\\"8\\\", \\\"Chromium\\\";v=\\\"126\\\", \\\"Google Chrome\\\";v=\\\"126\\",
          "sec-ch-ua-mobile: ?0",
          "sec-ch-ua-platform: \\\"Windows\\",
          "upgrade-insecure-requests: 1",
          "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
          "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
          "sec-fetch-site: none",
          "sec-fetch-mode: navigate",
          "sec-fetch-user: ?1",
          "sec-fetch-dest: document",
          "accept-encoding: gzip, deflate, br, zstd",
          "accept-language: zh-CN,zh;q=0.9",
          "priority: u=0, i"
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
    "cap_length": 54,
    "dst_port": 443,
    "src_port": 21744,
    "ip": {
      "id": 1807,
      "ttl": 57,
      "ip_version": 4,
      "dst_ip": "205.185.123.167",
      "src_ip": "50.7.158.106"
    },
    "tcp": {
      "ack": 10376462,
      "checksum": 60121,
      "seq": 2857718670,
      "window": 237
    }
  }
}

]

ja3_configs1 = [
{
  "ip": "120.244.234.63:14426",
  "http_version": "h2",
  "method": "GET",
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
  "tls": {
    "ciphers": [
      "TLS_GREASE (0x4A4A)",
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
        "name": "TLS_GREASE (0xbaba)"
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
        "name": "extensionEncryptedClientHello (boringssl) (65037)",
        "data": "00000100017e00200b2e436c984c7aac3ef7c4412726d8cc9e1c4e1ba710c256156f15692efa887a00d02bd9aaf8dfa899ba2c84fbc857b58d1a3b048a767743902b0dc95cc5f6af9ba70d6b8956b8ae196fa97a7a57213c278d06d05a5baf1592686e1053a32c4ea3a21a58c8aa6080e968fbd3f3df002067631096c23f095b081ed4453399bf4384b62c0ca3c052ad3c67db3aa6ff4492aa81398fee678d6954e87f48b47fbf4040609167c0408a8e9fae31141b218eded2819e90b169363bd2ba36eca35c2fb1112cb28a28de4aa7fb5b5232eb39ce79886a38d17769c9adcea82ad9589a50cedefd40188e0c8d116f06938887f06fe8799c"
      },
      {
        "name": "application_settings (17513)",
        "protocols": [
          "h2"
        ]
      },
      {
        "name": "extended_master_secret (23)",
        "master_secret_data": "",
        "extended_master_secret_data": ""
      },
      {
        "name": "supported_groups (10)",
        "supported_groups": [
          "TLS_GREASE (0x5a5a)",
          "X25519Kyber768 (25497)",
          "X25519 (29)",
          "P-256 (23)",
          "P-384 (24)"
        ]
      },
      {
        "name": "key_share (51)",
        "shared_keys": [
          {
            "TLS_GREASE (0x5a5a)": "00"
          },
          {
            "X25519Kyber768 (25497)": "a6ef8073c7a42f5c53a26560aa60745a42d7ea74a4b152c74eaf4b7a89f33b31cbf48ce14b00fad88de796946c460c80453b916376c0c100b3047d6ff1914cd8553040ba416188e0d5a727fcbe6c835ae5e69a807526f9db81fe849eb2279e554595d54aa1771671add4bd3a34b296e21a1b4b50e5a018a3b5bcd8752fda2c8c480277663c80bd736a76d267a7da404971563eb2ac0d7bc1262637d47c7dbcf74f4b1b6019b3406a5c679de250db017a26fbb0a336c59fab127e79a1909bca57016815e90fa99c7327e0cfce475607b90cd4bc6512153e56d699c6c519562cca29468e4aa939e0a107c1a91299a1066b36ce1cb67b9a324cb6d06ec1eba45bf0503abba48713076f16947d3153e67cbb315750b881270b49b817e06ae6162bedf62b7d865315f016eb4761a0a6a4a823c8cce013cfc71e2441a8ea94c095e7bc94072668183d8f6b9bcd7a670978209a1347a6e4ac8dfa49f5c5af12a1156a393875f7a5a2982462ec5c944a3d184424ee87bcbdb9c260255381688a046881568c75d3876baca76cb95312e8e538e99b529f563233e11cad84976fca4f178c3c50312d270643551b64e1c6caec042594aa24db356700c827122552752b5f09c25eb2dc1a4d347890b210289660f5544cdb3692f8890c7fa575845649ed428c5d450a4b5138d9124d4108b6eeda916ca802b36213b339b915b2c8c606c8a05427c1ac2a364022eb8bb6e9900086d137aabb718ce87eeee192e13807ed7938526460837c5b5950492b598120f3c0045435ffa7073b952e87fb6c3d28beae04097ec583691a6e7d606167ca4b55e5b033c85ddf203a5bba69e06314a13762f5745f0e80ba6bdc4ed36634c486a6a3d34864ab25c86a11885bca57fa74e9569024d586c4a1584b91bce3c360cbfb0ef3c6883bc110eadc3f333284f0792d8f8787bd259295b2233292138fe32a69b2ca95aa60825537435ac44a98abb745c933b8b6e3ab5fbbf2152372513c842ed7c0bbade815088c56f0ea046738cc83610e9110749ed90368c6b271f69515779a8d6b9fb5d1940767b0814b140c2254e41481fdc633b5457658c13e4b7192182b4f49252da1899766b74bd29586914b24627c8636c7183496b0d9841b8bf859b6e38e7f910ac78c1600293af5f071993aab74771f39c0a5eabaaee2073c4686078fb64d55554cbad35262319ae5029c533191477930ac687340165839e10fe75a5990271e30027f25f735a40a4eaee6c9590c7d6510a686b53283c9b1c29c5e292396262c5eff445ba7396710413ed6f0b3ca378786d550f1d589cea7793e2437ee2c81212a50548b6d607c97f50930b9128df66aa9fe33658ff85c411740d9f90417ba37df2596de67b87bbb542bb2415cc4a730b0b8a26798d3d42aa3fa785477620e1cca9124395a410304ec26182122428403092b19a1b1283b44cf30cbad78e2588e8c8d97612cfc5936bf2495b3893765441c88897cd75b16f8f9b679bcaefc86a93e5b4b6f2806dc2640666b99cdf3a57edbb78974ab7cc42d170cba53f005a699bed9989b62e465ced3c0b814b06560036444600732267b995c8df426a4e14740348a8c15bfe2f68ff5201b0bbb6fefa4bdbc0c8284c867f6d2288e037f459c1d7e38753712589ae7345bcb8e7e0644a80f6a446d6607ff5c8720969ac2ee17bd18eb3bda77605d018a4ca9b9fad255"
          },
          {
            "X25519 (29)": "89e503ccc8353c7d642288a3de53acc519736c6ae17113233969394b1378e67e"
          }
        ]
      },
      {
        "name": "server_name (0)",
        "server_name": "tls.peet.ws"
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
        "name": "psk_key_exchange_modes (45)",
        "PSK_Key_Exchange_Mode": "PSK with (EC)DHE key establishment (psk_dhe_ke) (1)"
      },
      {
        "name": "extensionRenegotiationInfo (boringssl) (65281)",
        "data": "00"
      },
      {
        "name": "signed_certificate_timestamp (18)"
      },
      {
        "name": "application_layer_protocol_negotiation (16)",
        "protocols": [
          "h2",
          "http/1.1"
        ]
      },
      {
        "name": "supported_versions (43)",
        "versions": [
          "TLS_GREASE (0xbaba)",
          "TLS 1.3",
          "TLS 1.2"
        ]
      },
      {
        "name": "TLS_GREASE (0x4a4a)"
      },
      {
        "name": "pre_shared_key (41)",
        "data": "00770071ff8430609d903585b095f068fc90283f2746f2a61ffaefec7a8ce71774e20705d7c5ca1ebc5ae71f6007a41ed8c589ba7871309fae4cb1ff9b881a03a345622315e4abb74abd2e40afdfdebef75232247c6d5fdb687710d2a619c5ffc7a22e517d25b85d12cf97b42f264bfc0b8f824fc62f542a390021205270a1dbff9bc7ae7acd4d11ab4557c186691127996e4eeea66fe250fcfd29c0"
      }
    ],
    "tls_version_record": "771",
    "tls_version_negotiated": "772",
    "ja3": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,5-11-35-65037-17513-23-10-51-0-13-27-45-65281-18-16-43-41,25497-29-23-24,0",
    "ja3_hash": "d7d2b85786ae345e1b834726895c54f4",
    "ja4": "t13d1517h2_8daaf6152771_abb8c90afe16",
    "peetprint": "GREASE-772-771|2-1.1|GREASE-25497-29-23-24|1027-2052-1025-1283-2053-1281-2054-1537|1|2|GREASE-4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53|0-10-11-13-16-17513-18-23-27-35-41-43-45-5-51-65037-65281-GREASE-GREASE",
    "peetprint_hash": "9cb72b909981b498e833d0f5e5929c70",
    "client_random": "0896631dd89ed2e1236ecc8518dc494bba648f10334444830b4e4abc80dc7c1d",
    "session_id": "b68938d7657a8a66baba561e0c351e45e1989d016c09ba7eed4997fd5821ce83"
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
        "length": 468,
        "headers": [
          ":method: GET",
          ":authority: tls.peet.ws",
          ":scheme: https",
          ":path: /api/all",
          "cache-control: max-age=0",
          "sec-ch-ua: \\\"Not/A)Brand\\\";v=\\\"8\\\", \\\"Chromium\\\";v=\\\"126\\\", \\\"Google Chrome\\\";v=\\\"126\\",
          "sec-ch-ua-mobile: ?0",
          "sec-ch-ua-platform: \\\"Windows\\",
          "upgrade-insecure-requests: 1",
          "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
          "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
          "sec-fetch-site: none",
          "sec-fetch-mode: navigate",
          "sec-fetch-user: ?1",
          "sec-fetch-dest: document",
          "accept-encoding: gzip, deflate, br, zstd",
          "accept-language: zh-CN,zh;q=0.9",
          "priority: u=0, i"
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
    "cap_length": 599,
    "dst_port": 443,
    "src_port": 14426,
    "ip": {
      "id": 34593,
      "ttl": 109,
      "ip_version": 4,
      "dst_ip": "205.185.123.167",
      "src_ip": "120.244.234.63"
    },
    "tcp": {
      "ack": 3604194335,
      "checksum": 38367,
      "seq": 2182159194,
      "window": 1028
    }
  }
}
]

server_config = {
    "captcha_port": 30100,
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

def get_api_url(r):
    h = host[str(r)]
    h = gV.get(h,{}).get("ldp") or gV.get(h,{}).get("dr") or "us"
    return "https://"+h+".pftk.temu.com/pmm/api/pmm/api"
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

import os
token = os.environ.get("TEMU_API_TOKEN", '0ff2c7333576e51ba850f1792c8ad7d5')

api_host = os.environ.get("TEMU_API_HOST", '127.0.0.1:30100')

if_ja3 = False
if __name__ == '__main__':

    print(get_dr(210))
    print(get_api_url(211))