---
title: "WebAction.Request | Microsoft Docs"
ms.date: 4/17/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Cube.Properties
<code>WebAction.Request(<b>method</b> as text, <b>url</b> as text, optional <b>options</b> as nullable record) as action</code>
  
## About  
Creates an action that, when executed, will return the results of performing a <code>method</code> request against <code>url</code> using HTTP as a binary value. An optional record parameter, <code>options</code>, may be provided to specify additional properties. The record can contain the following fields: <ul> <li><code>Query</code>: Programmatically add query parameters to the URL without having to worry about escaping. </li> <li><code>ApiKeyName</code>: If the target site has a notion of an API key, this parameter can be used to specify the name (not the value) of the key parameter that must be used in the URL. The actual key value is provided in the credential.</li> <li><code>Content</code>: Specifying this value changes the web request from a GET to a POST, using the value of the <code>Content</code> field as the content of the POST.</li> <li><code>Headers</code>: Specifying this value as a record will supply additional headers to an HTTP request.</li> <li><code>Timeout</code>: Specifying this value as a duration will change the timeout for an HTTP request. The default value is 100 seconds.</li> <li><code>IsRetry</code>: Specifying this logical value as true will ignore any existing response in the cache when fetching data.</li> <li><code>ManualStatusHandling</code>: Specifying this value as a list will prevent any builtin handling for HTTP requests whose response has one of these status codes.</li> <li><code>RelativePath</code>: Specifying this value as text appends it to the base URL before making the request.</li> </ul> 
