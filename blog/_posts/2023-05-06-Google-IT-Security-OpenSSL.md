---
layout: post
title: Google IT Security OpenSSL
---

> First, let's generate a 2048-bit RSA private key, and take a look at it. To generate the key, enter this command into the terminal:
> 
> ```bash
> openssl genrsa -out private_key.pem 2048
> ```
>
> This command creates a 2048-bit RSA key, called "private_key.pem". The name of the key is specified after the "-out" flag, and typically ends in ".pem". The number of bits is specified with the last argument. To view your new private key, use "cat" to print it to the screen, just like any other file:

```bash
cat private_key.pem
```

```
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAzsfKJLATSq+V1JGVNuz7TpSylxqyJapGLWNZfCVuRjVA+x3a
wdKpuqCPpYj31HjXoox1YW4EGwvoHamH+vR0e7jqDPP610VojlWqCFYPyl/ZzpGd
wi9aSWgCjJSAKmcSxIqwPq9qW82pTb0WVV/6VJH7HXnl8d4d4emiaAVTlTNzZTYZ
ti4njjg7gcbAtyDEGgbwhwWz7rVfifFCrdoDOKs/VGSLm4uTlnlaZjB0bZ7r+w0W
kIatqusixQDrdpOLKHnSsR4SkZKO1TfrJsejNjnKprOkvJXxrHFRw4FfQIsNH42x
dwpHrAJ6J6uL9ZZqEwciOXZoHdk5xFH8D4QbbQIDAQABAoIBAQCgNphe2LX51hXG
/42XYwJMHlZJUXvaRxXcsO9yiyXn6/cPGlCWgHzVhvYFkhxDWeXpod6IwM8ZjZ4o
7WPYg3OFMP7XTmp6ROL/9Uuq7dOKP73omVacUEgqPBZNifnL4NTfx31K9Gr5+l1F
SE53k8fHotvoOLx7LFgG5Bjbc9UQ8cnGUCicXyBQs+fuuVDyzylN3q+n358yXhZf
bxd7iL/b2nHLLWlrQtouGCAIhIOrqqMan+7bXjbbZe0aQLeXx+8VhPd3ITI6NPgn
eiJYFq+mHfogkfwqGXPvdCdzaIW/qzB38em1eLzqT8d2dKt83ynW/ovosgbDLHIj
n68/fCAZAoGBAOs0fVcruaOrKazCKLx2Dvba3haSq2k4XPf+TlgsjqpD4S9QYQww
jjyLMM/31oxnZZnTCIhAOLf1OYOng309j5+pGix24/VJTDRjbTHEMrH4rPhV0dTS
GgRlt4eQhlc/qZ6w5VRQSW5UIEiyrsPeSBRjPrY7lTTQdVpayMdWE6h7AoGBAOEP
87N77TycPfmqpe76aqnhS8WF92vtFH2zUOz45iLly1CMqfeBHE7cpb+TbIyPPd/l
9UhZvKao/sj4Igm99qVsNykizPU5o2DTKbpka/xwT3HHC6IZD1TlUo3vQzhxFKci
SUrAuFjULK2hFxvftuxWahRp5nyXIcLgb9UcRus3AoGACj/3Vl0pceB7qHOtosji
Tg+rrgAmSCeUpZoHgAAxF2pt3cn68LUM/cZzEh0S1HuNCe8QaB+kWR/uqbYbHNIZ
+DM+WMG1nXLcR0wt7gVG0Eqt/wR+aG/fgmGMZfP+Zr73fVroI4x8JrqzzXc79n0x
VvIcQYTHM84BzzY1mbo+kRECgYADP6my440PHOpAGlh+1JqJjTj8xuxFYIy1K8t1
QDqCMnL23LDvY6u277RsyYH9nWu1OaqKutDgTvwuhnZnUZin1qINM/VlbMmQ8jtd
92kfobdj2w2t71KrVQwWBGgh/m/f4bzRGWsPzTA/6V1eB6KqUq0BUm4DSmMwXvD+
UIQtjQKBgAJ2MhymliwePdj/V8sOgkfCPVqXGs4x6R1EnR9OKBkSKmNMvUVaflID
HxASmL26W0Idk1pAAzswCaFlvrbC37gaFIJqFkeHynzTplKt8cKdpSJ+amVrmD6t
vyU3CfSKM9HFeMNsnCHsVV8p2ZOQT3JvH31Qv0bH2JE9d9Au17AZ
-----END RSA PRIVATE KEY-----
```

