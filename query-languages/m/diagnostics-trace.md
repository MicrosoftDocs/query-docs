---
description: "Learn more about: Diagnostics.Trace"
title: "Diagnostics.Trace"
ms.subservice: m-source
---
# Diagnostics.Trace

## Syntax

<pre>
Diagnostics.Trace(
    <b>traceLevel</b> as number,
    <b>message</b> as anynonnull,
    <b>value</b> as any,
    optional <b>delayed</b> as nullable logical
) as any
</pre>

## About

Writes a trace `message`, if tracing is enabled, and returns `value`. An optional parameter `delayed` specifies whether to delay the evaluation of `value` until the message is traced. `traceLevel` can take one of the following values:

- [TraceLevel.Critical](tracelevel-type.md)
- [TraceLevel.Error](tracelevel-type.md)
- [TraceLevel.Warning](tracelevel-type.md)
- [TraceLevel.Information](tracelevel-type.md)
- [TraceLevel.Verbose](tracelevel-type.md)

## Example 1

Trace the message before invoking Text.From function and return the result.

**Usage**

```powerquery-m
Diagnostics.Trace(TraceLevel.Information, "TextValueFromNumber", () => Text.From(123), true)
```

**Output**

`"123"`
