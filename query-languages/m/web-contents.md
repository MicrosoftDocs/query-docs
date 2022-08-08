---
description: "Learn more about: Web.Contents"
title: "Web.Contents"
ms.date: 3/14/2022
---
# Web.Contents

## Syntax

<pre> 
Web.Contents(<b>url</b> as text, optional <b>options</b> as nullable record) as binary
</pre>
  
## About

Returns the contents downloaded from `url` as binary. An optional record parameter, `options`, may be provided to specify additional properties. The record can contain the following fields:

* `Query`: Programmatically add query parameters to the URL without having to worry about escaping.
* `ApiKeyName`: If the target site has a notion of an API key, this parameter can be used to specify the name (not the value) of the key parameter that must be used in the URL. The actual key value is provided in the credential.
* `Headers`: Specifying this value as a record will supply additional headers to an HTTP request.
* `Timeout`: Specifying this value as a duration will change the timeout for an HTTP request. The default value is 100 seconds.
* `ExcludedFromCacheKey`: Specifying this value as a list will exclude these HTTP header keys from being part of the calculation for caching data.
* `IsRetry`: Specifying this logical value as true will ignore any existing response in the cache when fetching data.
* `ManualStatusHandling`: Specifying this value as a list will prevent any builtin handling for HTTP requests whose response has one of these status codes.
* `RelativePath`: Specifying this value as text appends it to the base URL before making the request.
* `Content`: Specifying this value changes the web request from a GET to a POST, using the value of the option as the content of the POST.

The HTTP request is made as either a GET (when no Content is specified) or a POST (when there is Content). POST requests may only be made anonymously.

The headers of the HTTP response are available as metadata on the binary result. Outside of a custom data connector context, only a subset of response headers is available (for security reasons).

## Example 1

Retrieve the contents of `"https://bing.com/search?q=Power+Query"` using the `RelativePath` and `Query` options. These options can be used to dynamically query a static base URL.

**Usage**

```powerquery-m
let
    searchText = "Power Query"
in
    Web.Contents(
        "https://www.bing.com",
        [
            RelativePath = "search",
            Query = [q = searchText]
        ]
    )
```

**Output**

`binary`

## Example 2

Perform a POST against a URL, passing a binary JSON payload and parsing the response as JSON.

**Usage**

```powerquery-m
let
    url = ...,
    headers = [#"Content-Type" = "application/json"],
    postData = Json.FromValue([x = 235.7, y = 41.53]),
    response = Web.Contents(
        url,
        [
            Headers = headers,
            Content = postData
        ]
    ),
    jsonResponse = Json.Document(response)
in
    jsonResponse
```

**Output**

`table`

## Example 3

Connect to a secure URL that accepts an authentication key as part of its query string. Instead of hard-coding the secret key in M (which would pose a security risk), the key can be provided securely by specifying its name (not its value) in M, choosing Web API authentication, and entering the key value as part of the Web API credential. When used in this way, the following example will generate a request to `"https://contoso.com/api/customers/get?api_key=******"`.

**Usage**

``` powerquery-m
Web.Contents("https://contoso.com/api/customers/get", [ApiKeyName="api_key"])
```

**Output**

`binary`
