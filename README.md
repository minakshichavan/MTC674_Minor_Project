# MTC674_Minor_Project
Minor Project - Red Hat Package Manager for Payload Delivery

# Red Hat Package Manager for Payload Delivery
## _A Minor Project by Minakshi Pushpendra Chavan_


## Step 1 - Understanding the base system.
The base system used to create and build the dummy package is Red Hat Enterprise Linux 7.9 machine. The `rpm-build` and `rpm-sign` packages are already installed as follows.
```
[minakshi@rhel7-basemachine ~]$ whoami
minakshi
[minakshi@rhel7-basemachine ~]$ sudo rpm -q rpm-build rpm-sign
rpm-build-4.11.3-48.el7_9.x86_64
rpm-sign-4.11.3-48.el7_9.x86_64
[minakshi@rhel7-basemachine ~]$ cat /etc/redhat-release 
Red Hat Enterprise Linux Server release 7.9 (Maipo)
[minakshi@rhel7-basemachine ~]$ uname -a
Linux rhel7-basemachine 3.10.0-1160.71.1.el7.x86_64 #1 SMP Wed Jun 15 08:55:08 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
```
- Import a HTML file and watch it magically convert to Markdown
- Drag and drop images (requires your Dropbox account be linked)
- Import and save files from GitHub, Dropbox, Google Drive and One Drive
- Drag and drop markdown and HTML files into Dillinger
- Export documents as Markdown, HTML and PDF

## Step 2 - Gather the dummy code
Get the dummy code, create a `tar.gz` archive in an appropriate `tree` structure and place it under `~/rpmbuild` directory as follows.
```
[minakshi@rhel7-basemachine ~]$ ls rpmbuild/
SOURCES  SPECS
[minakshi@rhel7-basemachine ~]$ tree rpmbuild/
rpmbuild/
├── SOURCES
│   └── dummy-package-1.0.0.tar.gz
└── SPECS
    └── dummy-package.spec

2 directories, 2 files

[minakshi@rhel7-basemachine ~]$ tar tvf rpmbuild/SOURCES/dummy-package-1.0.0.tar.gz 
drwxrwxr-x minakshi/minakshi 0 2022-08-09 15:15 dummy-package-1.0.0/
drwxrwxr-x minakshi/minakshi 0 2022-08-09 15:48 dummy-package-1.0.0/usr/
drwxrwxr-x minakshi/minakshi 0 2022-08-09 15:15 dummy-package-1.0.0/usr/local/
drwxrwxr-x minakshi/minakshi 0 2022-08-09 15:15 dummy-package-1.0.0/usr/local/man/
drwxrwxr-x minakshi/minakshi 0 2022-08-09 15:21 dummy-package-1.0.0/usr/local/man/man8/
-rw-rw-r-- minakshi/minakshi 354 2022-08-09 15:19 dummy-package-1.0.0/usr/local/man/man8/dummy-package.1.gz
drwxrwxr-x minakshi/minakshi   0 2022-08-09 16:15 dummy-package-1.0.0/usr/bin/
-rw-rw-r-- minakshi/minakshi 1112 2022-08-09 16:15 dummy-package-1.0.0/usr/bin/dummy-binary
drwxrwxr-x minakshi/minakshi    0 2022-08-09 15:15 dummy-package-1.0.0/etc/
drwxrwxr-x minakshi/minakshi    0 2022-08-09 15:49 dummy-package-1.0.0/etc/dummy-package/
-rw-rw-r-- minakshi/minakshi   58 2022-08-09 15:49 dummy-package-1.0.0/etc/dummy-package/dummy-package.conf

[minakshi@rhel7-basemachine ~]$ ls -lR rpmbuild/
rpmbuild/:
total 0
drwxr-xr-x. 2 minakshi minakshi 40 Aug  9 16:27 SOURCES
drwxr-xr-x. 2 minakshi minakshi 32 Aug  9 16:10 SPECS

rpmbuild/SOURCES:
total 4
-rw-rw-r--. 1 minakshi minakshi 1250 Aug  9 16:15 dummy-package-1.0.0.tar.gz

rpmbuild/SPECS:
total 4
-rw-r--r--. 1 minakshi minakshi 1590 Aug  9 16:10 dummy-package.spec

[minakshi@rhel7-basemachine ~]$ file rpmbuild/SOURCES/dummy-package-1.0.0.tar.gz rpmbuild/SPECS/dummy-package.spec 
rpmbuild/SOURCES/dummy-package-1.0.0.tar.gz: gzip compressed data, from Unix, last modified: Tue Aug  9 16:15:57 2022
rpmbuild/SPECS/dummy-package.spec:           ASCII text
```
## Step 3 - Create a SPEC file 
The `spec` file is an important part of the build process for an `rpm` package. All necessary fields can be populated in here.
```
[minakshi@rhel7-basemachine ~]$ cat rpmbuild/SPECS/dummy-package.spec
Summary: This is a dummy package built by Minakshi Pushpendra Chavan.
Name: dummy-package
Version: 1.0.0
Release: 0.el7
Group: Applications/File
Source: dummy-package-%{version}.tar.gz
BuildArch: noarch
Requires: bash
Requires: rpm
License: GPLv2+
Vendor: G S Mandal's Maharashtra Institute of Technology, Aurangabad 
Packager: Minakshi Pushpendra Chavan
BuildRoot:  %{_tmppath}/%{name}-buildroot

%description
This is a dummy package built by Minakshi Pushpendra Chavan as a part of minor project for completion of first year of Master of Technology in Computer Science and Technology under the guidance of Prof Dr B S Sonawane Sir.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -m 0755 -d $RPM_BUILD_ROOT/etc/dummy-package
install -m 0755 -d $RPM_BUILD_ROOT/usr/bin
install -m 0755 -d $RPM_BUILD_ROOT/usr/local/man/man1


install -p etc/dummy-package/dummy-package.conf $RPM_BUILD_ROOT/etc/dummy-package/dummy-package.conf
install -p usr/bin/dummy-binary $RPM_BUILD_ROOT/usr/bin/dummy-binary
install -p usr/local/man/man8/dummy-package.1.gz $RPM_BUILD_ROOT/usr/local/man/man1/dummy-package.1.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/dummy-binary
%config /etc/dummy-package/dummy-package.conf
%doc /usr/local/man/man1/dummy-package.1.gz 

%post
echo "Please run "dummy-package" command to view deployment !"
echo "Your constructive feedback will be highly appreciated!!!"

%postun

echo "Hope You liked this minor project!"

%changelog
* Sun Jun 25 2022 Minakshi Pushpendra Chavan <shenguleminakshi265@gmail.com> 1.0.0
- Initial version

```

