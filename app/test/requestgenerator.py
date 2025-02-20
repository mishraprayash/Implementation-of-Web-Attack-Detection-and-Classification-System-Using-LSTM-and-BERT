import random

HOSTS = [
    "example.com",
    "api.sampleapi.net",
    "accounts.google.com",
    "www.facebook.com",
    "cdn.vmhost.com",
    "media.netflix.com",
    "auth.microsoft.com",
]

AUTH_HEADERS = [
    "", 
    "eysdoishdicu.sdkcbiusdc.sdcjkh_jknskdc",  # Common bearer token
    "",
    "ekskd.sdcsdc.sd_zxy0987654321",  # Another bearer token
    "eueue.wdcihnsd.sdcsdc_dX_NlcjpwYXNzd29yZA",  # Base64-encoded user:password
    "c3VwZXI6c2VjcmV0MTIz.oshdcksd234234.sdjhbsjhdc",  # Another Base64-encoded user:password
    "abc123xyz456.sdkchu",  # Custom token pattern
    "",
    "eyeewfwcbu.sdjbsdc.ajdhbcd_zjhb",  # Example API key
]


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",  # Chrome Windows
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",  # Chrome macOS
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Mobile/15E148 Safari/604.1",  # Safari iOS
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",  # Chrome Android

    # "PostmanRuntime/7.29.2",  # Postman user agent
    # "curl/7.85.0",  # cURL tool
    # "python-requests/2.28.1",  # Python Requests library
]

COOKIES = [
    "sessionid=abc123; path=hello;",
    "auth_token=xyz789; path=api;",
    "",
    "csrftoken=abcdef123456;",
    "cart_id=12345; path=shop;",
    "",
    "lang=en-US; path=hey;",
    "tracking_id=track98765; domain=example.com;",
    "login_state=logged_in; path=test;",
    ""
]

REFERERS = [
    "https://google.com/",
    "https://facebook.com/",
    "https://example.com/",
    "https://www.linkedin.com/in/johndoe/",
    "https://shop.amazon.com/",
    "https://docs.python.org/3/",
    "https://blog.medium.com/",
]

BODY_EXAMPLES = [
    "",  # No body (for GET requests)
    '{"username": "johndoe", "password": "securepass"}',  # JSON body for login
    '{"key1": "value1", "key2": "value2"}',  # Generic JSON payload
    "",
    '{"email": "user@example.com", "opt_in": true}',  # JSON for form submission
    "",
    '{"items": [{"id": 1, "qty": 2}, {"id": 2, "qty": 1}]}',  # Complex JSON (cart)
    "",
]

URI = [
    "api/v2/login",
    "api/v1/register" "/api/posts/",
    "/api/posts/1",
    "/api/posts/2/comments",
    "/api/users",
    "/api/users/1",
    "/api/users/1/followers",
    "/analytics",
    "/support/ticket",
    "/support/ticket/123/reply",
    "/",
]


HOSTS_MAL = [
    "select.com",  # Normal-looking host
    "testsite.org",  # Normal-looking host
    "vulnerable.com'; DROP TABLE users; --",  # SQLi in subdomain
    "sampleapi.net' OR '1'='1",  # SQLi attempting conditional always-true
    "malicious-site.com'; SELECT * FROM admin; --",  # SQLi injecting admin query
    "google.com'; DROP DATABASE testdb; --",  # SQLi database drop
    "facebook.com'; UNION SELECT NULL, NULL, version(); --",  # Union-based SQLi
]

AUTH_HEADERS_MAL = [
    "",
    "' OR '1'='1",  # Always-true condition
    " abcdef'; DROP TABLE tokens; --",  # SQLi in bearer token
    " dXNlcjpwYXNz.sdjc.sdcsd'; DELETE FROM users; --",  # Encoded SQLi
    "",
    " abcdef.akjasjksd.sahjdj'; SELECT * FROM admin_users; --",  # Injected SELECT statement
    " xyz.ab.ascsdc' UNION SELECT username, password FROM users; --",  # Union injection
    " '; SHUTDOWN --",  # Attempt to shut down DB
    "",
    " ksjbckdc.sdvsdvcs.sdcsdc' OR EXISTS(SELECT * FROM users WHERE username='admin') --",  # Subquery injection
]


