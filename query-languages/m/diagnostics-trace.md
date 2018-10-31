---
title: "Diagnostics.Trace | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Diagnostics.Trace
## Syntax

<pre>
Diagnostics.Trace(<b>traceLevel</b> as number, <b>message</b> as text, <b>value</b> as any, optional <b>delayed</b> as nullable logical) as any
</pre>
 
## About  
Writes a trace `message`, if tracing is enabled, and returns `value`. An optional parameter `delayed` specifies whether to delay the evaluation of `value` until the message is traced. `traceLevel` can take one of the following values: `TraceLevel.Critical` `TraceLevel.Error`, `TraceLevel.Warning`, `TraceLevel.Information`, `TraceLevel.Verbose`.   
  
## Example 1  
Trace the message before invoking Text.From function and return the result.  
  
```powerquery-m
Diagnostics.Trace(TraceLevel.Information, "TextValueFromNumber", () => Text.From(123), true)
```  
  
`"123"`  