## Step 4 - Build an RPM
The `rpmbuild` binary can be utilized to finally build an unsigned `rpm` package along with a source `rpm` as follows.
```
[minakshi@rhel7-basemachine ~]$ rpmbuild -ba rpmbuild/SPECS/dummy-package.spec
warning: bogus date in %changelog: Sun Jun 25 2022 Minakshi Pushpendra Chavan <shenguleminakshi265@gmail.com> 1.0.0
Executing(%prep): /bin/sh -e /var/tmp/rpm-tmp.wQe9HK
+ umask 022
+ cd /home/minakshi/rpmbuild/BUILD
+ cd /home/minakshi/rpmbuild/BUILD
+ rm -rf dummy-package-1.0.0
+ /usr/bin/gzip -dc /home/minakshi/rpmbuild/SOURCES/dummy-package-1.0.0.tar.gz
+ /usr/bin/tar -xf -
+ STATUS=0
+ '[' 0 -ne 0 ']'
+ cd dummy-package-1.0.0
+ /usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
+ exit 0
Executing(%build): /bin/sh -e /var/tmp/rpm-tmp.ZzmT5d
+ umask 022
+ cd /home/minakshi/rpmbuild/BUILD
+ cd dummy-package-1.0.0
+ exit 0
Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.I31QtH
+ umask 022
+ cd /home/minakshi/rpmbuild/BUILD
+ '[' /home/minakshi/rpmbuild/BUILDROOT/dummy-package-1.0.0-0.el7.x86_64 '!=' / ']'
+ rm -rf /home/minakshi/rpmbuild/BUILDROOT/dummy-package-1.0.0-0.el7.x86_64
++ dirname /home/minakshi/rpmbuild/BUILDROOT/dummy-package-1.0.0-0.el7.x86_64
+ mkdir -p /home/minakshi/rpmbuild/BUILDROOT
+ mkdir /home/minakshi/rpmbuild/BUILDROOT/dummy-package-1.0.0-0.el7.x86_64
+ cd dummy-package-1.0.0
+ rm -rf /home/minakshi/rpmbuild/BUILDROOT/dummy-package-1.0.0-0.el7.x86_64
+ install -m 0755 -d /home/minakshi/rpmbuild/BUILDROOT/dummy-package-1.0.0-0.el7.x86_64/etc/dummy-package
+ install -m 0755 -d /home/minakshi/rpmbuild/BUILDROOT/dummy-package-1.0.0-0.el7.x86_64/usr/bin
+ install -m 0755 -d /home/minakshi/rpmbuild/BUILDROOT/dummy-package-1.0.0-0.el7.x86_64/usr/local/man/man1
+ install -p etc/dummy-package/dummy-package.conf /home/minakshi/rpmbuild/BUILDROOT/dummy-package-1.0.0-0.el7.x86_64/etc/dummy-package/dummy-package.conf
+ install -p usr/bin/dummy-binary /home/minakshi/rpmbuild/BUILDROOT/dummy-package-1.0.0-0.el7.x86_64/usr/bin/dummy-binary
+ install -p usr/local/man/man8/dummy-package.1.gz /home/minakshi/rpmbuild/BUILDROOT/dummy-package-1.0.0-0.el7.x86_64/usr/local/man/man1/dummy-package.1.gz
+ /usr/lib/rpm/find-debuginfo.sh --strict-build-id -m --run-dwz --dwz-low-mem-die-limit 10000000 --dwz-max-die-limit 110000000 /home/minakshi/rpmbuild/BUILD/dummy-package-1.0.0
/usr/lib/rpm/sepdebugcrcfix: Updated 0 CRC32s, 0 CRC32s did match.
+ /usr/lib/rpm/check-buildroot
+ /usr/lib/rpm/redhat/brp-compress
+ /usr/lib/rpm/redhat/brp-strip-static-archive /usr/bin/strip
+ /usr/lib/rpm/brp-python-bytecompile /usr/bin/python 1
+ /usr/lib/rpm/redhat/brp-python-hardlink
+ /usr/lib/rpm/redhat/brp-java-repack-jars
Processing files: dummy-package-1.0.0-0.el7.noarch
Provides: config(dummy-package) = 1.0.0-0.el7 dummy-package = 1.0.0-0.el7
Requires(interp): /bin/sh /bin/sh
Requires(rpmlib): rpmlib(CompressedFileNames) <= 3.0.4-1 rpmlib(FileDigests) <= 4.6.0-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires(post): /bin/sh
Requires(postun): /bin/sh
Checking for unpackaged file(s): /usr/lib/rpm/check-files /home/minakshi/rpmbuild/BUILDROOT/dummy-package-1.0.0-0.el7.x86_64
Wrote: /home/minakshi/rpmbuild/SRPMS/dummy-package-1.0.0-0.el7.src.rpm
Wrote: /home/minakshi/rpmbuild/RPMS/noarch/dummy-package-1.0.0-0.el7.noarch.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.rXKoW9
+ umask 022
+ cd /home/minakshi/rpmbuild/BUILD
+ cd dummy-package-1.0.0
+ rm -rf /home/minakshi/rpmbuild/BUILDROOT/dummy-package-1.0.0-0.el7.x86_64
+ exit 0
```
See the binary package created at `/home/minakshi/rpmbuild/RPMS/noarch/dummy-package-1.0.0-0.el7.noarch.rpm` and source package at `/home/minakshi/rpmbuild/SRPMS/dummy-package-1.0.0-0.el7.src.rpm` respectively. The created `rpm` package is in fact an unsigned package as follows. Observe the `Signature` part which shows as `(none)`, means it needs to get signed now.
```
[minakshi@rhel7-basemachine rpmbuild]$ sudo rpm -qip /home/minakshi/rpmbuild/RPMS/noarch/dummy-package-1.0.0-0.el7.noarch.rpm
Name        : dummy-package
Version     : 1.0.0
Release     : 0.el7
Architecture: noarch
Install Date: (not installed)
Group       : Applications/File
Size        : 1524
License     : GPLv2+
Signature   : (none)
Source RPM  : dummy-package-1.0.0-0.el7.src.rpm
Build Date  : Tuesday 09 August 2022 05:26:42 PM IST
Build Host  : rhel7-basemachine
Relocations : (not relocatable)
Packager    : Minakshi Pushpendra Chavan
Vendor      : G S Mandal's Maharashtra Institute of Technology, Aurangabad
Summary     : This is a dummy package built by Minakshi Pushpendra Chavan.
Description :
This is a dummy package built by Minakshi Pushpendra Chavan as a part of minor project for completion of first year of Master of Technology in Computer Science and Technology under the guidance of Prof Dr B S Sonawane Sir.
```
## Step 5 - Generate GPG key to sign the rpm.
To get the package signed, one needs to have a private-public `gpg` keypair generated as follows.
```
[minakshi@rhel7-basemachine ~]$ gpg --gen-key
gpg (GnuPG) 2.0.22; Copyright (C) 2013 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
Your selection? 1
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048) 
Requested keysize is 2048 bits
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 
Key does not expire at all
Is this correct? (y/N) y

GnuPG needs to construct a user ID to identify your key.

Real name: Minakshi Pushpendra Chavan
Email address: shenguleminakshi265@gmail.com
Comment: A Minor Project under the guidance of Prof Dr B S Sonawane sir for fulfilment of MTech CST
You selected this USER-ID:
    "Minakshi Pushpendra Chavan (A Minor Project under the guidance of Prof Dr B S Sonawane sir for fulfilment of MTech CST) <shenguleminakshi265@gmail.com>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O
You need a Passphrase to protect your secret key.

We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: /home/minakshi/.gnupg/trustdb.gpg: trustdb created
gpg: key 3DF5524B marked as ultimately trusted
public and secret key created and signed.

gpg: checking the trustdb
gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
pub   2048R/3DF5524B 2022-08-09
      Key fingerprint = C13B 2C3F 751F 1473 1CA7  D288 E25C B92B 3DF5 524B
uid                  Minakshi Pushpendra Chavan (A Minor Project under the guidance of Prof Dr B S Sonawane sir for fulfilment of MTech CST) <shenguleminakshi265@gmail.com>
sub   2048R/486820E4 2022-08-09

[minakshi@rhel7-basemachine ~]$ gpg --list-keys
/home/minakshi/.gnupg/pubring.gpg
---------------------------------
pub   2048R/3DF5524B 2022-08-09
uid                  Minakshi Pushpendra Chavan (A Minor Project under the guidance of Prof Dr B S Sonawane sir for fulfilment of MTech CST) <shenguleminakshi265@gmail.com>
sub   2048R/486820E4 2022-08-09
```
The `public` key can be exported in a text file as follows.
```
[minakshi@rhel7-basemachine ~]$ gpg --export -a 'Minakshi Pushpendra Chavan (A Minor Project under the guidance of Prof Dr B S Sonawane sir for fulfilment of MTech CST)' > dummy-package-public-key.txt
[minakshi@rhel7-basemachine ~]$ cat dummy-package-public-key.txt
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v2.0.22 (GNU/Linux)

mQENBGLyPqMBCAC5eBF+/IwFzDxQi+O6lYIaumwaZDvk3J9YJkL9iJT8wnEj2knb
LYd+z4FkYGvlQShHwX2jaMuHmxP2fXOrV4Ux3nfAQv8fysRkG3l8HrCNXJVQbpTD
zTZbMKU6VwhTovlVcHMlznAIKfaTI2T8Dreb8j3RavLUBMs3n9bBAGDkxHOZgeQ+
3JI9RbbbitbC7T51ig1Owdq0xeCZnV81SPvipLt0IxtRTzQIdzRLi9Hrkhu5dqDd
tEwO+BdeFu1iIlpSgWRF7wGpye2sP8bjXaTJc81mb90YRS6hwYqKptlSu/p66BbW
v8V+Zm9hhJs2nyWIlLPy33cjypeTVV+3tA7vABEBAAG0l01pbmFrc2hpIFB1c2hw
ZW5kcmEgQ2hhdmFuIChBIE1pbm9yIFByb2plY3QgdW5kZXIgdGhlIGd1aWRhbmNl
IG9mIFByb2YgRHIgQiBTIFNvbmF3YW5lIHNpciBmb3IgZnVsZmlsbWVudCBvZiBN
VGVjaCBDU1QpIDxzaGVuZ3VsZW1pbmFrc2hpMjY1QGdtYWlsLmNvbT6JATkEEwEC
ACMFAmLyPqMCGwMHCwkIBwMCAQYVCAIJCgsEFgIDAQIeAQIXgAAKCRDiXLkrPfVS
S3F3B/478pEt0dITxcksuUZQRxXGGUbNXfYqSCgg2dd+uECXMnpN6xosqujMiIY0
SkephTuzV2vF5N24lfh15IgHWszM6B0rV6KuMO9v4VrHEav9U7EqIMKf+hzqmpvZ
d8Ki9Jyyga7VPdxZon8YkL4JqEWriaM/XyZF3IHqNwEpYg2iXxOEvXQoKLB+5q3k
wR5GQG+21NCVz8tFr7vYCV4rJaT9/Y3pToC+eHNXQVG1nbDSNGSfYZhfWoZHsovs
SiaA5Wa6wxGQ5j9pGzy3Nx3UrQLmz3Wk0P3T0g/fB7DeD0L019q9EyEw+uf3YCVJ
ge5vFbXzcdKQ/cmB1F/QOSj9/M88uQENBGLyPqMBCACodep+fPHJcriMbOQrLJte
GNE2kcNT2qlHjvNl0xCQFPtuJg4LAvAnhVLnjIme2/gEQRoyEUoCH/54PAjXm+Bp
sk6ErnYfkWU/Qq/YQiFdwWDM9kOmr09s1kH1ZEg7mV7qOhDa4QKane426JFCmsgB
+VIgG19Qod6LfZh6CRPCmpkfhgqOhr6j0k8r+wjXb+BJt59rGjWS0ftdOaOW32Te
dDxPY8DayMNjCbeLgj+r4X0lgd1wDyNw6eZMoth5tnxMUoH0vd5pwT5pt6cvFnjc
7dN1Ui7R5it5M+C0XTfPturTM6m4UuMJ/6kDZwpdzxLis9d9434GxGM/+CbhH/GJ
ABEBAAGJAR8EGAECAAkFAmLyPqMCGwwACgkQ4ly5Kz31UktdAwf9F05hxKWRxO8u
V+RCh6wtCf9QYsSXeQIoRbiDvfLmRN5SnPkQNwbx2Bd/C1umkZ6Y7KvXsVmSflxV
xsjkMPslexOKiHz8Imb/IMDU4yRMyORxIq+iZ7vEVDQFi4QiqBwc3oDfrzlYT9SY
lkNU6o3PNvbdaMpe2PLrGDWhMeTBhZUTeFbEpMmGY3G5wo8+og1tdZIPyWvOLQ5G
ocO1VDQSFcTY8ed0Ph5UjSpba6UD+sZBLsVepRFO4vitNcqV7yohQZlufc9hF1Lg
RP4Fg+6vDZcrNU55jjTgOTSznSIvx+jPJr/p6YbK0ZKSV56dsrTmq2xBBtz/JxKB
YwGH0Uw8cQ==
=E2sQ
-----END PGP PUBLIC KEY BLOCK-----
```
## Step 6 - Verify existing imported public keys and import a new key
The newly created `public` key can be imported in `rpm` database and to make a trust between vendor and client, it's necessary to import the key, else `yum` will by default won't let the package to get installed.
```
[minakshi@rhel7-basemachine ~]$ rpm -q gpg-pubkey --qf '%{name}-%{version}-%{release} --> %{summary}\n'
gpg-pubkey-352c64e5-52ae6884 --> gpg(Fedora EPEL (7) <epel@fedoraproject.org>)
gpg-pubkey-222d23d0-5910b0f0 --> gpg(Sublime HQ Pty Ltd <support@sublimetext.com>)
gpg-pubkey-fd431d51-4ae0493b --> gpg(Red Hat, Inc. (release key 2) <security@redhat.com>)
gpg-pubkey-2fa658e0-45700c69 --> gpg(Red Hat, Inc. (auxiliary key) <security@redhat.com>)
gpg-pubkey-7fac5991-4615767f --> gpg(Google, Inc. Linux Package Signing Key <linux-packages-keymaster@google.com>)
gpg-pubkey-d38b4796-570c8cd3 --> gpg(Google Inc. (Linux Packages Signing Authority) <linux-packages-keymaster@google.com>)
gpg-pubkey-f5cf6c1e-5544f037 --> gpg(RPM Fusion free repository for EL (7) <rpmfusion-buildsys@lists.rpmfusion.org>)
gpg-pubkey-d59097ab-52d46e88 --> gpg(packagecloud ops (production key) <ops@packagecloud.io>)
gpg-pubkey-038651bd-56c6038f --> gpg(https://packagecloud.io/slacktechnologies/slack (https://packagecloud.io/docs#gpg_signing) <support@packagecloud.io>)

[minakshi@rhel7-basemachine ~]$ sudo rpm --import dummy-package-public-key.txt
[minakshi@rhel7-basemachine ~]$ echo $?
0

[minakshi@rhel7-basemachine ~]$ rpm -q gpg-pubkey --qf '%{name}-%{version}-%{release} --> %{summary}\n'
gpg-pubkey-352c64e5-52ae6884 --> gpg(Fedora EPEL (7) <epel@fedoraproject.org>)
gpg-pubkey-222d23d0-5910b0f0 --> gpg(Sublime HQ Pty Ltd <support@sublimetext.com>)
gpg-pubkey-fd431d51-4ae0493b --> gpg(Red Hat, Inc. (release key 2) <security@redhat.com>)
gpg-pubkey-2fa658e0-45700c69 --> gpg(Red Hat, Inc. (auxiliary key) <security@redhat.com>)
gpg-pubkey-7fac5991-4615767f --> gpg(Google, Inc. Linux Package Signing Key <linux-packages-keymaster@google.com>)
gpg-pubkey-d38b4796-570c8cd3 --> gpg(Google Inc. (Linux Packages Signing Authority) <linux-packages-keymaster@google.com>)
gpg-pubkey-f5cf6c1e-5544f037 --> gpg(RPM Fusion free repository for EL (7) <rpmfusion-buildsys@lists.rpmfusion.org>)
gpg-pubkey-d59097ab-52d46e88 --> gpg(packagecloud ops (production key) <ops@packagecloud.io>)
gpg-pubkey-038651bd-56c6038f --> gpg(https://packagecloud.io/slacktechnologies/slack (https://packagecloud.io/docs#gpg_signing) <support@packagecloud.io>)
gpg-pubkey-3df5524b-62f23ea3 --> gpg(Minakshi Pushpendra Chavan (A Minor Project under the guidance of Prof Dr B S Sonawane sir for fulfilment of MTech CST) <shenguleminakshi265@gmail.com>)
```
Observe the last line in above output which shows that the key is now imported in `rpm database`.