USER_AGENTS_MAL = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",  # Normal User-Agent
    "Mozilla/5.0 (Windows NT 10.0)'; DROP TABLE logs; --",  # SQLi in User-Agent
    "' UNION SELECT NULL, NULL, version(); --",  # Union injection
    "Mozilla/5.0 (Linux; Android 13)'; DELETE FROM sessions; --",  # SQLi in mobile user-agent
    "curl/7.85.0'; INSERT INTO logs (data) VALUES ('hacked'); --",  # SQLi with curl
    "python-requests/2.28'; UPDATE users SET role='admin' WHERE username='guest'; --",  # SQLi in Python Requests
    "'; EXEC xp_cmdshell('whoami'); --",  # Attempt to execute shell command
]

COOKIES_MAL = [
    "sessionid=abc123'; DROP TABLE sessions; --",  # SQLi dropping table
    "",
    "auth_token=xyz789'; UNION SELECT username, password FROM admin; --",  # Union injection
    "csrftoken=' OR '1'='1",  # Always-true condition
    "cart_id=1'; DELETE FROM carts WHERE user_id=1; --",  # SQLi deleting cart
    "",
    "lang='; UPDATE settings SET value='hacked' WHERE key='theme'; --",  # SQLi updating settings
    "tracking_id=' UNION SELECT NULL, version(); --",  # Extracting DB version
    "",
    "login_state='; INSERT INTO admins (username, password) VALUES ('attacker', '12345'); --",  # SQLi inserting admin
]

REFERERS_MAL = [
    "https://select.com",  # Normal referer
    "https://example.com'; DROP DATABASE logs; --",  # SQLi dropping database
    "' UNION SELECT NULL, NULL FROM users; --",  # Union injection
    "https://malicious-site.com'; DELETE FROM posts WHERE id=1; --",  # SQLi deleting posts
    "'; INSERT INTO visits (ip) VALUES ('127.0.0.1'); --",  # SQLi inserting data
    "' OR EXISTS(SELECT * FROM admin_users); --",  # Subquery injection
    "'; EXEC sp_start_job 'malware_job'; --",  # Attempting stored procedure execution
]

BODY_EXAMPLES_MAL = [
    "' OR '1'='1",  # Always-true SQLi payload
    "",
    "'; DROP TABLE users; --",  # Dropping a table
    "' UNION SELECT username, password FROM admin_users; --",
    "",  # Extracting admin credentials
    "id=1' UNION SELECT NULL, version(); --",  # Extracting DB version
    "",
    "search=') OR ('1'='1",  # SQLi in search parameter
    "'; UPDATE users SET password='hacked' WHERE username='admin'; --",  # Updating sensitive data
    "'; EXEC xp_cmdshell('dir'); --",  # Executing shell command
    ""
]

URI_MAL = [
    "/api/v2/login?username=admin'--",  # SQLi in query parameter
    "/api/users?id=1' OR '1'='1",  # Always-true condition
    "/auth/login?user=admin' UNION SELECT username, password FROM users; --",  # Union-based SQLi
    "/products?id=1'; DROP TABLE products; --",  # Dropping a table
    "/cart/add?item='; DELETE FROM carts; --",  # SQLi deleting carts
    "/checkout?price=' UNION SELECT version(); --",  # Extracting version
    "/search?q=' OR EXISTS(SELECT * FROM information_schema.tables); --",  # Subquery injection
]

# Generate a normal request format for the model
def generate_request_normal():
    normal_request = {
        "agent": random.choice(USER_AGENTS),
        "auth": random.choice(AUTH_HEADERS),
        "body": random.choice(BODY_EXAMPLES),
        "cookie": random.choice(COOKIES),
        "host": random.choice(HOSTS),
        "referer": random.choice(REFERERS),
        "uri": random.choice(URI),
    }
    return normal_request



# Generate a malicious request format for the model
def generate_request_malicious():
    malicious_request = {
        "host": random.choice(HOSTS_MAL),
        "uri": random.choice(URI_MAL),
        "auth": random.choice(AUTH_HEADERS_MAL),
        "agent": random.choice(USER_AGENTS_MAL),
        "cookie": random.choice(COOKIES_MAL),
        "referer": random.choice(REFERERS_MAL),
        "body": random.choice(BODY_EXAMPLES_MAL),
    }
    malicious_request_sql = {
         "host": random.choice(HOSTS),
        "uri": random.choice(URI_MAL),
        "auth": random.choice(AUTH_HEADERS),
        "agent": random.choice(USER_AGENTS),
        "cookie": random.choice(COOKIES),
        "referer": random.choice(REFERERS),
        "body": random.choice(BODY_EXAMPLES),
    }
    return malicious_request_sql


