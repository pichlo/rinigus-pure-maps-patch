Name:          harbour-pure-maps-patch
Summary:       Patch: Alternative UI for Pure Maps
Version:       0.0.2
Release:       1
Group:         Patches
BuildArch:     noarch
Requires:      patchmanager
Requires:      harbour-pure-maps >= 1.8.0
Requires:      harbour-pure-maps <= 1.8.0

Vendor:        pichlo
Distribution:  SailfishOS
Packager:      Peter Pichler <maemo@pichler.co.uk>
License:       GPL

%description
An alternative layout for the Navigation Block and a few other visual elements, both in portrait and in landscape.

#%prep
#%setup -q -n %{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/patchmanager/patches/%{name}
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/%{name}
mkdir -p %{buildroot}/usr/share/harbour-pure-maps/qml
cp -r qml/* %{buildroot}/usr/share/harbour-pure-maps/qml

%pre
if [ -f /usr/sbin/patchmanager ]; then
    /usr/sbin/patchmanager -u %{name} || true
fi

%preun
if [ -f /usr/sbin/patchmanager ]; then
    /usr/sbin/patchmanager -u %{name} || true
fi

%files
%defattr(644,root,root,-)
%{_datadir}/patchmanager/patches/%{name}
%{_datadir}/harbour-pure-maps/qml/NarrativeLabel.qml
%{_datadir}/harbour-pure-maps/qml/NavigationBlockElement.qml

%changelog
* Wed Oct 31 2018 Peter Pichler <maemo@pichler.co.uk> 0.0.2-1
- Catch up with Pure Maps 1.8.0.

* Tue Oct 30 2018 Peter Pichler <maemo@pichler.co.uk> 0.0.1-2
- Moved the compass to the original place. It was quite fine there.

* Sun Oct 14 2018 Peter Pichler <maemo@pichler.co.uk> 0.0.1-1
- First build.