## Step 7 - Sign the rpm package
To sign the `rpm` package, one need to create `.rpmmacros` with the contents below.
```
[minakshi@rhel7-basemachine ~]$ vi .rpmmacros
[minakshi@rhel7-basemachine ~]$ cat .rpmmacros
%_signature gpg
%_gpg_name Minakshi Pushpendra Chavan (A Minor Project under the guidance of Prof Dr B S Sonawane sir for fulfilment of MTech CST)
```
And finally to get the package signed, here are the steps.
```
[minakshi@rhel7-basemachine rpmbuild]$ rpm --addsign /home/minakshi/rpmbuild/RPMS/noarch/dummy-package-1.0.0-0.el7.noarch.rpm
Enter pass phrase: 
Pass phrase is good.
/home/minakshi/rpmbuild/RPMS/noarch/dummy-package-1.0.0-0.el7.noarch.rpm:
[minakshi@rhel7-basemachine ~]$ echo $?
0
```
Verify the signed package.
```
[minakshi@rhel7-basemachine ~]$ rpm -qip rpmbuild/RPMS/noarch/dummy-package-1.0.0-0.el7.noarch.rpm
Name        : dummy-package
Version     : 1.0.0
Release     : 0.el7
Architecture: noarch
Install Date: (not installed)
Group       : Applications/File
Size        : 1524
License     : GPLv2+
Signature   : RSA/SHA1, Tuesday 09 August 2022 04:37:00 PM IST, Key ID e25cb92b3df5524b
Source RPM  : dummy-package-1.0.0-0.el7.src.rpm
Build Date  : Tuesday 09 August 2022 04:29:38 PM IST
Build Host  : rhel7-basemachine
Relocations : (not relocatable)
Packager    : Minakshi Pushpendra Chavan
Vendor      : G S Mandal's Maharashtra Institute of Technology, Aurangabad
Summary     : This is a dummy package built by Minakshi Pushpendra Chavan.
Description :
This is a dummy package built by Minakshi Pushpendra Chavan as a part of minor project for completion of first year of Master of Technology in Computer Science and Technology under the guidance of Prof Dr B S Sonawane Sir.
```
Observe the line `Signature` now, it shows `RSA/SHA1, Tuesday 09 August 2022 04:37:00 PM IST, Key ID e25cb92b3df5524b` as it's value. Means the package is now signed with an appropriate key. And that can also be verified by rpm command as follows.
```
[minakshi@rhel7-basemachine rpmbuild]$ rpm -K /home/minakshi/rpmbuild/RPMS/noarch/dummy-package-1.0.0-0.el7.noarch.rpm
/home/minakshi/rpmbuild/RPMS/noarch/dummy-package-1.0.0-0.el7.noarch.rpm: rsa sha1 (md5) pgp md5 OK
```
## Step 8 - Install the rpm package.
Installation of signed package is possible as follows. Verify the files deployed by the package as well as dummy man page.
```
[minakshi@rhel7-basemachine ~]$ sudo rpm -ivh rpmbuild/RPMS/noarch/dummy-package-1.0.0-0.el7.noarch.rpm
Preparing...                          ################################# [100%]
Updating / installing...
   1:dummy-package-1.0.0-0.el7        ################################# [100%]
Please run dummy-package command to view deployment !
Your constructive feedback will be highly appreciated!!!

[minakshi@rhel7-basemachine ~]$ dummy-binary 
 This is a dummy binary execution which will just check the presence of the files deployed by the dummy-package, nothing else!
 Configuration File : /etc/dummy-package/dummy-package.conf is present
 Binary Exe File : /usr/bin/dummy-binary is present
 Manual Page File : /usr/local/man/man1/dummy-package.1.gz is present


[minakshi@rhel7-basemachine rpmbuild]$ ls -l /etc/dummy-package/dummy-package.conf /usr/bin/dummy-binary /usr/local/man/man1/dummy-package.1.gz
-rwxr-xr-x. 1 root root   58 Aug  9 15:49 /etc/dummy-package/dummy-package.conf
-rwxr-xr-x. 1 root root 1112 Aug  9 16:40 /usr/bin/dummy-binary
-rwxr-xr-x. 1 root root  354 Aug  9 15:19 /usr/local/man/man1/dummy-package.1.gz

[minakshi@rhel7-basemachine rpmbuild]$ man dummy-package

dummy-package(1)            General Commands Manual           dummy-package(1)

NAME
       dummy-package - Built by Minakshi Pushpendra Chavan - MTech CST

SYNOPSIS
       G  S  Mandal's  Maharashtra Institute of Technology, Chh. Sambhajinagar
       (Formerly known as Aurangabad) - An Autonomous Institute [ h ] [ b ]

DESCRIPTION
       dummy-package This is actually a dummy package and dummy man page to be
       created as a part of minor project for the submission and completion of
       subject MTC674_Minor_Project

OPTIONS
       h      Option 1

       b      Option 2

                                                              dummy-package(1)
```
In this way, the dummay package is built in order to delivery the dummy payload using Red Hat Package Manager.
