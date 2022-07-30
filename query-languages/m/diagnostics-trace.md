---
description: "Learn more about: Diagnostics.Trace"
title: "Diagnostics.Trace | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Diagnostics.Trace
## Syntax

<pre>
Diagnostics.Trace(<b>traceLevel</b> as number, <b>message</b> as anynonnull, <b>value</b> as any, optional <b>delayed</b> as nullable logical) as any
</pre>

## About  

Writes a trace `message`, if tracing is enabled, and returns `value`. An optional parameter `delayed` specifies whether to delay the evaluation of `value` until the message is traced. `traceLevel` can take one of the following values:

- [TraceLevel.Critical](/powerquery-m/tracelevel-critical)
- [TraceLevel.Error](/powerquery-m/tracelevel-error)
- [TraceLevel.Warning](/powerquery-m/tracelevel-warning)  
- [TraceLevel.Information](/powerquery-m/tracelevel-information)  
- [TraceLevel.Verbose](/powerquery-m/tracelevel-verbose)
  
## Example 1  

Trace the message before invoking Text.From function and return the result.

**Usage**

```
Diagnostics.Trace(TraceLevel.Information, "TextValueFromNumber", () => Text.From(123), true)
```

**Output**

`"123"`
