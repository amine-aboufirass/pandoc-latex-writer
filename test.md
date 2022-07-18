---
title: A title
author: Amine Aboufirass
abstract: some abstract
---

::::{.glossary}
function
: An operation which has an input and output

variable
: A symbol which can take on any value in a defined domain
::::

# A header {#identifier .class key=value}

## A subheader

Mentioning a [function]{ .glossary } and a [variable]{ .glossary }.

This is some text.

This is some code `x = 3`.

A block of python code, referenced by Listing [lst:python-code-example]{ .listing }

``` { #lst:python-code-example .python caption="An example of python code" }
def f(x):
    return x**2

if __name__=="__main__":
    x = 3
    y = f(x)
    print(y)
```

A block of .NET code, referenced by Listing [lst:dotnet-code-example]{ .listing }

``` { #lst:dotnet-code-example .cs caption="An example of dotnet code" }
using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hello");
    }
}
```

An example of a listing imported from an external file:

``` {
    #lst:imported-code-block 
    .python 
    firstline=4 
    lastline=8 
    filename=imported-code-block.py
    caption="A block of code imported from an external file"
    }
```

A bulleted list:

- item
    - subitem
    - subitem
    - subitem
- item

An ordered list:

1. item
    1. subitem
    1. subitem
    1. subitem
1. item

A figure, referenced by Figure [fig:banana]{ .figure }

![A banana](banana.jpg){ #fig:banana scale=1.0 }

A simple table, referenced by Table [tab:my-simple-table]{ .table }

:::: {#tab:my-simple-table}
: Simple table caption

  Right     Left     Center     Default
-------     ------ ----------   -------
     12     12        12            12
    123     123       123          123
      1     1          1             1
::::

A grid table, referenced by Table [tab:my-grid-table]{ .table }

::::{#tab:my-grid-table}
: Grid table caption

+---------------+---------------+--------------------+
| Fruit         | Price         | Advantages         |
+===============+===============+====================+
| Bananas       |  1.34         | - built-in wrapper |
|               |               | - bright color     |
+---------------+---------------+--------------------+
| Oranges       |  2.10         | - cures scurvy     |
|               |               | - tasty            |
+---------------+---------------+--------------------+
::::

:::: { #tab:my-simple-table-explicit Right=2cm Left=1cm }
: Simple table caption, with explicit column widths

  Right     Left     Center     Default
-------     ------ ----------   -------
     12     12        12            12
    123     123       123          123
      1     1          1             1
::::


