# Introduction

These extended metadata keywords are prefixed by `x­-ads-`­ to make a distinction with standard JSON Schema keywords.

# Definitions

## Key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY",
and "OPTIONAL" in this document are to be interpreted as described in BCP 14
([https://tools.ietf.org/html/bcp14](https://tools.ietf.org/html/bcp14)) RFC2119 ([https://tools.ietf.org/html/rfc2119](https://tools.ietf.org/html/rfc2119))
RFC8174 ([https://tools.ietf.org/html/rfc8174](https://tools.ietf.org/html/rfc8174)) when, and only when, they appear
in all capitals, as shown here.

# Specification

### x-ads-accept

OPTIONAL keywords that MAY be specified when a parameter is declared as URI
(using metadata keywords format with uri ([http://json-schema.org/latest/json-schema-validation.html#rfc.section.8.3.6](http://json-schema.org/latest/json-schema-validation.html#rfc.section.8.3.6))) value.
It provide technical information about the model of the data expected in response to the given URI.
The value SHOULD be a valid media type.

Example for a parameter named "primary" typed "URI" that SHOULD return a GeoJson response:

```json
{
    "primary": {
        "label": "primary",
        "type": "string",
        "format": "uri",
        "x­ads­accept": "application/vnd.geo+json"
    }
}
```

### x-ads-constraint

If present, SHOULD be an object composed of 1 or several attribute(s) as
key/value pair(s) that provides inherent information about the parameter. In
order to interpret correctly the x­ads­constraint object, the member naming is
normalized as much as possible.

For instance, input data representing resource in relation with Earth Observation
can have a x­ads­constraint object whose attribute naming meets the
requirements of the OpenSearch Extension for Earth Observation
([https://portal.opengeospatial.org/files/?artifact_id=59981](https://portal.opengeospatial.org/files/?artifact_id=59981)) proposed by Open
Geospatial Consortium (O.G.C).

Example of a parameter named "ortho" with a "platform" and
"processingLevel" constraint attributes, whose naming stays within the
OpenSearch Extension for Earth Observation standard.

```json
"ortho": {
        "type": "string",
        "format": "uri",
        "x­ads­accept": "application/vnd.geo+json",
        "x­ads­constraint": {
        "platform": ["SPOT6", "SPOT7", "PHR1A", "PHR1B"],
        "processingLevel": "ORTHO"
    }
}
```

Example of a parameter named "aoi" with a "geometry" constraint attribute
equals to "POLYGON", whose naming stays within the OpenSearch Geo
Extension ([http://www.opensearch.org/Specifications/OpenSearch/Extensions/Geo/1.0/Draft_2](http://www.opensearch.org/Specifications/OpenSearch/Extensions/Geo/1.0/Draft_2)).

```json
"aoi": {
        "type": "string",
        "format": "uri",
        "x­ads­accept": "application/vnd.geo+json",
        "x­ads­constraint": {
        "geometry": "POLYGON",
    }
}
```

Any attribute naming outside standard, is identified in the list below: **TODO**

### x-ads-icon

This object is OPTIONAL and MUST be an Icon Object.

Example for a parameter named "localRadiometry" with a dedicated icon.

```json
{
    "localRadiometry": {
        "label": "use local radiometry?",
        "type": "boolean",
        "x­ads­icon": {
            "uri": "http://airbus.com.image/icons/gfd2454ds­45s212",
            "type": "image/jpeg"
        }
    }
}
```

### x-ads-isExpert

Specify if the input data is considered as "expert" or not. The value of x­ads­
isExpert is a boolean. If omitted the input data is not considered "expert".
