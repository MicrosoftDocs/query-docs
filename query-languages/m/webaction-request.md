---
description: "Learn more about: WebAction.Request"
title: "WebAction.Request | Microsoft Docs"
ms.date: 9/13/2021
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# WebAction.Request

## Syntax

<pre>
WebAction.Request(<b>method</b> as text, <b>url</b> as text, optional <b>options</b> as nullable record) as action
</pre>
  
## About

Creates an action that, when executed, will return the results of performing a `method` request against `url` using HTTP as a binary value. An optional record parameter, `options`, may be provided to specify additional properties. The record can contain the following fields:

* `Query`: Programmatically add query parameters to the URL without having to worry about escaping.
* `ApiKeyName`: If the target site has a notion of an API key, this parameter can be used to specify the name (not the value) of the key parameter that must be used in the URL. The actual key value is provided in the credential.
* `Headers`: Specifying this value as a record will supply additional headers to an HTTP request.
* `Timeout`: Specifying this value as a duration will change the timeout for an HTTP request. The default value is 100 seconds.
* `ExcludedFromCacheKey`: Specifying this value as a list will exclude these HTTP header keys from being part of the calculation for caching data.
* `IsRetry`: Specifying this logical value as true will ignore any existing response in the cache when fetching data.
* `ManualStatusHandling`: Specifying this value as a list will prevent any builtin handling for HTTP requests whose response has one of these status codes.
* `RelativePath`: Specifying this value as text appends it to the base URL before making the request.
* `Content`: Specifying this value will cause its contents to become the body of the HTTP request.

Note that this function is disabled in most contexts. Consider using [Web.Contents](/powerquery-m/web-contents) instead.

## Example 1

Perform a GET request against Bing.

```powerquery-m
WebAction.Request(WebMethod.Get, "https://bing.com")
```

`
Action
`
