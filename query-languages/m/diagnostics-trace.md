---
title: "Diagnostics.Trace | Microsoft Docs"
ms.date: 01/16/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Diagnostics.Trace
## Syntax

<pre>
Diagnostics.Trace(<b>traceLevel</b> as number, <b>message</b> as anynonnull, <b>value</b> as any, optional <b>delayed</b> as nullable logical) as any
</pre>
 
## About  

Writes a trace <code>message</code>, if tracing is enabled, and returns <code>value</code>. An optional parameter <code>delayed</code> specifies whether to delay the evaluation of <code>value</code> until the message is traced. <code>traceLevel</code> can take one of the following values:

- <code>TraceLevel.Critical</code>    
- <code>TraceLevel.Error</code>    
- <code>TraceLevel.Warning</code>  
- <code>TraceLevel.Information</code>  
- <code>TraceLevel.Verbose</code>
  
## Example 1  

Trace the message before invoking Text.From function and return the result.

```
Diagnostics.Trace(TraceLevel.Information, "TextValueFromNumber", () => Text.From(123), true)
```

`"123"` 
