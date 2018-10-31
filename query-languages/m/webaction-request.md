---
title: "WebAction.Request | Microsoft Docs"
ms.date: 10/19/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# WebAction.Request
`WebAction.Request(<b>method</b> as text, <b>url</b> as text, optional <b>options</b> as nullable record) as action`
  
## About  
Creates an action that, when executed, will return the results of performing a `method` request against `url` using HTTP as a binary value. An optional record parameter, `options`, may be provided to specify additional properties. The record can contain the following fields: <ul> <li>`Query`: Programmatically add query parameters to the URL without having to worry about escaping. </li> <li>`ApiKeyName`: If the target site has a notion of an API key, this parameter can be used to specify the name (not the value) of the key parameter that must be used in the URL. The actual key value is provided in the credential.</li> <li>`Content`: Specifying this value changes the web request from a GET to a POST, using the value of the `Content` field as the content of the POST.</li> <li>`Headers`: Specifying this value as a record will supply additional headers to an HTTP request.</li> <li>`Timeout`: Specifying this value as a duration will change the timeout for an HTTP request. The default value is 100 seconds.</li> <li>`IsRetry`: Specifying this logical value as true will ignore any existing response in the cache when fetching data.</li> <li>`ManualStatusHandling`: Specifying this value as a list will prevent any builtin handling for HTTP requests whose response has one of these status codes.</li> <li>`RelativePath`: Specifying this value as text appends it to the base URL before making the request.</li> </ul> 
