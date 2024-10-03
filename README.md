# DigitalOcean Serverless Functions Example
## MaxMind GeoLite2 geoip (ip2geo) database
This repository contains an example API designed 
as a cloud function to run on DigitalOcean 
Serverless Functions. 

This ip2geo API retrieves a geolocation information 
by IP address of the client and responds with JSON 
that contains the country code, the flag that tells 
if it is within EU or not, the continent where the country 
located and the ASN number that the IP address belong to.

DigitalOcean Team does great at writing documentation 
for developers, yet from time to time their writings
lack of more advanced usage examples of Functions.
This repository tries to fix this.

# Deploy to DigitalOcean Functions
```doctl sls deploy --remote-build functions```

# Invoke/Demo
```doctl serverless functions invoke example/geoIp --web```

# Features
This example features the following topics:
- `build.sh` for building a virtual environment 
and installing dependencies of the function during deployment;
- `curl` for downloading the required files during 
the deployment;
- event parameters of cloud functions for obtaining
the request data;
- GeoLite2 Country and GeoLite2 ASN databases 
accessed using the official `geoip2` library.

# Notice about limitations
While the cloud function works seamlessly with 
GeoLite2 database, it may not work with full GeoIP2 database
due to its size: the DigitalOcean Functions, as well as other cloud providers, 
has limits on the deployed bundle size.

# More examples
Remember to check out the official DigitalOcean repo: 
https://github.com/digitalocean/sample-functions-python-helloworld
