cURL - Command Line Download and Transfer Powerhouse
This README file provides a comprehensive guide to using cURL, a powerful command-line tool for transferring data over various protocols, including HTTP. It also covers the fundamentals of URLs and HTTP requests/responses to empower your cURL usage.

cURL Options
| Option | Description |
| --- | --- |
| `-A, --user-agent <agent string>` | Set the User-Agent string to send to the HTTP server²[1] |
| `-b, --cookie <name=data>` | Send cookies from string/file²[1] |
| `-c, --cookie-jar <filename>` | Write cookies to <filename> after operation²[1] |
| `-d, --data <data>` | Send specified data in POST request²[1] |
| `-e, --referer <URL>` | Referer URL (where the user came from)²[1] |
| `-F, --form <name=content>` | Specify HTTP multipart POST data²[1] |
| `-G, --get` | Send the -d data with a HTTP GET²[1] |
| `-H, --header <header/@file>` | Pass custom header(s) to server²[1] |
| `-i, --include` | Include protocol response headers in the output²[1] |
| `-k, --insecure` | Allow connections to SSL sites without certs²[1] |
| `-L, --location` | Follow redirects²[1] |
| `-O, --remote-name` | Write output to a file named as the remote file²[1] |
| `-P, --proxytunnel` | Operate through a HTTP proxy tunnel²[1] |
| `-q` | If used as the first parameter disables .curlrc²[1] |
| `-R, --remote-time` | Set the remote file's time on the local output²[1] |
| `-s, --silent` | Silent mode. Don't output anything²[1] |
| `-T, --upload-file <file>` | Transfer local <file> to remote site²[1] |
| `-u, --user <user:password>` | Server user and password²[1] |
| `-v, --verbose` | Make the operation more talkative²[1] |
| `-x, --proxy [protocol://]<host[:port]>` | Use proxy on given port²[1] |
| `-z, --time-cond <date expression>` | Transfer based on time condition²[1] |

Understanding the Web: URLs and HTTP
URL (Uniform Resource Locator): A unique address that specifies the location of a resource on the internet. It follows a specific format.

How to Read a URL:
<scheme>://<host>[:<port>]<path>[?<query_string>][#<fragment>]

Scheme: The protocol used to access the resource (e.g., http, https, ftp).
Host: The domain name or IP address of the server hosting the resource.
Port: (Optional) A specific port number used by the service (usually port 80 for HTTP).
Path: The location of the resource on the server (e.g., /directory/file.html).
Query String: (Optional) Parameters appended to the URL for specific data requests (e.g., ?search_query=cats).
Fragment: (Optional) An anchor tag within the document to jump to a specific section (e.g., #introduction).

Domain Name: A human-readable address that translates to an IP address (e.g., wikipedia.org).
Subdomain: A subdivision within a domain (e.g., www is a subdomain of wikipedia.org).
Ports: Port numbers specify communication channels on a server (default port 80 for HTTP).

Query Strings: Used to pass data to a web page (e.g., search queries or filters).

cURL in Action
HTTP Request: A message sent by a client (your browser) to a server requesting a resource (webpage, file).
HTTP Response: The server's response to the request, containing the requested data (webpage content) and status information (success codes, error codes).
HTTP Headers: Lines of information included in both requests and responses that provide details about the communication (content type, authentication, etc.).
HTTP Message Body: The main content of the request or response (e.g., HTML code of a webpage).
HTTP Request Method: Specifies the action desired (GET to retrieve data, POST to submit data).
HTTP Response Status Code: A numerical code indicating the success or error of the request (e.g., 200 for success, 404 for not found).
HTTP Cookie: A small piece of data stored by a website on your browser to remember information (e.g., login state, preferences).
Making a cURL Request:

Bash
curl https://www.example.com

content_copy
This retrieves the webpage from "https://www.example.com". Explore the curl --help or curl -h command for more options.

Example: Downloading a File:

Bash
curl https://example.com/file.txt -o filename.txt
content_copy
This downloads the file "file.txt" and saves it locally as "filename.txt".

Behind the Scenes: Typing "google.com" in Your Browser
DNS Lookup: Your browser translates the domain name "google.com" into a numerical IP address using the Domain Name System (DNS).
HTTP Request: Your browser sends an HTTP GET request to the IP address of google.com.
Server Response: The Google server processes the request and sends an HTTP response containing the Google homepage content.
Rendering: Your browser interprets the HTML code and displays the Google homepage on your screen.
This is a simplified explanation, but it highlights how cURL interacts with the underlying HTTP protocol for data transfer.

Additional Resources:
cURL Manual: https://curl.se/docs/tutorial.html
cURL Options Summary: https://github.com/Traurige/Eneko/releases