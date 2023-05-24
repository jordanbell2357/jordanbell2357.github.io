---
layout: post
title: Google IT Security md5sum and shasum
topic: cli
---

```bash
cat > file.txt <<EOF
Whoever thinks a faultless Piece to see,
  Thinks what ne’er was, nor is, nor e’er shall be.
In ev’ry Work regard the Writer’s End,
  Since none can compass more than they Intend;
  And if the Means be just, the Conduct true,
  Applause, in spite of trivial Faults, is due.
As Men of Breeding, oft the Men of Wit
  T’ avoid great Errors, must the less commit,
  Neglect the Rules each Verbal Critick lays,
  For not to know some Trifles, is a Praise.
Most Criticks fond of some subservient Art,
  Still make the Whole depend upon a Part,
  They talk of Principles, but Parts they prize,
  And All to one lov’d Folly Sacrifice.
EOF
```

> You'll now generate the MD5 sum for the file and store it. To generate the sum for your new file, enter this md5sum command:
>
> ```bash
> md5sum file.txt > file.txt.md5
> ```
> This creates the MD5 hash, and saves it to a new file. You can take a look at the hash by printing its contents to the screen, using this command:
>
> ```bash
> cat file.txt.md5
> ```
> This should print the hash to the terminal, which should look something like this:

`1e95a5e71c61c50188fbd9be3ec55420  file.txt`

> More importantly, you can also verify that the hash is correct, and that the original file hasn't been tampered with since the sum was made. To do this, enter this command and see the following output, which indicates that the hash is valid:
>
> ```bash
> md5sum -c file.txt.md5
> ```
>
> `file.txt: OK`

We add a single space at the end of a copy of `file.txt`:

```bash
cp file.txt badfile.txt
md5sum badfile.txt > badfile.txt.md5
cat badfile.txt.md5
```

`1e95a5e71c61c50188fbd9be3ec55420  badfile.txt`

```bash
md5sum -c badfile.txt.md5
```

```
badfile.txt: OK
```

```bash
echo " " >> badfile.txt
md5sum -c badfile.txt.md5
```

```
badfile.txt: FAILED
md5sum: WARNING: 1 computed checksum did NOT match
```

```bash
md5sum badfile.txt > new.badfile.txt.md5
cat new.badfile.txt.md5
```

`3f5554cbe38d7feb184e97d7e9db511a  badfile.txt`

> To create the SHA1 sum and save it to a file, use this command:
>
> ```bash
> shasum file.txt > file.txt.sha1
> ```

```bash
cat file.txt.sha1
```
```
e03033f6a4b5dc5494591ec610393b4d5518d8f4  file.txt
```

> Now, verify the hash using the command below. (Like before, this would fail if the original file had been changed.)
>
> ```bash
> shasum -c file.txt.sha1
> ```
>
> `file.txt: OK`

> The same tool can be used to create a SHA256 sum. The "-a" flag specifies the algorithm to use, and defaults to SHA1 if nothing is specified. To generate the SHA256 sum of the file, use this command:
>
> ```bash
> shasum -a 256 file.txt > file.txt.sha256
> ```

```bash
cat file.txt.sha256
```
```
4161ecc29ef36470a9346b7ee9e2b1b6fc58eddb62d5bc5a581961c435bce3a6  file.txt
```

> Finally, to verify the SHA256 sum, you can use the same command as before:
>
> ```bash
> shasum -c file.txt.sha256
> ```
>
> `file.txt: OK`

We copy delete the last line of `file.txt`:

```bash
sed -i '$d' file.txt
shasum -c file.txt.sha256
```

```
file.txt: FAILED
shasum: WARNING: 1 computed checksum did NOT match
```

But then:

```bash
echo "  And All to one lov’d Folly Sacrifice." >> file.txt
shasum -c file.txt.sha256
```

`file.txt: OK`