> Now, let's generate the public key from the private key, and inspect that one, too. Now that you have a private key, you need to generate a public key that goes along with it. You can give that to anyone who wants to send you encrypted data. When data is hashed using your public key, nobody will be able to decrypt it unless they have your private key. To create a public key based on a private key, enter the command below. You should see the following output ("writing RSA key"):

```bash
openssl rsa -in private_key.pem -outform PEM -pubout -out public_key.pem
```

```bash
cat public_key.pem
```

```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzsfKJLATSq+V1JGVNuz7
TpSylxqyJapGLWNZfCVuRjVA+x3awdKpuqCPpYj31HjXoox1YW4EGwvoHamH+vR0
e7jqDPP610VojlWqCFYPyl/ZzpGdwi9aSWgCjJSAKmcSxIqwPq9qW82pTb0WVV/6
VJH7HXnl8d4d4emiaAVTlTNzZTYZti4njjg7gcbAtyDEGgbwhwWz7rVfifFCrdoD
OKs/VGSLm4uTlnlaZjB0bZ7r+w0WkIatqusixQDrdpOLKHnSsR4SkZKO1TfrJsej
NjnKprOkvJXxrHFRw4FfQIsNH42xdwpHrAJ6J6uL9ZZqEwciOXZoHdk5xFH8D4Qb
bQIDAQAB
-----END PUBLIC KEY-----
```

> You'll simulate someone encrypting a file using your public key and sending it to you, which allows you (and only you!) to decrypt it using your private key. Similarly, you can encrypt files using other people's public keys, knowing that only they will be able to decrypt them.

> You'll create a text file that contains some information you want to protect by encrypting it. Then, you'll encrypt and inspect it. To create the file, enter the command below. It will create a new text file called "secret.txt" which just contains the text, "This is a secret message, for authorized parties only". Feel free to change this message to anything you'd like.

To practice Unix text processing, we rewrite the command in the format of a "here document".

```bash
cat > secret.txt <<EOF
This is a secret message, for authorized parties only

This is a secret message, for authorized parties only!
EOF
```

```bash
cat secret.txt
```

```
This is a secret message, for authorized parties only

This is a secret message, for authorized parties only!
```

> Then, to encrypt the file using your public key, enter this command:

```bash
openssl rsautl -encrypt -pubin -inkey public_key.pem -in secret.txt -out secret.enc
```

> This creates the file "secret.enc", which is an encrypted version of "secret.txt". Notice that if you try to view the contents of the encrypted file, the output is garbled. This is totally normal for encrypted messages because they're not meant to have their contents displayed visually.

> The encrypted file will now be ready to send to whoever holds the matching private key. Since that's you, you can decrypt it and get the original contents back. Remember that we must use the private key to decrypt the message, since it was encrypted using the public key. Go ahead and decrypt the file, using this command:

```bash
openssl rsautl -decrypt -inkey private_key.pem -in secret.enc
```

> Now, you'll create a hash digest of the message, then create a digital signature of this digest. Once that's done, you'll verify the signature of the digest. This allows you to ensure that your message wasn't modified or forged. If the message was modified, the hash would be different from the signed one, and the verification would fail.

> To create a hash digest of the message, enter this command:

```bash
openssl dgst -sha256 -sign private_key.pem -out secret.txt.sha256 secret.txt
```

> This creates a file called "secret.txt.sha256" using your private key, which contains the hash digest of your secret text file.
>
> With this file, anyone can use your public key and the hash digest to verify that the file hasn't been modified since you created and hashed it. To perform this verification, enter this command: