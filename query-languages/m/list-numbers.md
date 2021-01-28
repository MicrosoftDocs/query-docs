---
description: "Learn more about: List.Numbers"
title: "List.Numbers | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.Numbers

## Syntax

<pre>
List.Numbers(<b>start</b> as number, <b>count</b> as number, optional <b>increment</b> as nullable number) as list
</pre>
  
## About  
Returns a list of numbers given an initial value, count, and optional increment value. The default increment value is 1. <ul> <li><code>start</code>: The initial value in the list.</li> <li><code>count</code>: The number of values to create.</li> <li><code>increment</code>: <i>[Optional]</i> The value to increment by. If omitted values are incremented by 1.</li> </ul>

## Example 1
Generate a list of 10 consecutive numbers starting at 1.

```powerquery-m
List.Numbers(1, 10)
```

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> <tr><td>3</td></tr> <tr><td>4</td></tr> <tr><td>5</td></tr> <tr><td>6</td></tr> <tr><td>7</td></tr> <tr><td>8</td></tr> <tr><td>9</td></tr> <tr><td>10</td></tr> </table>

## Example 2
Generate a list of 10 numbers starting at 1, with an increment of 2 for each subsequent number.

```powerquery-m
List.Numbers(1, 10, 2)
```

<table> <tr><td>1</td></tr> <tr><td>3</td></tr> <tr><td>5</td></tr> <tr><td>7</td></tr> <tr><td>9</td></tr> <tr><td>11</td></tr> <tr><td>13</td></tr> <tr><td>15</td></tr> <tr><td>17</td></tr> <tr><td>19</td></tr> </table>
