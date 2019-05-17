---
title: "Uri.Parts | Microsoft Docs"
ms.date: 5/17/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Uri.Parts

## Syntax

<pre>
Uri.Parts(<b>absoluteUri</b> as text) as record
</pre> 
  
## About  
Returns the parts of the input <code>absoluteUri</code> as a record, containing values such as Scheme, Host, Port, Path, Query, Fragment, UserName and Password.
  
## Example 1  

Find the parts of the absolute URI "www.adventure-works.com".

```powerquery-m
Uri.Parts("www.adventure-works.com")
```  

<code>[ Scheme = "http", Host = "www.adventure-works.com", Port = 80, Path = "/", Query = [], Fragment = "", UserName = "", Password = "" ]</code>
  
## Example 2  

Decode a percent-encoded string.  
  
```powerquery-m
let UriUnescapeDataString = (data as text) as text => Uri.Parts("http://contoso?a=" & data)[Query][a] in UriUnescapeDataString("%2Bmoney%24") 
```  

<code>"+money$"</code>
  
