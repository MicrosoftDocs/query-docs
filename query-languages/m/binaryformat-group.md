---
title: "BinaryFormat.Group | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# BinaryFormat.Group

## Syntax

<pre>
BinaryFormat.Group(<b>binaryFormat</b> as function, <b>group</b> as list, optional <b>extra</b> as nullable function, optional <b>lastKey</b> as any) as function
</pre>

## About

The parameters are as follows: <ul> <li>The <code>binaryFormat</code> parameter specifies the binary format of the key value.</li> <li>The <code>group</code> parameter provides information about the group of known items.</li> <li>The optional <code>extra</code> parameter can be used to specify a function that will return a binary format value for the value following any key that was unexpected. If the <code>extra</code> parameter is not specified, then an error will be raised if there are unexpected key values.</li> </ul> The <code>group</code> parameter specifies a list of item definitions. Each item definition is a list, containing 3-5 values, as follows: <ul> <li>Key value. The value of the key that corresponds to the item. This must be unique within the set of items.</li> <li>Item format. The binary format corresponding to the value of the item. This allows each item to have a different format. </li> <li>Item occurrence. The <code>BinaryOccurrence.Type</code> value for how many times the item is expected to appear in the group. Required items that are not present cause an error. Required or optional duplicate items are handled like unexpected key values.</li> <li>Default item value (optional). If the default item value appears in the item definition list and is not null, then it will be used instead of the default. The default for repeating or optional items is null, and the default for repeating values is an empty list { }.</li> <li>Item value transform (optional). If the item value transform function is present in the item definition list and is not null, then it will be called to transform the item value before it is returned. The transform function is only called if the item appears in the input (it will never be called with the default value). </li> </ul>

## Example 1

The following assumes a key value that is a single byte, with 4 expected items in the group, all of which have a byte of data following the key. The items appear in the input as follows: <ul> <li>Key 1 is required, and does appear with value 11.</li> <li>Key 2 repeats, and appears twice with value 22, and results in a value of { 22, 22 }.</li> <li>Key 3 is optional, and does not appear, and results in a value of null.</li> <li>Key 4 repeats, but does not appear, and results in a value of { }.</li> <li>Key 5 is not part of the group, but appears once with value 55. The extra function is called with the key value 5, and returns the format corresponding to that value (BinaryFormat.Byte). The value 55 is read and discarded.</li> </ul>

```powerquery-m
let
    b = #binary({
        1, 11,
        2, 22,
        2, 22,
        5, 55,
        1, 11
    }),
    f = BinaryFormat.Group(
        BinaryFormat.Byte,
        {
            {1, BinaryFormat.Byte, BinaryOccurrence.Required},
            {2, BinaryFormat.Byte, BinaryOccurrence.Repeating},
            {3, BinaryFormat.Byte, BinaryOccurrence.Optional},
            {4, BinaryFormat.Byte, BinaryOccurrence.Repeating}
        },
        (extra) => BinaryFormat.Byte
    )
in
    f(b)
```

<table> <tr><td>11</td></tr> <tr><td>[List]</td></tr> <tr><td></td></tr> <tr><td>[List]</td></tr> </table>

## Example 2

The following example illustrates the item value transform and default item value. The repeating item with key 1 sums the list of values read using List.Sum. The optional item with key 2 has a default value of 123 instead of null.

```powerquery-m
let
    b = #binary({
        1, 101, 
        1, 102 
    }),
    f = BinaryFormat.Group(
        BinaryFormat.Byte,
        {
            {1, BinaryFormat.Byte, BinaryOccurrence.Repeating, 
              0, (list) => List.Sum(list)},
            {2, BinaryFormat.Byte, BinaryOccurrence.Optional, 123}
        }
    )
in
    f(b)
```

<table> <tr><td>203</td></tr> <tr><td>123</td></tr> </table>
