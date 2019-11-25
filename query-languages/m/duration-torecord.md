---
title: "Duration.ToRecord | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Duration.ToRecord

## Syntax

<pre>
Duration.ToRecord(<b>duration</b> as duration) as record
</pre>
  
## About  
Returns a record containing the parts the duration value, `duration`. <ul> <li><code>duration</code>: A <code>duration</code> from which the record is created.</li> </ul>

## Example 1
Convert `#duration(2, 5, 55, 20)` into a record of its parts including days, hours, minutes and seconds if applicable.

```powerquery-m
Duration.ToRecord(#duration(2, 5, 55, 20))
```

<table> <tr> <th>Days</th> <td>2</td> </tr> <tr> <th>Hours</th> <td>5</td> </tr> <tr> <th>Minutes</th> <td>55</td> </tr> <tr> <th>Seconds</th> <td>20</td> </tr> </table>
