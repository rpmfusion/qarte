Name:           qarte
Version:        2.6.0
Release:        1%{dist}
License:        GPLv3+
URL:            https://launchpad.net/qarte
Source0:        http://oqapy.eu/releases/%{name}-%{version}.tar.gz
Group:          Applications/Multimedia
Summary:        A browser for arte.tv web site
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  python2-devel
Requires:       PyQt4
Requires:       rtmpdump
BuildArch:      noarch

%description
Qarte allows browsing the archive of arte+7 & arteLiveWeb sites
and recording videos.

%prep
%setup -qn %{version}

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
chmod 755 %{buildroot}%{_datadir}/%{name}/%{name}.py
cp -pR medias %{buildroot}%{_datadir}/%{name}
cp -pR VWidgets %{buildroot}%{_datadir}/%{name}
cp -pR commonwidgets %{buildroot}%{_datadir}/%{name}
cp -pR crontab %{buildroot}%{_datadir}/%{name}
cp -pR locale %{buildroot}%{_datadir}

%find_lang %{name}

%files -f %{name}.lang
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/q_arte.desktop
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/96x96/apps/%{name}.png

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%changelog
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

