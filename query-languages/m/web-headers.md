---
description: "Learn more about: Web.Headers"
title: "Web.Headers"
---
# Web.Headers

## Syntax

<pre>
Web.Headers(<b>url</b> as text, optional <b>options</b> as nullable record) as record
</pre>

## About

Returns the headers downloaded from `url` as a record. An optional record parameter, `options`, may be provided to specify additional properties. The record can contain the following fields:

* `Query`: Programmatically add query parameters to the URL without having to worry about escaping.
* `ApiKeyName`: If the target site has a notion of an API key, this parameter can be used to specify the name (not the value) of the key parameter that must be used in the URL. The actual key value is provided in the credential.
* `Headers`: Specifying this value as a record will supply additional headers to an HTTP request.
* `Timeout`: Specifying this value as a duration will change the timeout for an HTTP request. The default value is 100 seconds.
* `ExcludedFromCacheKey`: Specifying this value as a list will exclude these HTTP header keys from being part of the calculation for caching data.
* `IsRetry`: Specifying this logical value as true will ignore any existing response in the cache when fetching data.
* `ManualStatusHandling`: Specifying this value as a list will prevent any builtin handling for HTTP requests whose response has one of these status codes.
* `RelativePath`: Specifying this value as text appends it to the base URL before making the request.

The HTTP request is made with the HEAD method. Outside of a custom data connector context, only a subset of response headers is available (for security reasons).

## Example 1

Retrieve the HTTP headers for `"https://bing.com/search?q=Power+Query"` using the RelativePath and Query options.

**Usage**

```powerquery-m
let
    searchText = "Power Query"
in
    Web.Headers(
        "https://www.bing.com",
        [
            RelativePath = "search",
            Query = [q = searchText]
        ]
    )
```

**Output**

```powerquery-m
([
    #"Cache-Control" = "private, max-age=0",
    #"Content-Encoding" = "gzip",
    #"Content-Length" = "0",
    #"Content-Type" = "text/html; charset=utf-8",
    Date = "Tue, 14 Dec 2021 16:57:25 GMT",
    Expires = "Tue, 14 Dec 2021 16:56:25 GMT",
    Vary = "Accept-Encoding"
]
meta [
    Response.Status = 200
])
```
