%define		pkgname skype
Summary:	p2p VoIP application
Summary(pl.UTF-8):	Aplikacja VoIP p2p
Name:		skype-static
Version:	2.1.0.81
Release:	4
# http://www.skype.com/company/legal/promote/distributionterms.html
# distributing on CD-ROM and similar media requires approval
License:	Commercial, redistributable (see LICENSE)
Group:		Applications/Communications
Source0:	http://download.skype.com/linux/%{pkgname}_static-%{version}.tar.bz2
# Source0-md5:	137a4a749c8fb3b76c3410514c7e2053
Patch0:		%{name}-desktop.patch
URL:		http://www.skype.com/
Conflicts:	skype
Provides:	skype-program = %{version}
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0
# https://developer.skype.com/jira/browse/SCL-569
%define		no_install_post_strip	1

%description
p2p VoIP application.

License requirement: The Software originates from Skype and use the
links and graphics as published and indicated on
<http://www.skype.com/go/redistribution/>.

%description -l pl.UTF-8
Aplikacja VoIP p2p.

Wymaganie licencyjne: to oprogramowanie pochodzi od Skype i
wykorzystuje odnośniki i grafikę w postaci opublikowanej i oznaczonej
na <http://www.skype.com/go/redistribution/>.

%prep
%setup -q -n %{pkgname}_static-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{pkgname},%{_datadir}/%{pkgname}/{lang,sounds,avatars},%{_desktopdir},/etc/dbus-1/system.d}

install -p %{pkgname} $RPM_BUILD_ROOT%{_bindir}
cp -a sounds/*.wav $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/sounds
cp -a lang/*.qm $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/lang
cp -a avatars/*.png $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/avatars
cp -a skype.conf $RPM_BUILD_ROOT/etc/dbus-1/system.d
cp -a *.desktop $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
cp -a icons/SkypeBlue_16x16.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{pkgname}.png
cp -a icons/SkypeBlue_32x32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{pkgname}.png
cp -a icons/SkypeBlue_48x48.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{pkgname}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
/etc/dbus-1/system.d/skype.conf
%attr(755,root,root) %{_bindir}/skype

%dir %{_datadir}/%{pkgname}
%{_datadir}/%{pkgname}/sounds
%{_datadir}/%{pkgname}/avatars

%dir %{_datadir}/%{pkgname}/lang
%lang(bg) %{_datadir}/%{pkgname}/lang/skype_bg.qm
%lang(de) %{_datadir}/%{pkgname}/lang/skype_de.qm
%lang(en) %{_datadir}/%{pkgname}/lang/skype_en.qm
%lang(es) %{_datadir}/%{pkgname}/lang/skype_es.qm
%lang(et) %{_datadir}/%{pkgname}/lang/skype_et.qm
%lang(fr) %{_datadir}/%{pkgname}/lang/skype_fr.qm
%lang(it) %{_datadir}/%{pkgname}/lang/skype_it.qm
%lang(ja) %{_datadir}/%{pkgname}/lang/skype_ja.qm
%lang(ko) %{_datadir}/%{pkgname}/lang/skype_ko.qm
%lang(lt) %{_datadir}/%{pkgname}/lang/skype_lt.qm
%lang(lv) %{_datadir}/%{pkgname}/lang/skype_lv.qm
%lang(pl) %{_datadir}/%{pkgname}/lang/skype_pl.qm
%lang(pt) %{_datadir}/%{pkgname}/lang/skype_pt_pt.qm
%lang(pt_BR) %{_datadir}/%{pkgname}/lang/skype_pt_br.qm
%lang(ro) %{_datadir}/%{pkgname}/lang/skype_ro.qm
%lang(ru) %{_datadir}/%{pkgname}/lang/skype_ru.qm
%lang(th) %{_datadir}/%{pkgname}/lang/skype_th.qm
%lang(tr) %{_datadir}/%{pkgname}/lang/skype_tr.qm
%lang(zh_CN) %{_datadir}/%{pkgname}/lang/skype_zh_s.qm
%lang(zh_TW) %{_datadir}/%{pkgname}/lang/skype_zh_t.qm

%{_iconsdir}/hicolor/*x*/apps/%{pkgname}.png
%{_desktopdir}/*.desktop
