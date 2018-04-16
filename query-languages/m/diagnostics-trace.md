---
title: "Diagnostics.Trace | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Diagnostics.Trace
<code>Diagnostics.Trace(<b>traceLevel</b> as number, <b>message</b> as text, <b>value</b> as any, optional <b>delayed</b> as nullable logical) as any</code>  
## About  
Writes a trace <code>message</code>, if tracing is enabled, and returns <code>value</code>. An optional parameter <code>delayed</code> specifies whether to delay the evaluation of <code>value</code> until the message is traced. <code>traceLevel</code> can take one of the following values: <code>TraceLevel.Critical</code> <code>TraceLevel.Error</code>, <code>TraceLevel.Warning</code>, <code>TraceLevel.Information</code>, <code>TraceLevel.Verbose</code>.   
  
## Example 1  
Trace the message before invoking Text.From function and return the result.  
  
<code>Diagnostics.Trace(TraceLevel.Information, "TextValueFromNumber", () => Text.From(123), true)</code>  
  
<code>"123"</code>  
