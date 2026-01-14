---
description: "Learn more about: DateTime.LocalNow"
title: "DateTime.LocalNow"
ms.subservice: m-source
ms.topic: reference
---
# DateTime.LocalNow

## Syntax

<pre>
DateTime.LocalNow() as datetime  
</pre>
  
## About

Returns a `datetime` value set to the current date and time on the system.

The value returned by this function depends on whether you're running your query on a local machine or online. For example, if you run your query on a system located in the U.S. Pacific Time zone, Power Query Desktop returns the date and time set on your local machine. However, if you run your query on the cloud, Power Query Online returns UTC time because it's reading the time set on the cloud virtual machines, which are all set to UTC.

## Example 1

Invoke this function on a local machine running Power Query Desktop.

**Usage**

```powerquery-m
DateTime.LocalNow()
```

**Output**

The current local date and time.

## Example 2

Invoke this function on the cloud running Power Query Online.

**Usage**

```powerquery-m
DateTime.LocalNow()
```

**Output**

The current online (UTC) date and time.

## Related content

[Local, fixed, and UTC variants of current time functions](m-local-fixed-utc-variants.md)
