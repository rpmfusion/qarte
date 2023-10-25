# bytecompile with Python 3
%global __python %{__python3}

Name:           qarte
Version:        5.5.0
Release:        1%{?dist}
Summary:        A browser for arte.tv web site
License:        GPLv3+
URL:            https://launchpad.net/qarte
Source0:        http://oqapy.eu/releases/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  python3-devel
Requires:       rtmpdump
Requires:       python3-qt5
Requires:       python3-m3u8
BuildArch:      noarch


%description
Qarte allows browsing the archive of arte+7 & arteLiveWeb sites
and recording videos.

%prep
%autosetup -p1 -n %{name}-%{version}

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
* Wed Oct 25 2023 Martin Gansser <martinkg@fedoraproject.org> - 5.5.0-1
- Update to 5.5.0

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 5.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 14 2023 Leigh Scott <leigh123linux@gmail.com> - 5.3.0-2
- Fix broken requires

* Thu Mar 30 2023 Martin Gansser <martinkg@fedoraproject.org> - 5.3.0-1
- Update to 5.3.0

* Wed Mar 29 2023 Martin Gansser <martinkg@fedoraproject.org> - 5.2.1-1
- Add RR python-m3u8
- Update to 5.2.1

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 30 2022 Martin Gansser <martinkg@fedoraproject.org> - 4.16.0-1
- Update to 4.16.0

* Tue Nov 02 2021 Sérgio Basto <sergio@serjux.com> - 4.15.1-1
- Update qarte to 4.15.1

* Tue Nov 02 2021 Sérgio Basto <sergio@serjux.com> - 4.15.0-1
- Update qarte to 4.15.0

* Mon Nov 01 2021 Sérgio Basto <sergio@serjux.com> - 4.14.0-2
- add fixes from upstream, rfbz #6161

* Sat Sep 04 2021 Sérgio Basto <sergio@serjux.com> - 4.14.0-1
- Update to 4.14.0 rfbz #6060

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 02 2020 Martin Gansser <martinkg@fedoraproject.org> - 4.11.0-1
- Update to 4.11.0

* Mon Sep 07 2020 Martin Gansser <martinkg@fedoraproject.org> - 4.10.0-1
- Update to 4.10.0

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Martin Gansser <martinkg@fedoraproject.org> - 4.7.0-1
- Update to 4.7.0

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 24 2018 Sérgio Basto <sergio@serjux.com> - 4.6.0-1
- Update to 4.6.0

* Wed Sep 12 2018 Martin Gansser <martinkg@fedoraproject.org> - 4.5.0-1
- Update to 4.5.0

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.4.0-3
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 16 2018 Martin Gansser <martinkg@fedoraproject.org> - 4.4.0-1
- Update to 4.4.0

* Tue Jul 10 2018 Nicolas Chauvet <kwizart@gmail.com> - 4.3.0-1
- Update to 4.3.0

* Tue Jul 10 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-2
- Rebuilt for Python 3.7

* Sun Apr 29 2018 Sérgio Basto <sergio@serjux.com> - 4.1.0-1
- Update 4.1.0

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

