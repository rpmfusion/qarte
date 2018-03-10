# bytecompile with Python 3
%global __python %{__python3}

Name:           qarte
Version:        4.0.0
Release:        3%{dist}
License:        GPLv3+
URL:            https://launchpad.net/qarte
Source0:        http://oqapy.eu/releases/%{name}-%{version}.tar.gz
Summary:        A browser for arte.tv web site

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  python3-devel
Requires:       rtmpdump
Requires:       python3-qt5
BuildArch:      noarch

%description
Qarte allows browsing the archive of arte+7 & arteLiveWeb sites
and recording videos.

%prep
%setup -q

%build

%install
install -D %{name} %{buildroot}%{_bindir}/%{name}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications q_arte.desktop
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/
cp -p %{name}.png %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/%{name}.png
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1 
mkdir %{buildroot}%{_datadir}/%{name}
cp -p *.py* %{buildroot}%{_datadir}/%{name}
cp -pR medias %{buildroot}%{_datadir}/%{name}
cp -pR gui %{buildroot}%{_datadir}/%{name}
cp -pR locale %{buildroot}%{_datadir}

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/q_arte.desktop
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/96x96/apps/%{name}.png

%changelog
* Sat Mar 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 4.0.0-3
- Remove RR qt5-qtmultimedia, depends on python3-qt5
- Re-add RR python3-qt5

* Sat Mar 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 4.0.0-2
- Add RR qt5-qtmultimedia

* Sat Mar 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 4.0.0-1
- Update to 4.0.0
- Add BR python3-devel
- Add bytecompile with Python 3 %%global __python %%{__python3}
- Remove RR python3-qt5
- Remove scriptlets

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 12 2016 Milan Bouchet-Valat <nalimilan@club.fr> - 3.2.0-1
- New upstream release.

* Thu Feb 11 2016 Milan Bouchet-Valat <nalimilan@club.fr> - 2.8.0-1
- New upstream release, fixing breakage due to change in Arte streams.

* Tue Nov 17 2015 Milan Bouchet-Valat <nalimilan@club.fr> - 2.6.0-2
- Fix FTBS by adding correct sources.

* Tue Nov 17 2015 Milan Bouchet-Valat <nalimilan@club.fr> - 2.6.0-1
- New upstream release, fixing breakage due to change in Arte streams.

* Wed May 27 2015 Milan Bouchet-Valat <nalimilan@club.fr> - 2.3.0-1
- New upstream release.

* Sat Sep 20 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 2.2.0-3
- Add back %%{dist} to Release.

* Thu Sep 18 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 2.2.0-2
- Add desktop-file-utils to BuildRequires.
- Fix license to GPLv3+.
- Remove %%{dist} from Release.

* Mon Sep 15 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 2.2.0-1
- New upstream release.

* Sun Jan 19 2014 Milan Bouchet-Valat <nalimilan@club.fr> 1.9.0-1
- Adapt Mageia package to RPMfusion.

* Tue Oct 22 2013 umeabot <umeabot> 1.8.5-4.mga4
+ Revision: 546102
- Mageia 4 Mass Rebuild

* Fri Oct 18 2013 zezinho <zezinho> 1.8.5-3.mga4
+ Revision: 520908
- fix l10n

* Thu Oct 17 2013 zezinho <zezinho> 1.8.5-2.mga4
+ Revision: 502167
- add manpage
- fix requires

* Wed Oct 16 2013 zezinho <zezinho> 1.8.5-1.mga4
+ Revision: 501750
- fix desktop file
- imported package qarte

