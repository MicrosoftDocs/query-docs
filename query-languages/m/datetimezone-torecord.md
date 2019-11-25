---
title: "DateTimeZone.ToRecord | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# DateTimeZone.ToRecord

## Syntax

<pre>
DateTimeZone.ToRecord(<b>dateTimeZone</b> as datetimezone) as record
</pre> 
  
## About  
Returns a record containing the parts of the given datetimezone value, `dateTimeZone`. <ul> <li><code>dateTimeZone</code>: A <code>datetimezone</code> value for from which the record of its parts is to be calculated.</li> </ul>

## Example 1
Convert the `#datetimezone(2011, 12, 31, 11, 56, 2, 8, 0)` value into a record containing Date, Time, and Zone values.

```powerquery-m
DateTimeZone.ToRecord(#datetimezone(2011, 12, 31, 11, 56, 2, 8, 0))
```

<table> <tr> <th>Year</th> <td>2011</td> </tr> <tr> <th>Month</th> <td>12</td> </tr> <tr> <th>Day</th> <td>31</td> </tr> <tr> <th>Hour</th> <td>11</td> </tr> <tr> <th>Minute</th> <td>56</td> </tr> <tr> <th>Second</th> <td>2</td> </tr> <tr> <th>ZoneHours</th> <td>8</td> </tr> <tr> <th>ZoneMinutes</th> <td>0</td> </tr> </table>
