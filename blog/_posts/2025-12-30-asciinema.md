# asciinema

<https://docs.asciinema.org/getting-started/>

We work out the example in this article:

<https://www.linuxjournal.com/content/bash-trap-command>

```bash
ctrlc_count=0

function no_ctrlc()
{
    let ctrlc_count++
    echo
    if [[ $ctrlc_count == 1 ]]; then
        echo "Stop that."
    elif [[ $ctrlc_count == 2 ]]; then
        echo "Once more and I quit."
    else
        echo "That's it.  I quit."
        exit
    fi
}

trap no_ctrlc SIGINT

while true
do
    echo Sleeping
    sleep 10
done
```

<pre>
# Copyright 2019 Mitch Frazier <mitch -at- linuxjournal.com>
#
# This software may be used and distributed according to the terms of the
# MIT License or the GNU General Public License version 2 (or any later version).
</pre>

<script src="https://asciinema.org/a/DHKlfVPuZSYphUDzSba9GDlD0.js" id="asciicast-DHKlfVPuZSYphUDzSba9GDlD0" async="true"></script>
