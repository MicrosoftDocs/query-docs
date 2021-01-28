---
description: "Learn more about: Web.Contents"
title: "Web.Contents | Microsoft Docs"
ms.date: 11/23/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

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

The headers of the HTTP response are available as metadata on the binary result. Outside of a custom data connector context, only the Content-Type header is available. 


