---
description: "Learn more about: Time.ToRecord"
title: "Time.ToRecord | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Time.ToRecord

## Syntax

<pre>
Time.ToRecord(<b>time</b> as time) as record
</pre>
  
## About  
Returns a record containing the parts of the given Time value, `time`. <ul> <li><code>time</code>: A <code>time</code> value for from which the record of its parts is to be calculated.</li> </ul>

## Example 1
Convert the `#time(11, 56, 2)` value into a record containing Time values.

```powerquery-m
Time.ToRecord(#time(11, 56, 2))
```

<table> <tr> <th>Hour</th> <td>11</td> </tr> <tr> <th>Minute</th> <td>56</td> </tr> <tr> <th>Second</th> <td>2</td> </tr> </table>
