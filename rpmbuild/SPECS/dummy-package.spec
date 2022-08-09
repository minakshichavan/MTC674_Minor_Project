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
