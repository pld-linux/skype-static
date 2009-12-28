Summary:	p2p VoIP application
Summary(pl.UTF-8):	Aplikacja VoIP p2p
Name:		skype-static
%define		_altname skype
Version:	2.1.0.47
Release:	3
# http://www.skype.com/company/legal/promote/distributionterms.html
# distributing on CD-ROM and similar media requires approval
License:	Commercial, redistributable (see LICENSE)
Group:		Applications/Communications
Source0:	http://download.skype.com/linux/%{_altname}_static-%{version}.tar.bz2
# Source0-md5:	84cd16086d499b766a6ea9524271c0b9
Patch0:		%{name}-desktop.patch
URL:		http://www.skype.com/
Conflicts:	skype
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
%setup -q -n %{_altname}_static-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{_altname},%{_datadir}/%{_altname}/{lang,sounds,avatars},%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps/,%{_desktopdir},%{_sysconfdir}/dbus-1/system.d}

install %{_altname} $RPM_BUILD_ROOT%{_bindir}
install sounds/*.wav $RPM_BUILD_ROOT%{_datadir}/%{_altname}/sounds
install lang/*.qm $RPM_BUILD_ROOT%{_datadir}/%{_altname}/lang
install avatars/*.png $RPM_BUILD_ROOT%{_datadir}/%{_altname}/avatars
install skype.conf $RPM_BUILD_ROOT%{_sysconfdir}/dbus-1/system.d
install icons/SkypeBlue_16x16.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{_altname}.png
install icons/SkypeBlue_32x32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{_altname}.png
install icons/SkypeBlue_48x48.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{_altname}.png
install *.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{_altname}
%{_datadir}/%{_altname}/sounds
%{_datadir}/%{_altname}/avatars

%dir %{_datadir}/%{_altname}/lang
# %lang(ar) %{_datadir}/%{_altname}/lang/skype_ar.qm
%lang(bg) %{_datadir}/%{_altname}/lang/skype_bg.qm
# %lang(cs) %{_datadir}/%{_altname}/lang/skype_cs.qm
# %lang(cz) %{_datadir}/%{_altname}/lang/skype_cz.qm
# %lang(da) %{_datadir}/%{_altname}/lang/skype_da.qm
%lang(de) %{_datadir}/%{_altname}/lang/skype_de.qm
# %lang(el) %{_datadir}/%{_altname}/lang/skype_el.qm
%lang(en) %{_datadir}/%{_altname}/lang/skype_en.qm
%lang(es) %{_datadir}/%{_altname}/lang/skype_es.qm
%lang(et) %{_datadir}/%{_altname}/lang/skype_et.qm
# %lang(fi) %{_datadir}/%{_altname}/lang/skype_fi.qm
%lang(fr) %{_datadir}/%{_altname}/lang/skype_fr.qm
# %lang(he) %{_datadir}/%{_altname}/lang/skype_he.qm
# %lang(hu) %{_datadir}/%{_altname}/lang/skype_hu.qm
%lang(it) %{_datadir}/%{_altname}/lang/skype_it.qm
%lang(ja) %{_datadir}/%{_altname}/lang/skype_ja.qm
%lang(ko) %{_datadir}/%{_altname}/lang/skype_ko.qm
%lang(lv) %{_datadir}/%{_altname}/lang/skype_lv.qm
%lang(lt) %{_datadir}/%{_altname}/lang/skype_lt.qm
# %lang(nl) %{_datadir}/%{_altname}/lang/skype_nl.qm
# %lang(nb) %{_datadir}/%{_altname}/lang/skype_nb.qm
%lang(pl) %{_datadir}/%{_altname}/lang/skype_pl.qm
%lang(pt_BR) %{_datadir}/%{_altname}/lang/skype_pt_br.qm
%lang(pt) %{_datadir}/%{_altname}/lang/skype_pt_pt.qm
%lang(ro) %{_datadir}/%{_altname}/lang/skype_ro.qm
%lang(ru) %{_datadir}/%{_altname}/lang/skype_ru.qm
# %lang(sv)  %{_datadir}/%{_altname}/lang/skype_sv.qm
%lang(th) %{_datadir}/%{_altname}/lang/skype_th.qm
%lang(tr) %{_datadir}/%{_altname}/lang/skype_tr.qm
# probably zh
%lang(zh_CN) %{_datadir}/%{_altname}/lang/skype_zh_s.qm
# probably zh_TW
%lang(zh_TW) %{_datadir}/%{_altname}/lang/skype_zh_t.qm

/etc/dbus-1/system.d/skype.conf
%{_iconsdir}/hicolor/*x*/apps/%{_altname}.png
%{_desktopdir}/*.desktop
