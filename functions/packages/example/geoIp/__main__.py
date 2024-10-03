from http import HTTPStatus

import geoip2.database


UNKNOWN_CONTINENT = 'U'
UNKNOWN_COUNTRY = 'U'
UNKNOWN_ASN = -1

COUNTRY_MMDB = 'GeoLite2-Country.mmdb'
ASN_MMDB = 'GeoLite2-ASN.mmdb'


def main(args):
    try:  # Get the IP address of the client from proxy headers
        ip_addr = args['http'] \
                      ['headers']['x-forwarded-for']
    except KeyError:
        ip_addr = args.get("ip", None)
        
    if ip_addr is None:
        return { "statusCode": HTTPStatus.BAD_REQUEST }
    
    country_reader = geoip2.database.Reader(COUNTRY_MMDB)
    asn_reader = geoip2.database.Reader(ASN_MMDB)
    
    asn = -1
    continent = UNKNOWN_CONTINENT
    country = UNKNOWN_COUNTRY
    
    try:
        asn = asn_reader \
              .asn(ip_addr) \
                  .autonomous_system_number
    except Exception:
        pass
    
    try:
        c = country_reader.country(ip_addr)
        continent = c.continent.code
        country = c.country.iso_code
        is_eu = c.country.is_in_european_union
    except Exception:
        pass    
    
    return {
        "headers": { 
            "Content-Type": "application/json"
        },
        
        "statusCode": HTTPStatus.OK,
        
        "body": {
            "ip": ip_addr,
            "asn": asn,
            "continent": continent,
            "country": country,
            "is_eu": is_eu
        }
    } 