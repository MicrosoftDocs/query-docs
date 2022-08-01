---
description: "Learn more about: OData.Feed"
title: "OData.Feed"
ms.date: 3/16/2022
---
# OData.Feed

## Syntax

<pre>
OData.Feed(<b>serviceUri</b> as text, optional <b>headers</b> as nullable record, optional <b>options</b> as any) as any
</pre>

## About

Returns a table of OData feeds offered by an OData service from a uri `serviceUri`, headers `headers`. A boolean value specifying whether to use concurrent connections or an optional record parameter, `options`, may be specified to control the following options:

* `Query`: Programmatically add query parameters to the URL without having to worry about escaping.
* `Headers`: Specifying this value as a record will supply additional headers to an HTTP request.
* `ExcludedFromCacheKey`: Specifying this value as a list will exclude these HTTP header keys from being part of the calculation for caching data.
* `ApiKeyName`: If the target site has a notion of an API key, this parameter can be used to specify the name (not the value) of the key parameter that must be used in the URL. The actual key value is provided in the credential.
* `Timeout`: Specifying this value as a duration will change the timeout for an HTTP request. The default value is 600 seconds.
* `EnableBatch`: A logical (true/false) that sets whether to allow generation of an OData $batch request if the MaxUriLength is exceeded (default is false).
* `MaxUriLength: A number that indicates the max length of an allowed uri sent to an OData service. If exceeded and EnableBatch is true then the request will be made to an OData $batch endpoint, otherwise it will fail (default is 2048).
* `Concurrent`: A logical (true/false) when set to true, requests to the service will be made concurrently. When set to false, requests will be made sequentially. When not specified, the value will be determined by the service’s AsynchronousRequestsSupported annotation. If the service does not specify whether AsynchronousRequestsSupported is supported, requests will be made sequentially.
* `ODataVersion`: A number (3 or 4) that specifies the OData protocol version to use for this OData service. When not specified, all supported versions will be requested. The service version will be determined by the OData-Version header returned by the service.
* `FunctionOverloads`: A logical (true/false) when set to true, function import overloads will be listed in the navigator as separate entries, when set to false, function import overloads will be listed as one union function in the navigator. Default value for V3: false. Default value for V4: true.
* `MoreColumns`: A logical (true/false) when set to true, adds a "More Columns" column to each entity feed containing open types and polymorphic types. This will contain the fields not declared in the base type. When false, this field is not present. Defaults to false.
* `IncludeAnnotations`: A comma separated list of namespace qualified term names or patterns to include with "\*" as a wildcard. By default, none of the annotations are included.
* `IncludeMetadataAnnotations`: A comma separated list of namespace qualified term names or patterns to include on metadata document requests, with "\*" as a wildcard. By default, includes the same annotations as IncludeAnnotations.
* `OmitValues`: Allows the OData service to avoid writing out certain values in responses. If acknowledged by the service, we will infer those values from the omitted fields. Options include:
  * `ODataOmitValues.Nulls`: Allows the OData service to omit null values.
* `Implementation`: Specifies the implementation of the OData connector to use. Valid values are "2.0" or null.

## Example 1

Connect to the TripPin OData service.

**Usage**

```powerquery-m
OData.Feed("https://services.odata.org/V4/TripPinService")
```

**Output**

`table`
