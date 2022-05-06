
# author: `Trotylson`

The script can be useful for automatic searching and, for example, deleting files that you want to remove from your machine or perform some operation on them.

- [x] multifunctionality
- [x] easy to use
---
---

# HOW IT WORKS:

Inside script you will find `packet` dictionary:

    packet = {
        'do' : "what script have to do",
        'packet_name' : 'add a name of newly script',
        'start_at' : 'location where script start searching',
        'looking_for' : 'location where script will be activated'
    }

You have to edit a `keys` `values` in this packet, for example:

    packet = {
        'do' : "import os\nos.system('ip a')",
        'packet_name' : 'warning.txt',
        'start_at' : '/mnt/',
        'looking_for' : 'd'
    }

In this example, the script will search for the `d` directory / drive from `mnt`.
Once it finds the above location, it will start the process of creating a script named `warning.txt`, after which it will implement the requested `import os\nos.system('ip a')` code inside and then run it.

Our injected script:

    import os
    os.system('ip a')


---
---
## UPDATES / CHANGES


| ver.        | date        |   update / change     |
| :---:       |    :----:   |     :---:     |
| 1.1         | 06.05.2022  | simplification in the form of a dictionary named `packet`   |
| 1.0         | 04.05.2022  | iterating through files, creating a file at the target path   |

