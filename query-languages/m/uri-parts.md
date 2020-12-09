---
title: "Uri.Parts | Microsoft Docs"
ms.date: 4/22/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Uri.Parts

## Syntax

<pre>
Uri.Parts(<b>absoluteUri</b> as text) as record
</pre> 
  
## About  
Returns the parts of the input `absoluteUri` as a record, containing values such as Scheme, Host, Port, Path, Query, Fragment, UserName and Password.
  
## Example 1  

Find the parts of the absolute URI "www.adventure-works.com".

```powerquery-m
Uri.Parts("www.adventure-works.com")
```  

<table> <tr> <th>Scheme</th> <td>http</td> </tr> <tr> <th>Host</th> <td>www.adventure-works.com</td> </tr> <tr> <th>Port</th> <td>80</td> </tr> <tr> <th>Path</th> <td>/</td> </tr> <tr> <th>Query</th> <td>[Record]</td> </tr> <tr> <th>Fragment</th> <td></td> </tr> <tr> <th>UserName</th> <td></td> </tr> <tr> <th>Password</th> <td></td> </tr> </table>

  
## Example 2  

Decode a percent-encoded string.  
  
```powerquery-m
let 
    UriUnescapeDataString = (data as text) as text => Uri.Parts("http://contoso?a=" & data)[Query][a]
in
    UriUnescapeDataString("%2Bmoney%24")
```  

`"+money$"`
  